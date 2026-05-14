# 1 - Task:

# Create a Python program that:

# Asks user for a username
# Appends it into a file called logins.txt
# Then reads the file and prints ALL previous logins
# Requirements:
# Use "a" mode to store login
# Use "r" mode to display history
# Use with open(...)
# Example output:
# Enter username: ali

# Login stored!

# Previous logins:
# ali
# ahmad
# sara

# username = input("Enter the username: ")

# with open("logins.txt", "a") as f:
#     f.write(username + "\n")

# print("Login saved successfully!\n")

# with open("logins.txt", "r") as f:
#     print("Previous logins:")
#     print(f.read().strip().split("\n")) 
    # strip is used to remove any leading or trailing whitespace characters, including the newline character at the end of the file.
    # split("\n") is used to split the string into a list of logins based on the newline character, so each login will be an individual element in the list.



# in file handling if i we don't know the path of a file we can use the following code to get the path of the file:
# print(os.path.abspath("logins.txt")) //abs means absolute path, it will give us the full path of the file logins.txt

# now we can use the paths of file to read , write and copy the file from one location to another location.

import os
# url=os.path.exists("problem.txt") #it finds in your current working directory 
# print(url)

# url1=os.path.abspath("login.txt") #abs path will attach this file to the current folder 
# # print(url1)
# url2=os.path.abspath("problem.txt")
# # print(url2) #this will throw error as the file doesn't exist in current folder 

# # get current working directory getcwd
# current_directory=os.getcwd() # get current working directory
# print(current_directory)


# wrong version , here the urls have the same directory which is not actualy existing 
# with open(url1 , "r") as f : 
#     content=f.read()
# with open(url2  , "w") as f: 
#     f.write(content)
# with open(url2 , "r") as f : 
#     c=f.read()
#     print(c)


# you should either manually give the paths , or you can also join the paths like this 


# url= r"D:\local_projects\FileHandling2\project1\logins.txt"
# url2=os.path.join("D:\\local_projects\\filehandling2\\project2" , "problem.txt")
# with open(url , "r") as f : 
#     content=f.read()
# with open(url2  , "w") as f: 
#     f.write(content)
# with open(url2 , "r") as f : 
#     c=f.read()
#     print(c)




# gw=os.getcwd()
# print(gw)
# D:\local_projects\FileHandling2\project1 this is the output 




# another version 
# here it tells the importance of using abspath , becuase it converts the file in current path which is okay as logins.txt exists in the current path 

url= os.path.abspath("logins.txt") #building reltive to absolute path 
url2=os.path.join("D:\\local_projects\\filehandling2\\project2" , "problem.txt") #its path is not current folder that's why we built the path by joining 
with open(url , "r") as f : 
    content=f.read()
with open(url2  , "w") as f: 
    f.write(content)
with open(url2 , "r") as f : 
    c=f.read()
    print(c)



gw=os.getcwd()
print(gw)











