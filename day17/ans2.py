# credits: Hyperneutrino
# https://github.com/hyperneutrino/advent-of-code/blob/main/2024/day17p2.py

import re

program = list(map(int, re.findall(r"\d+", open("day17\\input.txt").read())[3:]))

def find(target, ans):
    if target == []: return ans
    for t in range(8):
        a = ans << 3 | t
        b = 0
        c = 0
        output = None

        def combo(operand):
            if 0 <= operand <= 3: return operand
            if operand == 4: return a
            if operand == 5: return b
            if operand == 6: return c

        for pointer in range(0, len(program) - 2, 2):
            ins = program[pointer]
            operand = program[pointer + 1]
            if ins == 1:
                b = b ^ operand
            elif ins == 2:
                b = combo(operand) % 8
            elif ins == 4:
                b = b ^ c
            elif ins == 5:
                output = combo(operand) % 8
            elif ins == 6:
                b = a >> combo(operand)
            elif ins == 7:
                c = a >> combo(operand)
            if output == target[-1]:
                sub = find(target[:-1], a)
                if sub is None: continue
                return sub

print(find(program, 0))