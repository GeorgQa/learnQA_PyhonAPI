class TestExample:
    def test_check_math1(self):
        a = 5
        b = 9
        expected_sum = 14
        assert a+b == expected_sum, f"Sum of varibales a and b not equal to {expected_sum}"

    def test_check_math2(self):
        a = 11
        b = 9
        expected_sum = 20
        assert a+b == expected_sum, f"Sum of varibales a and b not equal to {expected_sum}"
