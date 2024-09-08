class GrandFather:
      gfbike="Jawa"
      def gf_display(self):
          print("Grand father bike",self.gfbike)

class Father(GrandFather):
      fbike="Yezdi"
      def f_display(self):
          print("Father bike",self.fbike)

class Son(Father):
      sbike="Honda"
      def s_display(self):
          print("Sons bike",self.sbike)
          print("GF bike inherted var",self.gfbike)
          print("F bike inherted var", self.fbike)
          print("GF bike inherted function", self.gf_display())
          print("F bike inherted  function", self.f_display())

s=Son()
s.s_display()
s.gf_display()
