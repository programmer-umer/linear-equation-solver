
# Rules
# 1- Linear Equation only
# Only two spaces are allowed between any of factor !important
# General Form
# ax + b = c 
# ax - b = c 
# Examples
# x + 100 = 250
# x7898 + 4567 = 3456
# 2x + 99 = 100

equation = ''

def input_equation():
    global equation
    equation = input("Enter the linear equation: ")
    first_equality = equation.find("=")
    if  first_equality == -1:
        print("Enter a Valid Linear Equation")
        exit()
    second_equality = equation.find("=", first_equality+1, len(equation))
    if second_equality != -1:
        print("A linear equation contains only one equal sign!")
        exit()

def solve():

    x_cofficient = ''
    a = ''
    x = equation.find("x")
    if x == 0:
        if equation[x+1] == '+' or equation[x+1] == '-' or equation[x+2] == '+' or equation[x+2] == '-' :
            x_cofficient = 1
        else:

            flag1 = equation.find("+")
            flag2 = equation.find("-")
            flag3 = equation.find("=")

            if flag1 != -1:
                x_cofficient = equation[x+1:flag1]
            elif flag2 != -1:
                x_cofficient = equation[x+1:flag2]
            else:
                x_cofficient = equation[x+1:flag3]
                                
    else:
        x_cofficient = equation[:x]

    flag1 = equation.find("+")
    flag2 = equation.find("-")
    flag3 = equation.find("=")

    if flag1 != -1:
        a = equation[flag1+1:flag3]
    if flag2 != -1:
        a = equation[flag2+1:flag3]

    b = equation[flag3+1:len(equation)]

    if flag1 != -1:
        solution = (int(b) - int(a)) / int(x_cofficient)
    elif flag2 != -1:
        solution = (int(b) + int(a)) / int(x_cofficient)
    else:
        print("Sorry we cannot solve this equation!")
        exit()
    print(f"The solution to this equation is {solution}")
if __name__ == "__main__":
    input_equation()
    try:
        solve()
    except:
        print("Please Read the rules above! We have detected some problem")
