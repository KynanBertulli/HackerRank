
secret_word = "giraffe"
guess = ""
count = 0
while guess != secret_word:
    guess = input("enter guess: ")
    count+= 1
    print("try " + str(count))

print("you win!")