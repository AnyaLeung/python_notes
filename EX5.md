#More Variables and Printing

* A **string** is how you make something that your program might give to a human. 

* You embeded **variables** in **string** by **using specialized format sequences**

* `'Hi, %s, you have $%d.' % ('Michael', 1000000)`

* `%` 格式化字符
* 在字符串**内部**，有几个`%?`占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个`%?`，**括号**可以省略。
* 常见的占位符有：
`%d` 整数 </br>
`%f` 浮点数 </br>
`%s` 字符串 </br>
`%x` 十六进制整数 </br>
`%r`print this no matter what

* variable need to **start with a character**, so `a1` would work, but `1` will not.

* **use the round()** function like this: round(1.7333).

* `TypeError: 'str' object is not callable.`</br>
may forgot the `%` between the string and the list of variables.

*mark*:

* *Try to write some variables that convert the inches and pounds to centimeters and kilograms. Work out the math in Python*.
