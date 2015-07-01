#!/usr/bin/env python

import sys,subprocess

file = ''
file_output_o = ''
classname = '';

def usage():
	print "\nNSAM linker, made by https://github.com/UrzayElvis , for quick access compiling ASM poporses, you can redistribute this program freely, by Python programming \n\n"
	print "Usage: ./nsam_linker.py [file]"
	sys.exit(0)

def main():
	global file
	global nasm
	global classname
	global file_output_o
	global gcc
	if(len(sys.argv)<=1):
		usage()

	file = sys.argv[1]
        classname = file.split('.')[0]
        file_output_o = classname+'.o'
	try:
	        subprocess.call("nasm -f elf "+file,shell=True)
	        subprocess.call('ld -m elf_i386 -s -o '+classname+' '+file_output_o,shell=True)
	except:
		print "E: Elvis linker couldn't perform this action [Errors], Exiting..."
		sys.exit(0)
	
	r = raw_input("Execute (n/y) ")
	if r == 'n' or r == 'N':
		pass
	else:
		print 
		subprocess.call('./'+classname)       
main()
