from os import system
from nose.tools import assert_equal
from random import sample, uniform, randint, shuffle
from sort_list import sort_list, sort_string


def rand_word_selection(lst, n):
    # Take a random selection of words from a list that are at least 4 characters long
    word_subset = [lst[idx].strip() for idx in sample(range(len(lst)), n) if len(lst[idx]) > 4]

    # Sort list alphabetically
    word_subset = sorted(word_subset)

    # Randomly capitalize words
    word_subset = [word.capitalize() if uniform(0, 1) > 0.5 else word for word in word_subset]

    return word_subset


def rand_int_list(n):
    # Define length of random integer list
    int_len = int(n / 2)

    # Random list of int_len integers as strings
    int_list = sample(range(-999999, 999999), int_len)
    int_list = [str(elem) for elem in int_list]

    # Sort list
    int_list.sort(key=int)

    return int_list


def combine_lists(word_list, int_list):
    # Choose random indices to decide where to insert integers into word list
    idx_list = sample(range(0, len(word_list)), len(int_list))

    # Drop duplicate indices
    idx_list = list(set(idx_list))

    # Sort index list
    idx_list.sort()

    # Insert integers into word list
    for cnt, idx in enumerate(idx_list):
        word_list.insert(idx, int_list[cnt])

    # Return expanded word list list
    return word_list


def symbol_into_element(elem):
    # Create list of non-alpha-numeric symbols to insert into single element
    symbol_list = "@#$%&;^*~"

    # Break characters of element into list
    elem = [char for char in elem]

    # Insert up to two non-alpha-numeric symbols randomly into character list
    for cnt in range(randint(1, 2)):
        symbol = sample(symbol_list, 1)[0]
        elem.insert(randint(0, len(elem)), symbol)

    # Join character list back into single string
    elem = "".join(elem)

    return elem


def symbols_into_list(lst):
    # Choose random set of indices that decides which words will be transformed
    symbol_idxs = sample(range(len(lst)), int(len(lst)/2) + 1)

    # Insert symbols into randomly chosen words
    lst = [symbol_into_element(lst[idx]) if idx in symbol_idxs else lst[idx] for idx in range(len(lst))]

    return lst


def shuffle_list(lst):
    # Create dictionary storing indices (key) and type of element (word/integer)
    type_idx = {}
    for idx in range(len(lst)):
        if lst[idx].replace("-", "").isdigit():
            type_idx[idx] = "integer"
        else:
            type_idx[idx] = "word"

    # Extract separate lists for word and integers from lst
    int_list = [_int for _int in lst if _int.replace("-", "").isdigit()]
    word_list = [word for word in lst if not word.replace("-", "").isdigit()]

    # Shuffle lists
    shuffle(int_list)
    shuffle(word_list)

    # Create new list and insert now sorted words/integers into same indices they occupied in lst
    sorted_list = []
    for idx in range(len(lst)):
        if type_idx[idx] == "word":
            sorted_list.append(word_list.pop(0))
        else:
            sorted_list.append(int_list.pop(0))

    return sorted_list


def generate_test_strings(num_words):
    # Import word data
    with open("google-10000-english-no-swears.txt", "r+") as f:
        word_list = f.readlines()

    # Extract random subset of words
    word_subset = rand_word_selection(word_list, num_words)

    # Create list of random integers
    int_list = rand_int_list(len(word_subset))

    # Combine words and integers into a sorted list
    sorted_list = combine_lists(word_subset, int_list)

    # Join sorted list into one string
    sorted_string = " ".join(sorted_list)

    # Randomly shuffle order of words/integers in sorted list
    scrambled_list = shuffle_list(sorted_list)

    # Randomly insert non-alpha-numeric symbols into the full list of words and integers
    scrambled_list = symbols_into_list(scrambled_list)

    # Join scrambled list into one string
    scrambled_string = " ".join(scrambled_list)

    return sorted_string, scrambled_string


def get_unscrambled_string(scrambled_string):
    # Write scrambled string to file
    with open("scrambled_string.dat", "w") as f:
        f.write(scrambled_string)

    # Run sort_list.py to unscramble scrambled_string
    system("python sort_list.py scrambled_string.dat unscrambled_string.dat")

    # Read in unscrambled string
    with open("unscrambled_string.dat", "r+") as f:
        unscrambled_string = f.readlines()[0]

    # Clean up files
    system("rm *dat")

    return unscrambled_string


def main():

    # Run a tests on distinct methods and overall sorting algorithm involving many different strings
    for sample_size in range(50, 550, 50):
        # Create a sorted string and also a scrambled version of it
        sorted_string, scrambled_string = generate_test_strings(sample_size)

        # Generate shuffled list and string for testing
        shuffled_list = shuffle_list(sorted_string.split())
        shuffled_string = " ".join(shuffled_list)

        # Test sort_list and sort_string methods
        assert_equal(sorted_string.split(), sort_list(shuffled_list), "sort_list failed!")
        assert_equal(sorted_string, sort_string(shuffled_string), "sort_string failed!")

        # Unscramble string using sorting algorithm
        unscrambled_string = get_unscrambled_string(scrambled_string)

        # Compare sorted_string and unscrambled_string
        assert_equal(sorted_string, unscrambled_string, "Overall sorting algorithm failed!")

    print "All tests passed!"


if __name__ == "__main__":
    main()
