'''
Default Data Tables for a basic 2Pass Assembler
'''


opcode_table = {
	"cla":"0000", "lac":"0001", "sac":"0010","add":"0011", 
	"sub":"0100","brz":"0101","brn":"0110", "brp":"0111", 
	"inp":"1000", "dsp":"1001", "mul":"1010", "div":"1011", 
	"stp":"1100","start":"ad","dc":"dl","ds":"dl","end":"ad",
	"CLA":"0000", "LAC":"0001", "SAC":"0010","ADD":"0011", 
	"SUB":"0100","BRZ":"0101","BRN":"0110", "BRP":"0111", 
	"INP":"1000", "DSP":"1001", "MUL":"1010", "DIV":"1011", 
	"STP":"1100","START":"ad","DC":"dl","DS":"dl","END":"ad"
}

reg_table = {
	"acc":129, "r1":130, "r2":131
}

location_counter = 0

symbol_table = {
	"acc":129, "r1":130, "r2":131
}

literal_table = {
	
}

error_type = ["invalid opcode","undefined symbol","duplicate label"]

error_list = list()

def read_opcode_from_file(loc):
	return read_opcode(readfile(loc))

def read_opcode(text):
	opcode_table.clear()
	lines = text.split('\n')
	for i in lines:
		opcode = lines.split('\t')
		opcode_table[opcode[0]]=str(opcode)

def readfile(location='assemblycode.txt'):
	f = open(location,'r+')
	text = f.read()
	f.close()
	return text

