#!/usr/bin/python

import os
import re
import gzip
from linkage import get_linkage


def bam_to_sam(parameterANT,cell_name):
	star_out_path = parameterANT["STAR_OUT_PATH"]
	trans_cmd = "samtools view -h "+star_out_path
		+"STAR_out_"+cell_name
		+"/Aligned.toTranscriptome.out.bam > "
		+star_out_path
		+"STAR_out_"+cell_name
		+"/TranscriptCoord.sam"
	os.sys(trans_cmd)
	print "bam to sam for "+cell_name+" finished\n"

def trim_head(parameterANT,cell_name):
	
	star_out_path = parameterANT["STAR_OUT_PATH"]
	with open(star_out_path+"STAR_out_"+cell_name+"/TranscriptCoord.sam",'r') as orig:
		content = orig.read()
		pattern = re.compile(r"^[^@]")
		trim_header = pattern.findall(content)
	return trim_header

def read_to_umi(parameterANT,cell_name):
	cell_path = parameterANT["CELL_DIR"]
	cell_number,tran_dict = get_linkage(parameterANT)
	read_file = cell_path+"cell_"+cell_number[cell_name]+"_"+cell_name+".fastq.gz"
	umi_file = cell_path+"cell_"+cell_number[cell_name]+"_"+cell_name+".umi"

	fastq_list = []
	with gzip.open(read_file,'r') as rf:
		for line in rf:
			if line[0] == '@':
				# '@' dumped
				fastq_list.append(line[1:].strip())


	umi_list = []
	with open(umi_file,'r') as uf:
		for line in uf:
			umi_list.append(line.strip())

	read_umi_map = dict()
	for i in range(0,len(fastq_list)):
		read_umi_map[fastq_list[i]] = umi_list[i]

	return read_umi_map
