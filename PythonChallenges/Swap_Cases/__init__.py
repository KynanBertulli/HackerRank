def swap_case(s):
    a1 = list(s)
    for i in range(len(a1)):
        if(a1[i].isupper()):
            a1[i] = a1[i].lower()
        else:
            a1[i]= a1[i].upper()
    return a1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print("".join(result))