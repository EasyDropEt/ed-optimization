from datetime import datetime
from uuid import uuid4

from ed_domain.core.entities.order import OrderStatus, ParcelSize
from ed_domain.queues.ed_optimization.order_model import OrderModel
from ortools.linear_solver import pywraplp

orders: list[OrderModel] = []

orders = [
    {
        "id": uuid4(),
        "consumer": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Bole Road",
                "latitude": 9.0108,
                "longitude": 38.7613,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "business": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Kazanchis",
                "latitude": 9.0301,
                "longitude": 38.7500,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "latest_time_of_delivery": datetime.now(),
        "parcel": {
            "size": ParcelSize.SMALL,
            "weight": 2.5,
            "dimensions": {"length": 10, "width": 5, "height": 3},
            "fragile": True,
        },
        "order_status": OrderStatus.PENDING,
    },
    {
        "id": uuid4(),
        "consumer": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Piassa",
                "latitude": 9.0371,
                "longitude": 38.7617,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "business": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Arat Kilo",
                "latitude": 9.0456,
                "longitude": 38.7632,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "latest_time_of_delivery": datetime.now(),
        "parcel": {
            "size": ParcelSize.MEDIUM,
            "weight": 5.0,
            "dimensions": {"length": 20, "width": 10, "height": 5},
            "fragile": False,
        },
        "order_status": OrderStatus.PENDING,
    },
    {
        "id": uuid4(),
        "consumer": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Megenagna",
                "latitude": 9.0201,
                "longitude": 38.8000,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "business": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Bole Michael",
                "latitude": 9.0156,
                "longitude": 38.7700,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "latest_time_of_delivery": datetime.now(),
        "parcel": {
            "size": ParcelSize.LARGE,
            "weight": 10.0,
            "dimensions": {"length": 30, "width": 15, "height": 10},
            "fragile": True,
        },
        "order_status": OrderStatus.PENDING,
    },
    {
        "id": uuid4(),
        "consumer": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Sar Bet",
                "latitude": 9.0256,
                "longitude": 38.7800,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "business": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Mexico",
                "latitude": 9.0356,
                "longitude": 38.7900,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "latest_time_of_delivery": datetime.now(),
        "parcel": {
            "size": ParcelSize.SMALL,
            "weight": 1.0,
            "dimensions": {"length": 5, "width": 5, "height": 5},
            "fragile": False,
        },
        "order_status": OrderStatus.PENDING,
    },
    {
        "id": uuid4(),
        "consumer": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Gurd Shola",
                "latitude": 9.0401,
                "longitude": 38.8000,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "business": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "CMC",
                "latitude": 9.0501,
                "longitude": 38.8100,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "latest_time_of_delivery": datetime.now(),
        "parcel": {
            "size": ParcelSize.MEDIUM,
            "weight": 3.0,
            "dimensions": {"length": 15, "width": 10, "height": 5},
            "fragile": True,
        },
        "order_status": OrderStatus.PENDING,
    },
    {
        "id": uuid4(),
        "consumer": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Bole Medhanialem",
                "latitude": 9.0601,
                "longitude": 38.8200,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "business": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Bole Atlas",
                "latitude": 9.0701,
                "longitude": 38.8300,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "latest_time_of_delivery": datetime.now(),
        "parcel": {
            "size": ParcelSize.LARGE,
            "weight": 7.5,
            "dimensions": {"length": 25, "width": 15, "height": 10},
            "fragile": False,
        },
        "order_status": OrderStatus.PENDING,
    },
    {
        "id": uuid4(),
        "consumer": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Bole Rwanda",
                "latitude": 9.0801,
                "longitude": 38.8400,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "business": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Bole Olympia",
                "latitude": 9.0901,
                "longitude": 38.8500,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "latest_time_of_delivery": datetime.now(),
        "parcel": {
            "size": ParcelSize.SMALL,
            "weight": 2.0,
            "dimensions": {"length": 10, "width": 5, "height": 5},
            "fragile": True,
        },
        "order_status": OrderStatus.PENDING,
    },
    {
        "id": uuid4(),
        "consumer": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Bole Japan",
                "latitude": 9.1001,
                "longitude": 38.8600,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "business": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Bole Dembel",
                "latitude": 9.1101,
                "longitude": 38.8700,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "latest_time_of_delivery": datetime.now(),
        "parcel": {
            "size": ParcelSize.MEDIUM,
            "weight": 4.0,
            "dimensions": {"length": 20, "width": 10, "height": 10},
            "fragile": False,
        },
        "order_status": OrderStatus.PENDING,
    },
    {
        "id": uuid4(),
        "consumer": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Bole Edna Mall",
                "latitude": 9.1201,
                "longitude": 38.8800,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "business": {
            "id": uuid4(),
            "location": {
                "id": uuid4(),
                "address": "Bole Friendship",
                "latitude": 9.1301,
                "longitude": 38.8900,
                "postal_code": "1000",
                "city": "Addis Ababa",
                "country": "Ethiopia",
            },
        },
        "latest_time_of_delivery": datetime.now(),
        "parcel": {
            "size": ParcelSize.LARGE,
            "weight": 6.0,
            "dimensions": {"length": 25, "width": 15, "height": 15},
            "fragile": True,
        },
        "order_status": OrderStatus.PENDING,
    },
]


def optimize_orders_into_groups(orders, group_size=2):
    num_orders = len(orders)

    # Create the solver
    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        print("Solver not available.")
        return None

    # Solve the problem
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solution found.")
        groups = [[] for _ in range(group_size)]
        for i in range(num_orders):
            for j in range(group_size):
                if x[i][j].solution_value() > 0.5:
                    groups[j].append(orders[i])
        return groups
    else:
        print("No optimal solution found.")
        return None


if __name__ == "__main__":
    optimize_orders_into_groups(orders)
