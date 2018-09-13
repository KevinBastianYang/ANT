export PATH=$PATH:/home/yangjc/summer_proj/kallisto_linux-v0.44.0

kallisto pseudo -i ./transcriptome/transcripts.idx -o ./TCC_output_all/ --umi -b /home/yangjc/summer_proj/allcells/E31_TCC/new_umi_read_list.txt -t 8
