#1.Introduce boolean type
sunny = True #注意首字母大写
print(1, type(sunny), sunny)

#2.Compare I
number1 = 3
number2 = 5
print(2, number1 < number2) #'number1 < number2' 是一个布尔表达式

#3.Compare II
number1 = 3
number2 = 3
print(3, number1 >= number2)

#4.Compare III
number = 30
boolean = number == 30 #区别'='和'=='
print(4, boolean)

#5.Compare IV
number = 30
boolean = number != 30 #'!='不等于
print(5, boolean)

#6.String compare
pw = "123456"
boolean = pw == "password"
print(6, boolean)

#7.Logical operator -- not
boolean = 3.14159265359 == 3
opposite = not boolean
print(7, opposite)

#8.Logical operator -- and
boolean1 = True
boolean2 = False
print(8, boolean1 and not boolean2) #not 优先级大于 and

#9.Logical operator -- or
boolean1 = False
boolean2 = True
print(9, boolean1 or boolean2)

#10.Mix
rainy = False
sunny = not rainy
print(10.1, rainy and sunny)
print(10.2, len("password") >= 8)