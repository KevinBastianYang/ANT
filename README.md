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

