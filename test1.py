import parser

a = parser.expr("print(\"hello world\")")
b = parser.st2tuple(a)
print(b)