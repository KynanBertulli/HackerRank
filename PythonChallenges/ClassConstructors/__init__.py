""""
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39




"""




if __name__ == '__main__':
    classList = []
    scorelist = []
    nameList = []
    results = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        classList.append([name, score])
        scorelist.append(score)
        nameList.append(name)

    sorted_scores = sorted(scorelist)
    class_Dict = dict(zip(nameList,scorelist))
    # print(str(class_Dict))
    # print(sorted_scores)
    list(class_Dict)
    sorted(class_Dict)
    print(class_Dict)
    for i in sorted_scores[1:]:
        if sorted_scores[i] <= sorted_scores[i+1]:
            results = sorted_scores[i]
    print(results)

