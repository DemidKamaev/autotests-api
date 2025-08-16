from typing import TypedDict

from httpx import Response

from clients.api_clients import APIClient


class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию
    """
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str  # Название ключа совпадает с API


class AuthenticationClient(APIClient):
    """
    Клиет для работы с /api/v1/authentication
    """
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя

        :param request: Словарь с email и password  (а.)
        :return: Ответ от сервера в виде объекта httpx.Response
        :self.post(...): метод базового APIClient, который делает POST-запрос.
        """
        return self.post("/api/v1/authentication", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации

        :param request: Словарь с refreshToken
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)

