class City(object):
    populations = 3000000
    def __init__(self, name, companies):
        self.name = name
        self.companies = companies
    
    @classmethod
    def get_populations(cls):
        return cls.populations
    
    
    @staticmethod
    def is_Megacity(companies):
        return companies >= 20
            
    
    def give_info(self):
        print(f"{self.name} has got {self.companies} big companies")
        
        
my_city = City("Tashkent", 200)
my_city.give_info()
print('--------------------\n')

print(City.get_populations())

print(City.is_Megacity(200))
