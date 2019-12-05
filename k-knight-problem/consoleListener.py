
class ConsoleListener:

    def __init__(self, n, m):
        self.n = n
        self.m = m
    
    def fireChange(self, csp, assignment):

        result = []
        for _ in range(0, self.n):
            temp = []
            for _ in range(0, self.m):
                temp.append("A")
            result.append(temp)

        for var in assignment.get_variables():
            val = assignment.get_assignment(var)
            result[val[0]-1][val[1]-1] = var.get_name()

        to_print = ""
        for i in range(0, len(result)):
            to_print += str(result[i]) + "\n"

        print(to_print)