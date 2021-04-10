###########################################
### 第６回 文字列に値を埋め込んでみよう ###
###########################################

# name = "taguchi"
# score = 52.8
# 
# # print("name: %s, score: %f" % (name, score))
# # print("name: %-10s, score: %10.2f" % (name, score))
# 
# # print("name: {0}, score: {1}".format(name, score))
# print("name: {0:>10s}, score: {1:<10.2f}".format(name, score))

#########################################################################################

#####################################
### 第７回 ifで条件分岐してみよう ###
#####################################

# score = int(input("score ? "))
# 
# # > >= < <= == !=
# # if score > 80:
# #     print("Great!")
# # elif score > 60:
# #     print("Good!")
# # else:
# #     print("so so ...")
# 
# print("Great!" if score > 80 else "so so ...")


#########################################################################################

################################
### 第８回 whileでループ処理 ###
################################

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("end")


#########################################################################################

################################
### 第９回 forで繰り返し処理 ###
################################

# for i in range(10):
#     if i == 5:
#         # break
#         continue
#     print(i)
# else:
#     print("end")


#########################################################################################

###################################
### 第１０回 関数を作ってみよう ###
###################################

# # def say_hi():
# #     print("hi")
# #
# # say_hi()
# 
# # def say_hi(name, age):
# def say_hi(name, age = 20):
#     print("hi {0} ({1})".format(name, age))
# 
# say_hi("tom", 23)   # tom (23)
# say_hi("bob", 21)   # bob (21)
# say_hi("steve")     # steve (20)
# say_hi(age = 18, name = "rick")


#########################################################################################

###########################################
### 第１１回 関数の返り値を使ってみよう ###
###########################################

# def say_hi():
#     pass
#     # print("hi")
#     # return "hi"
#     # print("hello")
# 
# msg = say_hi()
# print(msg)


#########################################################################################

###########################################
### 第１２回 変数のスコープを理解しよう ###
###########################################

# # msg = "hello" # グローバル変数
# #
# # def say_hi():
# #     msg = "hi" # ローカル変数
# #     print(msg)
# #
# # say_hi()
# # print(msg)
# 
# # msg = "hello" # グローバル変数
# #
# # def say_hi():
# #     print(msg)
# #
# # say_hi()
# # print(msg)
# 
# msg = "hello" # グローバル変数
# 
# def say_hi():
#     global msg
#     msg = "hello global"
#     print(msg)
# 
# say_hi()
# print(msg)



#########################################################################################

#####################################
### 第１３回 クラスを作ってみよう ###
#####################################

# # user_name = "taguchi"
# # user_score = 10
# 
# class User:
#     pass
# 
# tom = User() # インスタンス
# tom.name = "tom"
# tom.score = 20
# 
# bob = User()
# bob.name = "bob"
# bob.level = 5
# 
# print(tom.name)
# print(bob.level)


#########################################################################################

#############################################
### 第１４回 コンストラクタを使ってみよう ###
#############################################

# # class User:
# #     pass
# #
# # tom = User()
# # tom.name = "tom"
# # tom.score = 20
# #
# # bob = User()
# # bob.name = "bob"
# # bob.level = 5
# 
# class User:
#     def __init__(self, name):
#         # インスタンス変数
#         self.name = name
# 
# tom = User("tom")
# bob = User("bob")
# 
# print(tom.name)
# print(bob.name)



#########################################################################################

#########################################
### 第１５回 クラス変数を使ってみよう ###
#########################################

# class User:
#     # クラス変数
#     count = 0
#     def __init__(self, name):
#         User.count += 1
#         self.name = name
# 
# print(User.count) # 0
# tom = User("tom")
# bob = User("bob")
# print(User.count) # 2
# 
# print(tom.count) # 2


#########################################################################################

#######################################
### 第１６回 メソッドを使ってみよう ###
#######################################

# class User:
#     count = 0
#     def __init__(self, name):
#         User.count += 1
#         self.name = name
#     # インスタンスメソッド
#     def say_hi(self):
#         print("hi {0}".format(self.name))
#     # クラスメソッド
#     @classmethod
#     def show_info(cls):
#         print("{0} instances".format(cls.count))
# 
# tom = User("tom")
# bob = User("bob")
# 
# # tom.say_hi()
# # bob.say_hi()
# 
# User.show_info()


#########################################################################################

#######################################
### 第１８回 クラスを継承してみよう ###
#######################################

# class User:
#     def __init__(self, name):
#         self.name = name
#     def say_hi(self):
#         print("hi {0}".format(self.name))
# 
# class AdminUser(User):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def say_hello(self):
#         print("hello {0} ({1})".format(self.name, self.age))
#     # override
#     def say_hi(self):
#         print("[admin] hi {0}".format(self.name))
# 
# bob = AdminUser("bob", 23)
# print(bob.name)
# bob.say_hi()
# bob.say_hello()


#########################################################################################

###########################################
### 第１９回 クラスを多重継承してみよう ###
###########################################

# class A:
#     def say_a(self):
#         print("A!")
#     def say_hi(self):
#         print("hi! from A!")
# class B:
#     def say_b(self):
#         print("B!")
#     def say_hi(self):
#         print("hi! from B!")
# 
# # class C(A, B):
# class C(B, A):
#     pass
# 
# c = C()
# # c.say_a()
# # c.say_b()
# c.say_hi()


#########################################################################################

#########################################
### 第２０回 モジュールでファイル分割 ###
#########################################

# # myapp.py
# # import user
# # from user import AdminUser
# from user import AdminUser, User
# 
# # bob = user.AdminUser("bob", 23)
# bob = AdminUser("bob", 23)
# 
# tom = User("tom")
# 
# print(bob.name)
# bob.say_hi()
# bob.say_hello()
# 
# 
# #user.py
# class User:
#     def __init__(self, name):
#         self.name = name
#     def say_hi(self):
#         print("hi {0}".format(self.name))
# 
# class AdminUser(User):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def say_hello(self):
#         print("hello {0} ({1})".format(self.name, self.age))
#     def say_hi(self):
#         print("[admin] hi {0}".format(self.name))
# 
# # print("hello")

#########################################################################################

#####################################
### 第２２回 例外処理をしてみよう ###
#####################################

# class MyException(Exception):
#     pass
# 
# def div(a, b):
#     try:
#         if (b < 0):
#             raise MyException("not minus")
#         print(a / b)
#     except ZeroDivisionError:
#         print("not by zero!")
#     except MyException as e:
#         print(e)
#     else:
#         print("no exception!")
#     finally:
#         print("-- end --")
# 
# div(10, -3)
# # div(10, 3)
# # div(10, 0)


#########################################################################################

#######################################
### 第２３回 リスト型を使ってみよう ###
#######################################

# scores = [40, 50]
# # print(scores[0]) # 40
# # scores[0] = 45
# # print(len(scores)) # 2
# # scores.append(100)
# # print(scores)
# 
# # for score in scores:
# #     print(score)
# 
# for i, score in enumerate(scores):
#     print("{0}: {1}".format(i, score))


#########################################################################################

#####################################
### 第２４回 タプルを使ってみよう ###
#####################################

# # items = (50, "apple", 32.5)
# # print(items[1])
# # items[1] = "pen"
# 
# print(list((1, 3, 5)))
# print(tuple([1, 3, 5]))


#########################################################################################

#################################################
### 第２５回 スライスで要素を切り出してみよう ###
#################################################

# # scores = [40, 50, 70, 90, 60]
# # print(scores[1:4]) # 50, 70, 90
# # print(scores[:2]) # 40, 50
# # print(scores[3:]) # 90, 60
# # print(scores[-3:]) # 70, 90, 60
# 
# s = "hello"
# print(s[1:4])


#########################################################################################

#####################################
### 第２６回 集合型を使ってみよう ###
#####################################

# # a = set([5, 4, 8, 5])
# # a = {5, 3, 8, 5}
# # print(a)
# # print(5 in a) # True
# # a.add(2)
# # a.remove(3)
# # print(a)
# # print(len(a))
# 
# a = {1, 3, 5, 8}
# b = {3, 5, 8, 9}
# print(a | b)
# print(a & b)
# print(a - b)


#########################################################################################

#####################################
### 第２７回 辞書型を使ってみよう ###
#####################################

# sales = {"taguchi": 200, "fkoji": 400}
# # print(sales["taguchi"])
# # sales["taguchi"] = 300
# # sales["dotinstall"] = 500
# # del(sales["fkoji"])
# # print(sales)
# 
# for key, value in sales.items():
#     print("{0}: {1}".format(key, value))

#########################################################################################

#######################################
### 第２８回 イテレータを理解しよう ###
#######################################

# # scores = [40, 50, 70, 90, 60]
# # it = iter(scores)
# # print(next(it))
# # print(next(it))
# # print("hello")
# # print(next(it))
# #
# # for score in scores:
# #     print(score)
# 
# def get_infinite(): # ジェネレータ
#     i = 0
#     while True:
#         yield i * 2
#         i += 1
# 
# g = get_infinite()
# print(next(g))
# print(next(g))
# print(next(g))


#########################################################################################

##########################################
### 第２９回 map, lambdaを使ってみよう ###
##########################################

# # def triple(n):
# #     return n * 3
# 
# # print(list(map(triple, [1, 2, 3])))
# 
# # lambda 引数: 処理
# print(list(map(lambda n: n * 3, [1, 2, 3])))


#########################################################################################

#####################################
### 第３０回 filterを使ってみよう ###
#####################################

# # def is_even(n):
# #     return n % 2 == 0
# 
# # print(list(filter(is_even, range(10))))
# 
# print(list(filter(lambda n: n % 2 == 0, range(10))))

