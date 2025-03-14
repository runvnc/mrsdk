# MindRoot Python SDK

A simple Python client for interacting with the MindRoot API. This SDK provides programmatic access to run tasks with MindRoot AI agents.

## Agent Definition Requirements

**Note that for the `results` field to be filled in, the Agent you reference MUST have the
`task_result` command enabled from the `chat` plugin section under Available Commands
(`/admin` | Agents | select agent from drop down).**

## Installation

You can install the package from PyPI:

```bash
pip install mrsdk
```

This is the recommended installation method for most users.

Alternatively, you can install directly from GitHub:

```bash
pip install git+https://github.com/mindroot/mindroot-python-sdk.git
```

Or install from a local copy:

```bash
pip install -e .
```

## Quick Start

```python
from mrsdk import MindRootClient

# Initialize client with your API key and MindRoot URL
client = MindRootClient(
    api_key="your_api_key_here",
    base_url="http://localhost:8010"
)

# Or use environment variable
# export MINDROOT_API_KEY=your_api_key_here
# client = MindRootClient(base_url="http://localhost:8010")

# Run a task with an agent
result = client.run_task(
    agent_name="Assistant",
    instructions="What is the square root of 256? Show your work."
)

# Print the result
print(result["results"])
```

## Advanced Usage

### Getting the Full Trace

```python
result = client.run_task(
    agent_name="Assistant",
     base_url="http://localhost:8010",
    instructions="Please write a program to calculate the first 10 prime numbers.",
    include_trace=True
)

# Print the result
print(result["results"])

# Print the full trace of commands executed by the agent
import json
for cmd in result["full_results"]:
    print(json.dumps(cmd, indent=2))
```

### Handling Errors

```python
from mrsdk import MindRootClient, MindRootError

client = MindRootClient(base_url="http://localhost:8010")

try:
    result = client.run_task("Assistant", "Complex task instructions here")
    print(result["results"])
except MindRootError as e:
    print(f"Error from MindRoot API: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Changing the Base URL

```python
# For connecting to a custom MindRoot instance
client = MindRootClient(
    api_key="your_api_key_here",
    base_url="https://mindroot.your-company.com",  # Always required
    timeout=600  # Increase timeout for complex tasks (in seconds)
)
```

## Command-line Interface

The package includes a simple command-line interface for quick testing:

```bash
# Set your API key
export MINDROOT_API_KEY=your_api_key_here

# Run the example script (specify the MindRoot server URL)
python -m mrsdk.cli "What is the square root of 256? Show your work." --url http://localhost:8010

# Include full trace in the output
python -m mrsdk.cli "Calculate the first 10 prime numbers." --url http://localhost:8010 --trace

# Specify a different agent
python -m mrsdk.cli "Translate this to French: Hello, world!" --agent Translator
```

## API Reference

### MindRootClient

```python
client = MindRootClient(api_key=None, base_url="http://localhost:8010", timeout=300)
```

**Parameters:**

-- `base_url` (str, required): Base URL of the MindRoot API server (e.g., `http://localhost:8010`).
- `timeout` (int): Request timeout in seconds. Default is 300 (5 minutes).

### Methods

#### run_task

```python
result = client.run_task(agent_name, instructions, include_trace=False)
```

**Parameters:**

- `agent_name` (str): Name of the agent to run the task.
- `instructions` (str): Instructions or prompt for the agent.
- `include_trace` (bool): Whether to include the full trace of commands in the result. Default is False.

**Returns:**

A dictionary containing the task results:

- If `include_trace` is False, returns only the final textual result.
- If `include_trace` is True, returns a dict with 'results', 'full_results', and 'log_id' keys.

**Raises:**

- `MindRootError`: If the API returns an error or if the request fails.
- `requests.RequestException`: For network-related errors.

## License

MIT
