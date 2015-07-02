r/bin/env python

'''
   NSAM linker, made by https://github.com/UrzayElvis ,
   for quick access compiling ASM poporses, you can redistribute this program freely, by Python programming
'''

import sys,subprocess,shlex

file = ''
file_output_o = ''
classname = ''
nasm = []
gcc = []

def catch():
	print '\033[91m'+"E: linker couldn't perform this action [Errors], Exiting..."
	sys.exit(0)	
def usage():
	print "\nNSAM linker, made by https://github.com/UrzayElvis , for quick access compiling ASM poporses, you can redistribute this program freely, by Python programming \n\n"
	print "Usage: ./nsam_linker.py [file]"
	sys.exit(0)
def main():
	global file
	global classname
	global file_output_o
	global nasm
	global gcc
	if(len(sys.argv)<=1):
		usage()

	file = sys.argv[1]
	classname = file.split('.')[0]
	file_output_o = classname+'.o'
	nasm = shlex.split("nasm -f elf "+file)
	gcc = shlex.split('ld -m elf_i386 -s -o '+classname+' '+file_output_o)
	try:
		compile_o = subprocess.Popen(nasm)
		buffer_stream = compile_o.communicate()[0]
		if compile_o.returncode<=0:
			subprocess.Popen(gcc)
		else:
			raise ValueError("Compile error")
	except OSError:
		catch()
	except ValueError:
		catch()
main()
exit(0)
