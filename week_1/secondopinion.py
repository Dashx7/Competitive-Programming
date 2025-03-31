
# Online Python - IDE, Editor, Compiler, Interpreter

input_num = int(input())
minutes = input_num//60
input_num-=minutes*60
hours = minutes//60
minutes-=hours*60

# print(hours,minutes,input_num)
print(f"{hours} : {minutes} : {input_num}")

