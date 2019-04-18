"""

HackerRank Python
Mutations
@author Kynan Bertulli


"""
# string = string[:5] + "k" + string[6:]
# abracadabra
# 5 k
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)