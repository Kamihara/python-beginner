# 3-8

# : int 整数型として宣言（後から代入される値で変化するのであまり意味はない）
num: int = 1
# : str 文字列型として宣言（後から代入される値で変化するのであまり意味はない）
name: str = 'Mike'
is_ok = True

# type関数 変数の型を得る
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))


# 整数型だった変数に文字列を代入すると文字列型になる
num = name
print(num, type(num))

# int関数で文字列を整数に
new_num = int('1')
print(new_num, type(new_num))


# 3-9
# セパレーターと終了文字を指定できる
print('Hi', 'Mike', sep=',', end='.\n')
print('Hi', 'Mike', sep=',', end='.\n')

# 3-10
import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

# math関数のhelpを出力する
print((help(math)))


# 3-11
# 'でも”でもどちらでも可
print('hello')
print("hello")

# いろんなエスケープの仕方
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")
print('hello.\nHow are you?')

# r指定で\nを無視
print(r'C:\name\name')

# プログラムを出力するときとかに便利
print("##############")
print("""\
line1
line2
line3\
""")
print("##############")

# 演算もできる
print('Hi,' * 3 + 'Mike.')

# 文字列を()内に入れて出力するとひと繋がりになる
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

# 3-12
# 文字列のスライス
word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print('#################')
print(word[:2])
print('#################')
print(word[2:])
print('#################')
word = 'j' + word[1:]
print(word)
print(word[:])
n = len(word)
print(n)


# 3-13
s = 'My name is Mike, Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print("######################")


print(s.find("Mike"))
print(s.rfind("Mike"))
print(s.count("Mike"))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))



# 4-17
r = [1,2,3,4,5,1,2,3]
print(r.index(3,3))
print(r.count(4))

if 10 in r:
     print("exist")

r.sort()
print(r)
r.sort(reverse=True)
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

x = '####'.join(to_split)
print(x


print(help(list))


# 4-18
i = [1,2,3,4,5]
j = i
i[0] = 100
print('i=', i)
print('j=', j)

x= [1,2,3,4,5]
y = x.copy()
x[0] = 100
print('x=', x)
print('y=', y)

X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)

P = ["a", "b"]
Q = P
P[0] = "x"
print(id(P))
print(id(Q))
print(P)
print(Q)


