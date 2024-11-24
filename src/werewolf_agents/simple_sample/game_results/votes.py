import json

# Specify the filename
# file_name = 'game_results_1731184417_YP8.json'
# file_name = 'game_results_1731186938_xxC.json'
# file_name = 'game_results_1731196725_CLa.json'
# file_name = 'game_results_1731198135_3RV.json'
# file_name = 'game_results_1731198898_WQZ.json'
file_name = 'game_results_1731201895_wtK.json'

# Load the game data
# with open('/mnt/data/game_results_1731184417_YP8.json', 'r') as file:
with open('./'+file_name, 'r') as file:
    game_data = json.load(file)

# Function to find wolves
def find_wolves(player_roles):
    return [player for player, role in player_roles.items() if role == 'wolf']

# Function to get all votes cast by James
def votes_by_james(vote_history):
    james_votes = {}
    for round_number, votes in vote_history.items():
        james_vote = votes.get('James')
        if james_vote:
            james_votes[round_number] = james_vote
    return james_votes

# Function to evaluate James's accuracy in identifying wolves
def evaluate_james_accuracy(james_votes, wolves):
    correct_guesses = sum(1 for vote in james_votes.values() if vote in wolves)
    total_votes = len(james_votes)
    accuracy = (correct_guesses / total_votes) * 100 if total_votes > 0 else 0
    return accuracy

# Extract required data from JSON
player_roles = game_data['player_roles']
vote_history = game_data['success_game_stats']['vote_history']['alive_players_votes']
winner = game_data['success_game_stats']['winner']

# Process data
wolves = find_wolves(player_roles)
james_votes = votes_by_james(vote_history)
james_accuracy = evaluate_james_accuracy(james_votes, wolves)

# Print the results
print("Wolves in the game:", wolves)
print("Votes cast by James:", james_votes)
print(f"James's accuracy in identifying wolves: {james_accuracy:.2f}%")
print("Who won the game:", winner)

output_file = file_name + '.out'
          
# Write the results to a file
with open(output_file, 'w') as file:
    file.write(f"Wolves in the game: {wolves}\n")
    file.write(f"Votes cast by James: {james_votes}\n")
    file.write(f"James's accuracy in identifying wolves: {james_accuracy:.2f}%\n")
    file.write(f"Who won the game: {winner}\n")

print("Results have been written to:", output_file)
