#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

@app.route("/recursion_route")
def recursion_route() -> None:
    args = request.view_args
    recursion(args)
    
def recursion(args):
    if len(args) == 1:
        eval(args.pop())
        return
    args.pop()
    recursion(args)