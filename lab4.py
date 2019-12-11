def Wraps (outside_function):
  def Wrapper (inside_function):
    inside_function.__name__ = outside_function.__name__
    inside_function.__doc__ = outside_function.__doc__
    return inside_function
  return Wrapper

def Wrapper (outside_function):
  @Wraps(outside_function)
  def wrapper (*args, **kwargs):
    outside_function(*args, **kwargs)
  return wrapper

@Wrapper
def Some_method (*args, **kwargs):
  """Documentation for method Lab4 in lab4"""
  pass

def main():
    print(Some_method.__name__)
    print(Some_method.__doc__)

if __name__ == "__main__":
    main()
