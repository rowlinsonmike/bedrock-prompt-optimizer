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

The Bedrock Prompt Optimizer is a CLI. Here's how to use it:

```bash
bpo optimize --prompt INPUT_FILE --output OUTPUT_FILE --model-id MODEL_ID --region AWS_REGION
```

### Arguments

- `--prompt`: Path to the input prompt file (required)
- `--output`: Path to the output file where the optimized prompt will be saved (default: optimized_prompt.txt)
- `--model-id`: Bedrock model ID (default: will prompt to select from a list of models)
- `--region`: AWS region (default: us-east-1)

### Example

```bash
bpo optimize --prompt input.txt --model-id amazon.nova-pro-v1:0 --region us-east-1
```

This command will:
1. Read the prompt from `input.txt`
2. Optimize it
3. Save the optimized prompt to `optimized_prompt.txt`

## Notes

- Ensure you have the necessary AWS credentials configured to access the Bedrock service.
