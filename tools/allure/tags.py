from enum import Enum


class AllureTag(str, Enum):
    COURSES = "COURSES"
    DASHBOARD = "DASHBOARD"
    REGRESSION = "REGRESSION"
    USER_LOGIN = "USER_LOGIN"
    NAVIGATION = "NAVIGATION"
    REGISTRATION = "REGISTRATION"
    AUTHORIZATION = "AUTHORIZATION"

# Обратите внимание, что мы наследуем от str и Enum, чтобы значения enum воспринимались
# как строки и могли использоваться напрямую в коде.
# Используем enum-ы вместо строк: