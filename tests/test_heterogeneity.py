from logchimera.heterogeneity import _load_log_data

def test_load_log_data():
    """Test function."""
    log_lines = ["Header1","abc"]
    log_templates = ["Header2","abc"]
    log_variables = ["Header3","[]"]
    expected = [log_lines, log_templates, log_variables]
    actual = _load_log_data(input_file="tests/test_data/test_file_logchimera_heterogeneity_load_log_data.csv")
    print(actual)
    assert actual == expected, "Loading data does not work properly!"
