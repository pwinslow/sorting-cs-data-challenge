# Sorting CS Data Challenge
**Goal**:

Write a program that takes a list of strings containing integers and words and returns a sorted version of
the list where all words are in alphabetical order and all integers are in numerical order. Furthermore, if
the nth element in the list is an integer it must **remain** an integer, and if it is a word it must **remain** a word.

In addition, the strings and integers may contain characters that are ascii symbols that neither belong to letter set
nor digit set (i.e. "#", "%", ";", etc). You are required to remove them during the process so that the output will
contain only letters or digits. For example, if a string is "sym*bo+l", the output should be "symbol". If an integer
is "12%3", the output should be "123". You don't have to worry about strings or integers that contain only
non-letter-non-digit characters, like "^!?", "&", etc.

**Input/Output**:

The input for your code will be a file that includes a single, possibly empty, line containing a space-separated list of strings to be sorted. Words will not contain spaces, will contain upper-case, lower-case letters a-z and maybe non-letter-non-digit characters. Integers will be in the range -999999 to 999999, and might also contain non-letter-non-digit characters.

The program should take the input file name as the first argument, output file as the second argument:

	root:#  ./listSorting.py <path-to-input-file>/list.txt <path-to-output-file>/result.txt

**Algorithm**:

My algorithm is based on 7 steps. For each step, I'll list the cumulative O(N) in terms of space (O<sub>S</sub>(N)) and time (O<sub>T</sub>(N)).
* Read the string in
    * Here I read in a single line from a file and store it as a single string so I assume O<sub>S</sub>(1) and O<sub>T</sub>(1) so far.
* Use regular expressions to remove non-alpha-numeric characters everywhere from the string while preserving spaces and negative signs
    * Here I'm still only storing a single string but I've had to scan through the entire string looking for non-alpha-numeric characters, leaving me with O<sub>S</sub>(1) and O<sub>T</sub>(N).
* Split the string up into a list of strings and integers
    * I'm now storing a string and a list. Also, I had to scan through the string again looking for spaces so I should now be at O<sub>S</sub>(N) and 2xO<sub>T</sub>(N).
* Create a hash map, mapping list index to dtype of element where dtype is either "integer" or "word"
    * This represents more storage plus I had to run through the list again, giving 2xO<sub>S</sub>(N) and 3xO<sub>T</sub>(N).
* Extract integers/words into their own separate lists and sort these independently
    * Here, I had to search through the list again looking for integers/words and I've also now stored all the elements of the original list into two separate lists, taking up the same amount of memory overall. This gives 2xO<sub>S</sub>(N) and 4xO<sub>T</sub>(N).
* Create a new list and append elements to this list by popping off the first element of either the integer or word list depending on the value of the hashmap for that particular index value.
    * I've now created a new list and popped off each element of the integer/word lists into this new list, i.e., the amount of space taken up shouldn't have changed. However, I had to run through the entire list again to do this so I should now be at 2xO<sub>S</sub>(N) and 4xO<sub>T</sub>(N).
* Join this list into one single string and write result to file based on requested output filename
    * I'm now storing quite a bit less but, in order to join the string together, I had to run through the list again so that the final complexity becomes 2xO<sub>S</sub>(N) and 5xO<sub>T</sub>(N).

Since I didn't make use of any nested loop structures at any point, I think my algorithm is O<sub>S</sub>(N) and O<sub>T</sub>(N) in the end.


**Running Algorithm**:

To run the sorting algorithm, specify the file containing your scrambled string and the filename you would like the sorted output to be written to at the cmd line as

    python list_sorting.py <path-to-input-file>/input-filename.txt <path-to-output-file>/desired-output-filename.txt

**Run Testing Suite**:

The testing suite randomly generates strings of integers and words which have non-alpha-numeric symbols randomly inserted into them. It does this by leveraging a list of 10,000 english words (obtained from [here](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-no-swears.txt)) and pythons random library. Unit testing uses tools from pythons nose library. To run the testing suite, simply run

    python test_suite.py