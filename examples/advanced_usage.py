"""
Advanced usage examples for the MindRoot SDK.
"""

import os
import json
import sys
import time
from typing import Dict, Any

# Add the parent directory to the path so we can import the SDK
# Note: This is only needed for the example - when properly installed, you can import directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mrsdk import MindRootClient, MindRootError


def process_results(result: Dict[str, Any]) -> None:
    """Helper to process and display command results nicely."""
    if 'full_results' not in result:
        print(f"Result: {result['results']}")
        return
    
    print(f"Final result: {result['results']}")
    print(f"Log ID: {result.get('log_id', 'N/A')}")
    print("\nCommand execution trace:")
    
    for i, cmd in enumerate(result.get('full_results', [])):
        cmd_name = cmd.get('cmd', 'unknown')
        print(f"\n[{i+1}] Command: {cmd_name}")
        
        # For certain commands, format the output nicely
        if cmd_name == 'execute_command' and 'args' in cmd:
            print(f"  Script:\n{cmd['args'].get('cmd')}")
        elif 'args' in cmd and cmd['args']:
            print(f"  Args: {json.dumps(cmd['args'], indent=2)}")
            
        if 'result' in cmd and cmd['result']:
            if isinstance(cmd['result'], str) and len(cmd['result']) > 500:
                # Truncate long results
                print(f"  Result: {cmd['result'][:500]}...\n  [truncated]")  
            else:
                print(f"  Result: {cmd['result']}")


def main():
    """Run advanced examples using the MindRoot SDK."""
    # Check if API key is available
    api_key = os.environ.get("MINDROOT_API_KEY")
    if not api_key:
        print("Error: MINDROOT_API_KEY environment variable not set")
        print("Please set it with: export MINDROOT_API_KEY=your_api_key_here")
        sys.exit(1)
    
    # Initialize the client with a longer timeout and required base_url
    client = MindRootClient(
        base_url="http://localhost:8010",  # Required base URL for the MindRoot server
        timeout=600  # 10 minutes timeout
    )
    
    try:
        # Example 1: Data extraction task
        print("\n===== EXAMPLE 1: Data Extraction =====\n")
        instructions = """Please extract the following information into JSON format:
        
        Name: John Smith
        Email: john.smith@example.com
        Age: 42
        Address: 123 Main St, Anytown, CA 12345
        Phone: (555) 123-4567
        """
        result = client.run_task("Assistant", instructions, include_trace=True)
        print(f"Instructions:\n{instructions}\n")
        process_results(result)
        
        # Example 2: Code generation task
        print("\n\n===== EXAMPLE 2: Code Generation =====\n")
        instructions = """Write a Python function that calculates the Fibonacci sequence up to n terms.
        Include docstring and example usage."""
        result = client.run_task("Assistant", instructions, include_trace=True)
        print(f"Instructions:\n{instructions}\n")
        process_results(result)
        
        # Example 3: Sequential tasks (conversation simulation)
        print("\n\n===== EXAMPLE 3: Sequential Tasks =====\n")
        
        # First part of the conversation
        print("STEP 1: Initial query")
        instructions = "What are the three largest planets in our solar system?"
        result1 = client.run_task("Assistant", instructions)
        print(f"User: {instructions}")
        print(f"Assistant: {result1['results']}\n")
        
        # Follow-up question
        print("STEP 2: Follow-up question")
        instructions = "For the largest one, how many Earth masses is it?"
        result2 = client.run_task("Assistant", instructions)
        print(f"User: {instructions}")
        print(f"Assistant: {result2['results']}")
        
    except MindRootError as e:
        print(f"MindRoot API Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
