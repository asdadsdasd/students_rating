from lxml import etree
from Types import DataType
from DataReader import DataReader


class XMLDataReader(DataReader):
    def read(self, path: str) -> DataType:
        """
        Читает XML-файл и возвращает данные в формате DataType.
        """
        try:
            tree = etree.parse(path)
            root = tree.getroot()

            data = {}
            for student in root:
                name = student.tag
                scores = {subject.tag: int(subject.text) for subject
                          in student}
                data[name] = scores

            return data

        except Exception as e:
            raise ValueError(f"Ошибка при чтении XML-файла: {e}")
