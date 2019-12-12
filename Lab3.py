def Html (tag):
    def Wrapper (function):
        def wrapper (text):
            return "<" + tag + ">" + function(text) + "</" + tag + ">"
        return wrapper
    return Wrapper


@Html("div")
@Html("h2")
@Html("b")
def Textprocessing (text):
    return text

def main():
    print(Textprocessing("Hello world!"))

if __name__ == "__main__":
    main()
