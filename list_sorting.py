import sys
import re


def sort_list(lst):
    type_idx = {}
    for idx in range(len(lst)):
        if lst[idx].replace("-", "").isdigit():
            type_idx[idx] = "integer"
        else:
            type_idx[idx] = "word"

    # Extract separate lists for word and integers from scrambled_list
    int_list = [_int for _int in lst if _int.replace("-", "").isdigit()]
    word_list = [word for word in lst if word.replace("-", "").isdigit() is False]

    # Sort both lists, disregarding capitalization
    int_list.sort(key=int)
    word_list.sort(key=lambda s: s.lower())

    # Create new list and insert now sorted words/integers into same indices they occupied in scrambled_string
    sorted_list = []
    for idx in range(len(lst)):
        if type_idx[idx] == "word":
            sorted_list.append(word_list.pop(0))
        else:
            sorted_list.append(int_list.pop(0))

    return sorted_list


def sort_string(scrambled_string):
    # Remove symbols
    scrambled_string = re.sub("[^a-zA-Z\d\s\-]", "", scrambled_string)

    # Create dictionary storing indices (key) and type of element (word/integer)
    scrambled_list = scrambled_string.split()
    sorted_list = sort_list(scrambled_list)

    # Join sorted list into single string
    sorted_string = " ".join(sorted_list)

    return sorted_string


def main():
    # Read I/O file names from the cmd line
    input_file, output_file = sys.argv[1:]

    # Read data from input file
    with open(input_file, "r+") as f:
        scrambled_string = f.readlines()

    # Remove symbols and sort string
    sorted_string = sort_string(scrambled_string[0])

    # Write unscrambled string to file
    with open(output_file, "w") as f:
        f.write(sorted_string)


if __name__ == "__main__":
    main()
