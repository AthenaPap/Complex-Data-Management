import sys

list_1 = []
lst_2 = []

def throwException(e):
	print("Excecution failed: " + e)
	sys.exit(0)



def scan(filename):
	while True:
		line = filename.readline()
		if line == '':
			
			yield None
		yield line



def mj(line_1, line_2, list_1, list_2):

	
	while True:
		if line_1.split('\t')[0] == line_2.split('\t')[0]:
			
			line = line_1.split('\t')[0] + "\t" 
			for i in range(len(list_1)):
				line += line_1.split('\t')[list_1[i]] + "\t"
			for j in range(len(list_2)):
				line += line_2.split('\t')[list_2[j]] + "\t" 
			yield (line)
		elif line_1.split('\t')[0] < line_2.split('\t')[0]:
			line_1 = next(scan(input_file_1))
		elif line_1.split('\t')[0] > line_2.split('\t')[0]:
			line_2 = next(scan(input_file_2))
		
			



if __name__ == "__main__":
	if len(sys.argv) == 5:
		print("Running")
	else:
		throwException("2 arguments are required")

	input_file_1 = open(sys.argv[1], 'r')
	input_file_2 = open(sys.argv[2], 'r')
	
	output_file = open("output.tsv", 'w')
	
	try:
		list_1 = list(map(int, sys.argv[3].strip('[]').split(',')))
		list_2 = list(map(int, sys.argv[4].strip('[]').split(',')))
	except:
		throwException("Empty list")
	

	
	

	
	line_1 = next(scan(input_file_1))
	line_2 = next(scan(input_file_2))

	
	previous_line = next(scan(input_file_1))
	previous_id = previous_line.split('\t')[0]
	line = mj(previous_line, next(scan(input_file_2)), list_1, list_2)	#tsekare tis dio prwtes grammes.
	
	
	
	
	next_line = next(scan(input_file_2))
	next_id = next_line.split('\t')[0]
	
	while line:
		if (previous_id == next_id):
			
			output_file.write(next(line).strip() + "\n")
			line = mj(previous_line, next_line, list_1, list_2)
			
			next_line = next(scan(input_file_2))
			next_id = next_line.split('\t')[0]
			

		else:
			previous_line = next(scan(input_file_1))
			previous_id = previous_line.split('\t')[0]
	
			output_file.write(next(line).strip() + "\n")
			
			line = mj(previous_line, next_line, list_1, list_2)
			next_line = next(scan(input_file_2))
			next_id = next_line.split('\t')[0] 
			
	
	
	
				


	output_file.close()
	input_file_1.close()
	input_file_2.close()
	
		
				


