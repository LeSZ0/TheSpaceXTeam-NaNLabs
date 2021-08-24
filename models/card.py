from dataclasses import dataclass
from typing import Optional
from random import randint, choice
from slugify import slugify
import string
from .category import Category


@dataclass()
class CardType:
    name: str

    @property
    def slug(self) -> str:
        return slugify(self.name)


@dataclass()
class Card:
    type: CardType
    description: str = ''
    category: Optional[Category] = None
    title: str = ''

    def __str__(self) -> str:
        return f'{self.title if self.title != "" else self.description[:7] + "..."}'

    def __repr__(self):
        return f'Card({str(self)})'

    def card_type_is(self, t: str) -> bool:
        """Returns a boolean if the card's type is the same as the type passed as a param (t)"""
        return self.type.slug.__contains__(t)

    def serialize(self) -> dict:
        return {
            "type": self.type.name,
            "description": self.description,
            "category": self.category.name if self.category else None,
            "title": self.title
        }

    @staticmethod
    def make_bug_title() -> str:
        """Make a title for a bug card

        This method generates a title for a bug card using the following pattern bug-{word}-{number}.
        "word" and "number" would be selected randomly.
        """

        word = ''.join(choice(string.ascii_letters) for _ in range(5))  # Generates a random word using letters

        return f'bug-{word}-{randint(0, 9)}'
