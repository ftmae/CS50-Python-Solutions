import requests
import sys

def get_cli_coin():
    try:
        coin = float(sys.argv[1])
        return coin
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")

def convert_coin_to_usd(coin):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        amount = coin*(response["bpi"]["USD"]["rate_float"])
        return amount
    except requests.RequestException:
        sys.exit()
        
def main():
    coin = get_cli_coin()
    amount = convert_coin_to_usd(coin)
    print(f"${amount:,.4f}")
if __name__ == "__main__":
    main()
