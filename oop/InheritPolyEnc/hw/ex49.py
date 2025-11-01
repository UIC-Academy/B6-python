class Player:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Player<{self.name}, {self.age}>"
    

class Team:
    def __init__(self, name: str, members: list[Player] = []):
        self.__name = name
        self.__members = members
        
    def add_player(self, id, name, age):
        new_player = Player(id=id, name=name, age=age)
        self.__members.append(new_player)
        return True

    def pop_player(self, id):
        for player in self.__members:
            if player.id == id:
                self.__members.remove(player)
                return True
        
        return False
    
    def __len__(self):
        return len(self.__members)
        
    def __str__(self):
        return f"Team<{self.__name}>"
    

team1 = Team("Chaqqonlar")
team1.add_player(id="P0123", name="Eshmat", age=19)
team1.add_player(id="P0124", name="Toshmat", age=18)
print(len(team1))