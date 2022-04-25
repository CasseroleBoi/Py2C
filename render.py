import ast
from cgi import print_environ

def Render(line):
    #if(type(line) == type(ast.Assign())):
    #    return Assign(line)
    #if(type(line) == type(ast.Constant())):
    #    return Constant(line)

    l = str(type(line))[8:-2]
    if(l[:4] == "ast."):
        #print("     ", l[4:])

        #possible vulnerability?
        try: return eval(l[4:]+"(line)")
        except NameError:
            raise NotImplementedError(f"Not yet implemented - keyword not recognized - <{l[4:]}>")
    raise NotImplementedError("this type is not recognized")
    
        



def Assign(arg: ast.Assign):
    if(len(arg.targets) == 1):
        return f"p2c_Variable {arg.targets[0].id} = {Render(arg.value)}"
    else:
        raise NotImplementedError("Not yet implemented - multiple assignments")


def Constant(arg: ast.Constant):
    return arg.value


OPERATIONS = {
    ast.Add: '+'
}
def BinOp(arg: ast.BinOp):
    try: return f"{Render(arg.left)} {OPERATIONS[type(arg.op)]} {Render(arg.right)}"
    except: raise NotImplementedError("Not yet implemented - unknown operation")

def Name(arg: ast.Name):
    if(type(arg.ctx) == ast.Load):
        return arg.id
    else:
        raise NotImplementedError("Not yet implemented - unknown usage of <Name>")