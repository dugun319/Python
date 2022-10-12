import random
import time

getstr = random.getstate()
list(getstr)
print("\nLine_7 getstr = ", getstr[1][0])
print()

random.seed(random.random())
getstr = random.getstate()
list(getstr)
print("\nLine_13 getstr = ", getstr[1][0])
print()

a = random.random()
print(a)
print(len(str(a)))

a = random.random()
print(a)
print(len(str(a)))

getstr = random.getstate()
list(getstr)
print("\nLine_26 getstr = ", getstr[1][0])
print()


random.seed(time.strftime("%d", time.localtime()))
#random.seed(time.localtime())

getstr = random.getstate()
list(getstr)
print("\nLine_35 getstr = ", getstr[1][0])
print()

# print(random.setstate())

# 이 메서드를 사용하여 보안 토큰을 생성해서는 안 됩니다.

print(random.randbytes(3))

getstr = random.getstate()
list(getstr)
print("\ngetstr = ", getstr[1][0])
print()

print(random.randbytes(2))
print(random.randbytes(1))

print(random.randrange(10))
print(random.randrange(0, 50, 10))
print(random.randint(0, 45))

print(random.getrandbits(1))
print(random.getrandbits(2))
print(random.getrandbits(3))


# SEED Change
random.seed()

getstr = random.getstate()
list(getstr)
print("\ngetstr = ", getstr[1][0])
print()


print(random.randbytes(3))

getstr = random.getstate()
list(getstr)
print("\ngetstr = ", getstr[1][0])
print()


print(random.randbytes(2))
print(random.randbytes(1))

getstr = random.getstate()
list(getstr)
print("\ngetstr = ", getstr[1][0])
print()

print(random.randrange(10))
print(random.randrange(0, 50, 10))
print(random.randint(0, 45))


print("\n\nrandom.getrandbits\n")

print(random.getrandbits(1)) # 0 to 1
print(random.getrandbits(2)) # 0 to 3
print(random.getrandbits(3)) # 0 to 7


print("\n\nrandom.choice\n")

print(random.choice(["Life", "is", "too", "short", "You", "Need", "Python"]))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


print("\n\nrandom.choices\n")

str = ["Life", "is", "too", "short", "You", "Need", "Python"]
print(random.choices(str, weights=[43, 1, 1, 1, 1, 1, 1], k = 10))


print("\n\nrandom.shuffle\n")

random.shuffle(str)
print(str)
print(random.shuffle(str))


print("\n\nrandom.uniform\n")

print(random.uniform(1, 5))


# LOTTO / random.sample 중복 없는 반복추출

print("\n\n선택은 당신의 몫입니다. 살지 말지\n")
lottery = []
for i in range(1, 46):
    lottery.append(i)
print(random.sample(lottery, 6))

print()

random.seed(random.random())
getstr = random.getstate()
list(getstr)
print("\nrandom.seed(random.random()) getstr = ", getstr[1][0])
print()

