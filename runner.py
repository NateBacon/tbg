# Character creation to rival Bethesda



class CreatePlayer:

    player_name = ""
    player_hp = 0
    player_str = 0
    player_acc = 0
    player_att = 0
    player_spe = 0
    player_sta = 0
    player_cha = 0
    player_int = 0

    MAX_HEALTH = 50

    POINTS_CAP = 35
    points_spent = 0

    def prompt(self, message):
        print("Points left:" + str(self.POINTS_CAP - self.points_spent))
        ret = int(input("How " + message + " are you on a scale of 1-10?"))
        if(self.points_spent + ret > self.POINTS_CAP):
            print("We dont want you not having fun, do we?")
            ret = self.prompt(message)
        elif(ret < 0 or ret > 10):
            print("I can't quite see how that number fits the scale. Try again.")
            ret = self.prompt(message)
        else:
            self.points_spent += ret
            return ret
        return ret

    def create_player(self):
        self.player_name = input("What is your name, traveler?")
        self.player_str = self.prompt("strong")
        self.player_acc = self.prompt("accurate")
        self.player_att = self.prompt("attuned")
        self.player_spe = self.prompt("fast")
        self.player_sta = self.prompt("fit")
        self.player_cha = self.prompt("charismatic")
        self.player_int = self.prompt("intelligent")
        self.player_hp = self.MAX_HEALTH * ((self.player_str + self.player_sta)/20) # If a player has max strength and stamina, give them 50 hp
        self.write_player()
        return

    def write_player(self):
        with open("player.dat", "w+") as f:
            f.write("hp " + str(self.player_hp) + "\n")
            f.write("str " + str(self.player_str) + "\n")
            f.write("acc " + str(self.player_acc) + "\n")
            f.write("att " + str(self.player_att) + "\n")
            f.write("spe " + str(self.player_spe) + "\n")
            f.write("sta " + str(self.player_sta) + "\n")
            f.write("cha " + str(self.player_cha) + "\n")
            f.write("int " + str(self.player_int) + "\n")
            f.close()
        return

    def __init__(self):
        self.create_player()
        return

if __name__ == '__main__':
    x = CreatePlayer()
