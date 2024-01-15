def can_travel_circuit(gas, cost):
    n = len(gas)
    start, total_tank, current_tank = 0, 0, 0

    for i in range(n):
        net_gas = gas[i] - cost[i]
        total_tank += net_gas
        current_tank += net_gas

        if current_tank < 0:
            start = i + 1
            current_tank = 0

    return start if total_tank >= 0 else -1

# Example usage:
gas1 = [1, 2, 3, 4, 5]
cost1 = [3, 4, 5, 1, 2]
print(can_travel_circuit(gas1, cost1))  # Output: 3

gas2 = [2, 3, 4]
cost2 = [3, 4, 3]
print(can_travel_circuit(gas2, cost2))  # Output: -1