import re

nums = list(map(int, re.findall(r"\d+", open("day17\\input.txt").read())))
a, b, c, program = nums[0], nums[1], nums[2], nums[3:]

output = []

def combo_op(n):
    if n<4:
        return n
    if n==4:
        return a
    if n==5:
        return b
    if n==6:
        return c

idx = 0
while True:
    if idx >= len(program):
        break
    opcode = program[idx]
    operand = program[idx+1]
    if opcode==0:
        a = a >> combo_op(operand)
        idx += 2
    elif opcode==1:
        b = b ^ operand
        idx += 2
    elif opcode==2:
        b = combo_op(operand) % 8
        idx += 2
    elif opcode==3:
        if a==0:
            idx += 2
        else:
            if idx != operand:
                idx = operand
            else:
                idx += 2
    elif opcode==4:
        b = b ^ c
        idx += 2
    elif opcode==5:
        res = combo_op(operand) % 8
        output.append(res)
        idx += 2
    elif opcode==6:
        b = a >> combo_op(operand)
        idx += 2
    elif opcode==7:
        c = a >> combo_op(operand)
        idx += 2

res = ','.join([str(x) for x in output])
print(res)