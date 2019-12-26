class Room:
    def __init__(self, location, status='dirty'):
        self.location = location
        self.status = status


class NRoomEnvironment:
    def __init__(self, agent, n_rooms):
        self.rooms = []
        for r in range(0, n_rooms):
            self.rooms.append(Room('Room'+str(r+1)))

        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.step = 1
        self.delay = 100
        self.action = ''
        self.score = 0

    def set_delay(self, delay):
        self.delay = delay

    def execute_step(self, n=1):

        for _ in range(0, n):
            if self.currentRoom.status == 'dirty':
                self.score -= 10

            self.display_perception()
            self.agent.sense(self)
            to_do = self.agent.act()

            if to_do == 'clean':
                self.currentRoom.status = to_do
                self.score += 25
            elif to_do == 'start':
                self.score -= 1
                self.currentRoom = self.rooms[0]
            else:
                self.score -= 1
                next_left = [r for r in range(0, len(self.rooms)) if self.rooms[r] == self.currentRoom][0] + 1
                self.currentRoom = self.rooms[next_left]

            self.action = to_do
            self.display_action()
            self.step += 1

    def display_perception(self):
        print("Step[%d]: Room[%s] - Status[%s] - Score[%d]" % (self.step, self.currentRoom.location, self.currentRoom.status, self.score))

    def display_action(self):
        print("Step[%d]: Action[%s]" % (self.step, self.action))


class VacuumAgent:
    def __init__(self):
        self.environment = None

    def sense(self, environment):
        self.environment = environment

    def act(self):
        en = self.environment
        if en.currentRoom.status == 'dirty':
            return 'clean'
        elif [r for r in range(0, len(en.rooms)) if en.rooms[r] == en.currentRoom][0] == len(en.rooms)-1:
            return 'start'
        else:
            return 'next'


if __name__ == '__main__':
    agent = VacuumAgent()
    env = NRoomEnvironment(agent, 5)

    env.execute_step(15)
