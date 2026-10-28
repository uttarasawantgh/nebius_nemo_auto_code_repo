import os
import sys
from nebius_tools.client import NebiusTokenFactoryClient

class CodeAuditor:
    """
    Automated code auditor leveraging NVIDIA open-source models via Nebius Token Factory 
    to perform static analysis, vulnerability checks, and structural optimization reviews.
    """
    def __init__(self):
        self.nebius_client = NebiusTokenFactoryClient()

    def audit_file(self, file_path: str, model_name: str = "nvidia/Nemotron-3-Ultra-550b-a55b") -> str:
        """Reads a local source file and audits its structure, error handling, and quality using Nebius Token Factory."""
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' not found."

        with open(file_path, "r", encoding="utf-8") as f:
            code_content = f.read()

        prompt = (
            f"Please perform a thorough architectural code audit on the following file ({file_path}). "
            "Identify potential bugs, security vulnerabilities, edge-case failure modes, "
            "and suggest clean refactoring improvements:\n\n"
            f"```python\n{code_content}\n```"
        )

        response = self.nebius_client.client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a principal software code auditor specializing in reliable, high-performance agentic systems."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "app.py"
    print(f"[*] Auditing '{target_file}' using Nebius Token Factory...")
    auditor = CodeAuditor()
    audit_report = auditor.audit_file(target_file)
    print("\n" + "="*60)
    print("--- Nebius Nemotron Code Audit Report ---")
    print("="*60)
    print(audit_report)
    print("="*60)