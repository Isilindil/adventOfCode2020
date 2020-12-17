#!/usr/bin/python

class Boat :
    def __init__(self):
        self.facing = "E"
        self.coord = [0, 0]
        self.waypoint = [1, 10]

    def __str__(self):
        return "boat facing : {}\ncoord : {}, {}".format(self.facing, self.coord[0], self.coord[1])

    def move_part_one(self, direction, value):
        if direction == "F" :
            direction = self.facing
        if direction == "N" :
            self.coord[0] += int(value)
        elif direction == "S" :
            self.coord[0] -= int(value)
        elif direction == "W":
            self.coord[1] -= int(value)
        elif direction == "E":
            self.coord[1] += int(value)

        facing_list = ["N", "E", "S", "W"]
        new_facing = facing_list.index(self.facing)
        if direction == "R" :
            new_facing += (value // 90)
            new_facing = new_facing % 4
        elif direction == "L" :
            new_facing -= value // 90
        self.facing = facing_list[new_facing]

    def move_part_two(self, direction, value):
        if direction == "F" :
            self.coord[0] += value*self.waypoint[0]
            self.coord[1] += value*self.waypoint[1]
        elif direction == "N" :
            self.waypoint[0] += int(value)
        elif direction == "S" :
            self.waypoint[0] -= int(value)
        elif direction == "W":
            self.waypoint[1] -= int(value)
        elif direction == "E":
            self.waypoint[1] += int(value)
        else :
            rotation = value // 90
            if rotation % 2 == 0 :
                self.waypoint[0], self.waypoint[1] = -self.waypoint[0], -self.waypoint[1]
            else :
                if direction == "R" :
                    for _ in range(rotation) :
                        self.waypoint[0], self.waypoint[1] = -self.waypoint[1], self.waypoint[0]
                elif direction == "L" :
                    for _ in range(rotation):
                        self.waypoint[0], self.waypoint[1] = self.waypoint[1], -self.waypoint[0]

    def manhattan_distance_from_origin(self):
        return abs(self.coord[0])+abs(self.coord[1])


if __name__ == "__main__" :
    with open("input") as a :
        data = a.read().split("\n")
    a.close()

    boat_one = Boat()
    boat_two = Boat()

    for dv in data :
        d = dv[0]
        v = int(dv[1:])
        boat_one.move_part_one(d, v)
        boat_two.move_part_two(d, v)
        print(boat_two.coord)
        print(boat_two.waypoint)

    print(boat_one)
    print(boat_one.manhattan_distance_from_origin())
    print(boat_two)
    print(boat_two.manhattan_distance_from_origin())
