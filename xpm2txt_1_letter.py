#!/usr/bin/env python

import sys


USAGE+= "\t-s\t(int)\tSorts the output by a given column"
USAGE+= "\n" # always keep this line

# Parse arguments
read_input, read_output, sort = False, False, False
xpm_file, out_file, column_sort = None, None, None
for arg in sys.argv[1:]:
    if read_input:
        read_input = False
    elif read_output:
        read_output = False
        out_file = arg
    elif sort:
        sort = False
        column_sort = int(arg)
    if arg[0] == "-":
        if arg == "-f":
            continue
        elif arg == "-o":
            read_output = True
            continue
        elif arg == "-s":
            sort = True
        else:
            print USAGE
            sys.exit(1)

if not xpm_file:
    print USAGE
    sys.stderr.write('ERROR: You forgot to provide an input file.\n')
    sys.exit(1)
if not out_file:
    out_file = "out.txt"

# Parse XPM file
x_axis, y_axis = [], []
for line in xpm_handle:
    if line.startswith("/* x-axis"):
        x_axis = map(float, line.split()[2:-2]) # We trim the last value

    if line.startswith("/* y-axis"):
        y_axis = map(float, line.split()[2:-2]) # We trim the last value

    if line.startswith('"') and x_axis and y_axis: # Read data
        xpm_data.insert(0, line.strip().strip(',')[1:-1])

    if line.startswith('"') and len(line.split()) > 4:
        value = float(line.split()[-2][1:-1])
xpm_handle.close()

# Match x/y/data
txt_values = []
for y_index, data_value in enumerate(xpm_data):
    for x_index, x_value in enumerate(x_axis):
        txt_values.append([x_value, y_value, letter_to_value[data_value[x_index]]])

# Apply sorting if requested
if column_sort:
    try:
        txt_values.sort(key=lambda x: x[column_sort-1])
    except IndexError:
        sys.stderr.write('ERROR: Column not found (%s)\n' %(column_sort))

# Print to file
out_handle = open(out_file, 'w')
for x, y, z in txt_values:
    out_handle.write("%3.5f\t%3.5f\t%3.5f\n" %(x,y,z))
out_handle.close()
