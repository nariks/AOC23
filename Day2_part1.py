with open("input_day2.txt") as file:
    games = [game.rstrip().split(":") for game in file]

cubes_in_bag = {"red": 12, "green": 13, "blue": 14}
game_count = 0

for game in games:
    game_number = int(game[0].split()[1])
    game_runs = game[1].split(";")
    possible_candidate = []
    for game_run in game_runs:
        cubes = game_run.split(",")
        result = {}

        for cube in cubes:
            result[cube.strip().split()[1]] = int(cube.split()[0])

        possible_candidate.extend([result[color] <= cubes_in_bag[color] for color in result])

    if not (False in possible_candidate):
        game_count += game_number


print(game_count)
