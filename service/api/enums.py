import enum


class ActionEnum(str, enum.Enum):
    CREATE = "CREATE"
    VIEW = "VIEW"
    VIEW_ALL = "VIEW_ALL"
    VIEW_ASSIGNED = "VIEW_ASSIGNED"
    EDIT = "EDIT"
    DELETE = "DELETE"
    INDUCE = "INDUCE"
