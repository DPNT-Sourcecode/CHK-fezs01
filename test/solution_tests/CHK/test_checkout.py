import sys

sys.path.append("../lib")
from ..lib.solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout(self):
        assert checkout_solution.checkout("") == 0
