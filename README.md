ANT(Alignment-Narrowed TCC-Matrix)
=======
This repository is designed to demonstrate ANT, an algorithm that transforms the genome alignment results to build TCC-matrix, to faciliate the single-cell RNA-seq quantification. Currently the supported single-cell protocol is drop-seq.


Getting started
----------

### Data source
The data used for demonstration came from [here](https://www.ncbi.nlm.nih.gov/pubmed/29024657), including 3381 selected cells.

### File illustration
1. Read Alignment：   align.json   alignment.py
2. Alignment Narrowing：   ANT_path.json getParameterANT.py linkage.py preprocess.py ANT_process.py
3. Matrix Construction：   parallel.py

### Run
The path to the raw data is located in align.json and ANT_path.json. If you get the raw data or modify the path to your own, you can simply run the following command to get started!
```python
python parallel.py
```
* Some parameters you need to input: 1. The alignment json file position 2. The ANT json file position 3.
* The input of ANT: 1. The demultiplexed single-cell reads and umis (drop-seq protocol) 
* The output of ANT: 1. Constructed TCC matrix for these cells 2. Equivalence classes and their numbers
