#!/usr/bin/env python
###Author:JCY
###Usage: process_para() is a function that processes the json read in file
import os
import json
import sys 
import getopt

def process_para(arg):
	if not len(arg):
		print "Usage: python python_file -i your_parameter.json\n"
		sys.exit(1)
	else:
		try:
			opts, args = getopt.getopt(arg,"i:")
		except getopt.GetoptError:
			print "Usage: python python_file -i your_parameter.json\n"
			sys.exit(2)

       		for opt, ar in opts:
       			try:
       				json_file = open(ar,'r')
				print "json file read in correctly\n"		
       			except IOError as err:
       				print "File Error:"+str(err)+'\n'
       				sys.exit(3)
       			else:
       				try:
					parameter = json.load(json_file)
					json_file.close()
       				except ValueError as e:
					print "json file content error\n"
					sys.exit(4)
       				else:
       					return parameter

def main(argv):
	parameter = process_para(argv)
	if not isinstance(parameter,int):
		return parameter

if __name__ == '__main__':
	main(sys.argv[1:])
