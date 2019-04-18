"""

HackerRank Python
Split and Join
@author Kynan Bertulli


"""

def split_and_join(line):
    # write your code here
    splitword = line.split(" ")
    joinword = "-".join(splitword)
    return joinword

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)