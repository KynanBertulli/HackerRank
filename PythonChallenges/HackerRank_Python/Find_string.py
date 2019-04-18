"""

HackerRank Python
Find a String
@author Kynan Bertulli


"""

# ABCDCDC
# CDC
def count_substring(string, sub_string):
    str = string.split()
    str2 = []
    count = 0
    for i in str:
        if i not in str2:
            str2.append(i)

    for i in range(0, len(str2)):
        print('Frequency of', str2[i], 'is :', str.count(sub_string)
    # count = string.count(sub_string)
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(str(count))