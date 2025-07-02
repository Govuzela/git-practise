#!/usr/bin/env python3

#import sys
#import pprint

import argparse

parser = argparse.ArgumentParser()


parser.add_argument('--read_filename','--read_file_path',type = str,default= '/Users/mnoneleligovuzela/Desktop/Self-actualisation/Computation science/pythons dev basics/scripting /a primer on sci-compute/CHP 4/code along examples/exdata2.txt',help='read file directory',metavar = 'read_filepath' )


parser.add_argument('--write_filename','--write_file_path',type = str,default= '/Users/mnoneleligovuzela/Desktop/Self-actualisation/Computation science/pythons dev basics/scripting /a primer on sci-compute/CHP 4/code along examples/write_exdata2.txt',help='write file directory',metavar = 'write_filepath' )

args = parser.parse_args()

read_filepath = args.read_filename

wfilename =args.write_filename

months = []
values = []

i = 0 # I used it to be able to skip the first line


#infile =open(read_filepath,'r')

def data_extract(file):
    
    with open(file,'r') as infile:
        
        infile.readline() # skips the first line
        
        data = [line.split() for line in infile]

        annual_avg = data[-1][1]

        data = [(m,float(v)) for m,v in data[:-1]]

    return data,annual_avg

dt,annual_av = data_extract(read_filepath)

months = []

values = []

#======Writing the data out==========


def extract_write(wfilename):
    
    with open(wfilename,'w') as outfile:

        header ='\t Annual rainfall data for the city of Rome \n'

        outfile.write(header)

        for tup in dt:
            text = '%s\t%g \n'%(tup[0],tup[1])
            outfile.write(text)
            months.append(tup[0])
            values.append(tup[1])
        
extract_write(wfilename)
        
#print('Data',dt)
print('Annual average',annual_av)



rain_mean  = sum(values)/len(values)
print('The mean rainfal  for [%s] is %g '%(','.join(months),rain_mean))



#==========Authors functions=========

#def extract_data(filename):
#infile = open(filename, ’r’)
#infile.readline() # skip the first line
#months = []
#rainfall = []
#for line in infile:
#words = line.split()
## words[0]: month, words[1]: rainfall
#months.append(words[0])
#rainfall.append(float(words[1]))
#infile.close()
#months = months[:-1] # Drop the "Year" entry
#annual_avg = rainfall[-1] # Store the annual average
#rainfall = rainfall[:-1] # Redefine to contain monthly data
#return months, rainfall, annual_avg
#months, values, avg = extract_data(’rainfall.dat’)
#print ’The average rainfall for the months:’
#for month, value in zip(months, values):
#print month, value
#print ’The average rainfall for the year:’, avg
