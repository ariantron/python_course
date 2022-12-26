# CRUD
# -------
# CREATE
# READ
# UPDATE
# DELETE

f = open("test.txt", "w")
f.write("Hello World")
f.close()

g = open("test.txt", "r")
print(str(g.read()))
g.close()
