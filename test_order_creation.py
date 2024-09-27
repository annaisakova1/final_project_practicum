import sender_stand_request
from data import order_data


def test_create_order_and_check_by_track():
    # 1. Создать заказ
    create_order_response = sender_stand_request.create_order(order_data)

    # Проверяем, что заказ был успешно создан
    assert create_order_response.status_code == 201, f"Expected status code 201, got {create_order_response.status_code}"

    # Получаем трек-номер заказа
    track_number = create_order_response.json().get("track")
    assert track_number is not None, "Track number is not found in the response"

    # 2. Проверить заказ по треку
    get_order_response = sender_stand_request.get_order_by_track(track_number)

    # Проверить, что код ответа 200
    assert get_order_response.status_code == 200, f"Expected status code 200, got {get_order_response.status_code}"
