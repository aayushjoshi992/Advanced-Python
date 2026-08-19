try:
    with(
        open('file1.txt') as f1,
        open('file2.txt') as f2,
        open('file3.txt') as f3,
    ):
        print("hello")
except FileNotFoundError:
    print("No file found")



