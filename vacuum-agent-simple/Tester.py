
from TwoRoomEnvironment import TwoRoomEnvironment
from VacuumAgent import VacuumAgent


agent = VacuumAgent()
two_room = TwoRoomEnvironment(agent)
two_room.execute_step(10)


