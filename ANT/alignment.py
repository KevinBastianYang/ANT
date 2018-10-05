#!/usr/bin/python
import os
import json
import sys
import getopt

def process_para_star(arg):
	try:
		opts, args = getopt.getopt(arg,"i:")
	except getopt.GetoptError:
		print "Usage: python alignment.py -i your_align_parameter.json\n"
		sys.exit(2)

	for opt, ar in opts:
		try:
			with open(ar,'r') as json_file:
				print "json file read in correctly\n"		
		except IOError as err:
    		print "File Error:"+str(err)+'\n'
    		sys.exit(3)
    	else:
    		try:
    			parameter = json.load(json_file)
    		except ValueError as e:
    			print "json file content error\n"
    			sys.exit(4)
    		else:
    			return parameter

def alignment_STAR(parameter):
	cell_dir = parameter["CELL_DIR"]
	#mkdir for each output and then run STAR
	star_outpath = parameter["outFileNamePrefix"]
	os.sys("mkdir"+star_outpath)
	for file in os.listdir(cell_dir):
		if os.path.splitext(file)[1] == ".gz":
			mkdir_cmd = "mkdir "+star_outpath+"STAR_out_"+file[10:21]+"/"
			os.sys(mkdir_cmd)

			star_cmd = parameter["STAR"]["star"]+" --runThreadN "+parameter["NUM_THREADS"]
						+" --genomeDir "+parameter["STAR"]["genomeDir"]
						+" --readFileIn "+cell_dir+file +" --readFilesCommand zcat"
						+" --genomeLoad LoadAndKeep"+" --quantMode TranscriptomeSAM GeneCounts"
						+" --outFileNamePrefix "+star_outpath+"STAR_out_"+file[10:21]+"/"
    		print("Running STAR alignment on cell "+file[10:21]+'\n')
    		os.sys(star_cmd)

    print "STAR alignment finished\n"


def main(argv):
	parameter = process_para_star(argv)
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
