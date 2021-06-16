# Complex-Data-Management

# Python

## Exercise 1
### Execution Method: 
python3 excercise1.py title.basics.tsv title.akas.tsv outfile.tsv or 
python3 excercise1.py title.basics.tsv title.akas.tsv

In order to merge the 2 files we create the merge_join(first_filename, second_filename, output_filename) function. As first_filename and second_filename we define the names of the 2 input files to be merged, and as output_filename the name of the file that will contain the merge.
We read the first two lines from both files. Those lines contain the headers of the files. We merge them in order to have the header of the output file. 
After that we move on to the next line in both files: line_1 = first_file.readline() and line_2 =second_file.readline().
While we are not to EOF for both files we check if the key field of title.basics.tsv is equal with the first field of title.akas.tsv. If this is true then we write the proper line in output file and we continue with the next line of both files.
In case that line_1 < line_2 it means that the second file does not contain any id that appears in the first file so we read the next line of the first file,
otherwise we read the next line of the second one. 
