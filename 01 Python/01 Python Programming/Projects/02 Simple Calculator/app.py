class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
            return num1 * num2

    def div(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Can't divided by zero"
        except Exception as e:
            return f"Error: {e}"

    def mod(self, num1, num2):
        return num1 % num2


try:
    num1 = int(input("Enter number : "))
    op = input("Select the operator [+, -, *, /, %] : ")
    num2 = int(input("Enter number : "))

    cal = Calculator()

    if op == "+":
        print(cal.add(num1, num2))
        
    elif op == "*":
        print(cal.mul(num1, num2))
        
    elif op == "/":
        print(cal.div(num1, num2))
        
    elif op == "%":
        print(cal.mod(num1, num2))
    else:
        print("Invalid operator")
    
except ValueError:
    print("Error : please enter valid numeric values.")
except Exception as e:
    print(f"Error {e}")