def Wraps (fun):
  def Wrapper (fn):
    fn.__name__ = fun.__name__
    fn.__doc__ = fun.__doc__
    return fn
  return Wrapper

def Wrapper (fun):
  @Wraps(fun)
  def wrapper (a):
    fun(a)
  return wrapper

@Wrapper
def Lab4 (a):
  """Documentation for method Lab4 in lab4"""
  pass

def main():
    print(Lab4.__name__)
    print(Lab4.__doc__)

if __name__ == "__main__":
    main()