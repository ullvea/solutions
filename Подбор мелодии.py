N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, n, t=False):
        self.n = n
        self.t = t
        if self.t and self.n in LONG_PITCHES:
            self.ind = LONG_PITCHES.index(self.n)
            self.n = LONG_PITCHES[self.ind]
        elif self.t and self.n in PITCHES:
            self.ind = PITCHES.index(self.n)
            self.n = LONG_PITCHES[self.ind]
        else:
            self.ind = PITCHES.index(self.n)

    def __str__(self):
        if self.t:
            if self.n == 'до':
                self.n = 'до-о'
            elif self.n == 'ре':
                self.n = 'ре-э'
            elif self.n == 'ми':
                self.n = 'ми-и'
            elif self.n == 'фа':
                self.n = 'фа-а'
            elif self.n == 'соль':
                self.n = 'со-оль'
            elif self.n == 'ля':
                self.n = 'ля-а'
            elif self.n == 'си':
                self.n = 'си-и'
        return f'{self.n}'

    def __eq__(self, other):
        return self.ind == other.ind

    def __lt__(self, other):
        return self.ind < other.ind

    def __ne__(self, other):
        return self.ind != other.ind

    def __le__(self, other):
        return self.ind <= other.ind

    def __gt__(self, other):
        return self.ind > other.ind

    def __ge__(self, other):
        return self.ind >= other.ind

    def __lshift__(self, other):
        if self.n in PITCHES:
            return Note(PITCHES[(self.ind - other) % N])
        return Note(LONG_PITCHES[(self.ind - other) % N], True)

    def __rshift__(self, other):
        if self.n in PITCHES:
            return Note(PITCHES[(self.ind + other) % N])
        return Note(LONG_PITCHES[(self.ind + other) % N], True)

    def get_interval(self, other):
        dif = abs(self.ind - other.ind)
        return INTERVALS[dif]

    def __repr__(self):
        return self.n


class Melody:
    def __init__(self, mel=None):
        if mel is None:
            self.mel = []
        else:
            self.mel = mel

    def append(self, x):
        self.mel.append(x)

    def replace_last(self, x):
        self.mel[-1] = x

    def remove_last(self):
        self.mel = self.mel[:-1]

    def clear(self):
        self.mel = []

    def __len__(self):
        return len(self.mel)

    def __rshift__(self, other):
        flag = True
        ans = []
        for i in range(len(self.mel)):
            if self.mel[i].ind + other > 6:
                flag = False
                break
            ans.append(self.mel[i].__rshift__(other))
        if flag:
            return Melody(ans.copy())
        return Melody(self.mel.copy())

    def __lshift__(self, other):
        flag = True
        ans = []
        for i in range(len(self.mel)):
            if self.mel[i].ind - other < 0:
                flag = False
                break
            ans.append(self.mel[i].__lshift__(other))
        if flag:
            return Melody(ans.copy())
        return Melody(self.mel.copy())

    def __str__(self):
        return ", ".join([str(i) for i in self.mel]).capitalize()