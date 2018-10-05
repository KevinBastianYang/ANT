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
2. Alignment Narrowing
3. Matrix Construction

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








### Run
The path to the raw data is located in align.json and ANT_path.json. If you get the raw data or modify the path to your own, you can simply run the following command to get started!
```python
python parallel.py
```
* Some parameters you need to input: 1. The alignment json file position 2. The ANT json file position 3.
* The input of ANT: 1. The demultiplexed single-cell reads and umis (drop-seq protocol) 
* The output of ANT: 1. Constructed TCC matrix for these cells 2. Equivalence classes and their numbers
