import csv

from logchimera.heterogeneity import estimate_heterogeneity_csv_file, estimate_heterogeneity_generic_file
from logchimera.mixing import mixing_labeled_data, mixing_unlabeled_data

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


def estimate_heterogeneity(file_path, csv_file=False):
    """
    Estimate heterogeneity for a log file.

    Parameters:
    -----------
    file_path : str
        The path to the log file to be analyzed.

    csv_file : bool, optional (default=False)
        Specifies whether the input file is in CSV format or not. If set to True, the function expects
        the log file to contain the following three columns: Content, EventTemplate, Variables. If set
        to False, a generic log file format will be assumed, and the function will attempt to estimate
        heterogeneity based on the file's content (each log on a new line).

    Returns:
    --------
    h_level : float
        The estimated level of heterogeneity in the log file, with higher values indicating greater
        heterogeneity (from 0 to 1).

    Notes:
    ------
    - Heterogeneity is estimated based on the log file's content and structure.
    - When `csv_file` is set to True, the function assumes a specific CSV format with predefined columns (three columns named: Content, EventTemplate, Variables).
    - When `csv_file` is set to False, the function attempts to estimate heterogeneity from the generic log
      file format, with each log entry separated by a new line character.

    Example Usage:
    -------------
    To estimate heterogeneity for a generic log file:
    >>> h_level = estimate_heterogeneity("generic_log.txt")

    To estimate heterogeneity for a CSV-formatted log file:
    >>> h_level = estimate_heterogeneity("csv_log.csv", csv_file=True)
    """
    h_level = 0

    if csv_file:
        h_level = estimate_heterogeneity_csv_file(file_path)
    else:
        h_level = estimate_heterogeneity_generic_file(file_path)
    
    return h_level

def mixing(percentage, file_path, labels=False, dataset_name="Apache"):
    """
    Increase log heterogeneity through mixing.

    This function takes a file path and a percentage value as input.
    
    Parameters:
        file_path (str): The path to the file to be changed.
        percentage (float): The amount of logs to be replaced, ranging from 1 to 25.

    Returns:
        float: The new heterogeneity level after mixing the logs.
    """
    print("Computing initial heterogeneity...")
    estimate_heterogeneity(file_path)

    perc = 0
    if not labels:
        print("No labels functionality not available")
        return "No labels functionality not available"
    else:
        print("\nMixing...")
        mixed_file_save_path = mixing_labeled_data(percentage, file_path)

    estimate_heterogeneity(mixed_file_save_path)

def fuzzing(file_path):
    """
    Increase log heterogeneity through fuzzing.

    This function takes a file path as input.
    
    Parameters:
        file_path (str): The path to the file to be fuzzed.

    Returns:
        float: The new heterogeneity level after fuzzing the file.
    """
    pass

def function_test(test_string):
    '''
    '''
    return ""