from lib.solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_with_empty_cart(self):
        assert checkout_solution.checkout("") == 0

    def test_checkout_with_no_offer(self):
        assert checkout_solution.checkout("ABC") == 100

    def test_checkout_Item_A_with_offer(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_checkout_Mix_Item_with_and_with_offer(self):
        assert checkout_solution.checkout("AAAABCD") == 245

    def test_checkout_invaild_input(self):
        assert checkout_solution.checkout("AAAA-BCD") == -1

    def test_checkout_invaild_input_lower_case(self):
        assert checkout_solution.checkout("AAAAbBCD") == -1
