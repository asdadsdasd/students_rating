# -*- coding: utf-8 -*-
import argparse
import os
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XMLDataReader import XMLDataReader
from GoodStudentsCounter import GoodStudentsCounter


def get_path_from_arguments(args):
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str,
                        required=True, help="Path to datafile")

    args = parser.parse_args(args)
    return args.path


def get_reader_by_extension(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".xml":
        return XMLDataReader()
    elif ext == ".txt":
        return TextDataReader()
    else:
        raise ValueError(f"Unsupported file extension: {ext}")


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = get_reader_by_extension(path)
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    good_students_count = GoodStudentsCounter(students).count_good_students()
    print(f"Number of good students (all scores >= 76): {good_students_count}")


if __name__ == "__main__":
    main()
