import json
from flask import Blueprint, request
from utils import create_card

card_views = Blueprint('card_views', __name__)


@card_views.route('/', methods=['POST'])
def create_card_api() -> json:
    data: dict = dict(json.loads(request.get_data()))

    created_card_response = create_card(data)

    return created_card_response
