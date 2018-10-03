export PATH=$PATH:/home/yangjc/summer_proj/STAR-2.6.0c/bin/Linux_x86_64
counter=0
for file in `ls /home/yangjc/summer_proj/allcells/E31_TCC/*.gz`
do
    STAR --runThreadN 8 --genomeDir /home/yangjc/summer_proj/onecell_test/STAR_test/genomeindex  --readFilesIn $file  --readFilesCommand zcat --genomeLoad LoadAndKeep --quantMode TranscriptomeSAM GeneCounts --outFileNamePrefix ./STAR_out_${file:52:12}/
    let "counter+=1"
    echo $counter
done
