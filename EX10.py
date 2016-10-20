# Why do the \n newlines not work when I use %r?
# That's how %r formatting works; it prints it the way you wrote it (or close to it). It's the "raw" format for debugging.</br>
# ↑不懂
"""
%r 和 %s:
python字符串格式化有2种形式: %r, %s, 先看1个例子:

  >>> "this is %s" % 'python'
  'this is python'
  >>> "this is %r" % 'python'
  "this is 'python'"

第一个%s会被格式化为python, 而第二个%r则会被格式化为'python'.
这也就是%r表示raw的原因, 相比于%s仅仅格式化某个变量的内容, %r还会告诉你这个变量的性质比如''字符串.

更深入一点点, **python中一切都是对象**, %r %s 其实对应于对象的2种表示形式(方法) __repr__, __str__ . 比如:

>>> class A(object):
...     def __init__(self, name):
...         self.name = name
...     def __str__(self):
...         return "<class A obj-> %s>" % self.name
...     def __repr__(self):
...         return "<class A obj-> %r>" % self.name

>>> a = A(name="neo1218")
>>> a
<class A obj-> 'neo1218'>
>>> a.__str__()
'<class A obj-> neo1218>'

可以看出对象的默认表示方法是__repr__, 相比于__str__, 好处在于你可以看出'neo1218'是个字符串.
"""

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
