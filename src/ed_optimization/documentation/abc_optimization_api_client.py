from abc import ABCMeta, abstractmethod

from ed_domain.documentation.common.api_response import ApiResponse
from ed_domain.queues.ed_optimization.order_model import OrderModel


class ABCOptimizationApiClient(metaclass=ABCMeta):
    @abstractmethod
    def create_order(self, order_model: OrderModel) -> ApiResponse[None]: ...
