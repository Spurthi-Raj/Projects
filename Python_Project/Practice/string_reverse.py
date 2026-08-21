# using while loop
# name = input("Enter the string : ")
# print("original string is : ",name)
# r_name = ""
# count = len(name)
# while count > 0:
#     r_name = r_name + name[count-1]
#     count = count-1
# print("reversed string : ",r_name)


# using for loop
# name = input("Enter the string : ")
# print("original string is :",name)
# r_name = ""
# for char in name:
#     r_name = char + r_name
# print("reversed string :",r_name)


# name = "spurthi"
# print(name[::-1])


# ------split method-------

# it breaks up a string at specified saperator,and returns list of string

msg = "Hello hi good morning"
new_msg = msg.split()
print(new_msg,len(new_msg))

# ---------- string replace --------------
s = "spoorthi"
print(s.replace('o','u'))