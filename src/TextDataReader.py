# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader

class TextDataReader(DataReader):
    def __init__(self):
        self.key = ""
        self.students: DataType = {}

    def read(self, path):
        with open(path, encoding='utf-8') as file:
            for line in file:
                if not line.startswith(" "):
                    self.key = line.strip()
                    self.students[self.key] = []
                else:
                    subj, score = line.split(":", maxsplit=1)
                    self.students[self.key].append((subj.strip(), int(score.strip())))
        return self.students
