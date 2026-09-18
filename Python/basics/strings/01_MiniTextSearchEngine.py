# 🔥🔥🔥 Hard Challenge 3 — Mini Text Search Engine

# This is the serious one.

# Write a program that receives:

# text = """
# Python is a powerful programming language.
# Python is easy to learn.
# Many students learn Python because Python is useful.
# """

# and a search word:

# query = "python"

# Your program should report:

# Word: python
# Occurrences: 4
# First position: ...
# Last position: ...

# But there are rules.

# Rules

# 1. Case-insensitive

# These should all count as the same word:

# Python
# python
# PYTHON
# PyThOn

# 2. Whole-word matching

# For:

# python

# these count:

# Python
# python
# PYTHON

# but these do NOT count:

# python3
# pythonic
# mypython

# 3. Don't use:

# str.count()

# for the actual occurrence calculation.

# 4. Don't use regular expressions.

# 5. Don't hard-code the positions.

# 6. It must work for arbitrary text and arbitrary queries.

# Example

# If:

# text = "Python python PYTHON pythonic mypython python3"
# query = "python"

# the answer should be:

# Occurrences: 3

# because only the first three are complete words.

# 🚨 Final Boss Extension

# Modify Challenge 3 so that it accepts multiple queries:

# queries = ["python", "learn", "powerful", "student"]

# and produces something like:

# python    -> 4
# learn     -> 2
# powerful  -> 1
# student   -> 1

# The program should work regardless of how many queries are provided.

text=input("Enter the String:").lower()
query=input("Enter the word u want to search:").lower()

ls=[]

for i in text:
    if i not in ",.?:;":
        ls.append(i)
ntext="".join(ls)
t=ntext.split()
count=0
for i in t:
    if i==query:
        count+=1
print("Word:",query)
print("Ocurrences:",count)

if count>0:
    fo=text.find(query)
    first=-1
    last=-1

    while fo!=-1:

        if fo==0:
            left=True
        else:
            left= not text[fo-1].isalnum()

        if fo+len(query)==len(text):
            right=True
        else:
            right= not text[fo+len(query)].isalnum()

        if left and right:

            if first==-1:
                first=fo

            last=fo

        fo=text.find(query,fo+len(query))

    if first==last:
        print("Occurence Index:",first)
    else:
        print("First Occurence index:",first)
        print("Last Occurence index:",last)

else:
    print("Word not found.")

