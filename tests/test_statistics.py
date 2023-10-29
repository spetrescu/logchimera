from logchimera.statistics import compute_no_unique_words, compute_no_unique_chars

def test_compute_no_unique_words():
    """Test function for computing unique number of words"""
    log_lines = ["Log line 1", "Log line 2"] # there should be 4 words in these log lines, namely "Log", "line", "1", and "2".
    expected = 4
    actual = compute_no_unique_words(log_lines=log_lines)
    assert actual == expected, "Function for computing unique number of words in statistics module is not working!"

def test_compute_no_unique_chars():
    """Test function for computing unique number of characters"""
    log_lines = ["Log line 1", "Log line 2"] # there should be 10 chars
    expected = 10
    actual = compute_no_unique_chars(log_lines=log_lines)
    assert actual == expected, "Function for computing unique number of characters in statistics module is not working!"
