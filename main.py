def input_equation():
    equation = input("Enter the linear equation: ")
    first_equality = equation.find("=")
    if  first_equality == -1:
        print("Enter a Valid Linear Equation")
        exit()
    second_equality = equation.find("=", first_equality+1, len(equation))
    if second_equality != -1:
        print("A linear equation contains only one equal sign!")
        exit()

if __name__ == "__main__":
    input_equation()