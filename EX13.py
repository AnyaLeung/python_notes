# script being another name for your .py files
# MODULE: these little things you import to make your Python program do more | IMPORT MODULES

from sys import argv

script, first, second, third = argv

print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is：', third)

# The `argv` is the "argument variable"

# What's the difference between argv and raw_input()?
# **where** the user is required to give input. 
# If they give your script inputs on the **command line**, then you use argv.
# If you want them to input using the keyboard **while the script is running**, then use input().
