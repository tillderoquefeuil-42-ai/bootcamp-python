import time
import logging
from random import randint

def log(func):
    logging.basicConfig(filename='machine.log', level=logging.INFO, format='(tde-roqu)%(message)s')

    def inner1(*args, **kwargs):
        begin = time.time()
        returned_value = func(*args, **kwargs)
        end = time.time()

        logging.info("Running: {:16}[ exec-time = {:.3f} ms ]".format(func.__name__, end - begin))

        return returned_value  
    return inner1


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")



if __name__ == "__main__":
    
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    
    machine.make_coffee()
    machine.add_water(70)
