from logchimera.parser import parse_log_lines

def test_parsing_logs():
    """Test function for parsing logs function."""
    expected = [['mod_jk child workerEnv in error state 6', 'mod_jk child workerEnv in error state <*>'],
                ['mod_jk child workerEnv in error state 7', 'mod_jk child workerEnv in error state <*>']]
    actual = parse_log_lines(file_path="tests/test_data/parser_module/test_file_initial_parser_functionality.csv")
    actual = actual[["Content", "EventTemplate"]]
    actual = actual.values.tolist()
    assert actual == expected, "Sanity check parsing functionality is not working!"

def test_parsing_logs_number_of_logs():
    """Test function for checking if parsing returns the same number of logs."""
    expected = 3000
    actual = parse_log_lines(file_path="tests/test_data/parser_module/test_file_parser_for_checking_number_logs_parsed.csv")
    actual = actual[["Content", "EventTemplate"]]
    actual = len(actual.values.tolist())
    assert actual == expected, "Parser does not return the same number of logs as in the input file!"