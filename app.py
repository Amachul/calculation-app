s = input("Enter expression to calculate")
if s.find("+")>0:
    a = int(s[:s.find("+")].strip())
    b = int(s[s.find("+")+1:].strip())
    print(f'Result is {a+b}')
elif s.find("-")>0:
    a = int(s[:s.find("-")].strip())
    b = int(s[s.find("-")+1:].strip())
    print(f'Result is {a-b}')
else:
    print("Unknown expression")