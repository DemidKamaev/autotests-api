from typing import TypedDict

from httpx import Response

from clients.api_clients import APIClient


class CreateRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateRequestDict) -> Response:
        """
        Метод создает пользователя

        :param request: Словарь (тело запроса в JSON-формате)
        :return: ответ от сервере в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
