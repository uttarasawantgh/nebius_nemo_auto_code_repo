import os
import sys
import subprocess
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the Nebius client we just created
from nebius_tools.client import NebiusTokenFactoryClient

def run_pytest():
    """Executes pytest against the test suite and captures the result."""
    print("[+] Running automated test suite...")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v"],
        capture_output=True,
        text=True
    )
    return result.returncode == 0, result.stdout + "\n" + result.stderr

def main():
    if not os.getenv("NEBIUS_API_KEY"):
        print("[!] Error: NEBIUS_API_KEY environment variable is missing. Check your .env file.")
        sys.exit(1)

    nebius = NebiusTokenFactoryClient()
    print("[+] Initializing Autonomous Write-Run-Test Dev Loop...")
    
    # 1. Run tests
    passed, test_log = run_pytest()
    
    if not passed:
        print("[!] Test failure detected. Invoking Nebius Token Factory (NVIDIA Nemotron-3 Ultra)...")
        
        # 2. Query Nebius Token Factory for deep reasoning & bug diagnosis
        analysis = nebius.review_architecture(
            code_diff="app.py baseline evaluation and router harness", 
            test_output=test_log,
            model_name="nvidia/Nemotron-3-Ultra-550b-a55b"
        )
        
        print("\n" + "="*50)
        print("--- Nemotron-3 Ultra Root Cause Diagnosis ---")
        print("="*50)
        print(analysis)
        print("="*50 + "\n")
        print("[+] Handoff complete. Ready for Claude Code execution fix.")
    else:
        print("[+] All baseline tests passed successfully! Running secondary edge case verification via Nebius Nemotron Super...")
        
        # Optional: Generate additional coverage check via fast model
        sample_code = "def validate_telemetry(payload): return 'nominal' in payload.lower()"
        tests = nebius.generate_tests(code_snippet=sample_code, model_name="nvidia/Nemotron-3-Ultra-550b-a55b")
        print("\n--- Generated Edge Case Unit Tests ---")
        print(tests)

if __name__ == "__main__":
    main()