#!/usr/bin/env python
###Author:JCY
###Usage:get_linkage() is a function that provide 2 transition data, cell_to_number and tran_dict 
def get_linkage(parameter):

	#cell_to_number: cell barcode and its number
	cell_to_number = dict()
	with open(parameter["CELL_LIST"],'r') as file_cell:
		for line in file_cell:
			cell = line.split()[0]
			cell_split = cell.split('_')
			cell_to_number[cell_split[2]] = cell_split[1]

	#tran_dict: transcript and its number
	tran_dict = dict()
	with open(parameter["TRANS_ID"],'r') as file_tran:
		for line in file_tran:
			line = line.split()
			tran_dict[line[1].strip()] = str(line[0])

	return cell_to_number, tran_dict

