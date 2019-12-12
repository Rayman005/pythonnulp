class Shape:
  def area(self):
    pass

class Triangle(Shape):
  def __init__ (self, side_a, side_b, side_c):
    self.side_a = side_a
    self.side_b = side_b
    self.side_c = side_c
  def area (self):
    squre = (self.side_a+self.side_b+self.side_c)/2
    return (squre*(squre-self.side_a)*(squre-self.side_b)*(squre-self.side_c))**0.5

class Square(Shape):
  def __init__ (self, side):
    self.side = side
  def area (self):
    return self.side**2

class Circle(Shape):
  def __init__ (self, radious):
    self.radious = radious
  def area (self):
    return 3.14*self.radious**2

class View:
  def __init__ (self, shape:Shape):
    self.shape = shape
  def get_area (self):
    return self.shape.area()

if __name__ == "__main__":
  triangle = Triangle(2,3,4)
  square = Square(2)
  circle = Circle(3)

  view_t = View(triangle)
  view_s = View(square)
  view_t = View(circle)

  print("Triangle: " + str(view_t.get_area()))
  print("Square: " + str(view_s.get_area()))
  print("Circle: " + str(view_c.get_area()))
