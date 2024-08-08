import grpc
import minter.grpc.api_pb2 as mapi
import minter.grpc.api_pb2_grpc as mapi_grpc
from google.protobuf.empty_pb2 import Empty


def get_address_info(address):
    channel = grpc.insecure_channel('localhost:8842')
    stub = mapi_grpc.ApiServiceStub(channel)

    address_request = mapi.AddressRequest(address=address, height=0, delegated=False)
    address_response = stub.Address(address_request)

    print(address_response)

    status = stub.Status(Empty())
    print(status)


if __name__ == '__main__':
    address_to_check = "Mxab3ab394c5fbfb1ecfd9913e5280c125ed2e0e0a"
    get_address_info(address_to_check)

