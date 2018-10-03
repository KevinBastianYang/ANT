#!/bin/usr/env python

import os
import commands

command1 = "ls -d /home/yangjc/summer_proj/stage4/STAR_out_*"

files = commands.getoutput(command1)
files = files.split()

file_cell = open("/home/yangjc/summer_proj/allcells/E31_TCC/new_umi_read_list.txt", 'r')
file_output = open("/home/yangjc/summer_proj/stage4/STAR_output/out_mat.txt", 'a')

file_readcount = open("/home/yangjc/summer_proj/stage4/STAR_output/cell_readcount1.0.txt",'a')
# dict: cell barcode and its number
cell_number = dict()
for line in file_cell.readlines():
    cell = line.split()[0]
    cell_split = cell.split('_')
    cell_number[cell_split[2]] = cell_split[1]
file_cell.close()

tran_dict = dict()
file_tran = open("/home/yangjc/summer_proj/stage4/trans_number.txt", 'r')
for line in file_tran.readlines():
    line = line.split()
    tran_dict[line[1].strip()] = str(line[0])
file_tran.close()

# dict:store ec_umi relation of all cells
#ec_umi_dict = dict()
cell_read_counts = dict()
for file in files:
    read_counter = 0
    # transcript from bam to sam
    file_fastq_content = "zcat -c /home/yangjc/summer_proj/allcells/E31_TCC/cell_" + cell_number[
        file[-12:]] + '_' + file[-12:] + ".fastq.gz|grep '@'"
    fastq = commands.getoutput(file_fastq_content).split()
    umi_file = open(
        "/home/yangjc/summer_proj/allcells/E31_TCC/cell_" + cell_number[file[-12:]] + '_' + file[-12:] + ".umi", 'r')
    umi = umi_file.read().split()
    read_umi_map = dict()
    for i in range(0, len(fastq)):
        read_umi_map[fastq[i][1:]] = umi[i]

    umi_file.close()

    command2 = "samtools view -h " + file + "/Aligned.toTranscriptome.out.bam > " + file + "/TranscriptCoor.sam"
    commands.getoutput(command2)

    # trim header
    command3 = "grep '^[^@]' " + file + "/TranscriptCoor.sam"
    trim_header = commands.getoutput(command3).split('\n')
    # trans_number
    


    # extract the aligned reads
    # reads = []
    rtotr = dict()
    for i, records in enumerate(trim_header):
        records = records.split()
        rtotr.setdefault(records[0], []).append(tran_dict[records[2]])

    # reads = set(reads)
    umi_r = dict()
    for read in rtotr.keys():
        umi_r.setdefault(read_umi_map[read], []).append(read)
    # dict: ec and its umis
    finalset_umi = dict()

    for key, values in umi_r.items():

        trans_freq = dict()
        all_uniq_trans = []

        for value in values:
            # for each read, uniq and sort its transcripts
            uniq_trans = []
            for i in rtotr[value]:
                uniq_trans.append(i)
            uniq_trans = sorted(list(set(uniq_trans)))
            all_uniq_trans.append(uniq_trans)

            for j in uniq_trans:
                if j not in trans_freq.keys():
                    trans_freq[j] = 1
                else:
                    trans_freq[j] += 1

        for k, v in trans_freq.items():
            if v == 1:
                for ele in all_uniq_trans:
                    if k in ele:
                        ele.remove(k)
                        break
        #processed_reads = []
        for r in all_uniq_trans:
            if len(r):
                read_counter+= 1
    #cell_read_counts[cell_number[file[-12:]]] = read_counter

    file_readcount.write(cell_number[file[-12:]]+'\t'+str(read_counter)+'\n')
                #if r not in processed_reads:
                    #processed_reads.append(r)

        #processed_reads.sort(key=len)

        #if len(processed_reads):
"""
            intersection = list(set(processed_reads[0]).intersection(*processed_reads[1:]))
            s_set = []
            reads = processed_reads
            output_set = []

            while True:
                if len(intersection):
                    output_set.extend(intersection)
                    output_set.extend(s_set)
                    break
                else:
                    l_set = []
                    for r in reads:
                        if len(r) == len(reads[0]):
                            s_set.extend(r)
                        else:
                            l_set.append(r)
                    counter = 0
                    for i in l_set:
                        if not len(list(set(s_set).intersection(i))):
                            counter += 1
                    if counter == 0:
                        output_set.extend(s_set)
                        break
                    else:
                        intersection = list(set(l_set[0]).intersection(*l_set[1:]))
                        reads = l_set

            output_set.sort()

            finalset_umi.setdefault(' '.join(output_set), []).append(key)
            # store the dict in each cell number: 1-3381
            ec_umi_dict[cell_number[file[-12:]]] = finalset_umi
            
# establish ec and its number
ec_number = []
for single_cell in ec_umi_dict.keys():

    for ecs in ec_umi_dict[single_cell].keys():
        ec_number.append(ecs)

ec_number = list(set(ec_number))

for single_cell in ec_umi_dict.keys():
    for ecs in ec_umi_dict[single_cell].keys():
        file_output.write(
            str(ec_number.index(ecs)) + '\t' + single_cell + '\t' + str(len(ec_umi_dict[single_cell][ecs])) + '\n')
"""
file_output.close()

file_readcount.close()





