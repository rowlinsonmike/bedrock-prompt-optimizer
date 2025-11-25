<h3 align="center">
    Bedrock Prompt Optimizer (bpo)
</h3>

<p align="center">
<img style="border-radius:8px;" alt="demo" src="docs/bpo.gif"/>
</p>

A CLI wrapper around the Amazon Bedrock Agents Runtime `optimize_prompt` method, which optimizes prompts for the given model. Checkout available models [here](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html). 

## Installation

To install the Bedrock Prompt Optimizer cli, run:

```bash
pip install bpo
```

## Usage

### Arguments

- `--prompt`: Path to the input prompt file
- `--output`: Path to the output file where the optimized prompt will be saved (default: optimized_prompt.txt)
- `--model-id`: Bedrock model ID (default: will prompt to select from a list of models)
- `--region`: AWS region (default: us-east-1)
- `--stdout`: Print the optimized prompt to stdout instead of saving to a file
- `--clip`: Use the last thing copied to clipboard as the input text to optimize

### Example

```bash
bpo optimize --prompt input.txt --model-id amazon.nova-pro-v1:0 --region us-east-1
```

This command will:
1. Read the prompt from `input.txt`
2. Optimize it
3. Save the optimized prompt to `optimized_prompt.txt`

```bash
bpo optimize --clip --stdout
```

This command will:
1. Read the text from the last copied item in the clipboard
2. Provide a select input to pick a model from (just a subset of available models)
2. Optimize it
3. Output the optimized prompt to standard output

## Notes

- Ensure you have the necessary AWS credentials configured to access the Bedrock service.
