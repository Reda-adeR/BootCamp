class Phone:
    def __init__(self,phNum):
        self.phNum = phNum
        self.call_history = []
        self.msgs = []

    def call(self, call_obj):
        if not isinstance(call_obj, Phone):
            print("Phone Object is not valid to call")
            return
        if call_obj.phNum == self.phNum:
            print("You cannot call yourself")
            return
        str = f"the Number {call_obj.phNum} is calling {self.phNum}"
        self.call_history.append(str)
        print(str)

    def show_call_history(self):
        if not self.call_history:
            print("No call history")
            return
        print("call history : \n", "\n".join(self.call_history))

    def send_message(self, recv_obj, msg):
        if not isinstance(recv_obj, Phone):
            print("Phone Object is not valid to send msg")
            return
        dict = {
            "to" : recv_obj.phNum,
            "from" : self.phNum,
            "content" : msg
        }
        self.msgs.append(dict)
        print("You sent a msg to : ", recv_obj.phNum)