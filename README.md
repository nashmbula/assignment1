 Assignment 1. Symbolic / Model-Based Design View

The symbolic or model-based view represents problems through explicit, programmed rules and formal search algorithms.
 The computer follows programmed rules and a search algorithm to calculate the shortest path between two locations. It examines the available roads, compares the distances between different points, and selects the route with the lowest total distance. This process continues systematically until the destination is reached.
 Road networks are modeled as explicit graph structures, where intersections act as nodes and road segments act as edges with static distance weights. Deterministic Logics  Algorithms such as A* or Dijkstra’s algorithm operate over these pre-defined graphs to compute guaranteed optimal paths based on fixed, rule-based constraints.



 Data-Driven / Learning-Based Design View

The data-driven or learning-based view relies on analyzing large volumes of historical and real-time data to adapt, predict, and dynamically adjust system behavior.

Core Mechanism: The system uses a lot of data to understand traffic patterns and estimate how long a journey will take. For example, Maps can collect information about how fast cars are moving on different roads. It can also look at past traffic information and the time of day. By comparing this information, it can predict whether a road is busy or clear and estimate the time it will take to reach the destination.
 Real-Time Data Streams:Ingests live speed, location updates, and sensor data from millions of active devices to detect dynamic delays as they happen.
Predictive Analytics: Machine learning models process historical traffic patterns alongside live data streams to dynamically update ETAs and optimize alternate routes.
