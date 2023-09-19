import csv

from logchimera.statistics import (
    compute_no_unique_words, 
    compute_no_unique_chars,
    compute_no_unique_log_lengths, 
    compute_percentage_no_unique_words,
    compute_percentage_no_unique_chars, 
    compute_percentage_no_unique_log_lengths
)

def estimate_heterogeneity_csv_file(file_path):
    """
    Estimate heterogeneity for csv log file
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
    print("H level is", round(h_level, 3), "for", file_path)

    return round(h_level, 3)

def estimate_heterogeneity_generic_file(file_path):
    """
    Estimate heterogeneity for generaic log file
    The file should contain 2k log lines
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
    print("H level is", round(h_level, 3), "for", file_path)

    return round(h_level, 3)

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