from logchimera.datasets import get_pool_mixing_data
import pandas as pd
import csv
import os
import random
from logchimera.utils import (
    MINIMUM_PERCENTAGE,
    MAXIMUM_PERCENTAGE,
)

AVAILABLE_DATASETS = ["Apache", "BGL", "HPC", "Mac"]


def custom_mapping(percentage):
    if percentage <= MINIMUM_PERCENTAGE:
        return 1
    elif percentage >= MAXIMUM_PERCENTAGE:
        return 500
    else:
        x1, y1 = 1, 1
        x2, y2 = 25, 500
        output_value = y1 + (percentage - x1) * (y2 - y1) / (x2 - x1)
        return int(output_value)


def mixing_labeled_data(percentage, file_path, dataset_name="Apache", output_dir=None):
    """
    Increase log heterogeneity through mixing.

    Parameters:
        percentage (float): Percentage of logs to replace, 1–25.
        file_path (str): Path to a CSV file containing at least Content and EventTemplate columns.
        dataset_name (str): Name of the source dataset (Apache/BGL/HPC/Mac). Logs from this
            dataset are excluded from the mixing pool so only foreign logs are injected.
        output_dir (str, optional): Directory for the output file. Defaults to ./logchimera_output/.

    Returns:
        str: Path to the generated mixed CSV file.
    """
    if output_dir is None:
        output_dir = "logchimera_output"
    os.makedirs(output_dir, exist_ok=True)

    no_samples = custom_mapping(percentage)

    df = pd.read_csv(file_path)
    original_content = df["Content"].tolist()

    # Build the mixing pool (exclude logs from the source dataset)
    path_mixing_file = get_pool_mixing_data()
    log_lines_mixed = []
    dict_mixed = {}
    with open(path_mixing_file, "r") as mixed_file:
        reader = csv.reader(mixed_file, delimiter=",")
        next(reader)  # skip header
        for line, template, _, source in reader:
            if source == dataset_name:
                continue
            log_lines_mixed.append(line)
            dict_mixed[line] = template

    random.seed(1)
    sample_size = min(no_samples, len(log_lines_mixed))
    hetero_sample = random.sample(log_lines_mixed, sample_size)
    hetero_templates = [dict_mixed[el] for el in hetero_sample]

    # Compute how many replacements per template class
    template_counts = df["EventTemplate"].value_counts().to_dict()
    normalization_factor = sum(v for v in template_counts.values() if v >= 100)

    replacements = {}
    if normalization_factor > 0:
        for tmpl, count in template_counts.items():
            if count >= 100:
                n = int(count / normalization_factor * len(log_lines_mixed))
                if n > 0:
                    replacements[tmpl] = n

    # Apply replacements: for each template class, replace the first N matching rows
    for tmpl, n_replace in replacements.items():
        if not hetero_sample:
            break
        matching_indices = df.index[df["EventTemplate"] == tmpl].tolist()
        n_actual = min(n_replace, len(matching_indices), len(hetero_sample))
        for i in range(n_actual):
            new_line = hetero_sample.pop(0)
            new_tmpl = hetero_templates.pop(0)
            df.at[matching_indices[i], "Content"] = new_line
            df.at[matching_indices[i], "EventTemplate"] = new_tmpl

    final_df = df[["Content", "EventTemplate"]].copy()
    final_df["Variables"] = "-"

    new_content = final_df["Content"].tolist()
    equals = sum(1 for o, n in zip(original_content, new_content) if o == n)
    actual_pct = round(100 - equals * 100 / len(original_content), 1)
    print(f"Percentage of logs replaced via mixing: {actual_pct}%")

    header = ["Content", "EventTemplate", "Variables"]
    output_path = os.path.join(output_dir, f"mixed_{dataset_name}_{int(actual_pct)}pct.csv")
    final_df.to_csv(output_path, columns=header, index=False)
    print(f"Mixed file saved to: {output_path}")
    return output_path


def mixing_unlabeled_data(percentage, file_path):
    pass
