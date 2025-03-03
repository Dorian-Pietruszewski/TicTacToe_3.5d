


class Pionek:

    def __init__(self, team: str, power: int):
        self.team = team
        self.power = power

    def __repr__(self) -> str:
        return self.team+str(self.power)
    def __lt__(self, other) -> bool:
        return self.power<other.power
    def __le__(self, other) -> bool:
        return self.power<=other.power
    def __gt__(self, other) -> bool:
        return self.power>other.power
    def __ge__(self, other) -> bool:
        return self.power>=other.power
    
class Plansza:
    
    def __init__(self):
        self.area = [[[] for _ in range(3)] for _ in range(3)]
    
    def place(self, x: int, y: int, P: Pionek) -> bool:
        if not self.area[y][x] or self.area[y][x][-1].power < P.power:
            self.area[y][x].append(P)
            return True
        return False
    def move(self, x: int, y: int, x2: int, y2: int) -> bool:
        if self.area[y][x] and (not self.area[y2][x2] or self.area[y][x][-1] > self.area[y2][x2][-1]):
            P: Pionek = self.area[y][x].pop()
            self.place(x2,y2,P)
            return True
        return False
    def __repr__(self):
        s = map(lambda x: str(x).replace(" ", "\t"), [row for row in self.area])
        return "\n".join(s)

ASD = Plansza()

print(ASD.place(0,0,Pionek("B",2)))
print(ASD.place(0,0,Pionek("R",3)))
print(ASD.move(0,0,1,1))
print(ASD)