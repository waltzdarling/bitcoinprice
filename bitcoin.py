import requests
import json

# This is bitcoin price url
BITCOIN_API_URL = 'https://blockchain.info/ticker'


def get_api_response():
    response = requests.get(BITCOIN_API_URL)
    response_dict = json.loads(response.text)
    return response_dict


api_response = get_api_response()

print("Get today's Bitcoin price in your currency of choice")


def get_currencies(internal_api_response):
    currencies_list = list(internal_api_response)
    return currencies_list


def user_input(internal_currencies):
    while True:
        user_currency = input("Enter your currency: ")

        for currency in internal_currencies:
            if user_currency.upper() == currency:
                print(currency)
                return currency

        print("Invalid request, choose from supported" + " currencies")


def get_latest_bitcoin_price(internal_api_response, correct_user_currency):
    return internal_api_response[correct_user_currency]["last"]


def main(local_api_response, user_currency_amounts, user_currencies, conversion_results):
    currencies = get_currencies(local_api_response)
    currencies_str = ""

    for i, currency in enumerate(currencies):
        currencies_str += currency
        if i != len(currencies) - 1:
            currencies_str += ", "

    print(f"Supported currencies are: {currencies_str}")

    correct_user_currency = user_input(currencies)

    bitcoin_price_in_user_currency = get_latest_bitcoin_price(local_api_response, correct_user_currency)

    currency_amount = float(input("Please enter currency amount:"))
    bitcoins_amount = currency_amount / bitcoin_price_in_user_currency

    user_currency_amounts.append(currency_amount)
    user_currencies.append(correct_user_currency)
    conversion_results.append(bitcoins_amount)

    for i, user_currency_amount in enumerate(user_currency_amounts):
        print(f"Iteration {i} result:")
        print(f"{user_currency_amount} {user_currencies[i]} = {conversion_results[i]} Bitcoins")


user_currency_amounts = []
user_currencies = []
conversion_results = []

while True:
    main(api_response, user_currency_amounts, user_currencies, conversion_results)
    convert_more = input("Do you want to convert one more time? y/n: ")
    if convert_more != "y":
        break