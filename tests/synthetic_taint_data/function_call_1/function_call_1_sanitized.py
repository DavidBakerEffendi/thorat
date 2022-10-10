#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/function_call")
def function_call() -> None:
    command = request.view_args.get('operator')
    command_1 = function_a(command)
    command_2 = function_b(command_1)
    # Sink after function call chaining. Candidate for a false positive.
    eval(sanitize(command_2))

def function_a(command):
    return command

def function_b(command):
    return command

def sanitize(command: str) -> str:
    valid_commands = { 'list' : 'ls', 'stats': 'stat'}
    return valid_commands[command]