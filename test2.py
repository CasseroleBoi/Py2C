import ast
import FILE
from render import Render


source = "src3.py"
code = FILE.read(source)
print(ast.dump(code))

print()
x = code.body[0].targets[0].id

print(x, type(x))

print()
exec(compile(code, filename="", mode="exec"))



for line in code.body:
    #print(str(type(line)).ljust(25), ast.dump(line))

    print(Render(line), end=";\n")
    #print("===")
    