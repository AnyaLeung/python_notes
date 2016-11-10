# Why do the \n newlines not work when I use %r?
# That's how %r formatting works; it prints it the way you wrote it (or close to it). It's the "raw" format for debugging.</br>
# ↑不懂

"I am 6'2\" tall."
'I am 6\'2" tall'

tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
