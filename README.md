# 2PassSICAssembler
12bit SIC 2 Pass assembler without JSR and Macro Functionalitiy

## Usage
    usage: 2017234.py [-h] [-i INPUT] [-o OUTPUT] [-op OPCODE] 
    12 bit SIC assmebler 
      optional arguments:
        -h, --help        show this help message and exit
        -i INPUT, --input INPUT       assembly file location 
        -o OUTPUT, --output OUTPUT      output file location 
        -op OPCODE, --opcode OPCODE       opcode file location
       
## Structure
### Module
    1. Runner Module, to run all the code
    2. Assembler Class, which contains the general purpose assembler 
    3. Data Module, contains data for assembler class
    
### Datastructres
   
    1. Symbol Table, symbol LC pair, dictionary(hashes) with a unique key value pair
    2. Opcode Table, Opcode and type/binary pair, dictionary(hashes) with a unique key value pair
    3. Literal Table, literal mirror dictionary, a unique list(set)
    4. Location Counter, a simple binary counter
    
### Passes
![](2pass.jpg)
#### Pass 1
    Generates the Symbol/Literal Table 
#### Pass 2
    Generates the Machine Code Binary
    
### Biblography
System Software, Leland L. Beck
