from TransmissionCable import TransmissionCable
import random

class Program:
    cable: TransmissionCable

    def __init__(self, name: str, string_to_send: str):
        self.detected_collision = False
        self.node_id = None
        self.name = name
        self.string_to_send = string_to_send
        self.is_sending = False
        self.is_waiting_to_see_if_not_jam_incoming = False
        self.is_sending_jam_signal = False
        self.finish = False
        self.jam_signal_flag = False
        self.how_long_sending = 0
        self.iterations_to_send = 0

    def connect(self, cable: TransmissionCable, node_id: str):
        self.node_id = node_id
        self.cable = cable

    def check_what_is_on_transmission_cable(self):
        if not self.is_sending:
            self.iterations_to_send -= 1

        msg = self.cable.public_messages.get(self.node_id)
        if msg is None:
            if self.how_long_sending >= len(self.string_to_send):
                self.finish=True
            return

        if self.is_sending and self.jam_signal_flag:
            self.reset()
        if msg.jam:
            self.reset()
            self.jam_signal_flag = True
        else:
            if self.is_sending or self.is_waiting_to_see_if_not_jam_incoming:
                if msg.text != self.string_to_send[self.how_long_sending]:
                    self.detected_collision = True
        if self.is_sending:
            self.how_long_sending += 1
        print(self.how_long_sending, len(self.string_to_send))

    def reset(self):
        if self.cable.sending.get((self.node_id, self.name)):
            del self.cable.sending[(self.node_id, self.name)]
        self.how_long_sending = 0
        self.detected_collision = False
        self.iterations_to_send = random.randint(1, 2**len(self.cable.nodes))

    def send(self, text:str):
        if text == "":
            return
        self.cable.sending[(self.node_id, self.name)] = text
        self.how_long_sending = 0
        self.is_sending = True

    def send_jam_signal(self):
        self.jam_signal_flag = True
        self.send("JAMJAMJAM")




