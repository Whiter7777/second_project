import random
from string import ascii_letters


class RandomPostGenerator:
    @staticmethod
    def generate_random_name(letters_min_max: tuple[int, int]):
        name = "".join(random.choice(ascii_letters) for i in range(random.randint(
            letters_min_max[0], letters_min_max[1])))
        return name.title()

    @staticmethod
    def generate_random_post(letters_min_max: tuple[int, int], user_id: int):
        return {"title": RandomPostGenerator().generate_random_name(letters_min_max),
                "body": RandomPostGenerator().generate_random_name(letters_min_max),
                "userId": user_id
                }
