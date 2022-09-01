print("\n\nExercise_01")

score = {'국어':80, '영어':75, '수학':55}

a = (len(score.keys()))

score['Total'] = score['국어'] + score['영어'] + score['수학']
score['Average'] = score['Total'] / a

for k, v in score.items():
    print(k, "\t:", v)
    

print("\n\nExercise_02")

num = [13, 14]

for data in num:
    if(data%2 != 0):
        print(data, " is Odd Number")
    else:
        print(data, " is Even Number")


print("\n\nExercise_03")

S_ID = "881120-1068234"

print("The Year of Birth is 19", S_ID[0:2])
print("The date of Birth is ", S_ID[2:4], ".", S_ID[4:6])
print("The Number is ", S_ID[7:])


print("\n\nExercise_04")

pin = ['881120-1068234', '881120-2068234']

for data in pin:
    if(data[7] == '1'):
        # print(data[7])
        print(data, "is MALE!")
    else:
        # print(data[7])
        print(data, "is FEMALE!")


print("\n\nExercise_05")

a = "a:b:c:d"
print(a)

b = a.replace(':', '#')
print(b)


print("\n\nExercise_06")

a = [1, 3, 5, 4, 2]

a.sort()
a.reverse()

print(a)


print("\n\nExercise_07")

str = ["Life", "is", "too", "short"]
full_str = " ".join(str)

print(full_str)


print("\n\nExercise_08")

a = (1, 2, 3)
b = (4, )

c = a + b

print(c)


print("\n\nExercise_09")

a = dict()

a['name'] = 'python'
a[('a', )] = 'python'
#a[(1, [1])] = 'python'
a[250] = 'python'

print(a)


print("\n\nExercise_10")

a = {'A':90, 'B':80, 'C':70}
value = a.pop('B')

print("'B' is", value)
print(a)


print("\n\nExercise_11")
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
b = set(a)

print(b)


print("\n\nExercise_12")

a = b = [1, 2, 3]

a[1] = 4

print("a is", a)
print("b is", b)

print("id(a) is", id(a))
print("id(b) is", id(b))

print("왜냐하면, a에 b를 대입하면, b에 a의 value 값이 복사되는 것이 아니라 a의 주소값을 b에 넘겨주기 때문이다.")
