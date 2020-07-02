# palindrome 

# function to check for palindrome
def palindrome(string):
    # reverse the string
    rev_string = string[::-1]
    # compare the string with its reverse
    if string == rev_string:
        print("Given string is a palindrome.")
    else:print("Given string is not a palindrome.")
    
# calling the function and passing string as a parameter
palindrome(string = input("Enter your string : "))