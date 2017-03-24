from os import listdir, getcwd, system
from nose.tools import assert_equal


def generate_test_files():
    # Run create_test_lists.py to create test lists
    system("python create_test_lists.py")

    # Collect scrambled lists for testing
    scrambled_list = [_file for _file in listdir(getcwd()) if "scrambled_list" in _file]
    sorted_list = [_file for _file in listdir(getcwd()) if "sorted_list" in _file]

    # Run sort_list.py on each of the scrambled lists to unscramble them
    for lst in scrambled_list:
        prefactor = lst.split("_")[0]
        system("python sort_list.py %s %s_unscrambled_list.dat" % (lst, prefactor))

    # Collect unscrambled lists for testing
    unscrambled_list = [_file for _file in listdir(getcwd()) if "unscrambled_list" in _file]

    # Pass unscrambled and sorted lists for testing
    return unscrambled_list, sorted_list


def run_tests(unscrambled_list, sorted_list):
    # Read in all strings and compare them using nose.tools
    for idx in range(len(sorted_list)):
        with open(unscrambled_list[idx], "r+") as f:
            string1 = f.readlines()[0]
        with open(sorted_list[idx], "r+") as f:
            string2 = f.readlines()[0]

        assert_equal(string1, string2)

    print "All test cases passed!"


def cleanup():
    # Erase all files required tests
    system("rm *dat")


def main():
    # Generate sorted, scrambled, and unscrambled files for testing
    unscrambled_list, sorted_list = generate_test_files()

    # Run tests on all
    run_tests(unscrambled_list, sorted_list)

    # Clean up all spurious files
    cleanup()


if __name__ == "__main__":
    main()
