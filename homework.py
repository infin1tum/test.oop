class Animals:
    def __init__(self, name, age, weight, habitat, diet):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be of type string")  
        if isinstance(age, int):
            self.age  = age
        else:
            raise ValueError("Age must be of type int")       
        if  isinstance(weight, float):
            self.weight = weight
        else:
            raise ValueError("Weight must be of type float")
        if isinstance(habitat, str):
            self.habitat = habitat
        else:
            raise ValueError("Habitat must be of type str")
        if isinstance(diet, str):
            self.diet = diet
        else:
            raise ValueError("Diet must be of type str")
        
    def eat (self):
        return f"{self.name} is eating"
        
    def sleep (self):
        return f"{self.name} is sleeping"
        
    def make_sound (self):
        return f"{self.name} is making sound"
        
    def move (self):
        return f"{self.name} is moving"
        

    def __str__(self):
        return (f'name - {self.name}\n'
                f'age - {self.age}\n'
                f'weight - {self.weight}\n'
                f'habitat - {self.habitat}\n'
                f'diet - {self.diet}\n')
    
animal_1 = Animals(name = "тигр", age = 3, weight = 90.0, habitat = "лес", diet="плотоядный")
animal_2 = Animals("ягуар", 5, 100.0, "джунгли", "плотоядный")
animal_3 = Animals('леопард', 7, 80.0, "лес", "плотоядный")

print(f'{animal_1}\n'
      f'---------\n'
      f'{animal_2}\n'
      f'---------\n'
      f'{animal_3}\n'
      )
print(animal_1.eat())
print(animal_2.sleep())
print(animal_3.move())
                
class Reptiles(Animals):
    def __init__(self, name, age, weight, habitat, diet, venomous, color, speed, life_span):
        super().__init__(name, age, weight, habitat, diet)
        if  isinstance(venomous, bool):
            self.venomous = venomous
        else:
            raise ValueError("venomous must be of type bool")
        if  isinstance(color, str):
            self.color = color
        else:
            raise ValueError("color must be of type str")
        if  isinstance(speed, float):
            self.speed = speed
        else:
            raise ValueError("speed must be of type float")
        if  isinstance(life_span, int):
            self.life_span = life_span
        else:
            raise ValueError("life_span must be of type int")
        
    def crawl (self):
        return f"{self.name} is crawling"
        
    def shed_skin (self):
        return f"{self.name} is sheeds slin"
        
    def bask_in_sun (self):
        return f"{self.name} is basling in sun"
        
    def lay_eggs (self):
        return f"{self.name} is laing eggs"
        
    def __str__(self):
        return super().__str__()+(f'\nvenomous {self.venomous}\n'                         
                                  f'color - {self.color}\n'                                                         
                                  f'speed - {self.speed}\n'
                                  f'life_span - {self.life_span}\n')
snake = Reptiles(name = "змея", age = 3, weight = 90.0, habitat = "лес", diet = "плотоядный", venomous=True, color="yellow", speed=2.0, life_span=20 )
lizard = Reptiles("ящерица", 3, 1.0, "пустыня", "всеядный", False, "green", 10.0, 5)
turtle = Reptiles('черепаха', 300, 100.0, "лес", "всеядный", False, "green", 1.0, 300)

print(f'{snake}\n'
      f'---------\n'
      f'{lizard}\n'
      f'---------\n'
      f'{turtle}\n'
      )
print(snake.shed_skin())
print(lizard.bask_in_sun())
print(turtle.lay_eggs())
        

class Mammals(Animals):
    def __init__(self, name, age, weight, habitat, diet, strength, pride_size):
        super().__init__(name, age, weight, habitat, diet)
        if  isinstance(strength, int):
            self.strength = strength
        else:
            raise ValueError("strength must be of type float")
        if  isinstance(pride_size, int):
            self.pride_size = pride_size
        else:
            raise ValueError("pride_size must be of type int")
               
    def run (self):
        return f"{self.name} is running"
        
    def hunt (self):
        return f"{self.name} is hunting"
        
    def nurture_young (self):
        return f"{self.name} is nurturing young"
        
    def communicate (self):
        return f"{self.name} is communicating"
  
    def __str__(self):
        return super().__str__()+(f'\nstrength {self.strength}\n'                         
                                  f'pride_size - {self.pride_size}\n')
lion = Mammals(name = "лев", age = 4, weight = 130.0, habitat = "саванна", diet = "плотоядный", strength=50, pride_size=20 )
elephant = Mammals("слон", 60, 3000.0, "саванна", "травоядный", 200, 50,)
kangaroo = Mammals('кенгуру', 12, 60.0, "равнины", "травоядный",  80, 10)

print(f'{lion}\n'
      f'---------\n'
      f'{elephant}\n'
      f'---------\n'
      f'{kangaroo}\n'
      )
print(lion.hunt())
print(elephant.communicate())
print(kangaroo.run())


class ZooShow:
    def __init__(self, show_name, ticket_price, animal_performer):
        if isinstance(show_name, str):
            self.show_name = show_name
        else:
            raise ValueError("Show_name must be of type str")
        if isinstance(ticket_price, int):
            self.ticket_price = ticket_price
        else:
            raise ValueError("ticket_price must be of type int")
        if isinstance(animal_performer, str):
            self.animal_performer = animal_performer
        else:
            raise ValueError("animal_performer must be of type str")

    def animal_performer(self, animal_performer):
        return f"{animal_performer} is performing"

    def ticket_price(self, ticket_price):
        return f"{ticket_price} Money to show "

    def __str__(self):
        return (f'show_name {self.show_name}\n'
                f'ticket_price - {self.ticket_price}\n'
                f'animal_performer - {self.animal_performer}\n')


show = ZooShow(show_name="Zoo_show", ticket_price=100, animal_performer="lion")
show_2 = ZooShow("Zoo_show2", 100, "elephant")
show_3 = ZooShow('Zoo_show3', 100, "kangaroo")

print(f'{show}\n'
      f'---------\n'
      f'{show_2}\n'
      f'---------\n'
      f'{show_3}\n')
print(show.animal_performer())