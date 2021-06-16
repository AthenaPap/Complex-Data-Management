# Complex-Data-Management

# Python

## Exercise 1
### Execution Method: 
python3 excercise1.py title.basics.tsv title.akas.tsv outfile.tsv or 
python3 excercise1.py title.basics.tsv title.akas.tsv


### Algorithm Description: 

In order to merge the 2 files we create the merge_join(first_filename, second_filename, output_filename) function. As first_filename and second_filename we define the names of the 2 input files to be merged, and as output_filename the name of the file that will contain the merge.
We read the first two lines from both files. Those lines contain the headers of the files. We merge them in order to have the header of the output file. 
After that we move on to the next line in both files: line_1 = first_file.readline() and line_2 =second_file.readline().
While we are not to EOF for both files we check if the key field of title.basics.tsv is equal with the first field of title.akas.tsv. If this is true then we write the proper line in output file and we continue with the next line of both files.
In case that line_1 < line_2 it means that the second file does not contain any id that appears in the first file so we read the next line of the first file,
otherwise we read the next line of the second one. 

## Exercise 1
### Execution Method: 
python3 excercise2.py title.basics.tsv title.ratings.tsv [2] [1,2] or
python3 excercise2.py title.basics.tsv title.principals.tsv [2] [2]

### Algorithm Description: 
The function mj(line_1, line_2, list_1, list_2) takes as arguments the first line of the two input files. The lines of each file are being returned by the scan(filename) function. 
As nect step mj function ckecks if the ids are the same or not and it returns the line that should be written in the output file or not.
Specifically, if the ids are the same it creates the line "line" which contains the proper fields of the files and lists that are given as arguments in main function, 
it returns them to main where the entry in the output file is done and the the process continues repeatedly. In case the ids are different we move to the next line of each file according to the case, using the scan function. 
