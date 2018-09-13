for file in `ls /home/chelseaju/DropSeq_TCC/E31_TCC/*.gz`
do
    mkdir STAR_out_${file:46:12}
done

