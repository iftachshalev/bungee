from Maneger import Manager
r = 0
s = 0
for i in range(10):
    manager = Manager()
    manager.OUTPUT_TO_FILE = False
    e = manager.run()
    if e == 0:
        r += 1
    if e == 1:
        s += 1
print(e)


