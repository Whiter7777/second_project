from api.api_client import HTTPClient
from configurations.configuration import ConfigManager

def get_http_client(
        base_url: str = ConfigManager().get_config_data().baseUrl) -> HTTPClient:
    return HTTPClient(base_url=base_url)

