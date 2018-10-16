
'''
Assembler Class Module
for 12bit SIC 2 Pass assembler without JSR and Macro Functionalitiy
Author: Harsh Bandhey
'''


class Assembler:

	def __init__(self, opcode_table,symbol_table):
		self.source=""
		self.spoint=0
		self.opcode_table = opcode_table
		self.symbol_table = symbol_table
		self.location_counter = 0
		self.error_list = list()
		self.error_flag = False
		self.start_val = 0
		self.intermediate = list()
		self.final = list()
		self.prog_length = 0

	def render_source(self,source):
		self.source = source
		self.source = source.split('\n')
		if self.source==['']:
			raise AssertionError('Source file empty')

	def pass1(self):
		while self.iscomment(self.source[self.spoint]):
			self.spoint += 1
		label,opcode,operand = self.breakup(self.source[self.spoint])
		if opcode.lower() == "start":
			if operand!="":
				self.location_counter = int(operand)
				self.start_val = int(operand)
		if label!="":
			self.symbol_table[label] = self.location_counter
		self.intermediate.append(self.source[self.spoint])
		self.spoint += 1
		if self.iscomment(self.source[self.spoint]):
				self.spoint += 1
		label,opcode,operand = self.breakup(self.source[self.spoint])
		while opcode.lower()!="end":
			if self.iscomment(self.source[self.spoint]):
				self.spoint += 1
				continue
			if label!="":
				if label not in self.symbol_table.keys():
					self.symbol_table[label] = self.location_counter
				else:
					self.error_flag = True
					self.error_list.append(("duplicate label",self.spoint))
			if opcode.lower() in self.opcode_table.keys():
				if self.opcode_table[opcode]=="dl":
					self.symbol_table[label] = self.location_counter
				self.location_counter += 1
			else:
				self.error_flag = True
				self.error_list.append(("invalid opcode",self.spoint))
			self.intermediate.append(self.source[self.spoint])
			self.spoint += 1
			if self.spoint==len(self.source):
				self.error_list.append(("end less code",self.spoint))
			if self.iscomment(self.source[self.spoint]):
				self.spoint += 1
				continue
			label,opcode,operand = self.breakup(self.source[self.spoint])
		self.intermediate.append(self.source[self.spoint])
		for line_ind in range(self.spoint+1,len(self.source)):
			if not self.iscomment(self.source[line_ind]):
				self.intermediate.append(self.source[line_ind])
		self.prog_length = self.location_counter - self.start_val

	def pass2(self):
		ipoint = 0
		label,opcode,operand = self.breakup(self.intermediate[ipoint])
		if opcode.lower()=="start":
			self.final.append("_"*12)
			ipoint += 1
		label,opcode,operand = self.breakup(self.intermediate[ipoint])
		while opcode.lower()!="end":
			if self.iscomment(self.intermediate[ipoint]):
				ipoint+=1
				continue
			if self.opcode_table[opcode]=="dl":
				pass
			elif opcode in self.opcode_table.keys():
				bin1 = self.opcode_table[opcode]
				if operand != "":
					if operand in self.symbol_table.keys():
						bin2 = self.binandpad(self.symbol_table[operand])
					else:
						print(operand)
						bin2 = self.binandpad(0)
						self.error_flag = True
						self.error_list.append(("undefined symbol",ipoint))
				else:
					bin2 = self.binandpad(0)
				self.final.append(bin1+bin2)
			else:
				self.error_flag = True
				self.error_list.append(("invalid opcode",ipoint))
			ipoint += 1
			if ipoint==len(self.intermediate):
				self.error_list.append(("end less code",ipoint))
			label,opcode,operand = self.breakup(self.intermediate[ipoint])
		self.final.append("_"*12)


	def assemble(self,source):
		self.render_source(source)
		self.pass1()
		self.pass2()


	def iscomment(self,text):
		if text == "" or text.strip(" ")[0:2]=="//":
			return True
		else:
			return False


	def breakup(self,text):
		text = text.split(" ")
		if text[0] not in self.opcode_table.keys():
			label = text[0].strip(":")
			try:
				opcode = text[1]
			except IndexError:
				opcode = ""
			try:
				operand = text[2]
			except IndexError:
				operand = ""
		else:
			label = ""
			opcode = text[0]
			try:
				operand = text[1]
			except IndexError:
				operand = ""
		return label,opcode,operand

	def binandpad(self,num,leng=8):
		num = str(bin(int(num)))[2:]
		while len(num) < leng:
			num = "0" + num
		return num


	def output(self):
		temp = ""
		for i in self.symbol_table.keys():
			temp+=i+'\t'+str(self.binandpad(self.symbol_table[i]))+'\n'
		self.save('output/symbol_table.txt',temp)
		temp = ""
		for i in self.opcode_table.keys():
			temp+=i+'\t'+str(self.opcode_table[i])+'\n'
		self.save('output/opcode_table.txt',temp)
		temp=""
		for i in self.intermediate:
			temp+=i+'\n'
		self.save('output/intermediate.txt',temp)
		temp=""
		for i in self.final:
			temp+=i+'\n'
		self.save('output/output.txt',temp)
		self.save('output.txt',temp)

		
	def save(self,loc,text):
		f = open(loc,'w+')
		f.write(text)
		f.close()

	def print_status(self):
		if self.error_flag == False:
			print("Success output generated with no errors")
		else:
			print("Error in process, printing error stack")
			for i in self.error_list:
				print(i)


if __name__=="__main__":
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
