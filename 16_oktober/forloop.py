from math import sqrt


def robot_moves(moves):
    pos = [0, 0]
    for move in moves:
        dir_and_distance = move.split()
        if dir_and_distance[0].upper() == "UP":
            pos[0] += int(dir_and_distance[1])
        elif dir_and_distance[0].upper() == "DOWN":
            pos[0] -= int(dir_and_distance[1])
        elif dir_and_distance[0].upper() == "RIGHT":
            pos[1] += int(dir_and_distance[1])
        elif dir_and_distance[0].upper() == "LEFT":
            pos[1] -= int(dir_and_distance[1])

    return round(sqrt(pos[0] ** 2 + pos[1] ** 2))


def main():
    moves = ("UP 5", "DOWN 3", "LEFT 3", "RIGHT 2")
    dist = robot_moves(moves)
    print(dist)


if __name__ == '__main__':
    main()