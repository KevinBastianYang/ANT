#!/usr/bin/python
import os
import json
def para():
    json_file = open(input("The path of the json file:"))
    parameter = json.load(json_file)
    return parameter