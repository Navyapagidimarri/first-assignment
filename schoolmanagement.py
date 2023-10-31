class sahithi:
    def admission(self):
        self.books={books:int(input("enter amount of books"))}
        # self.uniform=int(input("enter amount of uniforms"))
        # self.fee=int(input("enter amount of fee"))

class nursery:
    def admission(self):
        
        self.books={books:int(input("enter amount of books"))}
        print("Wlcome to Sahithi "/n)
        print("to admit children into our school ,Follow the instructions"/n)
        print("books amount is :" ,self.books)
class lkg:
    def admission(self):
        
        self.books={books:int(input("enter amount of books"))}
        print("Wlcome to Sahithi "/n)
        print("to admit children into our school ,Follow the instructions"/n)
        print("books amount is :" ,self.books)
c1=sahithi()
c2=nursery()
c3=lkg()
for i in[c1,c2,c3]:
    i.admission()