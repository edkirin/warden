class BaseException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ObjectNotFoundError(BaseException):
    def __init__(self, object_class: str, object_id: int):
        self.message = f"Object {object_class} with id {object_id} not found"


class UserNotFoundError(ObjectNotFoundError):
    def __init__(self, tenant_id: int, external_user_id: int):
        self.message = f"User with tenant_id {tenant_id} and external_user_id {external_user_id} not found"
