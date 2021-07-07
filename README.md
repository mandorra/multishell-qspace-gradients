# Multi-shell Q-Space Gradients Schema Siemens

Generate a ready-to-import gradient table for a multi-shell DWI acquisition using Emmanuel Caruyer et al., 2013 uniform schemes in a Siemens scanner.

## Disclaimer
THERE IS NO WARRANTY FOR THIS SAMPLING SCHEME, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE SAMPLING SCHEME “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY OF THE SAMPLING SCHEME IS WITH YOU. SHOULD THE SAMPLING SCHEME PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

##  Usage

First step to use this script is go to Emmanuel Caruyer wesite and create the desired sampling "Samples.txt" file. (http://www.emmanuelcaruyer.com/q-space-sampling.php)

Second, clone this repository or "download as zip". In Linux you can give the script execution right with: "chmod a+x qspaceweight.py". Alternatively you can run the script in this way: "python qspaceweight.py"

Thir, run the script with -h to see the help. 

```
usage: qspaceweight.py [-h]
                       unitary_schema siemens_schema debug_file n_b0
                       interspersed bvalues [bvalues ...]

positional arguments:
  unitary_schema  Sample.txt generate from http://www.emmanuelcaruyer.com/q
                  -space-sampling.php
  siemens_schema  Output file name (*.dvs for avoiding errors in the scanner)
                  to store the weighted directions for Siemens scanner.
  debug_file      File name to store debug information.
  n_b0            Number of B0 in the begining of the acquisition.
  interspersed    Should the B0 volumes be interspersed? If false, they will
                  stay at the beginning.
  bvalues         B-Values vector separated by spaces (i.e: 1000 2000 3000).
                  Number must match the shells in [unitary_schema]

optional arguments:
  -h, --help      show this help message and exit
```
**Example of usage:**
```shell
python qspaceweight.py samples.txt siemens.dvs debug.txt 5 True 1000 2000 3000
```

## Comments:

Please note that the provided b-values must match the shells you included in Caruyer's website otherwise script will throw you an error.

## Cite:

I kindly ask to cite E. Caruyer's work if you use his sampling:

Emmanuel Caruyer, Christophe Lenglet, Guillermo Sapiro, Rachid Deriche. Design of multishell sampling schemes with uniform coverage in diffusion MRI. Magnetic Resonance in Medicine, Wiley, 2013, 69 (6), pp. 1534-1540. <http://dx.doi.org/10.1002/mrm.24736>
