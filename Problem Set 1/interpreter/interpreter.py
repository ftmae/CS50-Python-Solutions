expression = input("Expression:")
x, y, z = expression.split(" ")
nex=float(x)
nez=float(z)
match y:
    case '+':
        result=nex+nez
    case '-':
        result=nex-nez
    case '/':
        if nez==0:
            print("Division by 0 is not allowed.")
        else:
            result=nex/nez
    case '*':
        result=nex*nez
    case _:
        print("Unrecognisable operator.")

print(result)
