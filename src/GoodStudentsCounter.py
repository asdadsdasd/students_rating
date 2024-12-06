class GoodStudentsCounter:
    def __init__(self, data: dict):
        self.data = data

    def count_good_students(self) -> int:
        good_students_count = 0
        for student, subjects in self.data.items():
            if all(score >= 76 for _, score in subjects):
                good_students_count += 1
        return good_students_count
