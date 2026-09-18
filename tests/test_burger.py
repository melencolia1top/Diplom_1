import pytest

from data import (
    EXPECTED_RECEIPT,
    FILLING,
    MOVE_CASES,
    REMOVE_CASES,
    SAUCE,
)
from helpers import make_bun, make_ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)


class TestBurger:
    def test_set_buns_changes_burger_price(self, burger):
        burger.set_buns(make_bun(price=100))

        assert burger.get_price() == 200

    def test_add_ingredient_changes_burger_price(self, burger):
        burger.set_buns(make_bun(price=100))
        burger.add_ingredient(
            make_ingredient(INGREDIENT_TYPE_SAUCE, 'Соус', 50)
        )

        assert burger.get_price() == 250

    @pytest.mark.parametrize('index, expected_price', REMOVE_CASES)
    def test_remove_ingredient_changes_burger_price(
        self,
        burger,
        index,
        expected_price,
    ):
        burger.set_buns(make_bun(price=100))
        burger.add_ingredient(
            make_ingredient(INGREDIENT_TYPE_SAUCE, 'Первый', 10)
        )
        burger.add_ingredient(
            make_ingredient(INGREDIENT_TYPE_SAUCE, 'Второй', 20)
        )

        burger.remove_ingredient(index)

        assert burger.get_price() == expected_price

    def test_remove_ingredient_with_invalid_index_raises_error(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    @pytest.mark.parametrize(
        'index, new_index, expected_order',
        MOVE_CASES,
    )
    def test_move_ingredient_changes_order_in_receipt(
        self,
        burger,
        index,
        new_index,
        expected_order,
    ):
        burger.set_buns(make_bun())
        burger.add_ingredient(
            make_ingredient(INGREDIENT_TYPE_SAUCE, 'Первый', 10)
        )
        burger.add_ingredient(
            make_ingredient(INGREDIENT_TYPE_SAUCE, 'Второй', 20)
        )
        burger.add_ingredient(
            make_ingredient(INGREDIENT_TYPE_FILLING, 'Третий', 30)
        )

        burger.move_ingredient(index, new_index)

        assert expected_order in burger.get_receipt()

    def test_move_ingredient_with_invalid_index_raises_error(self, burger):
        burger.add_ingredient(
            make_ingredient(INGREDIENT_TYPE_SAUCE, 'Соус', 50)
        )

        with pytest.raises(IndexError):
            burger.move_ingredient(1, 0)

    def test_get_price_returns_price_of_bun_and_ingredients(self, burger):
        burger.set_buns(make_bun(price=100))
        burger.add_ingredient(make_ingredient(*SAUCE))
        burger.add_ingredient(make_ingredient(*FILLING))

        assert burger.get_price() == 325

    def test_get_price_without_bun_raises_error(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_returns_formatted_receipt(self, burger):
        burger.set_buns(make_bun())
        burger.add_ingredient(make_ingredient(*SAUCE))
        burger.add_ingredient(make_ingredient(*FILLING))

        assert burger.get_receipt() == EXPECTED_RECEIPT

    def test_get_receipt_without_bun_raises_error(self, burger):
        with pytest.raises(AttributeError):
            burger.get_receipt()
