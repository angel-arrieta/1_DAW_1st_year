import re
print("L={a^n b a, n>=0}")
result = re.match("a*ba$", input(">"))
if result:
    print("Correcto")
else:
    print("Incorrecto")
