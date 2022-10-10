#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

class WithStatement:
    def __init__(self, command):
        self.command = command
      
    def __enter__(self):
        print("Entered the __enter__ method")
  
    def __exit__(self, exception_type, exception_value, traceback):
        # The sink is inside the overriden __exit__ function
        eval(self.command)
    
    def print_len(self):
        print(self.command)

@app.route("/while_route")
def with_route() -> None:
    command = request.view_args.get('operator')
    with WithStatement(command) as instance:
        instance.print_len()