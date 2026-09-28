def get_stat(prompt):
	"""Ask for a non-negative whole-number stat."""
	while True:
		try:
			value = int(input(prompt))
			if value >= 0:
				return value
			print("Please enter 0 or a positive number.")
		except ValueError:
			print("Please enter a whole number.")


def add_player(players):
	"""Create a player and record their first game's stats."""
	name = input("Player name: ").strip()
	if not name:
		print("Player name cannot be blank.")
		return

	player = {
		"name": name,
		"games": [],
	}
	players.append(player)
	print(f"Added {name}.")
	add_game_stats(player)


def add_game_stats(player):
	"""Record one game's stats for a player."""
	game = {
		"points": get_stat("Points: "),
		"rebounds": get_stat("Rebounds: "),
		"assists": get_stat("Assists: "),
	}
	player["games"].append(game)
	print(f"Added game stats for {player['name']}.")


def add_game(players):
	"""Choose a player and record another game's stats."""
	if not players:
		print("Add a player before entering game stats.")
		return

	print("\nChoose a player")
	for index, player in enumerate(players, start=1):
		print(f"{index}. {player['name']}")

	try:
		player_number = int(input("Player number: "))
		if player_number < 1 or player_number > len(players):
			print("Please choose a number from the list.")
			return
	except ValueError:
		print("Please enter a whole number.")
		return

	add_game_stats(players[player_number - 1])


def view_players(players):
	"""Display all players currently stored in this session."""
	if not players:
		print("No players have been added yet.")
		return

	print("\nPlayer averages")
	for player in players:
		games = player["games"]
		game_count = len(games)
		average_points = sum(game["points"] for game in games) / game_count
		average_rebounds = sum(game["rebounds"] for game in games) / game_count
		average_assists = sum(game["assists"] for game in games) / game_count
		print(f"{player['name']} ({game_count} games)")
		print(
			f"  Points: {average_points:.1f} | "
			f"Rebounds: {average_rebounds:.1f} | "
			f"Assists: {average_assists:.1f}"
		)


def main():
	"""Run the Basketball Stats Tracker menu."""
	players = []

	while True:
		print("\nBasketball Stats Tracker")
		print("1. Add a player")
		print("2. Add game stats for a player")
		print("3. View player averages")
		print("4. Exit")
		choice = input("Choose an option: ").strip()

		if choice == "1":
			add_player(players)
		elif choice == "2":
			add_game(players)
		elif choice == "3":
			view_players(players)
		elif choice == "4":
			print("Goodbye!")
			break
		else:
			print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
	main()

