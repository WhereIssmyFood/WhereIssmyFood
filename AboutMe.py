Username = "WhereIssMyFood"
ShareInfo = False

if Username == "WhereIsMyFood":
  print("That's my name!")				
elif Username == "WhereIssMyFood":
	print("That's my Name, but with an Additional s lol")
	ShareInfo = True
else:
	print("What is my name..?")
	input(">> ")

UserInterestDictionary = {
	# Online
	"Coding":"Python, Lua, C++, C#, Javascript, Java",
	"Discord":"Food#9172",
	"Frameworks":"Pycord, Pygame",
	"Developing":"Games, Websites",
	# Personal
	"AboutMe":"I like Python the most, And I like cooking",
	"Cooking":True,
	"Age":14
}

WhatAmILearningList = [
	["Intermediate"]["Python", "Lua", "HTML and CSS", "Javascript"]
	["Beginner"]["Java", "C++ and C#"]
	["In the Future..."]["I will learn SQL because Why not?"]
]


Contact = """
[REDACTED] for Business
ninendoswitchiscool@gmail.com for Random stuff.
"""

Collaborations = f"I just wanna learn Coding, so if you have time to kill or wanna have fun, maybe {Contact} me!"

if ShareInfo == True:
	print(UserInterestDictionary, WhatAmILearningList, Contact, Collaborations)
else:
	print("go away")
	
