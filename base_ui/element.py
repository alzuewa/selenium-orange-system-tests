from dataclasses import dataclass
from enum import StrEnum


class By(StrEnum):
    ID = 'id'
    XPATH = 'xpath'
    LINK_TEXT = 'link text'
    PARTIAL_LINK_TEXT = 'partial link text'
    NAME = 'name'
    TAG_NAME = 'tag name'
    CLASS_NAME = 'class name'
    CSS_SELECTOR = 'css selector'


@dataclass
class Element:
    by: By
    value: str
    elem_description: str
