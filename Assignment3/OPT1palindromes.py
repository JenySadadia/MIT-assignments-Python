def is_palindrome(str):
    if(str==str[::-1]):
        print(str,"is pallindrome")
    else:
        print(str,"is not pallindrome")
str=input("Enter String:")
is_palindrome(str)