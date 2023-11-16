from logchimera.logchimera import estimate_heterogeneity

def test_estimate_heterogeneity():
    """Test estimating heterogeneity sanity check."""
    expected = 0.01
    actual = estimate_heterogeneity(file_path="tests/test_data/logchimera_module/test_file_logchimera_for_estimating_heterogeneity.csv")
    assert actual == expected, "Estimating heterogeneity function in logchimera module is not working!"