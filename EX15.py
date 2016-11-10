from sys import argv

script, filename = argv

txt = open(filename) #1-3 get a file name

print('Here\'s ur file %r:' % filename)
print(txt.read())# call a function on txt named read

print('Type the filename again:')
file_again = input('>')

txt_again = open(file_again)

print(txt_again.read())# u give a file a command by using the `.``

#  reading from a file
#  erase your work
