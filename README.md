ANT(Alignment-Narrowed TCC-Matrix)
=======
This repository is designed to demonstrate ANT, an algorithm that transforms the genome alignment results to build TCC-matrix, to faciliate the single-cell RNA-seq quantification. Currently the supported single-cell protocol is drop-seq.

Data source
----------
The data used for demonstration came from [here](https://www.ncbi.nlm.nih.gov/pubmed/29024657), including 3381 selected cells.

Getting started
----------
### Work flow
1. Genome Alignment using STAR
2. Alignment Narrowing and Matrix Construction

### Genome alignment using STAR

#### Configuration
The required parameters needed to run this step is in ```align.json``` file. The included parameters are:

* NUM_THREADS: The parallel threads to run STAR
* CELL_DIR: The path to the directory that contains the different demultiplexed cell files (*barcodes*.fastq.gz and *barcodes*.umi)
* STAR: star: The binary exectuable file, genomeDir: The path to the genome index, outFileNamePrefix: The assigned STAR output path

**Note:** Because the test was used on mouse cells, the corresponding genome index has been generated. Other species should previously use STAR genomeindex building to generate their own genome index. An example script I use is ```index_build.sh```. More details can be found [here](https://github.com/alexdobin/STAR).

#### STAR alignment
[STAR](https://academic.oup.com/bioinformatics/article/29/1/15/272537) is a fast genome alignment tool for short reads. We can run the following scripts to do this step.
```shell
python alignment.py -i /the/path/to/your/align.json
```
Then the alignment results will be under your assigned STAR output path.

### Alignment narrowing

#### Configuration
The required parameters needed to run this step is in ```ANT_path.json``` file. The included parameters are:

* CELL_DIR: It should be consistent with the one in ```align.json```
* STAR_OUT_PATH: It should be consistent with the STAR outFileNamePrefix parameter in ```align.json```
* CELL_LIST: A list of reads and corresponding umis. The example one is ```new_umi_read_list.txt```
* TRANS_ID: The reference transcripts and their ids
* THREADS: The parallel threads run this step
* OUTPUT_PATH: The output path of this step, OUT_ECS: contains the constructed equivalence classes and their ids, OUT_MAT: contains the constructed TCC matrix

**Note:** TRANS_ID should be changed accordingly if the species is not mouse. One way to do this is to download the reference transcrptome and assign random ids to different transcripts.

#### Narrowing and matrix construction
The wrapper file is ```parallel.py```. To do this step, we just need to run the following command.
```shell
python parallel.py -i /the/path/to/your/ANT_path.json
```
More about ANT
-----------
### Algorithm ideas
The following example shows the basic ideas of ANT. 

#### Read Alignment using STAR
* AAATTGGC is a [umi](https://en.wikipedia.org/wiki/Unique_molecular_identifier) from cell 1. There are 8 reads are labeled with this umi. These 8 reads are aligned to genome reference at first then was transformed to transcript coordinates. In this example, there are 4 types of alignment, in which seperate 2 reads are aligned to different transcript(s). 
![alt text](https://github.com/KevinBastianYang/ANT/blob/master/ANT/files/1.PNG)
![alt text](https://github.com/KevinBastianYang/ANT/blob/master/ANT/files/2.PNG)
![alt text](https://github.com/KevinBastianYang/ANT/blob/master/ANT/files/3.PNG)
![alt text](https://github.com/KevinBastianYang/ANT/blob/master/ANT/files/4.PNG)
![alt text](https://github.com/KevinBastianYang/ANT/blob/master/ANT/files/5.PNG)
![alt text](https://github.com/KevinBastianYang/ANT/blob/master/ANT/files/6.PNG)



Downstream
----------
The built TCC-matrix can be used in the downstream single-cell analysis, for example, cell type and stage identification.

Acknowledgement
----------
1. Enormous thanks to Chelsea Ju and Guangyu Zhou for their endless support and helps. Thanks to Prof. Wei Wang in ScAi for giving me this precious opportunity.
2. The alignment step is achieved with the help of STAR(Dobin, Alexander, et al.). Great thanks.
