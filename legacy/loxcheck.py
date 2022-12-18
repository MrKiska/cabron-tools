import time
import random
print  ('lox check')

print  ('gadaem na kofeinoi guschee...')
time.sleep(10)
n1 = random.randint(1,100)
if (n1 > 50):print("Vlad lox")
if (n1 < 50):print("Vlad ne lox")

n2 = random.randint(1,100)
if (n2 > 50):print("Valera lox")
if (n2 < 50):print("Valera ne lox")

n3 = random.randint(1,100)
if (n3 > 50):print("Vita lox")
if (n3 < 50):print("Vita ne lox")

n4 = random.randint(1,100)
if (n4 > 50):print("Gena lox")
if (n4 < 50):print("Gena ne lox")
print(n1, n2, n3, n4)