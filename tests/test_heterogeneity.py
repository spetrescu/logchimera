from logchimera.heterogeneity import _load_log_data, _parse_logs_for_estimating_heterogeneity, _sample_2k_logs_using_parsing, estimate_heterogeneity_generic_file

def test_load_log_data():
    """Test function."""
    log_lines = ["Header1","abc"]
    log_templates = ["Header2","abc"]
    log_variables = ["Header3","[]"]
    expected = [log_lines, log_templates, log_variables]
    actual = _load_log_data(input_file="tests/test_data/test_file_logchimera_heterogeneity_load_log_data.csv")
    assert actual == expected, "Loading data does not work properly!"

def test_parse_logs_for_estimating_heterogeneity():
    """Test function."""
    log_lines = ["mod_jk child workerEnv in error state 6", "mod_jk child workerEnv in error state 7", "mod_jk child workerEnv in error state 7"]
    log_templates = ["mod_jk child workerEnv in error state <*>", "mod_jk child workerEnv in error state <*>", "mod_jk child workerEnv in error state <*>"]
    expected = [[item1, item2] for item1, item2 in zip(log_lines, log_templates)]
    actual = _parse_logs_for_estimating_heterogeneity("tests/test_data/test_file_logchimera_heterogeneity_parse_logs_for_estimating_heterogeneity.csv")
    assert actual == expected, "Parsing functionality for estimating heterogeneity not working!"
    
def test_sample_2k_logs_using_parsing():
    """Test function."""
    log_lines = ["mod_jk child workerEnv in error state 6", "mod_jk child workerEnv in error state 7", "mod_jk child workerEnv in error state 7"]
    log_templates = ["mod_jk child workerEnv in error state <*>", "mod_jk child workerEnv in error state <*>", "mod_jk child workerEnv in error state <*>"]
    log_data = [[item1, item2] for item1, item2 in zip(log_lines, log_templates)]
    expected = log_data
    actual = _sample_2k_logs_using_parsing(log_data)
    assert actual == expected, "Sampling functionality for estimating heterogeneity using log parsing not working!"

def test_estimate_heterogeneity_generic_file_sanity_check():
    """Test function for estimate_heterogeneity_generic_file() sanity check"""
    expected = 0.01
    actual = estimate_heterogeneity_generic_file("tests/test_data/test_file_sanity_check_estimating_heterogeneity.csv")
    assert actual == expected, "The output for estimating heterogeneity for generic file is failing!"