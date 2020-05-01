import pandas
import numpy as np 

# ================================================================
# Scoreboard
#   add_UID(UID_str)
#     UID_str : UID string ("0x" excluded)
#   getCurrentScore()
#     return current score (int)
# ================================================================

class Scoreboard:
    def __init__(self, filepath, teamName, gameNum):
        raw_data = np.array(pandas.read_csv(filepath))#.values

        self.totalScore = 0
        self.team = teamName
        self.game = int(gameNum)

        print ("{} is playing Game{}!".format(self.team, self.game))

        self.cardList = [int(a, 16) for a in raw_data.T[0]]

        if self.game == 0:
            # data member specific for Game1: self.cardValue, self.visitList
            self.visitList = list()
            self.cardValue = dict()
            for i in range(len(raw_data)):
                self.cardValue[self.cardList[i]] = raw_data[i][1]
            print ("Successfully read the UID file!")

        elif self.game == 1:
            # data member specific for Game2: self.sequence, self.sequence_idx
            print ("Successfully read the UID file!")
            print("CardList:", list(map(hex, self.cardList)))
            sequence_str = input("Enter your sequence (by index, split by spacebars): ")
            self.sequence = list(map(int, sequence_str.split(' ')))
            self.sequence_idx = 0

    def add_UID(self, UID_str):
        UID = int(UID_str,16)

        if UID not in self.cardList:
            print("This UID doesn't exist in the UID list file:", hex(UID))
        else:
            if self.game == 0:
                if UID in self.visitList:
                    print("This UID is already visited:", hex(UID))
                else:
                    point = self.cardValue[UID]
                    self.totalScore += point
                    print("A treasure is found! You got " + str(point) + " points.")
                    print("Current score: "+ str(self.totalScore))
                    print("")
                    self.visitList.append(UID)

            elif self.game == 1:
                if self.sequence_idx >= len(self.sequence):
                    print("A treasure is found! But you finish the sequence already.")
                elif UID == self.cardList[self.sequence[self.sequence_idx]]:
                    self.totalScore += 100
                    print("A treasure is found! You got 100 points.")
                    print("Current score: "+ str(self.totalScore))
                    self.sequence_idx += 1
                    if self.sequence_idx == len(self.sequence):
                        print("Congratulation! You have visited the sequence correctly!")
                    print("")
                else:
                    print("Wrong order!! You should go to card {} first!".format(self.sequence[self.sequence_idx]))
                    print("")


    def getCurrentScore(self):
        return int(self.totalScore)