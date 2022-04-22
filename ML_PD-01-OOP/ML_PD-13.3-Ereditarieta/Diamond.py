# Diamond.py


class A:  
    def __init__(self):
        pass
    def eseguiti(self):
        print("Sono A")
                
class B(A): 
    def __init__(self):
        pass
    # def eseguiti(self):
    #         print("Sono B")

class C(A):
    def __init__(self):
        pass
    # def eseguiti(self):
    #     print("Sono C")
        
class D(B,C):
    def __init__(self):
        pass
    # def eseguiti(self):
    #     print("Sono D")

def main():
   my_obj = A()
   my_obj.eseguiti()

   my_obj = B()
   my_obj.eseguiti()

   my_obj = C()
   my_obj.eseguiti()

   my_obj = D()
   my_obj.eseguiti()


    
if __name__ == '__main__':
    main()