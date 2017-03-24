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

My algorithm is based on 7 steps. For each step, I'll list the cumulative O(N) in terms of space (O<sup>Space</sup>(N)):
* Read the string in
* Use regular expressions to remove non-alpha-numeric characters everywhere from the string while preserving spaces and negative signs
* Split the string up into a list of strings and integers
* Create a hash map, mapping list index to dtype of element where dtype is either "integer" or "word"
* Extract integers/words into their own separate lists and sort these independently
* Create a new list and append elements to this list by popping off the first element of either the integer or word list depending on the value of the hashmap for that particular index value.
* Join this list into one single string and write result to file based on requested output filename