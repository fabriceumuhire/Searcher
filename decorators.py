def announce(f):
    def wrapper():
        print("Running a function...")
        f()
        print("Done")
    return wrapper

@announce
def hello():
    print("Hello World")

hello()