class Bell:
    def __init__(self, *info, **kwargs):
        self.info = list(info)
        self.kwargs = kwargs
        self.c = 0

    def print_info(self):
        names = sorted(self.kwargs.keys())
        for i in range(len(names)):
            if i != len(names) - 1:
                print(f"{names[i]}: {self.kwargs[names[i]]}", end=", ")
            else:
                if self.info:
                    print(f"{names[i]}: {self.kwargs[names[i]]}", end="; ")
                else:
                    print(f"{names[i]}: {self.kwargs[names[i]]}")

        if len(self.info) == 0 and len(names) == 0:
            print("-")
        if len(self.info) != 0:
            print(", ".join(self.info))


class LittleBell(Bell):
    def sound(self):
        print("ding")

    def xd(self):
        return "LittleBell"


class BigBell(Bell):

    def sound(self):
        if self.c % 2 == 0:
            print("ding")
        else:
            print("dong")
        self.c += 1

    def xd(self):
        return "BigBell"


class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def sound(self):
        for i in self.bells:
            i.sound()
        print("...")

    def append(self, bell):
        self.bells.append(bell)

    def print_info(self):
        n = 0
        for i in self.bells:
            print(f"{n + 1} {i.xd()}")
            i.print_info()
            n += 1
        print()


class SizedBellTower(BellTower):
    def __init__(self, *bells, size=10):
        self.sized = size
        self.bells = []
        n = 0
        for i in list(bells):
            n += 1
            if n > self.sized:
                self.bells.append(i)
                del self.bells[0]
            else:
                self.bells.append(i)

    def append(self, bell):
        if len(self.bells) == self.sized:
            self.bells.append(bell)
            del self.bells[0]
        else:
            self.bells.append(bell)


class TypedBellTower(BellTower):
    def __init__(self, *bells, bell_type=LittleBell):
        self.bells = []
        self.bell_type = bell_type
        for i in list(bells):
            if type(i) is bell_type:
                self.bells.append(i)

    def append(self, bell):
        if type(bell) is self.bell_type:
            self.bells.append(bell)
