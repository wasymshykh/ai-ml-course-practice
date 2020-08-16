from Agent import Agent


class VacuumAgent(Agent):

    def __init__(self):
        pass

    def sense(self, environment):
        self.environment = environment

    def act(self):

        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        elif self.environment.currentRoom.location == 'A':
            return 'right'
        else:
            return 'left'
