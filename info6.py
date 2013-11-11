#!/usr/bin/python
from argparse import ArgumentParser
import re

argp = ArgumentParser(prog='IPv6 calculator')
argp.add_argument('-s', help='shorten address', action='store_true')
argp.add_argument('-v', '--verbose', help='verbose output', action='store_true')
argp.add_argument('address')
arg = argp.parse_args()

def synthax_correct(address):
	regexp = re.compile(r"[^0-9|:|\.|a-f|A-F]")
	match = re.search(regexp, arg.address)
	dublecolon = arg.address.split('::')
	if match or len(dublecolon) > 2:
		return False
	else: 
		regexp = re.compile(r"\.")
		if re.search(regexp, ''.join(address.split(':')[0:-1])):
			return False
		if re.search(regexp, ''.join(address.split(':')[-1])):  
			if len(address.split(':')[-1].split('.')) < 4:
				return False
			for digits in address.split(':')[-1].split('.'):
				if not digits.isdigit():
					return False
				if int(digits) not in range(0,255):
					return False
			if len(address.split(':')[0:-1]) > 6:
				return False
		return True

def add_missing_blocks(address):
	segments = address.split(':')
	dublecolon = address.split('::')
	insert = []
	if len(dublecolon) == 2:
		for _ in range(1,10-len(segments)):
			insert.append('0000')
		if address[0:2] == '::':
			insert.append('0000')
			insert = ':'.join(insert)
			return ':'.join([insert,dublecolon[1]])  
		elif address[-2:] == '::':
			insert.append('0000')
			insert = ':'.join(insert)
			return ':'.join([dublecolon[0],insert])
		else:
			insert = ':'.join(insert)
			return ':'.join([dublecolon[0],insert,dublecolon[1]])
	else:
		return address

def fill_4byte_blocks(address):
	segments = address.split(':')
	for i in range(0,len(segments)):
		segment = list(segments[i])
		if len(segment) < 4:
			for _ in range(0,4 - len(segment)):
				segment.insert(0,'0')
		segments[i] = ''.join(segment)
	return ':'.join(segments)	

def convert_decimal_notation(address):
	regexp = re.compile(r"\.")
	if re.search(regexp, address.split(':')[-1]):
		firstpart = address.split(':')[0:-1]
		temp = []
		lastpart = []
		for digit in address.split(':')[-1].split('.'):
			prehexstr =  str(hex(int(digit)))[2:]
			if len(prehexstr) == 1:
				prehexstr = "0%s" % prehexstr
			temp.append(prehexstr)
			if len(''.join(temp)) == 4:
				firstpart.append(''.join(temp))
				temp = []
		return ':'.join(firstpart)
	return address

def shorten_address(address):
	segments = address.split(':')
	start = 0
	length = 0
	longest_part = (0,0)
	active = False
	counter = 0
	for segment in segments:
		if segment == '0000':
			if not active:
				start = counter
				active = True
			length += 1 
		else:
			(_,l) = longest_part 
			if l < length:
				longest_part = (start,length)
			active = False
			length = 0
		counter += 1
	(_,l) = longest_part
	if l < length:
		longest_part = (start,length)
	(s,e) = longest_part
	del_counter = 0
	for i in range(s,s+e):
		segments.pop(i-del_counter)
		del_counter += 1				
	if del_counter > 0:
		segments.insert(s,'')
	returnstring = ':'.join(segments)
	if returnstring[0:1] == ':':
		returnstring = ''.join([':',returnstring])
	elif returnstring[-1] == ':':
		returnstring = ''.join([returnstring,':'])
	return returnstring

if synthax_correct(arg.address): 
	arg.address = convert_decimal_notation(arg.address)
	if arg.verbose:
		print "without suffix in decimal notation: %s" % arg.address
	arg.address = add_missing_blocks(arg.address) 
	fill_4byte_blocks(arg.address)
	if arg.verbose:
		print "full address notation             : %s" % arg.address
		print "prefix                            : %s::/64" % arg.address[0:19]	
		print "interface identifier              :                    %s" % arg.address[19:]
	if arg.s:
		arg.address = shorten_address(arg.address)
		if arg.verbose:
			print "auto shorted address              : %s" % arg.address 
else:
	exit('illegal synthax')

if not arg.verbose: 
	exit(arg.address)
else:
	exit()