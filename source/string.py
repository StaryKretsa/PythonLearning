nationality = ""
print(type(nationality))
#--------------------------
name = "Captain Future"
character = name[0]
print(character)
#--------------------------
name = "Captain Future"
rank = name[0:7]
print(rank)
#--------------------------
q = "What's your name?"
q = q.replace("name", "quest")
print(q)
#--------------------------
q1 = "What's your name?"
q2 =  'what\'s your name?'
print(q1)
print(q2)
#--------------------------
a = "Arthur, king of the Britons"
a += "\n"
a += "I seek the Holy Grail"
print(a)
#--------------------------
a = """what do you mean?
An African or a European \
swallow?"""
print(a)
#--------------------------
path = r"C:\notes"
print(path)
#--------------------------
q = 'What\'s the air speed \
velocity of an unladen swallow?'
word = q[-8:-1]		#负数从后向前复制
q = q.replace(word, "rabbit")
print(q)