#!/usr/bin/env python
###Author:JCY
###Usage: alignment_STAR() is a function carrying out read alignment to genomen reference
import os
import json
import sys
import getopt
from getParameterANT import process_para


def alignment_STAR(parameter):
	cell_dir = parameter["CELL_DIR"]
	#mkdir for each output and then run STAR
	star_outpath = parameter["STAR"]["outFileNamePrefix"]
	os.system("mkdir -p "+star_outpath)
	for file in os.listdir(cell_dir):
		if os.path.splitext(file)[1] == ".gz":
			mkdir_cmd = "mkdir "+star_outpath+"STAR_out_"+file[10:22]+"/"
			os.system(mkdir_cmd)

			star_cmd = parameter["STAR"]["star"]+" --runThreadN "+str(parameter["NUM_THREADS"])+" --genomeDir "+parameter["STAR"]["genomeDir"]+" --readFilesIn "+cell_dir+file +" --readFilesCommand zcat"+" --genomeLoad LoadAndKeep"+" --quantMode TranscriptomeSAM GeneCounts"+" --outFileNamePrefix "+star_outpath+"STAR_out_"+file[10:22]+"/"
			print "Running STAR alignment on cell "+file[10:22]+'\n'
			os.system(star_cmd)

	print "STAR alignment finished\n"

def main(argv):
	parameter = process_para(argv)
	if not isinstance(parameter,int):
		alignment_STAR(parameter)

if __name__ == '__main__':
	main(sys.argv[1:])

    
"""
def getpara():
    try:
    	with open(input("The path of the align json file:"),'r') as json_file:
    		print("json file read in correctly")
    except IOError as err:
    	print("File Error:"+str(err))
    	return -1
    else:
    	try:
    		parameter = json.load(json_file)
    	except ValueError as e:
    		print("json file content error")
    		return -2
    	else:
    		return parameter
"""
