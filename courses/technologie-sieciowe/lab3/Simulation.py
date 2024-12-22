import networkx as nx
from TransmissionCable import TransmissionCable
from Program import Program
from matplotlib import pyplot as plt
import time


class Simulation:
    def __init__(self):
        self.transmission_cable = TransmissionCable()
        self.programs = list()

    def add_program(self, name: str, string_to_send: str):
        program = Program(name, string_to_send)
        self.programs.append(program)
        self.transmission_cable.connect(program)

    def print(self):
        G = nx.Graph()
        nodelist = list()
        programs_colors = list()
        pos = self.transmission_cable.programs_positions
        pos.update(self.transmission_cable.nodes_positions)

        for program in self.programs:
            G.add_node(program.name)
            nodelist.append(program.name)
            if program.is_sending:
                programs_colors.append("#FFD02A")
            else:
                programs_colors.append("#35DB24")
        for cable_node in self.transmission_cable.nodes:
            G.add_node(cable_node)
            nodelist.append(cable_node)
            programs_colors.append("#96B1D2")

        nx.draw_networkx_nodes(G, pos=pos, nodelist=nodelist, node_color=programs_colors)


        public_messages = dict()
        for name, msg in self.transmission_cable.public_messages.items():
            public_messages[name] = msg.text
        nx.draw_networkx_labels(G, pos=pos, labels=public_messages)

        edge_colors = []
        edge_list = []
        edge_labels = self.transmission_cable.sending

        for edge in self.transmission_cable.cable_edges:
            G.add_edge(*edge)
            edge_list.append(edge)
            edge_colors.append("#000000")

        for edge in self.transmission_cable.connection_edges:
            G.add_node(edge)
            edge_list.append(edge)
            edge_colors.append("#2431A8")

        nx.draw_networkx_edges(G, pos=pos, edgelist=edge_list, edge_color=edge_colors)

        print(edge_labels)
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
        plt.show()

    def simulation_end(self):
        for program in self.programs:
            if not program.finish:
                print("program not finished")
                return False

        return self.transmission_cable.finish()

    def run(self):
        for program in self.programs:
            program.reset()
        while not self.simulation_end():

            for program in self.programs:
                program.check_what_is_on_transmission_cable()
                if program.detected_collision and not program.jam_signal_flag:
                    print("ok")
                    program.send_jam_signal()

            for program in self.programs:
                if program.iterations_to_send == 0 and not program.finish and not program.jam_signal_flag and not program.is_sending:
                    program.send(program.string_to_send)

            self.transmission_cable.propagate()
            self.print()
            time.sleep(0.5)
