import argparse
import os
from dotenv import load_dotenv
from bot import BasicSpotBot
import logging

def setup_logger():
    logging.basicConfig(
        filename='bot.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s]: %(message)s'
    )
    return logging.getLogger()

def main():
    setup_logger()
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    bot = BasicSpotBot(api_key, api_secret)

    parser = argparse.ArgumentParser(description="Feature-Packed Binance Spot Testnet Trading Bot")

    parser.add_argument("--symbol", type=str, required=True, help="Trading symbol, e.g., BTCUSDT")
    parser.add_argument("--side", type=str, choices=["BUY", "SELL"], required=True, help="Order side")
    parser.add_argument("--type", type=str, choices=["MARKET", "LIMIT"], required=True, help="Order type")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (for LIMIT orders)")

    args = parser.parse_args()

    
    current_price = bot.get_price(args.symbol)
    if current_price == 0:
        print("Could not fetch current price. Exiting.")
        return

    
    if args.type == "MARKET":
        required_amount = args.quantity * current_price
    elif args.type == "LIMIT":
        if args.price is None:
            print("Price required for LIMIT order")
            return
        required_amount = args.quantity * args.price
    else:
        print("Unsupported order type")
        return

    # Check available USDT balance
    available_balance = bot.check_balance("USDT")
    print(f"Available USDT: {available_balance} | Required: {required_amount}")

    if available_balance >= required_amount:
        if args.type == "MARKET":
            order = bot.place_market_order(args.symbol, args.side, args.quantity)
        elif args.type == "LIMIT":
            order = bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)
        else:
            print("Unsupported order type")
            return
    else:
        print(f"❌ Insufficient USDT balance: Available {available_balance}, Required {required_amount}")
        return

    if order:
        print("✅ Order placed successfully:")
        print(order)
    else:
        print("❌ Order failed. Check logs for details.")

if __name__ == "__main__":
    main()
