from importlib import resources

def get_pool_labeled_data():
    """Get path to the pool of labeled data (ground truth dataset) csv file [1].
    This dataset contains ~18k logs from nine publicly available datasets, namely Apache, BGL, HDFS, HealthApp, HPC, Mac, OpenStack, Spark, Windows
    
    Returns
    -------
    pathlib.PosixPath
        Path to file.

    References
    [1] Petrescu, S., den Hengst, F., Uta, A., and Rellermeyer, J. S. Log parsing evaluation in the era of modern software systems. In 34th IEEE International Symposium on Software Reliability Engineering (ISSRE) (2023).
    """
    with resources.path("logchimera.data", "labeled_log_data_18k.csv") as f:
        data_file_path = f
    return data_file_path

def get_pool_mixing_data():
    """Get path to the pool of mixing data.
    This dataset contains ~500 unique outlier logs, i.e., logs that appear <5% in the pool of 18k labeled data.
    
    Returns
    -------
    pathlib.PosixPath
        Path to file.
    """
    with resources.path("logchimera.data", "pool_mixing_data.csv") as f:
        data_file_path = f
    return data_file_path

def get_publicly_available_labeled_dataset(dataset_name):
    """Get path to one of the publicly available labeled datasets.
    Current options:
      - Apache
      - BGL
      - HPC
      - Mac
    Either of these datasets contains 2k log lines, with their corresponding templates.
    
    Returns
    -------
    pathlib.PosixPath
        Path to file.
    """
    with resources.path("logchimera.data", f"{dataset_name}_2k_labeled.csv") as f:
        data_file_path = f
    return data_file_path

def get_example_data_for_estimating_heterogeneity():
    """Get path to an example dataset for estimaing heterogeneity using logchimera.
    This dataset contains ~2k Apache logs
    
    Returns
    -------
    pathlib.PosixPath
        Path to file.

    """
    with resources.path("logchimera.data", "example_Apache_logs_for_estimating_heterogeneity.csv") as f:
        data_file_path = f
    return data_file_path 
