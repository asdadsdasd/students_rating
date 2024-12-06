# -*- coding: utf-8 -*-
import pytest
from src.GoodStudentsCounter import GoodStudentsCounter


class TestGoodStudentsCalculator:

    @pytest.fixture()
    def sample_data(self) -> dict:
        return {
            "Иванов Иван Иванович": [
                ("математика", 91), ("литература", 85),
                ("программирование", 78)
            ],
            "Петров Петр Петрович": [
                ("математика", 70), ("химия", 87), ("социология", 61)
            ],
            "Сидоров Сидор Сидорович": [
                ("физика", 76), ("химия", 88), ("математика", 92)
            ],
            "Кузнецов Алексей Сергеевич": [
                ("история", 85), ("гражданское право", 90)
            ]
        }

    def test_count_good_students_all_good(self, sample_data: dict) -> None:
        all_good_data = {
            "Иванов Иван Иванович": [("математика", 91),
                                     ("литература", 85),
                                     ("программирование", 78)],
            "Сидоров Сидор Сидорович": [("физика", 76),
                                        ("химия", 88), ("математика", 92)],
            "Кузнецов Алексей Сергеевич": [("история", 85),
                                           ("гражданское право", 90)],
            "Петров Петр Петрович": [("математика", 80),
                                     ("химия", 85), ("социология", 76)]
        }
        calculator = GoodStudentsCounter(all_good_data)
        result = calculator.count_good_students()
        assert result == 4, "All students should be counted as good students."

    def test_count_good_students_some_bad(self, sample_data: dict) -> None:
        some_bad_data = {
            "Иванов Иван Иванович": [("математика", 91),
                                     ("литература", 85),
                                     ("программирование", 78)],
            "Петров Петр Петрович": [("математика", 70),
                                     ("химия", 87), ("социология", 61)],
            "Сидоров Сидор Сидорович": [("физика", 76),
                                        ("химия", 88), ("математика", 92)]
        }
        calculator = GoodStudentsCounter(some_bad_data)
        result = (calculator.
                  count_good_students())
        assert result == 2, \
            "Only students with all scores >= 76 should be counted."

    def test_count_good_students_empty_data(self) -> None:
        empty_data = {}
        calculator = GoodStudentsCounter(empty_data)
        result = calculator.count_good_students()
        assert result == 0, "No students should be counted for empty data."

    def test_count_good_students_edge_cases(self) -> None:
        edge_case_data = {
            "Гусев Григорий": [("математика", 76), ("литература", 76)],
            "Тимофеев Тимур": [("программирование", 75), ("физика", 80)]
        }
        calculator = (
            GoodStudentsCounter(edge_case_data))
        result = (calculator.
                  count_good_students())
        assert result == 1, ("Only students with all scores >= 76 "
                             "should be counted, edge case handled.")
