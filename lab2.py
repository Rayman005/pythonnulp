import html

def Wrapper (func):
    def wrapper (text):
        a = html.escape(text)
        func(a)
    return wrapper


@Wrapper
def Restructure (text):
    print(text)

def main():
    Restructure("<div><h2><b>Hello world!</b></h1></div><br>")

if __name__ == "__main__":
    main()
