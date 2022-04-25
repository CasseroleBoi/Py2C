import FILE


FILES = [
    "test1.py",
    "test2.py"
]


for file in FILES:
    prd = FILE.read(file)
    print(prd)