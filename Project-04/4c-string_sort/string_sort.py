# Author: Timur Guner
# Date: 2021-04-28
# Description: Project 4c takes a list of string and alphabetically sorts them

def string_sort(string_list):
    """
    Sorts the strings alphabetically using insertion short
    """
    for index in range(1, len(string_list)):
        value = string_list[index]
        pos = index - 1
        while pos >= 0 and string_list[pos].lower() > value.lower():
            string_list[pos + 1] = string_list[pos]
            pos -= 1
        string_list[pos + 1] = value

def main():
    o1 = "HELLO"
    o2 = "dog"
    o3 = "steak sauce"
    o4 = "ZeBRa"
    o5 = "Timur"
    o6 = "zeBRA"
    string_list = [o1, o2, o3, o4, o5, o6]
    string_sort(string_list)
    print(string_list)

if __name__ == '__main__':
    main()