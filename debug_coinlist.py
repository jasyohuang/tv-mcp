#!/usr/bin/env python3
"""Debug coinlist loading"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from tradingview_mcp.core.services.coinlist import load_symbols
    from tradingview_mcp.core.utils.validators import COINLIST_DIR, EXCHANGE_SCREENER
    
    print(f"COINLIST_DIR: {COINLIST_DIR}")
    print(f"Directory exists: {os.path.exists(COINLIST_DIR)}")
    print(f"EXCHANGE_SCREENER: {EXCHANGE_SCREENER}")
    
    # Test loading symbols
    for exchange in ["kucoin", "binance", "bybit"]:
        symbols = load_symbols(exchange)
        print(f"{exchange}: {len(symbols)} symbols loaded")
        if symbols:
            print(f"  First few: {symbols[:3]}")
        else:
            # Debug path
            expected_path = os.path.join(COINLIST_DIR, f"{exchange}.txt")
            print(f"  Expected path: {expected_path}")
            print(f"  File exists: {os.path.exists(expected_path)}")
            
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
