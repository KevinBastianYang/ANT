export PATH=$PATH:/home/yangjc/summer_proj/STAR-2.6.0c/bin/Linux_x86_64
for file in `ls /home/yangjc/summer_proj/genome/mouse/`
do
    command+=/home/yangjc/summer_proj/genome/mouse/$file' '
done
STAR --runThreadN 8 --runMode genomeGenerate --genomeDir ./genomeindex --genomeF
astaFiles $command --sjdbGTFfile /home/yangjc/summer_proj/annotation/Mus_musculu
s.GRCm38.91.gtf --sjdbOverhang 62