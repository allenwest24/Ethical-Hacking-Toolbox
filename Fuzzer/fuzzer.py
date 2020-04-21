# !!! THIS FILE IS UNDER MAINTENANCE SO PARTS OF IT ARE A LITTLE MESSY RIGHT NOW. TRYING TO AUTOMATE A BIT BETTER. !!!

# These two for dealing with files and file paths
import sys
import os

# Retrieving command line arguments
import argparse

# For parsing model specification XML files
import xml.etree.ElementTree as ET

# Utility functions for printing pretty
import pprint

# Other useful tools
import itertools
from itertools import chain, combinations

# Required but I can't remember why
import subprocess

#-------------------------------------------------------------------------------------------------------------------------------------------

# Loads the model specification from the XML file provided.
def load_model(xml_file):
    try:
        tree = ET.parse(xml_file)
    except:
        print('Error: Unable to parse the XML file. Syntax Error?')
        sys.exit(-1)
        
    root = tree.getroot()
    
    optional_args = []
    positional_args = []
    
    opts = root.find('options')
    if opts:
        for opt in pos.iter('option'):
            optional_args.append((opt[0].text, opt[1].text))
            
    pos = root.find('positional')
    if pos:
        for arg in pos.iter('arg'):
            positional_args.append(arg[0].text)
            
    return optional_args, positional_args
    
#-------------------------------------------------------------------------------------------------------------------------------------------
    
# Exits the fuzzer if a non-exsistant file is passed to it in the command line 
def ensure_file_existence(file_path):
    if not os.path.isfile(file_path):
        print('Error: the file {} does not exist. Please check the path'.format(file_path))
        sys.exit(-1)
        
#-------------------------------------------------------------------------------------------------------------------------------------------

# Handles the command line arguments
def handle_cmd_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("config")
    parser.add_argument("binary")
    args = parser.parse_args()
    
    if not args.configendswith('.xml'):
        print('Error: the first parameter should end in an .xml extension')
        sys.exit(-1)
        
    ensure_file_existence(args.config)
    ensure_file_existence(args.binary)
    
    if not os.access(args.binary, os.X_OK):
        print('Error: {} is not executable'.format(args.binary))
        sys.exit(-1)
        
    return args
    
#-------------------------------------------------------------------------------------------------------------------------------------------

# Deals with the cmd line. Parameter vals will be available in args.config and args.binary.
args = handle_cmd_line()

# Load the model specification.
opts, pargs = load_model(args.config)

#TODO: find a better way to automatically initialize values based on the positional and optional arguments.
# Hard code the values you want to be used. Should be suspiciously tricky values expected to stress test the program.
NULL = []
INTEGER = []
STRING = []
ALL = []
TUPLE = []
length1 = len(pargs)
length2 = len(opts)
fullList = pargs.append(opts)

for i in opts:
    # To handle optional argument types
    if (i == 'null'):
        TUPLE == TUPLE + NULL
    if (i == 'string'):
        TUPLE == TUPLE + STRING
    if (i == 'integer'):
        TUPLE == TUPLE + INTEGER

comb = list(itertools.permutations(ALL, length1 + length2))

for t in comb:
    subp = []
    subp.append(args.binary)
    subp.extend(t)
    cmd = args.binary + " " + " ".join(t)
    process = subprocess.run(subp. stderr = subprocess.PIPE, stdout = subprocess.PIPE)
    s = "Traceback (most recentcall last)"
    if s in str(process.stderr) or s in str(process.stdout):
        print(cmd)
