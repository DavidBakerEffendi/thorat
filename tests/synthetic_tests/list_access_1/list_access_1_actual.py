#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/array_route")
def array_route() -> None:
    command = request.view_args.get('command') #source
    new_array = []
    new_array.append('list')
    new_array.append(command)
    new_array.append('ls')
    eval(new_array[1]) # sink