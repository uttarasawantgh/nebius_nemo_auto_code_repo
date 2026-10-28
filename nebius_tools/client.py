import os
from openai import OpenAI

class NebiusTokenFactoryClient:
    """
    Client wrapper for Nebius Token Factory serving NVIDIA open-weight models 
    via an OpenAI-compatible REST API.
    """
    def __init__(self):
        self.api_key = os.getenv("NEBIUS_API_KEY")
        # Official Nebius Token Factory base URL
        self.base_url = os.getenv("NEBIUS_BASE_URL", "https://api.tokenfactory.nebius.com/v1/")
        
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key
        )

    def generate_tests(self, code_snippet: str, model_name: str = "nvidia/Nemotron-3-Ultra-550b-a55b") -> str:
        """
        Synthesizes automated unit tests using fast, everyday Nemotron models 
        to stretch developer credits and maintain high responsiveness.
        """
        response = self.client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system", 
                    "content": "You are an expert software testing agent. Generate comprehensive pytest cases for the provided code. Output ONLY valid executable Python code inside standard code blocks."
                },
                {
                    "role": "user", 
                    "content": f"Write unit tests for the following code:\n\n```python\n{code_snippet}\n```"
                }
            ],
            temperature=0.1
        )
        return response.choices[0].message.content

    def review_architecture(self, code_diff: str, test_output: str, model_name: str = "nvidia/Nemotron-3-Ultra-550b-a55b") -> str:
        """
        Performs deep architectural debugging and root-cause analysis 
        using advanced reasoning models like Nemotron-3 Ultra.
        """
        response = self.client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system", 
                    "content": "You are a principal software engineer. Analyze code diffs and test failure outputs to pinpoint bugs and recommend structural fixes."
                },
                {
                    "role": "user", 
                    "content": f"Test Execution Failure Output:\n{test_output}\n\nRecent Code Changes:\n{code_diff}\n\nIdentify the root cause and provide fix instructions."
                }
            ],
            temperature=0.2
        )
        return response.choices[0].message.content