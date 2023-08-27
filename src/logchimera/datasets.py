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
    -
    """
    with resources.path("logchimera.data", "labeled_log_data_18k.csv") as f:
        data_file_path = f
    return data_file_path
