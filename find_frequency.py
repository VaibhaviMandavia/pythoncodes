# finding the frequency of each word in a sentence

# function to find the frequency
def find_frequency(string):
    # splitting the sentence using space as a separator and storing it in a list
    string = string.split(" ")
    string2 = []
    # looping through the list to find the words that are distinct
    for i in string:
        if i not in string2:
            string2.append(i)
    # printing the frequency of every distinct word present in the given sentence
    for i in range(0,len(string2)):
        print("Frequency of [ "+string2[i]+" ] is ",string.count(string[i]))

# calling the function and passing sentence as a parameter
find_frequency(input("Enter your sentence : "))