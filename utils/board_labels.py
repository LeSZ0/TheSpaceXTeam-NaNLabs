import requests
from conf import query_params, trello_url, board_id


def get_board_labels() -> list:
    board_labels_req = requests.get(
        url=f'{trello_url}/boards/{board_id}/labels',
        params=query_params
    )

    return list(board_labels_req.json())


def get_or_create_label(board_labels: list[{}], label_name: str) -> str:
    selected_label_id: str or None = None

    for x in board_labels:
        if label_name.lower() in x['name'].lower():
            selected_label_id = x['id']
            break

    if selected_label_id:
        return selected_label_id

    else:
        params: dict = query_params
        params['name'] = label_name
        create_board_label_req = requests.post(
            url=f'{trello_url}/boards/Z89XkNXi/labels',
            params=query_params
        )

        return create_board_label_req.json()['id']


def get_specific_label(board_labels: list[{}], label_name: str) -> str:
    return [x for x in board_labels if label_name.lower() in x['name'].lower()][0]['id']
