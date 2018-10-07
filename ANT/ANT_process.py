#!/usr/bin/python
from preprocess import bam_to_sam,trim_head,read_to_umi
from linkage import get_linkage

def alignment_narrow(parameter,cell_name):

    bam_to_sam(parameter,cell_name)
    trim_header = trim_head(parameter,cell_name)
    cell_number,tran_dict = get_linkage(parameter)
    read_umi_map = read_to_umi(parameter,cell_name)

    # extract the aligned reads

    rtotr = dict()
    for i, records in enumerate(trim_header):
        records = records.split()
        rtotr.setdefault(records[0], []).append(tran_dict[records[2]])

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

            ####bugging:
            output_set = list(set(output_set))


            output_set.sort()

            finalset_umi.setdefault(','.join(output_set), []).append(key)
    cell_finalset[cell_number[file[-12:]]] = finalset_umi
    print cell_number[file[-12:]]
    return cell_finalset
