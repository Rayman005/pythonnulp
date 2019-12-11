import html

def Wrapper (func):
    def wrapper (text):
        a = html.escape(text)
        return func(a)
    return wrapper


@Wrapper
def Textprocessing (text):
    print(text)

def main():
    Textprocessing("<div><h2><b>Hello world!</b></h1></div><br>")

if __name__ == "__main__":
    main()
