import csv
import random
from collections import Counter

from logchimera.statistics import (
    compute_no_unique_words, 
    compute_no_unique_chars,
    compute_no_unique_log_lengths, 
    compute_percentage_no_unique_words,
    compute_percentage_no_unique_chars, 
    compute_percentage_no_unique_log_lengths
)

from logchimera.utils import MAX_NO_LOGS_FOR_HETEROGENEITY_ANALYSIS

from logchimera.parser import parse_log_lines

def _estimate_heterogeneity_for_list_of_logs(list_of_logs):
    log_lines = list_of_logs
    no_unique_words = compute_no_unique_words(log_lines)
    no_unique_chars = compute_no_unique_chars(log_lines)
    no_unique_log_lengths = compute_no_unique_log_lengths(log_lines)

    no_unique_words_percentage = compute_percentage_no_unique_words(no_unique_words)
    no_unique_chars_percentage = compute_percentage_no_unique_chars(no_unique_chars)
    no_unique_log_lengths_percentage = compute_percentage_no_unique_log_lengths(no_unique_log_lengths)

    h_level = 0.4*no_unique_words_percentage + 0.2*no_unique_chars_percentage + 0.4*no_unique_log_lengths_percentage
    print(f"Metrics: (1) no_unique_words = {no_unique_words}, (2) no_unique_chars = {no_unique_chars}, (3) no_unique_log_lengths = {no_unique_log_lengths}")
    return round(h_level, 3)

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
    sample_log_data_2k_logs = random.sample(log_data, MAX_NO_LOGS_FOR_HETEROGENEITY_ANALYSIS)
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

def _parse_logs_for_estimating_heterogeneity(file_path):
    """
    Parse log data from a file and extract specific columns for estimating heterogeneity.

    This function reads log data from the specified file, selects the "Content" and "EventTemplate"
    columns, and converts them into a list of lists. The resulting list is suitable for further
    analysis to estimate heterogeneity within the log data.

    Parameters:
    file_path (str): The path to the log file to be parsed.

    Returns:
    list: A list of lists containing the values from the "Content" and "EventTemplate" columns.
    """
    df_parsed_logs = parse_log_lines(file_path)
    df_parsed_logs = df_parsed_logs[["Content", "EventTemplate"]]

    data_list = df_parsed_logs.values.tolist()
    return data_list

def estimate_heterogeneity_generic_file_using_log_parsing(file_path):
    """
    Estimate heterogeneity for generic log file
    The estimate is given for a 2k sample taken from the dataset using statistics generated by log parsing
    """
    # get list of parsed logs [initial_log_content, parsed_log]
    list_of_parsed_logs = _parse_logs_for_estimating_heterogeneity(file_path)

    # sample 2k using statistics from log parsing
    sample_log_data = _sample_2k_logs_using_parsing(list_of_parsed_logs)

    logs, templates = [item[0] for item in sample_log_data], [item[1] for item in sample_log_data]
    
    h_level = _estimate_heterogeneity_for_list_of_logs(logs)

    print("H level is", h_level, "for", file_path)
    
    return h_level

def _unique_number_of_elements_in_list(list_of_values):
    return list(set(list_of_values))

def _sample_2k_logs_using_parsing(log_data):
    """
    Sample 2000 logs using statistics generated by log parsing.

    Args:
        log_data (list): A list of log entries to sample from. Specifically, a list of lists, that contains the logs and their parsed templates.

    Returns:
        list: A list containing 2000 logs selected based on statistics generated using log parsing.
    """
    # check number of unique templates
    log_templates = [log[1] for log in log_data]
    unique_log_templates = _unique_number_of_elements_in_list(log_templates)

    if len(unique_log_templates) > MAX_NO_LOGS_FOR_HETEROGENEITY_ANALYSIS:
        # order list of logs based on template length
        sorted_data = sorted(log_data, key=lambda x: len(x[1]))

        unique_data = {}
        for log_message, log_template in reversed(sorted_data):
            unique_data.setdefault(log_template, (log_message, log_template))

        # Extract the first 2000 rows containing the log message and log template
        k = MAX_NO_LOGS_FOR_HETEROGENEITY_ANALYSIS
        result = list(unique_data.values())[:k]
        return result
    else:
        # Count the occurrences of each template
        template_counts = Counter(template for _, template in log_data)

        # Calculate the total number of log entries
        total_logs = len(log_data)

        # Append the percentage to each tuple in the list
        result = []
        for log_message, template in log_data:
            percentage = (template_counts[template] / total_logs) * 100
            result.append([log_message, template, percentage])

        log_data = result

        # Calculate the number of samples to take for each template
        samples_per_template = {}
        total_samples = MAX_NO_LOGS_FOR_HETEROGENEITY_ANALYSIS
        for _, _, percentage in log_data:
            samples = int(total_samples * (percentage / 100))
            samples_per_template[_] = samples

        result = []
        for log_template in unique_log_templates:

            no_samples_per_current_log_template = samples_per_template[log_template]

            for message, template, _ in log_data:
                if no_samples_per_current_log_template == 0:
                    break
                if log_template == template:
                    result.append([message, template])
                    no_samples_per_current_log_template -= 1

        return result
    

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