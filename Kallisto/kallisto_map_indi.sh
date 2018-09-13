#!/bin/bash

export PATH=$PATH:/home/yangjc/summer_proj/kallisto_linux-v0.44.0

for file in `ls /home/yangjc/summer_proj/allcells/E31_TCC/umi_read_list/umi_read_list_*`
do
kallisto pseudo -i ./transcriptome/transcripts.idx -o ./TCC_output_indi/TCC_output_${file:70:12} --umi -b $file -t 8
done
