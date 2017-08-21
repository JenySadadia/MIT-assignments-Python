class Address:
    def __init__(self, street, num):
        self.street_name = street
        self.number = num

class CampusAddress(Address):
    def __init__(self,office_num):
        office = office_num.split('-')
        new_offfice = office[0]+office[1][0]+'-'+office[1][1:]
        self.office_num = office_num
        self.street_name = '\'Massachusetts Ave\''
        self.number = 77
        Address.__init__(self,self.street_name,self.number)


sa = CampusAddress('32-G904')
print(sa.office_num)
print(sa.street_name)
print(sa.number)

