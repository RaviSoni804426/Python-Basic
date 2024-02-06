input_string=input("Enter string: ")
n=int(input("Enter n: "))
alphabets="abcdefghijklmnopqrstuvwxyz"
reverse=alphabets[::-1]
dict1=dict(zip(alphabets,reverse))
print(dict1)