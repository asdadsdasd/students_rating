import os
import pytest
from src.XMLDataReader import XMLDataReader


@pytest.fixture
def valid_xml_file():
    file_path = 'test_data.xml'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('''<?xml version="1.0" encoding="UTF-8" ?>
<root>
    <Иванов_Иван_Иванович>
        <математика>67</математика>
        <литература>100</литература>
        <программирование>91</программирование>
    </Иванов_Иван_Иванович>
    <Петров_Петр_Петрович>
        <математика>78</математика>
        <химия>87</химия>
        <социология>61</социология>
    </Петров_Петр_Петрович>
</root>''')
    yield file_path
    if os.path.exists(file_path):
        os.remove(file_path)


@pytest.fixture
def malformed_xml_file():
    file_path = 'malformed.xml'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('<root><Иван Иван><математика>80</математика></Иван Иван>')
    yield file_path
    if os.path.exists(file_path):
        os.remove(file_path)


def test_read_valid_file(valid_xml_file):
    """Проверяет корректность чтения файла с правильными данными."""
    reader = XMLDataReader()
    expected_data = {
        "Иванов_Иван_Иванович": {
            "математика": 67,
            "литература": 100,
            "программирование": 91,
        },
        "Петров_Петр_Петрович": {
            "математика": 78,
            "химия": 87,
            "социология": 61,
        },
    }
    assert reader.read(valid_xml_file) == expected_data


def test_read_invalid_file():
    reader = XMLDataReader()
    with pytest.raises(ValueError, match="Ошибка при чтении XML-файла"):
        reader.read("non_existent_file.xml")


def test_read_malformed_xml(malformed_xml_file):
    reader = XMLDataReader()
    with pytest.raises(ValueError, match="Ошибка при чтении XML-файла"):
        reader.read(malformed_xml_file)
