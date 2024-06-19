from shop_cosmed import Cosmed
import pytest


def test_cosmed_add_1_item_to_cart():
    cosmed = Cosmed()
    try:
        cosmed.check_cookie_dialog()
        cosmed.check_ads()
        cosmed.enter_search_key("衛生紙")
        cosmed.add_first_item_to_cart()
        assert cosmed.get_current_cart_num() == 1
    except Exception as e:
        cosmed.quit_chrome()
        pytest.fail(f"Test failed due to exception: {repr(e)}")


        
