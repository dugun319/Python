#hello.py

sentence = """The Zen of Python, by Tim Peters Beautiful is better than ugly.
Explicit is better than implicit. Simple is better than complex. 
Complex is better than complicated. Flat is better than nested.
Sparse is better than dense. Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity. 
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never. 
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those!"""

target = ['a', 'e', 'i', 'o', 'u', '1', '2']

# print(sentence)

# t_count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
t_count = {}

for charactor in sentence.lower():
    if charactor in target:
        t_count.setdefault(charactor, 0)
        t_count[charactor] += 1

for k, v in sorted(t_count.items()):
    print("Total number of [", k, "] is : ", v)

"""
for data in sentence.lower() :
    if data == 'a':
        t_count['a'] = t_count['a'] + 1
    elif data == 'e':
        t_count['e'] = t_count['e'] + 1
    elif data == 'i':
        t_count['i'] = t_count['i'] + 1
    elif data == 'o':
        t_count['o'] = t_count['o'] + 1
    elif data == 'u':
        t_count['u'] = t_count['u'] + 1
    else :
        print("This charator in not you wnat to find!")
"""

print("Total number of 'a' is ", t_count['a'], "\tsentence.count(a) is ", sentence.count('a') + sentence.count('A'))
print("Total number of 'e' is ", t_count['e'], "\tsentence.count(e) is ", sentence.count('e') + sentence.count('E'))
print("Total number of 'i' is ", t_count['i'], "\tsentence.count(i) is ", sentence.count('i') + sentence.count('I'))
print("Total number of 'o' is ", t_count['o'], "\tsentence.count(o) is ", sentence.count('o') + sentence.count('O'))
print("Total number of 'a' is ", t_count['u'], "\tsentence.count(u) is ", sentence.count('u') + sentence.count('U'))

