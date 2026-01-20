''''class Point3D:
  def __init__(self, x, y, z):
   self.x=x
   self.y=y
   self.z=z
  def copy(self):
   return Point3D(self.x, self.y, self.z)
  def __str__(self):
   return f"({self.x},{self.y}, {self.z})"
  def scale(self, n):
   self.x *= self.x
   self.y *= self.y
   self.z *= self.z



p1 = Point3D(1, 2, 3)
p2 = p1
p3 = p2.copy()
p1.scale(2)
p2.scale(2)
p3.scale(2)
print(p1, p2, p3)'''''



import copy
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def copy(self):
        return A(self.a,self.b)
    def __str__(self):
        return f"({self.a},{self.b})"
    def multiply(self,other):
        self.a=self.a* other
        self.b=self.b // other
s1 = A(21,31)
s2 = s1
s3 = s2.copy()
s4= copy.deepcopy(s3)
s1.multiply(2)
s2.multiply(2)
s3.multiply(2)
s4.multiply(2)
print(s1,s2,s3,s4)