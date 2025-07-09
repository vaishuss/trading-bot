from binance.client import Client
import logging

class BasicSpotBot:
    def __init__(self, api_key, api_secret):
        self.logger = logging.getLogger()
        self.client = Client(api_key, api_secret)
        self.client.API_URL = 'https://testnet.binance.vision/api'  # Spot Testnet base URL
        self.logger.info("Spot Bot initialized")

    def get_price(self, symbol):
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            price = float(ticker['price'])
            self.logger.info(f"Current {symbol} price: {price}")
            return price
        except Exception as e:
            self.logger.error("Error fetching price: %s", str(e))
            return 0

    def check_balance(self, asset):
        try:
            balance = self.client.get_asset_balance(asset=asset)
            available = float(balance['free'])
            self.logger.info(f"{asset} available balance: {available}")
            return available
        except Exception as e:
            self.logger.error("Error fetching balance: %s", str(e))
            return 0

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            self.logger.info("Market order placed: %s", order)
            return order
        except Exception as e:
            self.logger.error("Error placing market order: %s", str(e))
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            self.logger.info("Limit order placed: %s", order)
            return order
        except Exception as e:
            self.logger.error("Error placing limit order: %s", str(e))
            return None
