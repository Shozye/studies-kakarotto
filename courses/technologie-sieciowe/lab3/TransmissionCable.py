class Message:
    def __init__(self, text: str, origin=None, jam=False):
        self.text = text
        self.origin = origin
        self.jam = jam


class TransmissionCable:
    def __init__(self):
        self.nodes = []
        self.nodes_positions = dict()
        self.programs_positions = dict()
        self.sending = dict()
        self.cable_edges = list()
        self.connection_edges = list()
        self.messages = list()
        self.public_messages = dict()

    def connect(self, program):
        _id = str(len(self.nodes))
        program.connect(self, _id)
        self.nodes.append(_id)
        self.nodes_positions[_id] = ((len(self.nodes) - 1) * 100, 0)

        self.programs_positions[program.name] = ((len(self.nodes) - 1) * 100, 100)
        self.connection_edges.append((_id, program.name))

        if len(self.nodes) > 1:
            self.cable_edges.append((self.nodes[-1], self.nodes[-2]))

    def propagate(self):
        new_messages = list()
        print("sending", self.sending)
        print("msgs", self.messages)
        for node, message in self.messages:

            node_neighbours = list()
            for possible_edge in self.cable_edges:
                if node in possible_edge:
                    if node == possible_edge[0]:
                        node_neighbours.append(possible_edge[1])
                    else:
                        node_neighbours.append(possible_edge[0])
            if message.origin in node_neighbours:
                node_neighbours.remove(message.origin)

            for node_neighbour in node_neighbours:
                new_messages.append((node_neighbour, Message(message.text, origin=node, jam=message.jam)))

        new_sending = dict()
        for edge, text in self.sending.items():
            if text == "JAMJAMJAM":
                new_messages.append((edge[0], Message("", origin=None, jam=True)))
            else:
                new_messages.append((edge[0], Message(text[0], origin=None, jam=False)))
                text = text[1:]
                if text != "":
                    new_sending[edge] = text
        self.sending = new_sending

        self.messages = new_messages
        new_public_messages = dict()
        for node, message in new_messages:
            if new_public_messages.get(node) is None:
                new_public_messages[node] = Message(text=message.text, jam=message.jam)
            else:
                if message.jam:
                    new_public_messages[node].jam = True
                new_text = "".join([chr(ord(a) ^ ord(b)) for a, b in zip(new_public_messages[node].text, message.text)])
                new_public_messages[node].text = new_text
        self.public_messages = new_public_messages

    def finish(self):
        return len(self.messages) == 0 and len(list(self.sending.keys())) == 0



