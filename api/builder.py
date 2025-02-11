# from api.api_client import HTTPClient
from configurations.configuration import ConfigManager
from configurations.test_manager import TestManager

# def get_http_client(
#         base_url: str = ConfigManager().get_config_data().baseUrl) -> HTTPClient:
#     return HTTPClient(base_url=base_url)

class Builder:

    @staticmethod
    def get_objects(client, *ids):
        return client.get(TestManager().get_test_data().all_messages, params={'id': ids} if ids else None)

    @staticmethod
    def get_object(client, obj_id):
        return client.get(TestManager().get_test_data().all_messages_item.format(obj_id))

    @staticmethod
    def post_object(client, **kwargs):
        return client.post(routes.Routes.OBJECTS, **kwargs)

