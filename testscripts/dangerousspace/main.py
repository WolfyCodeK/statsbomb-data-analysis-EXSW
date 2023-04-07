import json

def load_json_data(json_data):
    data = []
    for game_data in json_data:
        data.append(json.loads(game_data))
    return data

def calculate_average_positions(data):
    total_positions = {}
    num_frames = len(data)

    for frame in data:
        for player in frame["homePlayers"] + frame["awayPlayers"]:
            player_id = player["playerId"]
            if player_id not in total_positions:
                total_positions[player_id] = {"xyz": [0, 0, 0], "count": 0}
            total_positions[player_id]["xyz"][0] += player["xyz"][0]
            total_positions[player_id]["xyz"][1] += player["xyz"][1]
            total_positions[player_id]["xyz"][2] += player["xyz"][2]
            total_positions[player_id]["count"] += 1

    average_positions = {}
    for player_id, player_data in total_positions.items():
        average_positions[player_id] = [
            coord / player_data["count"] for coord in player_data["xyz"]
        ]

    return average_positions

def main():
    json_data = [
        '{"period": 1, "frameIdx": 0, ...}',
        '{"period": 1, "frameIdx": 1, ...}',
        # ...
    ]

    data = load_json_data(json_data)
    average_positions = calculate_average_positions(data)

    for player_id, position in average_positions.items():
        print(f"Player {player_id} average position: {position}")

if __name__ == "__main__":
    main()
