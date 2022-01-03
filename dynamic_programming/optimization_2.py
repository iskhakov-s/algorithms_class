def cheapest_fare_td(rides, cache={():0}):
    if rides not in cache:
        cost1 = rides[-1] * 2.75
        cost2 = 33
        cost3 = 127
        if len(rides) > 1:
            cost1 += cheapest_fare_td(rides[:-1])
        if len(rides) > 7:
            cost2 += cheapest_fare_td(rides[:-7])
        if len(rides) > 30:
            cost3 += cheapest_fare_td(rides[:-30])
        cache[rides] = min(cost1, cost2, cost3)
    return cache[rides]


def cheapest_fare_bu(rides):
    if len(rides) == 0:
        return 0
    cheapest = [0]*len(rides)
    for idx, num_rides in enumerate(rides):
        cost1 = 2.75 * num_rides
        if idx >= 1:
            cost1 += cheapest[idx-1]
        cost2 = 33
        if idx >= 7:
            cost2 += cheapest[idx-7]
        cost3 = 127 
        if idx >= 30:
            cost3 += cheapest[idx-30]
        cheapest[idx] = min(cost1, cost2, cost3)
    return cheapest[len(rides)-1]
    

def main():
    rides = [()] * 4
    rides[0] = (2, 0, 1, 9, 10, 10, 10, 10, 10) # 38.50
    rides[1] = (1, 5, 8, 2, 4, 10, 5, 5) # 35.75
    rides[2] = (3, 0, 0, 0, 0, 0, 76, 2) # 38.5
    rides[3] = (1, 2, 1, 1, 1, 2, 1, 1)  # 27.5
    for i in range(4):
        print(cheapest_fare_bu(rides[i]))
        print(cheapest_fare_td(rides[i]))


if __name__ == '__main__':
    main()
