import csv
import random

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
    The estimate is given for a 2k random sample taken from the dataset
    """
    print("Dataset:", file_path)
    log_data = _load_log_data_generic_file(input_file=file_path)
    log_data_sample_2k = _sample_2k_logs(log_data)

    no_unique_words = compute_no_unique_words(log_data_sample_2k)
    no_unique_chars = compute_no_unique_chars(log_data_sample_2k)
    no_unique_log_lengths = compute_no_unique_log_lengths(log_data_sample_2k)

    no_unique_words_percentage = compute_percentage_no_unique_words(no_unique_words)
    no_unique_chars_percentage = compute_percentage_no_unique_chars(no_unique_chars)
    no_unique_log_lengths_percentage = compute_percentage_no_unique_log_lengths(no_unique_log_lengths)

    h_level = 0.4*no_unique_words_percentage + 0.2*no_unique_chars_percentage + 0.4*no_unique_log_lengths_percentage
    print(f"Metrics: (1) no_unique_words = {no_unique_words}, (2) no_unique_chars = {no_unique_chars}, (3) no_unique_log_lengths = {no_unique_log_lengths}")
    print("H level is", round(h_level, 3), "for", file_path)

    return round(h_level, 3)

def _sample_2k_logs(log_data):
    """
    Randomly samples 2000 logs from the given log_data.

    This function currently uses a fixed random seed for reproducibility to ensure that
    the same set of logs is sampled each time it's called.

    Args:
        log_data (list): A list of log entries to sample from.

    Returns:
        list: A list containing 2000 randomly selected log entries from log_data.
    """
    random.seed(0)
    sample_log_data_2k_logs = random.sample(log_data, 2000)
    return sample_log_data_2k_logs

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

def _load_log_data_generic_file(input_file):
    """
    Load log data from a generic text file and return it as a list of log lines.

    This function opens the specified input_file in read mode, reads its content line
    by line, and stores each line as a log entry in the returned list. Each log entry
    is stripped of leading and trailing whitespace.

    Args:
        input_file (str): The path to the input file containing log data.

    Returns:
        list: A list of log entries, where each entry is a string.

    Note:
        - The function assumes that each line in the input file represents a separate
          log entry.
    """
    file = open(input_file, 'r')
    log_lines = []

    with open(input_file) as f:
        for line in f:
            log_lines.append(line.strip())
    return log_lines