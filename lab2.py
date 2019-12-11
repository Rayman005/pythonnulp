import html

def Wrapper (func):
    def wrapper (text):
        net_text = html.escape(text)
        return func(net_text)
    return wrapper


@Wrapper
def Textprocessing (text):
    print(text)

def main():
    Textprocessing("<div><h2><b>Hello world!</b></h1></div><br>")

if __name__ == "__main__":
    main()
