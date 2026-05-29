from logchimera.heterogeneity import estimate_heterogeneity_csv_file, estimate_heterogeneity_generic_file_using_log_parsing
from logchimera.mixing import mixing_labeled_data
from logchimera.fuzzing import fuzz_data


def estimate_heterogeneity(file_path, csv_file=False):
    """
    Estimate heterogeneity for a log file.

    Parameters:
    -----------
    file_path : str
        The path to the log file to be analyzed.

    csv_file : bool, optional (default=False)
        If True, expects a CSV with columns Content, EventTemplate, Variables.
        If False, expects a plain-text file with one log per line.

    Returns:
    --------
    h_level : float
        Estimated heterogeneity in [0, 1]. Higher means more heterogeneous.

    Example Usage:
    -------------
    >>> from logchimera.logchimera import estimate_heterogeneity
    >>> from logchimera.datasets import get_example_data_for_estimating_heterogeneity
    >>> h = estimate_heterogeneity(get_example_data_for_estimating_heterogeneity(), csv_file=True)
    """
    if csv_file:
        h_level = estimate_heterogeneity_csv_file(file_path)
    else:
        h_level = estimate_heterogeneity_generic_file_using_log_parsing(file_path)
    return h_level


def mixing(percentage, file_path, labels=False, dataset_name="Apache", output_dir=None):
    """
    Increase log heterogeneity through mixing.

    Replaces a proportion of logs in the input file with foreign logs drawn from a
    pool of publicly available labeled data (logs not from the same source dataset).

    Parameters:
        percentage (float): Percentage of logs to replace, 1–25.
        file_path (str): Path to a CSV file with columns Content, EventTemplate, Variables.
        labels (bool): Must be True; unlabeled mixing is not yet implemented.
        dataset_name (str): Source dataset name (Apache/BGL/HPC/Mac). Foreign logs come from
            all other datasets in the pool.
        output_dir (str, optional): Directory for the output file. Defaults to ./logchimera_output/.

    Returns:
        tuple[float, str] | str: (new_h_level, mixed_file_path), or an error string when
            labels=False.
    """
    if not labels:
        return "No labels functionality not available"

    print("Computing initial heterogeneity...")
    initial_h = estimate_heterogeneity(file_path, csv_file=True)
    print(f"Initial heterogeneity: {initial_h}\n")

    print("Mixing...")
    mixed_file_path = mixing_labeled_data(percentage, file_path, dataset_name=dataset_name, output_dir=output_dir)

    print("\nComputing new heterogeneity after mixing...")
    new_h = estimate_heterogeneity(mixed_file_path, csv_file=True)
    print(f"New heterogeneity: {new_h}")

    return new_h, mixed_file_path


def fuzzing(file_path, output_dir=None):
    """
    Increase log heterogeneity through fuzzing.

    Uses the Drain log parser to discover variable slots in the input log lines, then
    replaces each variable value with a randomly sampled alternative from the labeled
    data pool.

    Parameters:
        file_path (str): Path to a plain-text log file (one log per line).
        output_dir (str, optional): Directory for the output file. Defaults to ./logchimera_output/.

    Returns:
        str: Path to the fuzzed plain-text file.

    Example Usage:
    -------------
    >>> from logchimera.logchimera import fuzzing
    >>> from logchimera.datasets import get_example_data_for_fuzzing
    >>> fuzzed_path = fuzzing(get_example_data_for_fuzzing())
    """
    fuzzed_file_path = fuzz_data(file_path, output_dir=output_dir)
    return fuzzed_file_path


def function_test(test_string):
    return ""
