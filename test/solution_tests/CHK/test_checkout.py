from lib.solutions.CHK import checkout_solution


class TestCheckout:
    # def test_checkout_invaild_input(self):
    #     assert checkout_solution.checkout("AAAA-BCD") == -1

    # def test_checkout_invaild_input_lower_case(self):
    #     assert checkout_solution.checkout("AAAAbBCD") == -1

    # def test_checkout_with_empty_cart(self):
    #     assert checkout_solution.checkout("") == 0

    # def test_checkout_with_no_offer(self):
    #     assert checkout_solution.checkout("ABC") == 100

    # def test_checkout_Item_A_with_offer(self):
    #     assert checkout_solution.checkout("AAA") == 130

    # def test_checkout_Mix_Item_with_and_with_offer(self):
    #     assert checkout_solution.checkout("AAAABCD") == 245

    def test_checkout_buy_two_get_one_free(self):
        assert checkout_solution.checkout("AAABCDEE") == 245

    def test_checkout_buy_four_get_two_free(self):
        assert checkout_solution.checkout("AAABBCDEEEE") == 325

    def test_checkout_buy_five_get_two_free(self):
        assert checkout_solution.checkout("AAABBCDEEEEE") == 365

    def test_checkout_buy_two_get_one_free_no_B(self):
        assert checkout_solution.checkout("AAACDEE") == 245



