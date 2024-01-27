from abc import ABC, abstractmethod

class IPrey(ABC):
    @abstractmethod
    def Flee(self):
        pass

class IPredator(ABC):
    @abstractmethod
    def Hunt(self):
        pass

class ForestAnimalCharacterHerbivorous(IPrey):
    def Flee(self):
        print("The forest animal runs away!")

class ForestAnimalCharacterCarnivorous(IPredator):
    def Hunt(self):
        print("The animal is searching for food!")

class SeaAnimalCharacter(IPrey, IPredator):
    def Flee(self):
        print("The sea animal swims away!")

    def Hunt(self):
        print("The sea animal is searching for smaller animals!")

if __name__ == "__main__":

    deer = ForestAnimalCharacterHerbivorous()
    tiger = ForestAnimalCharacterCarnivorous()
    orca = SeaAnimalCharacter()

    deer.Flee()
    tiger.Hunt()
    orca.Flee()
    orca.Hunt()
