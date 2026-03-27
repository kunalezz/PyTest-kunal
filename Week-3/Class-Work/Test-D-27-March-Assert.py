# create one Function, ask test equality (BTW two integer and between two strings)

# The function we are testing
def check_equality(val1, val2):
    return val1 == val2


class TestEqualityLogic:
    # Testing Integers
    def test_integer_equality(self):
        assert check_equality(10, 10) is True
        assert check_equality(10, 5) is False

    # Testing Strings
    def test_string_equality(self):
        assert check_equality("hello", "hello") is True
        assert check_equality("hello", "world") is False


