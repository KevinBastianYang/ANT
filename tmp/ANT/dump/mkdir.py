#!/usr/bin/python
import os
import json
from get_parameter import para

def makedir(cell_path,dir_path):
    for file in os.listdir(cell_path):
        if file[-3:] == ".gz":
            os.mkdir(dir_path+"/STAR_out_"+file[10:22],0755)

if __name__ == "__main__":
    parameter = para()
    makedir(parameter["CELL_DIR"],parameter["OUTPUT_DIR"])