math_marks=int(input("Enter math marks: "))
English_marks=int(input("Enter English marks: "))
if math_marks>80 and English_marks>80:
    print("A grade")
elif math_marks>80 or English_marks>80 :
    print("B grade")
else:
    print("C grade")