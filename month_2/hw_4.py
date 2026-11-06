class Football:
    def __init__(self, name, age, position, assists, goals, club):
        self.name = name
        self.age = age
        self.position = position
        self.assists = assists
        self.goals = goals
        self.club = club
    def __add__(self, other):
        return self.goals + other.goals
        return self.assists + other.assists

class Striker(Football):
    def __init__(self, name, age, position, assists, goals, club):
        super().__init__(name, age, position, assists, goals, club)

    def __str__(self):
        return f"{self.name}, {self.age} years old, plays as {self.position} for {self.club}. Goals: {self.goals}, Assists: {self.assists}"
        if 0 < self.goals <= 150:
            return f"{self.name} новичок с {self.goals} голами!"
        elif 150 < self.goals <= 300:
            return f"{self.name} профессионал с {self.goals} голами!"
        else:
            return f"{self.name} легенда с {self.goals} голами!"

class Midfielder(Football):
    def __init__(self, name, age, position, assists, goals, club):
        super().__init__(name, age, position, assists, goals, club)

    def __str__(self):
        return f"{self.name}, {self.age} years old, plays as {self.position} for {self.club}. Goals: {self.goals}, Assists: {self.assists}"
        if 0 < self.assists <= 100:
            return f"{self.name} новичок с {self.assists} голевыми передачами!"
        elif 100 < self.assists <= 200:
            return f"{self.name} профессионал с {self.assists} голевыми передачами!"
        else:
            return f"{self.name} легенда с {self.assists} голевыми передачами!"

class Defender(Football):
    def __init__(self, name, age, position, assists, goals, club):
        super().__init__(name, age, position, assists, goals, club)

    def __str__(self):
        return f"{self.name}, {self.age} years old, plays as {self.position} for {self.club}. Goals: {self.goals}, Assists: {self.assists}"
        if 0 < self.goals <= 50:
            return f"{self.name} новичок с {self.goals} голами!"
        elif 50 < self.goals <= 100:
            return f"{self.name} профессионал с {self.goals} голами!"
        else:
            return f"{self.name} легенда с {self.goals} голами!"

team1_player1 = Striker("Lionel Messi", 36, "Striker", 20, 700, "Paris Saint-Germain")
team1_player2 = Midfielder("Kevin De Bruyne", 30, "Midfielder", 100, 150, "Manchester City")
team1_player3 = Defender("Virgil van Dijk", 32, "Defender", 10, 80, "Liverpool")

team2_player1 = Striker("Cristiano Ronaldo", 39, "Striker", 15, 800, "Manchester United")
team2_player2 = Midfielder("Luka Modric", 38, "Midfielder", 90, 120, "Real Madrid")
team2_player3 = Defender("Sergio Ramos", 37, "Defender", 5, 60, "Paris Saint-Germain")

if team1_player1.goals > team2_player1.goals:
    print(f"{team1_player1.name} лучший нападающий с {team1_player1.goals} голами!")
elif team2_player1.goals > team1_player1.goals:
    print(f"{team2_player1.name} лучший нападающий с {team2_player1.goals} голами!")
else:
    print("оба лучшие!")

if team1_player2.assists > team2_player2.assists:
    print(f"{team1_player2.name} лучший полузащитник с {team1_player2.assists} ассистами!")
elif team2_player2.assists > team1_player2.assists:
    print(f"{team2_player2.name} лучший полузащитник с {team2_player2.assists} ассистами!")
else:
    print("оба лучшие!")

if team1_player3.goals > team2_player3.goals:
    print(f"{team1_player3.name} лучший защитник с {team1_player3.goals} голами!")
elif team2_player3.goals > team1_player3.goals:
    print(f"{team2_player3.name} лучший защитник с {team2_player3.goals} голами!")
else:
    print("оба лучшие!")

total_str = team1_player1 + team2_player1
print(f"Общее количество голов двух нападающих: {total_str}")
total_mid = team1_player2 + team2_player2
print(f"Общее количество ассистов двух полузащитников: {total_mid}")
total_def = team1_player3 + team2_player3
print(f"Общее количество голов двух защитников: {total_def}")
