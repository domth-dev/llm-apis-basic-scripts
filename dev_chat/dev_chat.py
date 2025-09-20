import os
import sys
from typing import List, Dict, Any
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from providers.anthropic_provider import AnthropicProvider
from providers.openai_provider import OpenAIProvider
from providers.azure_provider import AzureProvider
from providers.mistral_provider import MistralProvider
from providers.google_provider import GoogleGeminiProvider

load_dotenv()

console = Console()
SEPARATOR = "─" * 72
MAX_TURNS = 10

PROVIDERS = {
    "anthropic": AnthropicProvider,
    "openai": OpenAIProvider,
    "azure": AzureProvider,
    "mistral": MistralProvider,
    "gemini": GoogleGeminiProvider,
}


def choose_provider() -> str:
    console.rule("[bold]Choose provider")
    available = [name for name, cls in PROVIDERS.items() if cls is not None]

    table = Table(show_header=True, header_style="gold1 ")
    table.add_column("#", style="cyan", justify="right")
    table.add_column("provider", style="bold")
    for i, name in enumerate(available, 1):
        table.add_row(str(i), name)
    table.add_row("0", "quit")
    console.print(table)

    while True:
        sel = Prompt.ask("[bold]choose[/] (number)", default="1").strip().lower()
        if sel in ("0", "q", "quit", "exit"):
            sys.exit(0)
        if sel.isdigit():
            idx = int(sel)
            if 1 <= idx <= len(available):
                return available[idx - 1]
        console.print("[red]Invalid selection.[/] Enter a number from the list.")


def get_system_message() -> str:
    s = Prompt.ask("[bold]system message[/] (leave empty for default)", default="")
    if not s:
        s = "You are a helpful assistant."
    return s


def start_chat(provider_name: str, system_message: str) -> None:
    ProviderClass = PROVIDERS[provider_name]
    if ProviderClass is None:
        console.print(f"[red]Provider '{provider_name}' not available.[/]")
        return

    provider = ProviderClass(system_message=system_message)

    messages: List[Dict[str, Any]] = []
    transcript_md: List[str] = [f"# DevChat – {provider_name}\n", f"**System:** {system_message}\n", "\n"]

    console.rule(f"[bold green]DevChat: {provider_name}")
    console.print("Type [bold]switch[/] to change provider, [bold]exit[/] to quit.", style="dim")

    turns = 0
    while turns < MAX_TURNS:
        user_input = Prompt.ask("[turquoise2]you")
        if user_input.strip().lower() in ("exit", "quit", "q"):
            console.print("[dim]Bye.[/]")
            return
        if user_input.strip().lower() == "switch":
            console.print("[yellow]Switching provider…[/]\n")
            return

        messages.append({"role": "user", "content": user_input})
        transcript_md.append(f"**You:** {user_input}\n")

        console.print("[deep_pink1]assistant[/]>\n", end="")
        collected = []
        for piece in provider.response(messages=messages):
            console.print(piece, end="", style="spring_green1")
            collected.append(piece)
        console.print()  # newline after stream

        assistant_text = "".join(collected)
        messages.append({"role": "assistant", "content": assistant_text})
        transcript_md.append(f"**Assistant:**\n\n{assistant_text}\n\n")

        turns += 1
        console.print(SEPARATOR, style="dim")

    console.print("[yellow]Max turns reached. Conversation ended.[/]")

    try:
        out_name = f"transcript_{provider_name}.md"
        with open(out_name, "w", encoding="utf-8") as f:
            f.write("\n".join(transcript_md))
        console.print(f"[green]Saved transcript to[/] [bold]{out_name}[/]")
    except Exception:
        pass


if __name__ == "__main__":
    while True:
        choice = choose_provider()
        system_msg = get_system_message()
        start_chat(choice, system_msg)
        # loop back after chat ends or switch
