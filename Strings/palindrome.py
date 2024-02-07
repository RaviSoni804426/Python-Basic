def palindrome(str):
    clean_str = (str.replace(" ", "")).lower()
    reverse_str = clean_str[::-1]
    return (clean_str == reverse_str)
str=input("Enter a string: ")
if palindrome(str):
    print("palindrome")
else:
    print("not a palindrome")
    