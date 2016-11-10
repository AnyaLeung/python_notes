# Most of what software does is the following:
# 1 Take some kind of input from a person.
# 2 Change it.
# 3 Print out something to show how it changed.

print('How old are you?'),
age = input()
print('How tall are you?'),
height = input()
print('How much do you weigh?'),
weight = input()

print('So, you\'re %r old, %r tall and %r heavy.' % (age, height, weight))
# py3 format ('xxxxx%xxxx' % (xxx) )

#cannot run T T y?
# cuz  Python 3.x's input is python 2.x's raw_input 敲黑板

# We put a , (comma) at the end of each print line.
# This is so `print` doesn't end the line with a newline character and go to the next line.

# 轉化爲整數 `int()`
#  less than 80 characters long
