import grpc

import user_service_pb2
import user_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')  # создаем подключение к каналу
stub = user_service_pb2_grpc.UserServiceStub(channel)  # инициализируем заглушку с помощью
# которой мы будем выполнять gRPC запросы к серверу
response = stub.GetUser(user_service_pb2.GetUserRequest(username="Alice"))
print(response)

# Теперь мы можем выполнить запрос и получить ответ
# Вызываем метод на grpc_server: GetUser(), т.е. удаленную процедуру


# Для клиента нам необходимо создать канал (незащищенный канал)
# Потому что мы создавали сервер как add_insecure_port
# Соотвественно без защищенного соединения
# Соотвественно он у нас запущен на localhost:50051

# Далее нам необходимо использовать стаб - заглушка,
# С помощью которой мы можем выполнять запросы
# То есть нам необходимо как-то взаимодействовать с этим
# Сервисом: и мы выполняем это через заглушку
# user_service_pb2_grpc.UserServiceStub (Инициализируем ее)
# И на вход даем channel


