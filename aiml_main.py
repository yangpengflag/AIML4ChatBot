import aiml
import re

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

while True:
    a = kernel.respond(input("input>>"))
    print(a)

    reg2 = "13[0-9]\d{8}|14[5,7]\d{8}|15[0-3,5-9]\d{8}|17[0-3,5-8]\d{8}|18[0-9]\d{8}|166\d{8}|19[8-9]\d{8}"
    numbers = re.findall(reg2,a)
    #print(numbers)

