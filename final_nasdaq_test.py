#!/usr/bin/env python3
"""Final NASDAQ test"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("🚀 Testing NASDAQ with MCP server...")

# Test coin_analysis directly
try:
    from src.tradingview_mcp.server import coin_analysis
    
    print("\n📊 Testing AAPL analysis...")
    result = coin_analysis(symbol="AAPL", exchange="NASDAQ", timeframe="1D")
    
    if "error" in result:
        print(f"❌ Error: {result['error']}")
    else:
        print(f"✅ Success!")
        print(f"   Symbol: {result.get('symbol', 'N/A')}")
        price = result.get('price_data', {}).get('current_price')
        change = result.get('price_data', {}).get('change_percent')
        print(f"   Price: ${price} ({change:+.2f}%)" if price and change else "   Price: N/A")
        bbw = result.get('bollinger_analysis', {}).get('bbw')
        print(f"   BBW: {bbw}" if bbw else "   BBW: N/A")
        
except Exception as e:
    print(f"❌ Analysis failed: {e}")
    import traceback
    traceback.print_exc()

# Test top_gainers
try:
    print("\n📈 Testing NASDAQ top gainers...")
    from src.tradingview_mcp.server import top_gainers
    
    result = top_gainers(exchange="NASDAQ", limit=3)
    
    if "error" in result:
        print(f"❌ Error: {result['error']}")
    else:
        symbols = result.get('symbols', [])
        print(f"✅ Found {len(symbols)} gainers")
        for i, symbol in enumerate(symbols[:3], 1):
            name = symbol.get('symbol', 'N/A')
            change = symbol.get('changePercent', 0)
            print(f"   {i}. {name}: {change:+.2f}%")
            
except Exception as e:
    print(f"❌ Top gainers failed: {e}")

print("\n🏁 Test completed!")
