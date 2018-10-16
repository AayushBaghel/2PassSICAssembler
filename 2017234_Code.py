'''
Assembler Runner Module
for 12bit SIC 2 Pass assembler without JSR and Macro Functionalitiy
'''
from assembler import *
from data import *
import argparse

parser = argparse.ArgumentParser(description='12 bit SIC assmebler')
parser.add_argument('-i','--input', help='assembly file location')
parser.add_argument('-o','--output', help='output file location')
parser.add_argument('-op','--opcode', help='opcode file location')
args = parser.parse_args()

inp = 'assemblycode.txt'
output = 'output.txt'

if args.input:
	inp = args.input
if args.output:
	output = args.output

assembler = Assembler(opcode_table,reg_table)
assembler.assemble(readfile(inp))
assembler.output()
assembler.print_status()
