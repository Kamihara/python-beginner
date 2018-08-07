# # 3-8
#
# : int 整数型として宣言（後から代入される値で変化するのであまり意味はない）
# num: int = 1
# : str 文字列型として宣言（後から代入される値で変化するのであまり意味はない）
# name: str = 'Mike'
# is_ok = True
#
# type関数 変数の型を得る
# print(num, type(num))
# print(name, type(name))
# print(is_ok, type(is_ok))
#
#
# 整数型だった変数に文字列を代入すると文字列型になる
# num = name
# print(num, type(num))
#
# int関数で文字列を整数に
# new_num = int('1')
# print(new_num, type(new_num))


# # 3-9
# セパレーターと終了文字を指定できる
# print('Hi', 'Mike', sep=',', end='.\n')
# print('Hi', 'Mike', sep=',', end='.\n')

# # 3-10
# import math
#
# result = math.sqrt(25)
# print(result)
#
# y = math.log2(10)
# print(y)
#
# # math関数のhelpを出力する
# print((help(math)))


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


