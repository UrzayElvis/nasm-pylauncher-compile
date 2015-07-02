#!/usr/bin/env python

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
	print '\033[91m'+"E: linker couldn't perform the compilation and execution [Errors], Exiting..."
	sys.exit(0)
def run_file(file,run_on_startup=False):
	if run_on_startup:
		subprocess.call("./"+file)
		sys.exit(0)
	else:
		run = raw_input("Execute file (n/y) ")
		if run=='n':
			pass
		else:
			subprocess.call("./"+file)		
def usage():
	print "NSAM linker, made by https://github.com/UrzayElvis , for quick access compiling ASM poporses, you can redistribute this program freely, by Python programming\n"
	print "-r   --run  :optional it'll look for an executable file, asm and will not compile just run the given asm file\n"
	print "Examples: "
	print "./nsam_linker.py [file] compile and run"
	print "./nsam_linker.py [file] --run just run the file and do not compile"
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
	if(len(sys.argv[2]) and (sys.argv[2]=='--run' or sys.argv[2]=='-r')):
		run_file(classname,True)
	file_output_o = classname+'.o'
	nasm = shlex.split("nasm -f elf "+file)
	gcc = shlex.split('ld -m elf_i386 -s -o '+classname+' '+file_output_o)
	try:
		compilation = subprocess.Popen(nasm)
		buffer_stream = compilation.communicate()[0]
		if compilation.returncode<=0:
			compilation = subprocess.Popen(gcc)
			buffer_stream = compilation.communicate()[0]
			if compilation.returncode<=0:
				run_file(classname)
			else:
				raise ValueError("GCC Compiling error")
		else:
			raise ValueError("NSAM Compiling error")
	except OSError:
		catch()
	except ValueError:
		catch()
main()
