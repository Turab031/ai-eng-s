
import json

TOOL_DEFINITION = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get the current stock price given its ticker symbol.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker_symbol": {
                        "type": "string",
                        "description": "Ticker symbol of the stock, e.g. AAPL or TSLA."
                    }
                },
                "required": ["ticker_symbol"],
                "additionalProperties": False
            }
        }
    }
]

SYSTEM_PROMPT = """
You are a helpful stock market assistant.

When a user asks about a stock price:
1. Identify the correct stock ticker symbol.
2. Call the get_stock_price tool with the correct ticker symbol.
3. For comparisons, call the tool for each requested stock.
4. After receiving the tool results, present the information clearly
   and in a friendly manner.
5. Mention the currency and clarify that stock prices can change.

Do not invent stock prices. Only report prices returned by the tool.
Provide a brief explanation of your action without revealing private
chain-of-thought reasoning.
"""

FEW_SHOT_EXAMPLE = [
    # Example 1: Single stock price
    {
        "role": "user",
        "content": "How much is Apple stock right now?"
    },
    {
        "role": "assistant",
        "content": (
            "I'll look up Apple's current stock price using its "
            "ticker symbol, AAPL."
        ),
        "tool_calls": [
            {
                "id": "tool_call_01",
                "type": "function",
                "function": {
                    "name": "get_stock_price",
                    "arguments": json.dumps({
                        "ticker_symbol": "AAPL"
                    })
                }
            }
        ]
    },
    {
        "role": "tool",
        "tool_call_id": "tool_call_01",
        "content": json.dumps({
            "ticker": "AAPL",
            "price": 200.30,
            "currency": "USD"
        })
    },
    {
        "role": "assistant",
        "content": (
            "Apple (AAPL) is trading at $200.30 per share, "
            "according to the retrieved tool result. Stock prices "
            "fluctuate, so the price may have changed."
        )
    },

    # Example 2: Compare two stocks
    {
        "role": "user",
        "content": "Compare stock prices of Google and Microsoft."
    },
    {
        "role": "assistant",
        "content": (
            "I'll look up Alphabet (Google) under GOOGL and "
            "Microsoft under MSFT so I can compare their prices."
        ),
        "tool_calls": [
            {
                "id": "tool_call_02",
                "type": "function",
                "function": {
                    "name": "get_stock_price",
                    "arguments": json.dumps({
                        "ticker_symbol": "GOOGL"
                    })
                }
            },
            {
                "id": "tool_call_03",
                "type": "function",
                "function": {
                    "name": "get_stock_price",
                    "arguments": json.dumps({
                        "ticker_symbol": "MSFT"
                    })
                }
            }
        ]
    },
    {
        "role": "tool",
        "tool_call_id": "tool_call_02",
        "content": json.dumps({
            "ticker": "GOOGL",
            "price": 250.50,
            "currency": "USD"
        })
    },
    {
        "role": "tool",
        "tool_call_id": "tool_call_03",
        "content": json.dumps({
            "ticker": "MSFT",
            "price": 510.20,
            "currency": "USD"
        })
    },
    {
        "role": "assistant",
        "content": (
            "Here is the comparison based on the retrieved example "
            "results:\n"
            "- Alphabet (GOOGL): $250.50 per share\n"
            "- Microsoft (MSFT): $510.20 per share\n\n"
            "Microsoft has the higher share price in this example. "
            "Share price alone does not indicate which company is "
            "a better investment. Prices can change."
        )
    }
]


def run_agent(user_query:str)->None:
    return None


def run_agent(user_query:str)->None:
    """single turn agentic loop with cot reasoning"""
    message=[
        {"role":"system","content":SYSTEM_PROMPT},
        *FEW_SHOT_EXAMPLE,
        {"role":"user","content":user_query}
    ]
    
    print

def main():
    print("stock price agent(type 'quit'to exit)")
    
    print("-"*45)
    while True:
        query = input("\nYou:").strip()
        if not query:
            continue
        
        
        if  query.lower()in("quit","exit","q"):
            print("goodbye!")
            break
        
        run_agent(query)