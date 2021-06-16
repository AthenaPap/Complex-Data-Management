import sys 

def throwException(e):
	print("Excecution failed: " + e)
	sys.exit(0)


def merge_join(first_filename, second_filename, output_filename):
	
	first_file = open(first_filename, 'r')
	second_file = open(second_filename, 'r')
	output_file = open(output_filename, 'w')

	line_1 = first_file.readline().split('\t')
	line_1 = first_file.readline()
	
	line_2 = second_file.readline().split('\t')
	line_2 = second_file.readline()
	
	output_file.write(line_2[0] + '\t' + line_1[2] + '\t' + line_2[2] +'('+ line_2[3] +')'+'\n')


	while(line_1 and line_2):
		
		line_first = line_1.split('\t')
		line_second = line_2.split('\t')

		if line_first[0] == line_second[0]:
			output_file.write(line_first[0] + '\t' + line_first[2] + '\t' + line_second[2] + '\t' + line_second[3])
			line_1 = first_file.readline()
			line_2 = second_file.readline()
		elif line_1 < line_2:
			line_1 = first_file.readline()
		else:
			output_file.write(line_second[2] + '\t' + line_second[3])
			line_2 = second_file.readline()
	
	first_file.close()
	second_file.close()
	output_file.close()

def main():
	if len(sys.argv) == 4:
		print("Running")
		merge_join(sys.argv[1], sys.argv[2], sys.argv[3])
	elif len(sys.argv) == 3:
		print("Running")
		merge_join(sys.argv[1], sys.argv[2], "output.tsv")
		
	else:
		throwException("2 or 3 arguments are required")
		

	
if __name__ == "__main__":
	main()
	















