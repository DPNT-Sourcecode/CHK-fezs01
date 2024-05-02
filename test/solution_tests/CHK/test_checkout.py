from lib.solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_with_empty_cart(self):
        assert checkout_solution.checkout("") == 0

    def test_checkout_with_no_offer(self):
        assert checkout_solution.checkout("ABC") == 100


