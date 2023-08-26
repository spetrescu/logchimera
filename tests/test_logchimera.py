from logchimera.logchimera import function_test

def test_function_test():
    """Test function."""
    expected = ""
    actual = function_test(test_string="")
    assert actual == expected, "Test function is not working!"