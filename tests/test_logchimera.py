from logchimera.logchimera import estimate_heterogeneity

def test_estimate_heterogeneity():
    """Test estimating heterogeneity sanity check."""
    expected = 0.01
    actual = estimate_heterogeneity(file_path="tests/test_data/logchimera_module/test_file_logchimera_for_estimating_heterogeneity.csv")
    assert actual == expected, "Estimating heterogeneity function in logchimera module is not working!"

def test_estimate_heterogeneity_for_file_with_more_words_than_upper_limit_for_heterogeneity():
    """Testing heterogeneity estimation functionality when file has more words than upper bound."""
    expected = 0.446
    actual = estimate_heterogeneity(file_path="tests/test_data/logchimera_module/test_file_logchimera_for_upper_bound_word_limit_heterogeneity_estimation.csv")
    assert actual == expected, "Estimating heterogeneity function in logchimera module is not working for the case when the data contains more words than the upper bound limit!"

def test_estimate_heterogeneity_for_file_with_more_chars_than_upper_limit_for_heterogeneity():
    """Testing heterogeneity estimation functionality when file has more characters than upper bound."""
    expected = 0.208
    actual = estimate_heterogeneity(file_path="tests/test_data/logchimera_module/test_file_logchimera_for_upper_bound_character_limit_heterogeneity_estimation.csv")
    assert actual == expected, "Estimating heterogeneity function in logchimera module is not working for the case when the data contains more characters than the upper bound limit!"

def test_estimate_heterogeneity_for_file_with_more_log_lengths_than_upper_limit_for_heterogeneity():
    """Testing heterogeneity estimation functionality when file has more log lengths than upper bound."""
    expected = 0.406
    actual = estimate_heterogeneity(file_path="tests/test_data/logchimera_module/test_file_logchimera_for_upper_bound_log_length_limit_heterogeneity_estimation.csv")
    assert actual == expected, "Estimating heterogeneity function in logchimera module is not working for the case when the data contains more log lengths than the upper bound limit!"