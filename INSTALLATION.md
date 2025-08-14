# 🛠️ Installation Guide - TradingView MCP Server

## Prerequisites

- **Python 3.8+** (Python 3.10+ recommended)
- **UV Package Manager** (for dependency management)
- **Claude Desktop** (for MCP integration)
- **Internet Connection** (for TradingView data access)

## Step-by-Step Installation

### 1. Install UV Package Manager

UV is a fast Python package manager that handles all dependencies automatically.

#### On macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### On Windows:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Verify Installation:
```bash
uv --version
```

### 2. Configure Claude Desktop

#### Find Claude Desktop Config File:

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**Linux:**
```
~/.config/Claude/claude_desktop_config.json
```

#### Add MCP Server Configuration:

Open the config file and add this configuration:

```json
{
  "mcpServers": {
    "tradingview-mcp": {
      "command": "uv",
      "args": [
        "tool",
        "run",
        "--from",
        "git+https://github.com/atilaahmettaner/tradingview-mcp.git",
        "tradingview-mcp"
      ]
    }
  }
}
```

**If you already have other MCP servers configured:**
```json
{
  "mcpServers": {
    "existing-server": {
      "command": "...",
      "args": ["..."]
    },
    "tradingview-mcp": {
      "command": "uv",
      "args": [
        "tool",
        "run",
        "--from",
        "git+https://github.com/atilaahmettaner/tradingview-mcp.git",
        "tradingview-mcp"
      ]
    }
  }
}
```

### 3. Restart Claude Desktop

After adding the configuration:
1. **Completely quit Claude Desktop**
2. **Restart the application**
3. **Wait for initialization** (first startup may take 30-60 seconds)

### 4. Verify Installation

Ask Claude:
```
"Can you show me the available TradingView tools?"
```

You should see tools like:
- `top_gainers`
- `top_losers` 
- `bollinger_scan`
- `coin_analysis`
- `consecutive_candles_scan`

## Alternative Installation Methods

### Method 2: Local Development Setup

If you want to modify the code or run it locally:

```bash
# Clone the repository
git clone https://github.com/atilaahmettaner/tradingview-mcp.git
cd tradingview-mcp

# Install dependencies
uv sync

# Test the server
uv run python src/tradingview_mcp/server.py

# Run with MCP Inspector (for debugging)
uv run mcp dev src/tradingview_mcp/server.py
```

#### Claude Desktop Config for Local Setup:
```json
{
  "mcpServers": {
    "tradingview-mcp-local": {
      "command": "uv",
      "args": ["run", "python", "src/tradingview_mcp/server.py"],
      "cwd": "/path/to/your/tradingview-mcp"
    }
  }
}
```

### Method 3: Python Virtual Environment

If you prefer traditional Python environments:

```bash
# Clone repository
git clone https://github.com/atilaahmettaner/tradingview-mcp.git
cd tradingview-mcp

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .

# Run server
python src/tradingview_mcp/server.py
```

## Testing Your Installation

### Basic Functionality Test

Ask Claude these questions to verify everything works:

1. **Market Screening:**
   ```
   "Show me top 5 crypto gainers on KuCoin in 15 minutes"
   ```

2. **Technical Analysis:**
   ```
   "Analyze Bitcoin with all technical indicators"
   ```

3. **Pattern Detection:**
   ```
   "Find coins with Bollinger Band squeeze (BBW < 0.05)"
   ```

### Expected Results

You should get detailed responses with:
- ✅ Real-time price data
- ✅ Technical indicator values
- ✅ Bollinger Band ratings
- ✅ Market analysis insights

## Troubleshooting

### Issue 1: "Command not found: uv"

**Solution:** UV is not installed or not in PATH
```bash
# Re-run UV installation
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH (if needed)
export PATH="$HOME/.cargo/bin:$PATH"
```

### Issue 2: Claude doesn't see the MCP server

**Solution:** Configuration or restart issue
1. Check JSON syntax in config file
2. Ensure proper file path
3. Restart Claude Desktop completely
4. Wait 30-60 seconds for initialization

### Issue 3: "No data found" errors

**Solution:** API or exchange issue
- Try different exchanges (KuCoin usually works best)
- Use standard symbols (e.g., "BTCUSDT", "ETHUSDT")
- Check timeframe format ("15m", "1h", "1D")

### Issue 4: Slow responses

**Solution:** Normal behavior for first requests
- First request may take 10-30 seconds (warming up)
- Subsequent requests are much faster
- Consider smaller limits (5-10 items vs 50)

### Issue 5: Permission errors

**Solution:** Directory or file permissions
```bash
# Fix permissions
chmod +x ~/.local/bin/uv
chmod -R 755 ~/path/to/tradingview-mcp
```

## Performance Optimization

### Best Practices:
1. **Use KuCoin exchange** - Most reliable data source
2. **Start with standard timeframes** - 15m, 1h, 1D work best  
3. **Limit results** - Use 5-10 items for faster responses
4. **Cache requests** - Avoid rapid repeated requests

### Recommended Exchanges by Reliability:
1. 🥇 **KuCoin** - Fastest, most reliable
2. 🥈 **BIST** - Turkish stocks, very stable
3. 🥉 **Binance** - Good but may have rate limits

## Advanced Configuration

### Custom Timeouts:
```json
{
  "mcpServers": {
    "tradingview-mcp": {
      "command": "uv",
      "args": [
        "tool",
        "run", 
        "--from",
        "git+https://github.com/atilaahmettaner/tradingview-mcp.git",
        "tradingview-mcp"
      ],
      "env": {
        "TIMEOUT": "30"
      }
    }
  }
}
```

### Development Mode:
```json
{
  "mcpServers": {
    "tradingview-mcp-dev": {
      "command": "uv",
      "args": ["run", "mcp", "dev", "src/tradingview_mcp/server.py"],
      "cwd": "/path/to/tradingview-mcp"
    }
  }
}
```

## Getting Help

1. **Check the logs:** Claude Desktop → Settings → Developer → View Logs
2. **GitHub Issues:** [Report bugs here](https://github.com/atilaahmettaner/tradingview-mcp/issues)
3. **Documentation:** [Main README](README.md)
4. **Test locally:** Use `uv run python src/tradingview_mcp/server.py` to debug

---

**Happy Trading! 📈**
