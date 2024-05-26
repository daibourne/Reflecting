class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = 'repaired'

class AnakinsPod(Podracer):
        def __init__(self, max_speed, condition, price):
            super.init(max_speed, condition, price)

        def boost(self):
            self.max_speed *= 2
        
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"