from logchimera.datasets import get_pool_mixing_data, get_publicly_available_labeled_dataset
import pandas as pd
import csv
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

def mixing_labeled_data(percentage, file_path):
    """
    Increase log heterogeneity through mixing.

    This function takes a file path and a percentage value as input.
    
    Parameters:
        percentage (float): The amount of logs to be replaced, ranging from 1 to 25.
        file_path (str): The path to the file to be changed.

    Returns:
        string: The path of the generated file.
    """
    no_samples = custom_mapping(percentage)

    df = pd.read_csv(file_path)

    path_mixing_file = get_pool_mixing_data()
    path_mixing_file_tst = get_publicly_available_labeled_dataset("Apache")

    mixed_file = open(path_mixing_file, 'r')
    mixed_file.readline()


    s = df['EventTemplate'].value_counts().to_dict()
    listofkeys = []
    keys = {}
    for key in s:
        listofkeys.append(key)
        keys[key] = s[key]
    
    log_lines_mixed = []
    log_templates_mixed = []
    dict_mixed = {}
    for line, template, _, source in csv.reader(mixed_file, delimiter=','):
        if source == "Apache":
            continue
        else:
            log_lines_mixed.append(line)
            log_templates_mixed.append(template)
            dict_mixed[line] = template
    
    random.seed(1)
    increased_hetero_sample_content = random.sample(log_lines_mixed, no_samples)

    increased_hetero_sample_templates = []
    for el in increased_hetero_sample_content:
        increased_hetero_sample_templates.append(dict_mixed[el])
    

    list_of_values_apache = df.values.tolist()

    replacements = {}

    normalization_factor = 0

    for key in keys:
        if keys[key] >= 100:
            normalization_factor += keys[key]

    for key in keys:
        if keys[key] >= 100:
            replacements[key] = int(keys[key]/normalization_factor*len(log_lines_mixed))

    for line in replacements:
        for i in range(replacements[line]):
            for j in range(len(list_of_values_apache)):
                if list_of_values_apache[j][1] == line and increased_hetero_sample_content:
                    new_mixed_line = increased_hetero_sample_content.pop(0)
                    new_mixed_template = increased_hetero_sample_templates.pop(0)
                    list_of_values_apache[j][0] = new_mixed_line
                    list_of_values_apache[j][1] = new_mixed_template
                    break

    final_list_apache = []
    for i in range(len(list_of_values_apache)):
        final_list_apache.append([list_of_values_apache[i][0], list_of_values_apache[i][1]])

    final_df = pd.DataFrame(final_list_apache, columns=['Content', 'EventTemplate'])
    final_df['Variables'] = "-"

    header = ["Content", "EventTemplate", "Variables"]

    write_path_structured_temp = f"logchimera/test_results/mixed_file.csv"
    
    final_df.to_csv(write_path_structured_temp, columns = header, index=False)
    
    df_99 = pd.read_csv(write_path_structured_temp)
    df_99 = df_99[["Content"]]
    df_99_list = df_99.values.tolist()

    df_original = pd.read_csv(f"src/logchimera/data/Apache_2k_labeled.csv")
    df_original = df_original[["Content"]]

    df_original_list = df_original.values.tolist()
    equals = 0
    a = 0
    for original, modified in zip(df_original_list, df_99_list):
        a += 1
        if original == modified:
            equals += 1
    print(f"Percentage logs replaced using mixing {100-equals*100/2000}%")
    percentage = 100-equals*100/2000

    final_write_path_structured = f"src/logchimera/data/mixing_results/{int(percentage)}_file.csv"
    final_write_path_log = f"src/logchimera/data/mixing_results/{int(percentage)}_file_log.csv"

    final_df.to_csv(final_write_path_structured, columns = header, index=False)
    final_df.to_csv(final_write_path_log, columns = ["Content"], index=False)
    return final_write_path_structured

def mixing_unlabeled_data(percentage, file_path):
    """
    """
    pass