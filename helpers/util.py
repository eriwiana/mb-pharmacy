import random
import string

from home.consts import CURRENCIES


def h_random(aLen=32):
    letters = string.ascii_letters
    digits = string.digits
    chars = "_<>,.+"
    return "".join(random.choices(letters + digits + chars, k=aLen))


def h_random_ascii(aLen=32):
    letters = string.ascii_letters
    digits = string.digits
    return "".join(random.choices(letters + digits, k=aLen))


def format_currency(amount, currency, shorten=False):
    currency = CURRENCIES[currency]

    if shorten:
        return "{} {}".format(
            currency.symbol, shorten_currency_value(amount / currency.base)
        )

    if currency.base > 1:
        return "{} {:,.2f}".format(currency.symbol, amount / currency.base)
    return "{} {:,}".format(currency.symbol, amount)


def shorten_currency_value(value):
    if value >= 1000000000:
        return str(value // 1000000000) + "B"
    elif value >= 1000000:
        return str(round(value / 1000000, 2)).rstrip("0").rstrip(".") + "M"
    elif value >= 1000:
        return str(round(value / 1000, 2)).rstrip("0").rstrip(".") + "K"
    else:
        return str(value)
