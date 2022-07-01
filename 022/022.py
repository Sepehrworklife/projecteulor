"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""



alphabetical_value = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


def alphabetical_value_of_name(name):
    return sum([alphabetical_value[letter] for letter in name])

def find_index_of_string_in_array(array, string):
    return array.index(string) + 1

def main(file_path):
    try:
        file = open(file_path, "r")
        names = file.read().replace('"', '').split(',')
        names.sort()
        total = 0
        for name in names:
            total += alphabetical_value_of_name(name) * find_index_of_string_in_array(names, name)
        return total
    except Exception as e:
        print(e)
    finally:
        file.close()


# Check if answer is correct
print(f"The total of all the name scores in the file is {main('names.txt')}")
