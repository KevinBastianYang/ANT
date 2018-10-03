#!/usr/bin/python

from multiprocessing.dummy import Pool as ThreadPool
from ANT_process import alignment_narrow
from linkage import get_linkage
from getParameterANT import get_para
import alignment

def cal_Parallel(cells,threads = 8):

    pool = ThreadPool(threads)
    all_cell_data = pool.map(alignment_narrow,cells)
    pool.close()
    pool.join()
    return all_cell_data

def main():
	parameterANT = get_para()
	if not isinstance(parameterANT,int):
		alignment.alignment_STAR()
		threads = parameterANT["THREADS"]
		file_ecs = open(parameterANT["OUTPUT_PATH"]["OUT_ECS"],'a')
		file_output = open(parameterANT["OUTPUT_PATH"]["OUT_MAT"],'a')
		cell_number, tran_dict = get_linkage()
		cells_data = cal_Parallel(cell_number.keys(),threads)

		ec_number = []
    	for data in cells_data:
        	for i in data.values():
            	ecs_umis = i
        	ec_number.append(ec for ec in ecs_umis.keys())
    	ec_number = list(set(ec_number))

    	for i, ecs in enumerate(ec_number):
        	print ecs
        	file_ecs.write(str(i) + '\t' + ecs + '\n')

    	for data in cells_data:
        	for k,v in data.items():
            	cell = k
            	set_umi = v
        	for ecs in set_umi.keys():
            	file_output.write("{0}\t{1}\t{2}\t".format(ec_number.index(ecs),cell,len(set_umi.values())))
            	for i in set_umi.values():
                	file_output.write(i+',')
            	file_output.write('\n')
    	file_ecs.close()
    	file_output.close()

if __name__ == '__main__':
	main()

#next: modify the output\shrink ANT-process\add check\remove unecessary repeat
