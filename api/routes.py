from enum import Enum

class Routes(str, Enum):
    POSTS = "/posts"
    POSTS_ITEM = "/posts/{}"
    USERS = "/users"
    USERS_ITEM = "/users/{}"

    def __str__(self):
        return self.value
