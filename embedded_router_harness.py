import sys
import asyncio
from core.router import CoreSwitchyardRouter

def main():
    # Read prompt from command-line argument passed via subprocess or terminal
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Perform routine maintenance clearance check on Cabinet B."
    
    router = CoreSwitchyardRouter()
    model_used, result = router.route(prompt)
    
    # Formatted tags parsed by Streamlit / UI components
    print(f"[ROUTING_MODEL]: {model_used}")
    print(f"[ROUTING_OUTCOME]: {result}")

if __name__ == "__main__":
    main()