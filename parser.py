#### USER-ENTERED FUNCTIONS ####

def add(*args):
	return reduce(lambda x, y: int(x)+int(y), args)

def multiply(*args):
	return reduce(lambda x, y: int(x)*int(y), args)

functions = {'+' : add, '*' : multiply}

#### CORE PARSING MODULE ####

def is_single(input):
	# if input.program == computer_science: return True
	return input.find(')')+1 == len(input)
	# Kappa

def parse_single(input):
	input = input.strip('()')
	args = input.split(' ')[1:]
	fn = input.split(' ')[0]
	return functions[fn](*args)

def parse(input):
	if is_single(input):
		return parse_single(input)
	rightmost = input.find(')')+1
	partner = input[:rightmost].rfind('(')
	innermost = input[partner:rightmost]
	return parse(input.replace(innermost, str(parse_single(innermost))))

#### MAIN PROGRAM FLOW ####

while True:
	x = raw_input()
	print parse(x)