#single inheritance
# class properties:
#     def m1(self):
#         self.name="pagidimarri"
        
# class name(properties):
#       def m2(self):
#         self.myname="navya"
#         print(self.name+self.myname)
# c=name()
# c.m1()
# c.m2()



#hirarchical inheritance
# class Samsung:
#     brand = "Samsung"
#     print("we love sumsung brand ,we have so many sumsung items with us.let's see my collection")
#     def __init__(self, battery, price):
#         self.price = price
#         self.battery = battery

# class FlipPhone(Samsung):
#     def flip(self):
#         self.model = "Galaxy S23"
#         print("Flip phone features are", "price " ,self.price ,"battery" ,self.battery , "brand name", self.brand ,self.model)

# class smartTv(Samsung):
#     def Tv(self):
#         self.display="50 inches"
#         print("smart tv features are", "price " ,self.price ,"battery" ,self.battery , "brand name", self.brand ,self.display)
# c = FlipPhone(58000,"1000mh",)
# c.flip()
# c1=smartTv(80000,"5000mh")
# c1.Tv()

#multilevel programming for principal to teachers range
# class principal:
#       def orderto_teachers(self):
#             print("PRINCIPAL SAYS :Every teacher must ready reports cards :")
# class clsteacher(principal):
#       def classteacher(self):
#             print("CLASS TEACHER SAYS:every teacher please provide all subject marks for making report card:")
# class otherteacher(clsteacher):
#       def responce(self):
#             print("OTHERTEACHERS RESPONDING:we are ready with marcks  ")
# o1=otherteacher()
# o1.orderto_teachers()
# o1.classteacher()
# o1.responce()

#multiple Programming for principal techer to the parents
class principal:
      fee=50000
      def order_to_parents(self):
            print("PRINICIPALL TO PARENT :please clear school fee immediatly")
class teacher:
      def req_to_parents(self):
            print("TEACHER TO PARENTS :please check homework dairy  everyday")
class parent(principal,teacher):
      def reaction(self):
         print("RESPONCE TO PRINICIPAL ,TEACHER:we will clear fee and i will follow dairy daily ")
o1=parent()
o1.order_to_parents()
o1.req_to_parents()
o1.reaction()


#hybrid inheritance
# class PM:
#       def priminister(self):
#             print("he is the ruler of india - he can give policies for all over india when we have elections")
#             print("we will get 2000 rs per acra scheeme")
#       def leaderoffer(self):
#             print("we will give one lakh per 1000 votes to congress")
# class CM:
#       def chiefminister(self):
#             print("we will provide 5000 per acra")
#       def localoffer(self):
#             print("we will give 50 k per 1000 votes")
# class surpanch_candidate(PM):#single inheritance
#       def mywish(self):
#             print("iam congress candidate ,i assure 1000 votes to u",self.leaderoffer())
#       def myshare(self):
#             print("you are my party member,so i will share 20k per u from my waata")
# class wardmember(surpanch_candidate):#multi level in heritance
#       def mygoal(self):
#             print("what about my commsion sir i want 20k share")
      
# class common(PM,CM):#multiple inheritance
#       def commonpeople(self):
#             print("we will get central and state polocy cause i have an acra land")
#             print(self.priminister())
#             print(self.chiefminister())
# #o1=common()
# #o1.commonpeople()
# o3=wardmember()
# o3.mygoal()
# o3.myshare()