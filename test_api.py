#!/usr/bin/env python3
"""
Test script for TradingView MCP server API
"""

import sys
import subprocess
import json
from pathlib import Path

def test_tool_via_subprocess(tool_name: str, **kwargs):
    """Test a tool by running it via subprocess"""
    try:
        # Create a simple test script that imports and runs the tool
        script_content = f'''
import sys
import json
sys.path.insert(0, "src")

from tradingview_mcp.server import {tool_name}

try:
    result = {tool_name}(**{kwargs})
    print("SUCCESS:")
    print(json.dumps(result, indent=2, default=str))
except Exception as e:
    print(f"ERROR: {{e}}")
    import traceback
    traceback.print_exc()
'''
        
        # Write to temp file
        test_file = Path("temp_test.py")
        test_file.write_text(script_content)
        
        # Run with uv
        result = subprocess.run(
            ["uv", "run", "python", "temp_test.py"],
            capture_output=True,
            text=True,
            cwd="."
        )
        
        print(f"\n{'='*50}")
        print(f"Testing: {tool_name}({kwargs})")
        print(f"{'='*50}")
        
        if result.returncode == 0:
            print("STDOUT:", result.stdout)
        else:
            print("STDERR:", result.stderr)
            print("STDOUT:", result.stdout)
        
        # Cleanup
        test_file.unlink(missing_ok=True)
        
        return result
        
    except Exception as e:
        print(f"Test failed: {e}")
        return None

def main():
    print("🚀 TradingView MCP Server API Test")
    print("=" * 60)
    
    # Test 1: Top gainers
    test_tool_via_subprocess("top_gainers", 
                           exchange="KUCOIN", 
                           timeframe="15m", 
                           limit=5)
    
    # Test 2: Bollinger scan
    test_tool_via_subprocess("bollinger_scan",
                           exchange="KUCOIN",
                           timeframe="4h",
                           bbw_threshold=0.04,
                           limit=5)
    
    # Test 3: Volume breakout
    test_tool_via_subprocess("volume_breakout_scanner",
                           exchange="KUCOIN",
                           timeframe="15m",
                           volume_multiplier=2.0,
                           limit=5)
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    main()
