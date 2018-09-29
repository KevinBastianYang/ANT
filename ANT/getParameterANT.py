#!/usr/bin/python

import os
import json

def get_para():
	try:
		with open(input("The path of the ANT parameter json file"),'r') as json_f:
			print("json file read in correctly")
	except IOError as err:
		return -1
	else:
		try:
			para = json.load(json_f)
		except ValueError as e:
			print("json file content error")
			return -2
		else:
			return para
def main():
	get_para()

if __name__ == '__main__':
	main()