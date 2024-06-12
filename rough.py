# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

class A:
    def f1(self):
        print("class A")
class B:
    def f1(self):
        print("class B")

class C(B,A):
    def fun(self):
        print("helo")
c=C()
C.mro()
print(C.mro())