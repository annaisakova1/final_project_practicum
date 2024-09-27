import configuration
import requests
import data
from configuration import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH

def create_order(order_data):
    url = f"{URL_SERVICE}{CREATE_ORDER_PATH}"
    response = requests.post(url, json=order_data)
    return response

def get_order_by_track(track_number):
    url = f"{URL_SERVICE}{GET_ORDER_BY_TRACK_PATH}?t={track_number}"
    response = requests.get(url)
    return response