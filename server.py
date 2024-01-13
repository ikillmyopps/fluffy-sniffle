# server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

leaderboard = []

@app.route('/get_leaderboard', methods=['GET'])
def get_leaderboard():
    return jsonify(leaderboard)

@app.route('/update_leaderboard', methods=['POST'])
def update_leaderboard():
    data = request.get_json()
    name = data['name']
    score = data['score']

    # Update or add the player in the leaderboard
    player_exists = False
    for player in leaderboard:
        if player['name'] == name:
            player['score'] = max(player['score'], score)
            player_exists = True

    if not player_exists:
        leaderboard.append({'name': name, 'score': score})

    # Sort the leaderboard by score
    leaderboard.sort(key=lambda x: x['score'], reverse=True)

    return jsonify(leaderboard)

if __name__ == '__main__':
    app.run(debug=True)
