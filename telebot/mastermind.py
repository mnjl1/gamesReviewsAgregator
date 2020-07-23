from service.getDataFromDataBase import get_last_reviews


def get_response(msg):
    return get_last_reviews()
