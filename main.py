def show_field():

    print(f"""---------
| {position[0][0]} {position[0][1]} {position[0][2]} |
| {position[1][0]} {position[1][1]} {position[1][2]} |
| {position[2][0]} {position[2][1]} {position[2][2]} |
---------""")


def play():

    turn_counter = 1

    while turn_counter <= 9:

        player = "X" if turn_counter % 2 != 0 else "O"
        coordinates = input("Enter the coordinates: ").split()

        if coordinates[0].isnumeric() and coordinates[1].isnumeric():
            coordinates = [int(i) - 1 for i in coordinates]
        else:
            print("You should enter numbers!")
            continue

        if not 0 <= coordinates[0] <= 2 or not 0 <= coordinates[1] <= 2:
            print("Coordinates should be from 1 to 3!")
            continue
        elif position[coordinates[0]][coordinates[1]] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            position[coordinates[0]][coordinates[1]] = player

        show_field()
        turn_counter += 1

        if position[0][0] == position[1][1] == position[2][2] == player:
            return print(f"{player} wins")
        elif position[0][2] == position[1][1] == position[2][0] == player:
            return print(f"{player} wins")
        for i in range(3):
            if position[i][0] == position[i][1] == position[i][2] == player:
                return print(f"{player} wins")
            elif position[0][i] == position[1][i] == position[2][i] == player:
                return print(f"{player} wins")

    return print("Draw")


position = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
show_field()
play()
