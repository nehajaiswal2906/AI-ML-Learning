# 🔥🔥 Hard Challenge 2 — Word Frequency Analyzer

# Given:

# text = """
# Python is powerful, and Python is easy.
# I love Python because Python is powerful!
# """

# Build a program that:

# Converts words to lowercase.
# Removes punctuation such as . , ! ?.
# Splits the text into words.
# Counts how many times each word occurs.
# Prints the frequency of every word.

# For example, your output should contain results equivalent to:

# python : 4
# is : 3
# powerful : 2
# and : 1
# easy : 1
# i : 1
# love : 1
# because : 1
# Restrictions
# Don't use collections.Counter.
# Don't use regular expressions.
# Don't hard-code the words.
# The program must work with different input text.
# Extra challenge

# Print the most frequently occurring word and its frequency.

# Example:

# Most frequent: python (4)

# Skills tested: cleaning, traversal, replace(), split(), count(), 
# lists, nested logic, problem decomposition.


st=input("Enter the string:").lower()
ls=[]
for i in st:
        if i in ".,!?;:":
            continue
        else:
            ls.append(i)
wp="".join(ls)
print(wp)
nls=wp.split()
print(nls)
nl=[]
for i in nls:
    if i not in nl:
        nl.append(i)
hc=0
for i in nl:
    count=0
    while i in nls:
        count+=1
        nls.remove(i)
    if count>hc:
         hc=count
         word=i
    print(i,":",count)
if hc>1:
    print(f"The word with highest count is: {word}\nFrequency: {hc}")
else:
    print("All the words have same frequency which is equals to 1.")



