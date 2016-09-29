#More Variables and Printing

* A **string** is how you make something that your program might give to a human. 

* string have **variables embedded in** them. You embeded by **using specialized format sequences** and then **putting the variables at the end with a special syntax**.

* `'Hi, %s, you have $%d.' % ('Michael', 1000000)`

* `%`运算符就是用来格式化字符的。
* 在字符串内部，有几个`%?`占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个`%?`，**括号**可以省略。
* 常见的占位符有：
`%d` 整数，
`%f` 浮点数， 
`%s` 字符串，
`%x` 十六进制整数，
`%r`print this no matter what

* variable need to **start with a character**, so `a1` would work, but `1` will not.

* **use the round()** function like this: round(1.7333).

* `TypeError: 'str' object is not callable.`
You probably forgot the % between the string and the list of variables.

*mark:
Try to write some variables that *convert the inches and pounds to centimeters and kilograms*. Do not just type in the measurements. Work out the math in Python.*
填了Ex4的坑:D
