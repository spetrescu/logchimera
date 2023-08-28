import csv

from logchimera.statistics import (
    compute_no_unique_words, 
    compute_no_unique_chars,
    compute_no_unique_log_lengths, 
    compute_percentage_no_unique_words,
    compute_percentage_no_unique_chars, 
    compute_percentage_no_unique_log_lengths
)

def _load_log_data(input_file):
    file = open(input_file, 'r')
    log_lines = []
    log_templates = []
    log_variables = []

    line = ""
    with open(input_file, newline='') as f:
        reader = csv.reader(f)
        line = next(reader)

    for line, template, variable in csv.reader(file, delimiter=','):
        log_lines.append(line)
        log_templates.append(template)
        log_variables.append(variable)
    return [log_lines, log_templates, log_variables]


def estimate_heterogeneity(file_path):
    """
    Estimate heterogeneity for log file
    The file (csv) has to contain the following three columns:
    Content,EventTemplate,Variables
    """
    print("Dataset:", file_path)
    log_data = _load_log_data(input_file=file_path)
    
    log_lines = log_data[0]
    log_templates = log_data[1]
    log_variables = log_data[2]

    no_unique_words = compute_no_unique_words(log_lines)
    no_unique_chars = compute_no_unique_chars(log_lines)
    no_unique_log_lengths = compute_no_unique_log_lengths(log_lines)

    no_unique_words_percentage = compute_percentage_no_unique_words(no_unique_words)
    no_unique_chars_percentage = compute_percentage_no_unique_chars(no_unique_chars)
    no_unique_log_lengths_percentage = compute_percentage_no_unique_log_lengths(no_unique_log_lengths)

    h_level = 0.4*no_unique_words_percentage + 0.2*no_unique_chars_percentage + 0.4*no_unique_log_lengths_percentage
    print(f"Metrics: (1) no_unique_words = {no_unique_words}, (2) no_unique_chars = {no_unique_chars}, (3) no_unique_log_lengths = {no_unique_log_lengths}")
    print("H level for", file_path.split("/")[-1], "is:", h_level, "rounded:", round(h_level, 3))

    return h_level

def mixing(file_path, percentage, labels=True):
    """
    Increase log heterogeneity through mixing.

    This function takes a file path and a percentage value as input.
    
    Parameters:
        file_path (str): The path to the file to be changed.
        percentage (float): The amount of logs to be replaced, ranging from 1 to 25.

    Returns:
        float: The new heterogeneity level after mixing the logs.
    """
    pass

def function_test(test_string):
    '''
    '''
    return ""