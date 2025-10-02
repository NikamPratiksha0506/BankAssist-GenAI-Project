# tools_config.py

import requests
from langchain_core.tools import tool

# --------------------
# Calculator Tool
# --------------------
@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

# --------------------
# Python REPL Tool
# --------------------
@tool
def python_repl(code: str) -> dict:
    """Execute Python code and return local variables."""
    try:
        local_vars = {}
        exec(code, {}, local_vars)
        return local_vars
    except Exception as e:
        return {"error": str(e)}

# --------------------
# Requests Tool (Currency conversion)
# --------------------
@tool
def requests_tool(query: str) -> str:
    """
    Convert currency using live API.
    Example query: '5000 INR to USD'
    """
    try:
        amount_str, rest = query.split(" ", 1)
        amount = float(amount_str)
        from_currency, to_currency = rest.split(" to ")
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
        res = requests.get(url).json()
        if "result" in res:
            return f"{amount} {from_currency} = {res['result']} {to_currency}"
        return str(res)
    except Exception as e:
        return str(e)
