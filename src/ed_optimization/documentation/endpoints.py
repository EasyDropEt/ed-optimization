from ed_domain.documentation.common.base_endpoint import BaseEndpoint
from ed_domain.documentation.common.endpoint_description import \
    EndpointDescription
from ed_domain.documentation.common.http_method import HttpMethod
from ed_domain.queues.ed_optimization.order_model import OrderModel


class OptimizationEndpoint(BaseEndpoint):
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._descriptions: list[EndpointDescription] = [
            {
                "name": "create_order",
                "method": HttpMethod.POST,
                "path": f"{self._base_url}/orders",
                "request_model": OrderModel,
            },
        ]

    @property
    def descriptions(self) -> list[EndpointDescription]:
        return self._descriptions
