from Room import Room
from VacuumAgent import VacuumAgent
from Environment import Environment


class TwoRoomEnvironment(Environment):

    def set_delay(self, delay):
        self.delay = delay

    agent: VacuumAgent

    def __init__(self, agent):
        self.room1 = Room('A', 'dirty')
        self.room2 = Room('B', 'dirty')
        self.agent = agent
        self.currentRoom = self.room1
        self.step = 1
        self.delay = 100
        self.action = ''

    def execute_step(self, n=1):

        for _ in range(0, n):
            self.display_perception()
            self.agent.sense(self)
            to_do = self.agent.act()

            if to_do == 'clean':
                self.currentRoom.status = to_do
            elif to_do == 'right':
                self.currentRoom = self.room2
            else:
                self.currentRoom = self.room1

            self.action = to_do
            self.display_action()
            self.step += 1

    def execute_all(self):
        pass

    def display_perception(self):
        print("Step[%d]: Room[%s] - Status[%s]" %(self.step, self.currentRoom.location, self.currentRoom.status))

    def display_action(self):
        print("Step[%d]: Action[%s]" %(self.step, self.action))
