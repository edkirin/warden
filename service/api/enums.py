import enum


class ActionEnum(str, enum.Enum):
    CREATE = "CREATE"
    VIEW = "VIEW"
    EDIT = "EDIT"
    DELETE = "DELETE"
    VIEW_ASSIGNED = "VIEW_ASSIGNED"
    INDUCE = "INDUCE"
