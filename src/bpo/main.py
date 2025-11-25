import typer
from pathlib import Path
import boto3
from botocore.exceptions import ClientError
from typing import Optional
import questionary
import pyperclip
from .constants import MODELS
app = typer.Typer()

def optimize_prompt_bedrock(prompt: str, model_id: str, region: str) -> str:
    bedrock = boto3.client('bedrock-agent-runtime', region_name=region)
    try:
        response = bedrock.optimize_prompt(
            input={"textPrompt": {"text": prompt}},
            targetModelId=model_id,
        )
        for event in response["optimizedPrompt"]:
            if "optimizedPromptEvent" in event:
                op = event["optimizedPromptEvent"].get("optimizedPrompt", {})
                text_prompt = op.get("textPrompt", {})
                optimized_text = text_prompt.get("text").strip('"')
                return optimized_text
    except ClientError as e:
        typer.echo(f"An error occurred: {e}", err=True)
        raise typer.Exit(code=1)


@app.command()
def optimize(
    prompt: str = typer.Option(None,"--prompt","-p", help="Path to a prompt text file"),
    output: Path = typer.Option("optimized_prompt.txt","--output","-o", help="Path to the output file"),
    model_id: str = typer.Option(None, "--model_id","-m", help="Bedrock model ID"),
    region: str = typer.Option("us-east-1", "--region","-r", help="AWS region"),
    stdout: bool = typer.Option(False, "--stdout","-s", help="Print out results instead of saving to a file"),
    clipboard: bool = typer.Option(False, "--clip","-c", help="Use the latest string in the clipboard as the source text to optimize"),
):
    """
    Optimize a prompt using Amazon Bedrock
    """
    if not model_id:
        model_selection = questionary.select(
            "Select a model to optimize the prompt for:",
            choices=MODELS.keys()).ask()
        model_id = MODELS[model_selection]
    if clipboard:
        prompt_text = pyperclip.paste()
    else:
        if not prompt:
            typer.echo(f"supply --prompt or --clip", err=True)
            raise typer.Exit(code=1)
        elif not prompt.exists():
            prompt = Path(prompt)
            typer.echo(f"Input file {prompt} does not exist.", err=True)
            raise typer.Exit(code=1)

        with prompt.open('r') as f:
            prompt_text = f.read()

    optimized_prompt = optimize_prompt_bedrock(prompt_text, model_id, region)
    if stdout:
        typer.echo(optimized_prompt.replace('\\n', '\n'))
        return
    with open(output, "w", encoding="utf-8") as f:
        for line in optimized_prompt.split("\\n"):
            f.write(line + "\n")
    typer.echo(f"Optimized prompt written to {output}")

if __name__ == "__main__":
    app()
