import asyncio
import sys
import subprocess
from dotenv import load_dotenv  # <--- 1. Import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions, tool, create_sdk_mcp_server, AssistantMessage

# <--- 2. Load environment variables from .env file right at the start
load_dotenv()

@tool(
    name="switchyard_route_request",
    description="Route cell tower safety prompts through the local embedded router harness for tri-tiered vLLM evaluation.",
    input_schema={"prompt": str}
)
async def switchyard_route_tool(args):
    prompt = args.get("prompt")
    try:
        # Call the local embedded harness worker process
        result = subprocess.run(
            ["python3", "embedded_router_harness.py", prompt],
            capture_output=True,
            text=True,
            timeout=90.0
        )
        output_text = result.stdout if result.returncode == 0 else f"Harness Error: {result.stderr}"
        response_result = f"Embedded Router Output:\n{output_text}"
    except Exception as e:
        response_result = f"Subprocess Execution Failed: {e}"
        
    return {"content": [{"type": "text", "text": response_result}]}

async def main():
    # Receive input from app.py
    user_prompt = sys.argv[1] if len(sys.argv) > 1 else "Examine the tower safety logs."
    
    # Pass the required 'name' argument here
    server = create_sdk_mcp_server(name="switchyard_mcp_server", tools=[switchyard_route_tool])
    options = ClaudeAgentOptions(
        mcp_servers={"switchyard_server": server},
        allowed_tools=["mcp__switchyard_server__switchyard_route_request", "Read", "Write"]
    )
    
    async for message in query(prompt=f"Supervise and execute diagnostic for: {user_prompt}", options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)

if __name__ == "__main__":
    asyncio.run(main())