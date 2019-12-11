def Html (tag):
    def Wrapper (fun):
        def wrapper (a):
            return "<" + tag + ">" + fun(a) + "</" + tag + ">"
        return wrapper
    return Wrapper


@Html("div")
@Html("h2")
@Html("b")
def Textprocessing (a):
    return a

def main():
    print(Textprocessing("Hello world!"))

if __name__ == "__main__":
    main()
