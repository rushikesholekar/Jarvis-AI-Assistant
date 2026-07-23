"""Compatibility entry point for Jarvis command execution."""

from core.command_router import route_command


def execute(command: str):
    """Route a command and return its structured result."""
    return route_command(command)
