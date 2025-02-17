from pydantic import BaseModel
from models.post_model import PostModel
from models.user_model import UserModel


class TestDataModel(BaseModel):
    message_userid_real: int
    message_id_real: int
    message_id_unreal: int
    user_id: int
    userid_1: int
    id_101: int
    letters_quant_in_range: tuple
    message_id_99: PostModel
    user_id_5: UserModel
