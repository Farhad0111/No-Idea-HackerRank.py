class Farhad1:
    def __init__(self,m,a,A,B):
        self.m=m
        self.a=a
        self.A=A
        self.B=B
class Farhad2(Farhad1):
    def Faru(self):
        print(sum(((i in self.A)-(i in self.B) for i in self.a)))
farhad=Farhad2(m=input().split(),a=input().split(),A=input().split(),B=input().split())
farhad.Faru()