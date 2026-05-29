import ast
import os
import random

import pandas as pd

from logchimera.datasets import get_pool_labeled_data
from logchimera.parser import parse_log_lines


def _load_entity_pool(pool_path):
    """Extract all variable values from the labeled data pool as a flat list."""
    df = pd.read_csv(pool_path)
    entities = []
    for val in df["entities"].dropna():
        val = str(val).strip()
        if val.startswith("[") and val.endswith("]"):
            try:
                items = ast.literal_eval(val)
                if isinstance(items, list):
                    entities.extend(str(i).strip() for i in items if str(i).strip())
            except (ValueError, SyntaxError):
                pass
        elif val and val not in ("-", "[]"):
            entities.append(val)
    return list(set(entities))


def fuzz_data(file_path, output_dir=None):
    """
    Increase log heterogeneity through fuzzing.

    Parses the input log file using the Drain algorithm to discover templates and
    variable slots, then replaces each variable value with a randomly sampled
    alternative from the labeled-data pool.

    Parameters:
        file_path (str): Path to a plain-text log file (one log per line).
        output_dir (str, optional): Output directory. Defaults to ./logchimera_output/.

    Returns:
        str: Path to the fuzzed plain-text file.
    """
    if output_dir is None:
        output_dir = "logchimera_output"
    os.makedirs(output_dir, exist_ok=True)

    print("Parsing log file to extract templates and variables...")
    df_parsed = parse_log_lines(file_path)

    pool_path = get_pool_labeled_data()
    entity_pool = _load_entity_pool(pool_path)

    if not entity_pool:
        print("Warning: entity pool is empty — returning original logs unchanged.")
        return file_path

    print(f"Entity pool size: {len(entity_pool)} unique values")
    random.seed(1)
    random.shuffle(entity_pool)
    # Repeat the pool so we never exhaust it for large files
    cycling_pool = (entity_pool * ((len(df_parsed) // len(entity_pool)) + 2))
    pool_iter = iter(cycling_pool)

    fuzzed_lines = []
    for _, row in df_parsed.iterrows():
        content = str(row["Content"])
        param_list = row.get("ParameterList", [])

        if param_list:
            for param in param_list:
                replacement = next(pool_iter, str(param))
                content = content.replace(str(param), str(replacement), 1)

        fuzzed_lines.append(content)

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(output_dir, f"fuzzed_{base_name}.txt")

    with open(output_path, "w") as f:
        for line in fuzzed_lines:
            f.write(line + "\n")

    print(f"Fuzzed file saved to: {output_path}")
    return output_path
