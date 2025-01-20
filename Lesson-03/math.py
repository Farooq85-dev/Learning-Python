import math
import random

print(math.floor(3.5)) # 3

print(math.floor(-3.5)) # -4

print(math.trunc(-3.5)) # -3

print(math.trunc(23.5)) # 23


# octal
print(0o20) # 16
# hexal
print(0x20) # 32
# binary
print(0b100) # 4

x = 1
print(1 << 2) # 4

arr = [1,2,3,4,5,6,7,9,]
arr = ["Farooq", "Ahmed", "Arslan"]
print(random.randint(1 , 100))
print(random.randint(1 , 100))
print(random.choice(arr))
random.shuffle(arr)

print(arr)

nums = {1,2,3}

# union means:common values
print(nums & {1,2})

# intersection means:unique values from sets
print(nums | {1,2,4,5,6,7})

# difference
print(nums - {1,2,3}) # set()

print(type(nums)) # set


print(type(True)) # bool
print(True == 1) # True