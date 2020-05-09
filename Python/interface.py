import BT
import maze
import score

# hint: You may design additional functions to execute the input command, which will be helpful when debugging :)
#應該是好了(?
#幾個基本的function：讀取RFID、傳送指令、結束
class interface:
    def __init__(self):
        print("")
        print("Arduino Bluetooth Connect Program.")
        print("")
        self.ser = BT.bluetooth()      #創建出的bluetooth
        port = input("PC bluetooth port name: ")
        while(not self.ser.do_connect(port)):
            if(port == "quit"):
                self.ser.disconnect()
                quit()
            port = input("PC bluetooth port name: ")
        input("Press enter to start.")
        self.ser.SerialWrite('s')
        
    def tell_you(self, string):
        print(string)

    def get_UID(self):
        return self.ser.SerialReadByte()

    def send_action(self,dirc):
        # TODO : send the action to car
        self.ser.SerialWrite(dirc)
        return self.ser.SerialReadString()   #確認有接收到指令

    def end_process(self):
        self.ser.SerialWrite('e')
        self.ser.disconnect()