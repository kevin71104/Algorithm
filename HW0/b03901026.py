import sys

def operation1(input_string):
	'''
	input arg:
		input_list: string format data read from input file
			e.g. "1 2 3 4 5"

	output:
		output_list: a list of integers
			e.g. [1, 2, 3, 4, 5]
	'''

# Please finish this function here.
#####################################
	str1 = input_string.split(' ')
	output_list = [int(str1[i]) for i in range(len(str1))]
#####################################
	return output_list

def operation2(input_list):
	'''
	input arg:
		input_list: a list of integers
			e.g. [1, 2, 3, 4, 5]

	output:
		output_list: a list of integers with each item added by 1
			e.g. [2, 3, 4, 5, 6]
	'''

# Please finish this function here.
#####################################
	output_list = [input_list[i]+1 for i in range(len(input_list))]
#####################################
	return output_list

def operation3(input_list):
	'''
	input arg:
		input_list: a list of integers
			e.g. [2, 3, 4, 5, 6]

	output:
		output_list: insert integer 100 at the end of the list
			e.g. [2, 3, 4, 5, 6, 100]
	'''

# Please finish this function here.
#####################################
	output_list = input_list
	output_list.append(100)
#####################################
	return output_list

def operation4(input_list):
	'''
	input arg:
		input_list: a list of integers
			e.g. [2, 3, 4, 5, 6, 100]

	output:
		output_list: reverse the integers in the list
			e.g. [100, 6, 5, 4, 3, 2]
	'''

# Please finish this function here.
#####################################
	output_list = [input_list[-i-1] for i in range(len(input_list))]
#####################################
	return output_list

def operation5(input_list):
	'''
	input arg:
		input_list: a list of integers
			e.g. [100, 6, 5, 4, 3, 2]

	output:
		output_string: transform input_list into string format
			e.g. "100 6 5 4 3 2"
	'''

# Please finish this function here.
#####################################
	output_string = ' '.join(str(e) for e in input_list)
#####################################
	return output_string

if __name__ == "__main__":
	input_filename = sys.argv[1]
	output_filename = sys.argv[2]
	inputfile = open(input_filename, 'r')
	outputfile = open(output_filename, 'w')
	data = inputfile.read()

	output1 = operation1(data)
	#print(output1)
	output2 = operation2(output1)
	#print(output2)
	output3 = operation3(output2)
	#print(output3)
	output4 = operation4(output3)
	#print(output4)
	output5 = operation5(output4)

	outputfile.write(output5)
	inputfile.close()
	outputfile.close()
