#!/bin/usr/env python

import commands
import os
from multiprocessing.dummy import Pool as ThreadPool

def process(file):
    file_cell = open("/home/yangjc/summer_proj/allcells/E31_TCC/new_umi_read_list.txt", 'r')
    # dict: cell barcode and its number
    cell_number = dict()
    for line in file_cell.readlines():
        cell = line.split()[0]
        cell_split = cell.split('_')
        cell_number[cell_split[2]] = cell_split[1]
    file_cell.close()

    tran_dict = dict()
    file_tran = open("/home/yangjc/summer_proj/stage4/neo_id.txt", 'r')
    for line in file_tran.readlines():
        line = line.split()
        tran_dict[line[1].strip()] = str(line[0])
    file_tran.close()



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

    # command2 = "samtools view -h " + file + "/Aligned.toTranscriptome.out.bam > " + file + "/TranscriptCoord.sam"
    # commands.getoutput(command2)

    # trim header
    command3 = "grep '^[^@]' " + file + "/TranscriptCoor.sam"
    trim_header = commands.getoutput(command3).split('\n')
    # trans_number


    # extract the aligned reads

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
    cell_finalset = dict()
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
        processed_reads = []
        for r in all_uniq_trans:
            if len(r):
                if r not in processed_reads:
                    processed_reads.append(r)

        processed_reads.sort(key=len)

        if len(processed_reads):
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

            finalset_umi.setdefault(','.join(output_set), []).append(key)
    cell_finalset[cell_number[file[-12:]]] = finalset_umi
    print cell_number[file[-12:]]
    return cell_finalset

def cal_Parallel(dirs,threads = 8):

    pool = ThreadPool(threads)
    all_cell_data = pool.map(process,dirs)
    pool.close()
    pool.join()
    return all_cell_data

def main():
    dirs_command = "ls -d /home/yangjc/summer_proj/stage4/STAR_out_*"
    files = commands.getoutput(dirs_command)
    dir_indi = files.split()
    file_ecs = open("/home/yangjc/summer_proj/stage4/STAR_parallel/number_ecs.txt", 'a')
    #file_readcount = open("/home/yangjc/summer_proj/stage4.5/STAR_output/cell_readcount.txt", 'a')
    file_output = open("/home/yangjc/summer_proj/stage4/STAR_parallel/out_mat.txt", 'a')

    cells_data = cal_Parallel(dir_indi,8)

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
    #file_readcount

main()


