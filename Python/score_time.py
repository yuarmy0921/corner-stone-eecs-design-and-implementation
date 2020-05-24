import requests
import socketio
import sys


# ================================================================
# Scoreboard
#   add_UID(UID_str)
#     UID_str : UID string ("0x" excluded)
#   getCurrentScore()
#     return current score (int)
# ================================================================


class Scoreboard:
    def __init__(self, filepath, teamName, gameNum):
        # no need to read localfile

        self.totalScore = 0
        self.team = teamName
        self.game = int(gameNum)
        #change it!!!!!!!!!!!!!
        self.ip = 'http://ec2-18-204-36-51.compute-1.amazonaws.com'

        print("{} wants to play Game{}!".format(self.team, self.game))
        print("connecting to server......{}".format(self.ip))
        self.Socket = Socket(self.ip)

        try:
            g = requests.get(self.ip+'/game_status')
            playing_team = g.json()['current_team']
            if(playing_team != None):
                if(playing_team != teamName):
                    print('{} is current playing.\nPlease wait {} seconds for retry.'.format(
                        g.json()['current_team'], g.json()['time_remain']))
                    self.Socket.disconnect()
                    sys.exit(1)
            else:
                print("Game is starting.....")
                self.Socket.start_game(
                    {'gamemode': self.game, 'team': self.team})

        except:
            print("Failed to get game status or someone else is playing")
            print("Exiting the game.....")

            sys.exit(1)

    def add_UID(self, UID_str):
        self.Socket.add_UID({'uid_str': UID_str})

    def getCurrentScore(self):
        try:
            r = requests.get(self.ip+"/current_score")
            return r.json()['current_score']
        except:
            print("Failed to fetch current score")
            return None
        # return int(self.totalScore)

# ================================================================
# Socket interface
#   mySocket = Socket(ip)
# ================================================================


class Socket(socketio.ClientNamespace):
    sio = socketio.Client()

    def __init__(self, ip):
        #***********************#
        # pass in the namespace '/'
        # https://python-socketio.readthedocs.io/en/latest/client.html#class-based-namespaces
        #***********************#
        super().__init__('/')
        self.ip = ip
        try:
            self.sio.connect(self.ip)
        except:
            print('Failed to connect to server')
            sys.exit(1)
        self.sio.register_namespace(self)

    def on_connect(self):
        print("connected")
    
    def on_invalid_mode(self):
        print("Error:invalid gamemode!!")

    def on_game_end(self, data=None):
        print("game_end")
        self.disconnect()

    def on_game_started(self, data):
        print("Game started!")
        print("Playing game as\nTeam: {}\nMode: {}".format(
            data['current_team'], data['gamemode']))
        print("Please checkout {} for more information.".format(self.ip))

    def on_UID_added(self, message):
        print(message)

    def start_game(self, gamenum):
        self.emit("start_game", gamenum)

    def add_UID(self, UID_str):
        self.emit("add_UID", UID_str)


if __name__ == '__main__':
    # you can create a Scoreboard object
    # you don't need to pass in the file path
    myScoreboard = Scoreboard(None, 'Gru', 0)

    # you can add uid by calling add_UID
    myScoreboard.add_UID("0087A9AB")
    # you can get the score by calling getCurrentScore
    print(myScoreboard.getCurrentScore())
    # everything is just like usual
    # except make sure you have internet access ;)