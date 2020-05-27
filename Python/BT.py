from time import sleep
import serial
import connect
import threading
# these codes are for bluetooth
# hint: please check the function "sleep". how does it work?

#執行的任務：連接電腦端口
class bluetooth:
    def __init__(self, port: str, baudrate: int=9600):
        self.ser = serial.Serial(port, baudrate = baudrate)

    def is_open(self) -> bool:
        return self.ser.is_open

    def waiting(self) -> bool:
        return self.ser.in_waiting

    def do_connect(self, port):
        #把上一次連到的port關掉
        self.ser.close()
        print("Connecting...")
        try:
            self.ser = serial.Serial(port,9600,timeout=2)
            print("connect success")
            print("")
        except serial.serialutil.SerialException:
            print("fail to connect")
            print("")
            return False
        return True

    def disconnect(self):
        self.ser.close()

    def SerialWrite(self,output):      #接收指令的部分
        # send = 's'.encode("utf-8")
        #把接收到的字元指令解碼再寫進藍芽
        send = output.encode("utf-8")
        self.ser.write(send)

    def SerialReadString(self):
        # TODO: Get the information from Bluetooth. Notice that the return type should be transformed into hex.
        waiting = self.ser.in_waiting      #返回接收快取中的位元組數
        if waiting >= 0:
            rv = self.ser.read(waiting).decode("utf-8") #從串列中讀取位元組，再轉成英文字
            return rv
        return ""

    def SerialReadByte(self):
        sleep(0.05)
        waiting = self.ser.inWaiting()    #先判斷讀取到幾個位元組
        rv = self.ser.read(waiting)   #再把這一組讀出來
        
        if(rv):
            UID = hex(int.from_bytes(rv, byteorder='big', signed=False))   #從最高位照順序存下來
            self.ser.flushInput()    #清除快取
            return UID[-8:]
        return 0