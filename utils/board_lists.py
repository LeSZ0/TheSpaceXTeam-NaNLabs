import requests
from conf import query_params, trello_url, board_id


def get_board_lists() -> list:
    board_lists_req = requests.get(
        url=f'{trello_url}/boards/{board_id}/lists',
        params=query_params
    )

    return list(board_lists_req.json())


def get_specific_list(board_lists: list[{}], list_name: str) -> str:
    return [x for x in board_lists if list_name.lower() in x['name'].replace(' ', '').lower()][0]['id']
