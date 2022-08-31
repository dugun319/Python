print("\n\nExercise_01")

def Odd_Even(a):
    if a%2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

if __name__ == "__main__":
    print("The input number is 5")
    Odd_Even(5)
    print("The input number is 8")
    Odd_Even(8)



print("\n\nExercise_02")

def Sum_all(*nums):
    result = 0
    for i in nums:
        result = result + i
    
    return result / len(nums)

if __name__ == "__main__":
    print("The average is %d" %Sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9))



print("\n\nExercise_03")

input1 = '3' # input("첫번째 숫자를 입력하세요:")
input2 = '6' # input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)



print("\n\nExercise_04")

print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))



print("\n\nExercise_05")

f1 = open("C:\\Users\\KOSTA\\Newfile.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("C:\\Users\\KOSTA\\Newfile.txt", 'r')
data = f2.readline()
print(data)
f2.close()



print("\n\nExercise_06")

f1 = open("Newfile.txt", 'a')
data = input("Input the sentence: ")
f1.write(data)
f1.close()

f2 = open("Newfile.txt", 'r')
print(f2.read())
f2.close()
