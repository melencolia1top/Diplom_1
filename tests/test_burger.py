from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


def make_bun(name='Краторная булка', price=100):
    bun = Mock(spec=Bun)
    bun.get_name.return_value = name
    bun.get_price.return_value = price
    return bun


def make_ingredient(ingredient_type, name, price):
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = ingredient_type
    ingredient.get_name.return_value = name
    ingredient.get_price.return_value = price
    return ingredient


class TestBurger:
    def test_new_burger_has_no_bun(self, burger):
        assert burger.bun is None

    def test_new_burger_has_no_ingredients(self, burger):
        assert burger.ingredients == []

    def test_set_buns_sets_bun(self, burger):
        bun = make_bun()

        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredient_adds_ingredient(self, burger):
        ingredient = make_ingredient(INGREDIENT_TYPE_SAUCE, 'Соус', 50)

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize(
        'index, expected_ingredients',
        [
            (0, ['second']),
            (1, ['first']),
        ],
    )
    def test_remove_ingredient_removes_selected_ingredient(
        self,
        burger,
        index,
        expected_ingredients,
    ):
        burger.ingredients = ['first', 'second']

        burger.remove_ingredient(index)

        assert burger.ingredients == expected_ingredients

    def test_remove_ingredient_with_invalid_index_raises_error(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    @pytest.mark.parametrize(
        'index, new_index, expected_ingredients',
        [
            (0, 2, ['second', 'third', 'first']),
            (2, 0, ['third', 'first', 'second']),
        ],
    )
    def test_move_ingredient_moves_selected_ingredient(
        self,
        burger,
        index,
        new_index,
        expected_ingredients,
    ):
        burger.ingredients = ['first', 'second', 'third']

        burger.move_ingredient(index, new_index)

        assert burger.ingredients == expected_ingredients

    def test_move_ingredient_with_invalid_index_raises_error(self, burger):
        burger.ingredients = ['first']

        with pytest.raises(IndexError):
            burger.move_ingredient(1, 0)

    def test_get_price_returns_price_of_two_buns_and_ingredients(self, burger):
        bun = make_bun(price=100)
        sauce = make_ingredient(INGREDIENT_TYPE_SAUCE, 'Соус', 50)
        filling = make_ingredient(INGREDIENT_TYPE_FILLING, 'Начинка', 75)
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        assert burger.get_price() == 325

    def test_get_price_without_bun_raises_error(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_returns_formatted_receipt(self, burger):
        bun = make_bun(name='Краторная булка', price=100)
        sauce = make_ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Spicy', 50)
        filling = make_ingredient(INGREDIENT_TYPE_FILLING, 'Мясо', 75)
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        expected_receipt = (
            '(==== Краторная булка ====)\n'
            '= sauce Соус Spicy =\n'
            '= filling Мясо =\n'
            '(==== Краторная булка ====)\n\n'
            'Price: 325'
        )

        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_without_bun_raises_error(self, burger):
        with pytest.raises(AttributeError):
            burger.get_receipt()