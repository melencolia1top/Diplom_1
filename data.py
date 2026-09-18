from praktikum.ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)

SAUCE = (INGREDIENT_TYPE_SAUCE, 'Соус Spicy', 50)
FILLING = (INGREDIENT_TYPE_FILLING, 'Мясо', 75)

REMOVE_CASES = [
    (0, 220),
    (1, 210),
]

MOVE_CASES = [
    (
        0,
        2,
        '= sauce Второй =\n'
        '= filling Третий =\n'
        '= sauce Первый =',
    ),
    (
        2,
        0,
        '= filling Третий =\n'
        '= sauce Первый =\n'
        '= sauce Второй =',
    ),
]

EXPECTED_RECEIPT = (
    '(==== Краторная булка ====)\n'
    '= sauce Соус Spicy =\n'
    '= filling Мясо =\n'
    '(==== Краторная булка ====)\n\n'
    'Price: 325'
)
