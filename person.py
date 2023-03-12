
class Person:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def full_name(self: str) -> list:
        print(self.last_name, end=" ")
        return self.first_name 
    
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


if __name__ == '__main__':
    p1 = Person('Jimi', 'Hendrix', 55)
    print(p1.first_name, p1.last_name)
    print(p1.full_name()) # выводит Hendrix Jimi
    print(p1.is_adult())  # выводит True

  
    

    
  
    
    
    
