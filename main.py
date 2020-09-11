
import requests
import json

# url - can I use Blockchain URL?
BITCOIN_API_URL = 'https://blockchain.info/ticker'


# def bitcoin price function
def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_dict = json.loads(response.text)
    return response_dict["USD"]["last"]


if __name__ == '__main__':
    print(get_latest_bitcoin_price())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
