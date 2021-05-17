class C32:
    def __init__(self):
        self.state = "A"

    def rev(self):
        if self.state == "A":
            self.state = "B"
            return 0
        elif self.state == "B":
            self.state = "C"
            return 2
        elif self.state == "C":
            self.state = "D"
            return 3
        elif self.state == "D":
            self.state = "E"
            return 6
        elif self.state == "E":
            self.state = "F"
            return 7
        elif self.state == "F":
            raise RuntimeError


    def add(self):
        if self.state == "A":
            self.state = "C"
            return 1
        elif self.state == "C":
            return 4
        elif self.state == "F":
            self.state = "D"
            return 8
        else:
            raise RuntimeError

    def hurry(self):
        if self.state == "C":
            self.state = "E"
            return 5
        else:
            raise RuntimeError
