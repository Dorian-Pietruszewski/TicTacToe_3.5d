


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
    def check(self) -> str|None:
        if self.area[0][0] and self.area[1][1] and self.area[2][2] and self.area[0][0][-1].team == self.area[1][1][-1].team == self.area[2][2][-1].team:
            return self.area[1][1][-1].team
        if self.area[0][2] and self.area[1][1] and self.area[2][0] and self.area[0][2][-1].team == self.area[1][1][-1].team == self.area[2][0][-1].team:
            return self.area[1][1][-1].team
        
        for row in range(1,3):
            for col in range(3):
                if not self.area[row][0] or not self.area[row][col] or self.area[row][0][-1].team != self.area[row][col][-1].team:
                    break
            else:
                return self.area[row][col][-1].team
        
        for col in range(1,3):
            for row in range(3):
                if not self.area[0][col] or not self.area[row][col] or self.area[0][col][-1].team != self.area[row][col][-1].team:
                    break
            else:
                return self.area[row][col][-1].team
        

        return None



if __name__ == "__main__":
    A = Plansza()

    print(A.place(1,0,Pionek("B", 1)))
    print(A.place(1,1,Pionek("B", 3)))
    print(A.place(1,2,Pionek("B", 2)))

    print(A)

    print(A.check())