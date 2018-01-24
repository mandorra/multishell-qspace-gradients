# Multi-shell Q-Space Gradients Schema Siemens

Generate a ready-to-import gradient table for a multi-shell DWI acquisition using Emmanuel Caruyer et al., 2013 uniform schemes in a Siemens scanner.

##Usage

First step to use this script is go to Emmanuel Caruyer wesite and create the desired sampling "Samples.txt" file. (http://www.emmanuelcaruyer.com/q-space-sampling.php)

Second, clone this repository or "download as zip". In Linux you can give the script execution right with: "chmod a+x qspaceweight.py". Alternatively you can run the script in this way: "python qspaceweight.py"

Thir, run the script with -h to see the help. 

usage: qspaceweight.py [-h]
                       unitary_schema siemens_schema debug_file n_b0 bvalues
                       [bvalues ...]

positional arguments:
  unitary_schema  Sample.txt generate from http://www.emmanuelcaruyer.com/q
                  -space-sampling.php
  siemens_schema  Output file name (*.dvs for avoiding errors in the scanner)
                  to store the weighted directions for Siemens scanner.
  debug_file      File name to store debug information.
  n_b0            Number of B0 in the begining of the acquisition.
  bvalues         B-Values vector separated by spaces (i.e: 1000 2000 3000).
                  Number must match the shells in [unitary_schema]

optional arguments:
  -h, --help      show this help message and exit

Example of usage is as follows:

python qspaceweight.py samples.txt siemens.dvs debug.txt 5 1000 2000 3000


##Comments:

Please note that the provided b-values must match the shells you included in Caruyer's website otherwise script will throw you an error.
