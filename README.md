# gRPC Minter API.

### pygenproto.bat - запускает скрипт генерации кода из протофайла proto/api.proto

после генерации необходимо поправить импорт в ```minter/grpc/api_pb2_grpc.py``` с 
```python
import api_pb2 as api__pb2
```
на 
```python
import minter.grpc.api_pb2 as api__pb2
```

### main.py - минимальная программа примера использования. Вам необходим адрес публичной ноды с открытым gRPC портом, либо своя локально заущенная нода, с настроенным и открытым gRPC соединением
