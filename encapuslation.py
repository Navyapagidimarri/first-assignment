#sample encapsulation
# class encap:
#     def __init__(self,name,domain,company):
#        self.name=name
#        self._domain=domain
#        self.__company=company
# class python(encap):
#     def py (self):
#         print(f"{self.name} working in {self._domain}  {self._encap__company}")
# obj=python("navya","python","marolix")
# obj.py()


class sample:
    def __init__(self,bill,deposit,expenditure):
        self._bill=bill
        self._depost=deposit
        self._expenditure=expenditure
    def super(self):
        

