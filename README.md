# trading-bot
Binance Futures Testnet Python Trading Bot
A simple yet powerful Python-based trading bot for the Binance Futures Testnet (USDT-M). Supports Market, Limit, and Stop-Limit orders with both CLI and GUI (Tkinter) interfaces.

Features
✅ Place Market and Limit orders
✅ Support both Buy and Sell sides
✅ Use official Binance Futures Testnet API (REST via python-binance)
✅ Accept and validate user input via Command-line (CLI) and Graphical UI (Tkinter)
✅ Output order details and execution status
✅ Implement robust logging and error handling
✅ Cancel open orders by Order ID
✅ Bonus: Stop-Limit order type
✅ Bonus: Simple Tkinter GUI interface
Project Structure

FuturesTradingBot/
├── bot.py               # Main API interaction class
├── main.py              # Command-line interface for order management
├── futures_ui.py        # Graphical Tkinter-based trading UI
├── .env                 # API credentials (never share publicly)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

Getting Started
Install Dependencies:
pip install -r requirements.txt
Setup API Keys

1. Register at: https://testnet.binancefuture.com/en/futures/BTCUSDT
2. Generate API Key and Secret from API Management
3. Create a .env file in the project directory:
API_KEY=your_testnet_api_key_here
API_SECRET=your_testnet_api_secret_here

Usage
Command-Line (CLI)
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 75000
python main.py --symbol BTCUSDT --side SELL --type STOP --quantity 0.01 --stop_price 73000 --price 72900
python main.py --symbol BTCUSDT --cancel 12345678
Graphical User Interface (Tkinter)
python futures_ui.py
Fill out the form for symbol, side, order type, quantity, price, and stop price (if applicable) and click 'Place Order'
Logging
All actions and errors are logged to: futures_bot.log
Requirements
Python 3.8+
Binance Testnet API credentials
Support
For queries or help, contact me at sdk9750@gmail.com
Done ✅
Full requirements fulfilled with bonus enhancements.
