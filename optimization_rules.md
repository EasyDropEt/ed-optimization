# Optimization Rules

Optimization rules are a set of guidelines or best practices that can be followed to improve the performance and efficiency of code. These rules can apply to various programming languages and paradigms, and they often focus on reducing resource consumption, improving execution speed, and enhancing code readability and maintainability.

## Introduction

In this document, we outline a set of optimization rules specifically designed for handling orders in a delivery system. These rules aim to streamline the process, reduce delivery times, and improve overall efficiency.

## Order Model

The order model is a crucial part of our system, representing the data structure for handling orders. Below are the components of the order model:

```py
class OrderModel(TypedDict):
    id: UUID
    consumer: ConsumerModel
    business: BusinessModel
    latest_time_of_delivery: datetime
    parcel: Parcel

class BusinessModel(TypedDict):
    id: UUID
    location: LocationModel

class ConsumerModel(TypedDict):
    id: UUID
    location: LocationModel

class Parcel(TypedDict):
    size: ParcelSize
    weight: float
    dimensions: ParcelDimensions
    fragile: bool

class ParcelSize(StrEnum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class ParcelDimensions(TypedDict):
    length: int
    width: int
    height: float
```

### Explanation of Models

- **OrderModel**: Represents an order with details about the consumer, business, delivery time, and parcel.
- **BusinessModel**: Contains information about the business, including its location.
- **ConsumerModel**: Contains information about the consumer, including their location.
- **Parcel**: Details about the parcel, such as size, weight, dimensions, and whether it is fragile.

## Grouping Optimization Rules

This is essentially a traveling salesman problem, where the goal is to minimize the distance traveled while delivering parcels. We have order pick-up (business location) and drop-off (consumer location) points.

1. **Priority on Delivery Time**: The latest time of delivery should be given the highest priority. This ensures that all deliveries are made within the required timeframe.

2. **Grouping by Business**: Orders should be grouped by the same business, if possible. This reduces the number of trips needed and optimizes the delivery route.

3. **Distance Calculation**: Use a distance calculation algorithm (e.g., Haversine formula) to determine the distance between locations. This helps in optimizing the route taken for deliveries.

4. **Parcel Size and Weight Consideration**: When grouping orders, consider the size and weight of parcels. Larger or heavier parcels may require different handling or transportation methods.

5. **Fragility Consideration**: Fragile parcels should be handled with care. Grouping fragile parcels together can help in ensuring they are delivered safely.

6. **Dynamic Re-Grouping**: If new orders come in while deliveries are being made, consider re-grouping the remaining orders to optimize the route further.

7. **Real-Time Traffic Data**: If available, use real-time traffic data to adjust routes dynamically. This can help in avoiding delays and ensuring timely deliveries.

8. **Feedback Loop**: Implement a feedback loop to learn from past deliveries. This can help in improving the algorithm over time, making it more efficient and effective.

### Strategy: Hybrid Trigger

#### 🔧 Example Flow:
1. New delivery comes in.
2. Check if there’s a DeliveryJob within 3km and 30min window.
    a. If yes, append to that job.
    b. If no, place in temporary queue.
3 Periodically process the queue into new jobs.

#### 🔁 Hybrid Trigger 

Trigger:
- Try to group with existing jobs (if within time/location proximity).
- If no good match, temporarily queue it.
- Every X minutes, flush remaining to new jobs.

✅ Pros:
- Flexibility between speed and efficiency.
- Allows partial optimization without big delays.


## Conclusion

By following these optimization rules, you can improve the efficiency of your delivery system. These guidelines help in reducing delivery times, optimizing routes, and ensuring timely deliveries. For further reading, consider exploring algorithms related to the traveling salesman problem and other optimization techniques.
