from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


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
