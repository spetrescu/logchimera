from logchimera.statistics import (
    compute_no_unique_words, 
    compute_no_unique_chars, 
    compute_no_unique_log_lengths, 
    compute_percentage_no_unique_words,
    compute_percentage_no_unique_chars,
    compute_percentage_no_unique_log_lengths
)

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

def test_compute_no_unique_log_lengths():
    """Test function for computing unique number of log lengths"""
    log_lines = ["Log line 1", "Log line 12", "Log line 123", "Log line 1234"] # there should be 4 unique log lengths
    expected = 4
    actual = compute_no_unique_log_lengths(log_lines=log_lines)
    assert actual == expected, "Function for computing unique number of log lengths in statistics module is not working!"

def test_compute_percentage_no_unique_words():
    """Test function for computing the percentage (weight) of number of unique words."""
    no_unique_words = 100
    expected = 0.01
    actual = compute_percentage_no_unique_words(no_unique_words=no_unique_words)
    assert actual == expected, "Function for computing the percentage (weight) of number of unique words in statistics module is not working!"

def test_compute_percentage_no_unique_log_lengths():
    """Test function for computing the percentage (weight) of unique number of log lengths."""
    no_unique_log_lengths = 4
    expected = 0.01
    actual = compute_percentage_no_unique_log_lengths(no_unique_log_lengths=no_unique_log_lengths)
    assert actual == expected, "Function for computing the percentage (weight) of unique number of log lengths in statistics module is not working!"
