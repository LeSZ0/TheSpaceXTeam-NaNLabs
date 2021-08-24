import requests
from conf import query_params, trello_url, board_id
from random import choice


def get_board_members() -> list:
    board_members_req = requests.get(
        url=f'{trello_url}/boards/{board_id}/lists',
        params=query_params
    )

    return list(board_members_req.json())


def get_specific_member(board_members: list[{}], member_id: str) -> dict:
    return [x for x in board_members if member_id in x['id']][0]


def get_random_member(board_members: list[{}]) -> str:
    return choice(board_members)['id']
