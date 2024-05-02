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

    # def test_checkout_buy_two_get_one_free(self):
    #     assert checkout_solution.checkout("AAABCDEE") == 245

    # def test_checkout_buy_four_get_two_free(self):
    #     assert checkout_solution.checkout("AAABBCDEEEE") == 325

    # def test_checkout_buy_five_get_two_free(self):
    #     assert checkout_solution.checkout("AAABBCDEEEEE") == 365

    # def test_checkout_buy_two_get_one_free_no_B(self):
    #     assert checkout_solution.checkout("AAACDEE") == 245

    # def test_checkout_multi_buy_with_one_offer_applied(self):
    #     assert checkout_solution.checkout("AAAAAAACEE") == 400

    # def test_checkout_multi_buy_with_both_offer_applied_to_one_item(self):
    #     assert checkout_solution.checkout("AAAAAAAACEE") == 430

    # def test_checkout_multi_buy_with_both_offer_applied_to_one_item_and_one_extra(self):
    #     assert checkout_solution.checkout("AAAAAAAAACEE") == 480

    def test_checkout_buy_two_get_one_free_itself(self):
        assert checkout_solution.checkout("AAFFF") == 120

    def test_checkout_buy_two_get_one_free_itself_but_no_need_free(self):
        assert checkout_solution.checkout("AAFF") == 120

    def test_one(self):
        assert checkout_solution.checkout("FFFF") == 30

    def test_two(self):
        assert checkout_solution.checkout("FFFFF") == 40

    def test_three(self):
        assert checkout_solution.checkout("FF") == 20

    def test_four(self):
        assert checkout_solution.checkout("FFF") == 20

    def test_five(self):
        assert checkout_solution.checkout("FFFFFF") == 40

    def test_six(self):
        assert checkout_solution.checkout("FFFFFFF") == 50

