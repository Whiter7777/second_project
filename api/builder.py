class Builder:
    @staticmethod
    def get_objects(client, all_objects, *ids):
        return client.get(all_objects, params={'id': ids} if ids else None)

    @staticmethod
    def get_object(client, all_objects_item, obj_id):
        return client.get(all_objects_item.format(obj_id))

    @staticmethod
    def post_object(client, all_objects, **kwargs):
        return client.post(all_objects, **kwargs)
