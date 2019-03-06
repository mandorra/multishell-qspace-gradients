#!/usr/bin/env python
import csv
import argparse
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument('unitary_schema', type=str,
    help='Sample.txt generate from http://www.emmanuelcaruyer.com/q-space-sampling.php')
parser.add_argument('siemens_schema', type=str,
    help='Output file name (*.dvs for avoiding errors in the scanner) to store the weighted directions for Siemens scanner.')
parser.add_argument('debug_file', type=str,
    help='File name to store debug information.')
parser.add_argument('n_b0',type=int,
    help='Number of B0 in the begining of the acquisition.')
parser.add_argument('bvalues', nargs='+', 
    help='B-Values vector separated by spaces (i.e: 1000 2000 3000). Number must match the shells in [unitary_schema]')

args = parser.parse_args()

bvalues=np.array(args.bvalues,dtype=np.int)
n_b0 = int(args.n_b0)

schema = []
output = []

with open(args.unitary_schema) as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    start = False
    for row in reader:
        try:
            if start:
                u = np.array(row, dtype=np.float)
                schema.append(u)

            if row[0] == "#shell":
                start = True
        except:
            del schema[-1]
            print("Skipping empty row..")

# Check number of shells in input schema:
input_nshells = int(max([item[0] for item in schema]))
given_bvalues = bvalues.size

if input_nshells == given_bvalues:

    maxb = max(bvalues)

    with open(args.debug_file, 'w') as fd:

        fd.write("Maximum B-Value (MRI scaner should acquire all the time with this value): %d s/mm^2\n"%maxb)
        fd.write("B-values: %s s/mm^2\n\n\n"%str(bvalues))

        for n, dir in enumerate(schema):

            bvalue = bvalues[int(dir[0]-1)]
            weight = np.sqrt(float(bvalue)/float(maxb))
            u = dir[1:4]
            v = u*weight 
            output.append("( %f, %f, %f )"%(v[0],v[1],v[2]))
            dirs = int(n)

            #Write debug:
            fd.write("Direction #%s:\n------------\n"%n)
            fd.write("Assigned B-Value: %d\n"%bvalue)
            fd.write("Unitary direction vector: %s\n"%str(u))
            fd.write("Unitary direction vector norm: %f\n"%np.linalg.norm(u))
            fd.write("Assigned weight: %f\n"%weight)
            fd.write("Weighted direction vector: %s\n"%str(v))
            fd.write("Weighted direction vector norm: %f\n"%np.linalg.norm(v))
            fd.write("True B-value (proportional to G^2): %f\n"%(float(maxb)*np.square(np.linalg.norm(v))))
            fd.write("\n\n")
            

    #Create Siemens file
    with open(args.siemens_schema, 'w') as fd:

        fd.write("[directions=%d]\n"%(dirs+ n_b0 + 1))
        fd.write("CoordinateSystem = xyz\n")
        fd.write("Normalisation = none\n")
        n = 0

        for b0 in range(n_b0): 

            fd.write("Vector[%d] = ( 0.000, 0.000, 0.000 )\n"%n)
            n = n + 1

        for dir in output:

            fd.write("Vector[%d] ="%n + dir + "\n")
            n = n + 1

else:
    print(input_nshells)
    print(given_bvalues)
    print("ERROR: Given B-values number and provided Sample.txt shells number doesn't match. STOPPING.")






