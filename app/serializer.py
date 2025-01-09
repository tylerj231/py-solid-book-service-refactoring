import json
from abc import  ABC, abstractmethod
import xml.etree.ElementTree as ET


class Serializer(ABC):
    @abstractmethod
    def serialize(self):
        pass


class JsonSerializer(Serializer):
    def __init__(self, book):
        self.book = book

    def serialize(self):
        return json.dumps(
            {
                "title": self.book.title,
                "content": self.book.content
            }
        )


class XMLSerializer(Serializer):
    def __init__(self, book):
        self.book = book

    def serialize(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")
