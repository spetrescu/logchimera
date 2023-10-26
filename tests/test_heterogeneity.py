from logchimera.heterogeneity import _load_log_data, _parse_logs_for_estimating_heterogeneity

def test_load_log_data():
    """Test function."""
    log_lines = ["Header1","abc"]
    log_templates = ["Header2","abc"]
    log_variables = ["Header3","[]"]
    expected = [log_lines, log_templates, log_variables]
    actual = _load_log_data(input_file="tests/test_data/test_file_logchimera_heterogeneity_load_log_data.csv")
    print(actual)
    assert actual == expected, "Loading data does not work properly!"

def test_parse_logs_for_estimating_heterogeneity():
    """Test function."""
    log_lines = ["mod_jk child workerEnv in error state 6", "mod_jk child workerEnv in error state 7", "mod_jk child workerEnv in error state 7"]
    log_templates = ["mod_jk child workerEnv in error state <*>", "mod_jk child workerEnv in error state <*>", "mod_jk child workerEnv in error state <*>"]
    expected = [[item1, item2] for item1, item2 in zip(log_lines, log_templates)]
    actual = _parse_logs_for_estimating_heterogeneity("tests/test_data/test_file_logchimera_heterogeneity_parse_logs_for_estimating_heterogeneity.csv")
    assert actual == expected, "Loading data does not work properly!"
    