# def print_nto_1(n):
#     if n==0:
#         return
#     print(n)
#     print_nto_1(n-1)
# print_nto_1(5)
def print_n_to_1(n):
    if n == 0:
        return
    
    print_n_to_1(n - 1)
    print(n)
print_n_to_1(5)