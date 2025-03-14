"""
Basic usage example for the MindRoot SDK.
"""

import os
import json
import sys

# Add the parent directory to the path so we can import the SDK
# Note: This is only needed for the example - when properly installed, you can import directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mrsdk import MindRootClient, MindRootError


def main():
    """Run a simple example using the MindRoot SDK."""
    # Check if API key is available
    api_key = os.environ.get("MINDROOT_API_KEY")
    if not api_key:
        print("Error: MINDROOT_API_KEY environment variable not set")
        print("Please set it with: export MINDROOT_API_KEY=your_api_key_here")
        sys.exit(1)
    
    # Initialize the client
    client = MindRootClient()
    
    try:
        # Example 1: Basic task
        print("\n===== EXAMPLE 1: Basic Task =====\n")
        instructions = "What is the square root of 256? Show your work."
        result = client.run_task("Assistant", instructions)
        print(f"Instructions: {instructions}")
        print(f"Result: {result['results']}")
        
        # Example 2: Task with trace
        print("\n===== EXAMPLE 2: Task with Trace =====\n")
        instructions = "Generate a list of the first 5 prime numbers."
        result = client.run_task("Assistant", instructions, include_trace=True)
        print(f"Instructions: {instructions}")
        print(f"Result: {result['results']}")
        print("\nCommand trace:")
        for cmd in result.get('full_results', []):
            print(f"Command: {cmd.get('cmd')}")
            if 'result' in cmd and cmd['result']:
                print(f"Result: {cmd['result']}\n")
    
    except MindRootError as e:
        print(f"MindRoot API Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
