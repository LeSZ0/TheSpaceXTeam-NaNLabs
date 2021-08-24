import requests
from models import CardType, Card, Category
from .board_lists import get_board_lists, get_specific_list
from .board_members import get_board_members, get_random_member
from .board_labels import get_or_create_label, get_board_labels
from conf import query_params, trello_url


def bug_card(card: Card, data: dict, params: dict) -> dict:
    card.description = data.get('description')
    card.title = card.make_bug_title()
    board_lists: list = get_board_lists()
    list_selected: str = get_specific_list(board_lists, 'todo')
    board_members: list = get_board_members()

    params['idList'] = list_selected
    params['name'] = card.title
    params['desc'] = card.description
    params['idMembers'] = [get_random_member(board_members)]
    params['idLabels'] = [get_or_create_label(get_board_labels(), 'Bug')]

    return params


def task_card(card: Card, category: str, params: dict) -> dict:
    card.category = Category(category)
    list_selected: str = get_specific_list(get_board_lists(), 'todo')
    params['idList'] = list_selected
    params['idLabels'] = [get_or_create_label(get_board_labels(), card.category.name)]

    return params


def issue_card(card: Card, description: str, params: dict) -> dict:
    list_selected: str = get_specific_list(get_board_lists(), 'todo')
    card.description = description
    params['idList'] = list_selected
    params['desc'] = card.description
    params['idLabels'] = []

    return params


def create_card(data: dict) -> any:
    card_type: CardType = CardType(data.get('type'))
    new_card: Card = Card(
        type=card_type,
        title=data.get('title')
    )

    params: dict = {}

    if new_card.card_type_is('bug'):
        params = bug_card(new_card, data, query_params)

    elif new_card.card_type_is('task'):
        params = task_card(new_card, data.get('category'), query_params)

    elif new_card.card_type_is('issue'):
        params = issue_card(new_card, data.get('description'), query_params)

    params['name'] = new_card.title

    create_card_req = requests.post(
        url=f'{trello_url}/cards',
        params=params
    )

    return create_card_req.text
