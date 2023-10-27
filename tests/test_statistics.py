from logchimera.statistics import compute_no_unique_words

def test_compute_no_unique_words():
    """Test function for computing unique number of words"""
    log_lines = ["Log line 1", "Log line 2"] # there should be 4 words in these log lines, namely "Log", "line", "1", and "2".
    expected = 4
    actual = compute_no_unique_words(log_lines=log_lines)
    assert actual == expected, "Function for computing unique number of words in statistics module is not working!"
