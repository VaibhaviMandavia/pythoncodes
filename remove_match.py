# to remove matches from two strings

# function to remove matches
def remove_match(string1,string2):
    # converting string to a list
    string1 = list(string1)
    string2 = list(string2)
    #looping through the first string to find its match in the second string
    for i in string1[:]:
        if i in string2:
            # removing the match from both the lists
            print(i+" removed")
            string1.remove(i)
            string2.remove(i)
    # printing the remaining string
    print(string1,string2)

# calling the function and passing two strings as parameters
remove_match(input("enter first string : "), input("enter second string: "))