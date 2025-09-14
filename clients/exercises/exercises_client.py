from typing import TypedDict

from httpx import Response, QueryParams

from clients.api_clients import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий для определенного курса.
    """
    courseId: str


class CreateExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на обновление данных задания.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий для определенного курса.

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=QueryParams(query))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получение задания.

        :param exercise_id: идентификатор задания.
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercises_api(self, request: CreateExercisesQueryDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercises_api(self, exercise_id: str, request: UpdateExercisesQueryDict) -> Response:
        """
        Метод обновления данных задания.

        :param exercise_id: идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercises_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания

        :param exercise_id: идентификатор задания.
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
