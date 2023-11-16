from logchimera.parser import parse_log_lines

def test_parsing_logs():
    """Test function for parsing logs function."""
    expected = [['mod_jk child workerEnv in error state 6', 'mod_jk child workerEnv in error state <*>'],
                ['mod_jk child workerEnv in error state 7', 'mod_jk child workerEnv in error state <*>']]
    actual = parse_log_lines(file_path="tests/test_data_parser/test_file_initial_parser_functionality.csv")
    actual = actual[["Content", "EventTemplate"]]
    actual = actual.values.tolist()
    assert actual == expected, "Test function is not working!"