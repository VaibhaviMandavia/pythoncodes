# to find the longest word present in a sentence

# function to find the longest word
def longest_word(sentence):
    # split the sentence using space as a separator and store it in a list
    sentence = sentence.split(" ")
    max_len = 0
    # loop through the list of words to find the the length of the longest word 
    for i in sentence:
        length = len(i)
        if length > max_len:
            max_len = length
    # loop through the list of words to find the longest word
    for i in sentence:
        if len(i) == max_len:
            # print the longest word with its length
            print("The longest word in the sentence is : "+i+" and its length is : ",max_len)

# calling the function and passing string(sentence) as a parameter
longest_word(input("Enter your sentence: "))
