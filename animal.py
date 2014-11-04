class Animal():
    "Class for animal objects"
    
    def __init__(self, name):
        
        self.name = name
        self.clues = []
        
    def add_clue(self, clue):
        
        self.clues.append(clue)
        
    def guess_who_am_i(self):
        print("I will give you " + str(len(self.clues)) + " hints, guess what animal I am \n")
        for i in range(len(self.clues)): 
            
            print(self.clues[i])
            answer = input("Who am I? ").strip()
            
            if answer.lower() == self.name.lower():
                
                print("You got it! I am " + self.name + "\n")
                break
            else:
                
                print("Nope, try again! \n")
                
                if i == (len(self.clues) - 1):
                    
                    
                    print("I'm out of hints! The answer is: " + self.name + "\n")
            

if __name__ == "__main__":
    
    
    
    e = Animal("elephant")
    t = Animal("tiger")
    b = Animal("bat")
    
    
    e.add_clue("I have exceptional memory")
    e.add_clue("I am the largest land-living mammal in the world")
    e.add_clue("I have tusks")
    
    t.add_clue("I am the biggest cat")
    t.add_clue("I come in black and white or orange and black")
    t.add_clue("I live in the wild but you can also find me in zoos")
    
    b.add_clue("I use echo-location")
    b.add_clue("I can fly")
    b.add_clue("I see well in dark")
    
    
    e.guess_who_am_i()
    t.guess_who_am_i()
    b.guess_who_am_i()
