if __name__ == "__main__":

    print("\n\nExercise_01\n")

    a = "Life is too short, you need python"

    if "wife"in a: print("wife")
    elif "python"in a and "you"not in a: print("python")
    elif "shirt"not in a: print("shirt")
    elif "need"in a: print("need")
    else: print("none")


    print("\n\nExercise_02\n")

    num = 0
    total = 0

    while num < 1001 :
        if num%3 == 0:
            total = total + num
        num = num + 1

    print("The Sum of 3 multiples is %d" %total)


    print("\n\nExercise_03\n")
    num = 0

    while num < 5:
        a = 0
        while a < num + 1:
            print("*", end="")
            a = a + 1
        num = num + 1
        print()



    print("\n\nExercise_04\n")

    for i in range(1, 101):
        print(i, end = "  ")


    print("\n\nExercise_05\n")
    total = 0
    ave = 0
    score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

    for indi_score in score:
        total = total + indi_score
        
    ave = total / len(score)

    print("Total score of class is %d" %total)
    print("Average score of class is %d" %ave)


    print("\n\nExercise_06\n")

    numbers = [1, 2, 3, 4, 5]
    result = [data * 2 for data in numbers if data%2 != 0]
    print(result)

    result2 = [num * 3 for num in range(1, 100) if num%3 == 0]
    print(result2)
    print("The length of result2 is %d" %len(result2))

    result3 = [i + j for i in range(1, 5) for j in range(1, 10)]
    print(result3)


    print("\n\nExercise_07\n")
    num1 = 1
    num2 = 1
    total = [num1, num2]

    for i in range(0, 20):
        num3 = num1 + num2
        total.append(num3)
        num1 = num2
        num2 = num3

    print(total)

    ratio = []

    for i in range(0, 19):
        ratio.append(total[i+1] / total[i])

    print(ratio)

    sum = 0

    for i in range(0, len(ratio)):
        sum = sum + ratio[i]

    print(sum / len(ratio))

