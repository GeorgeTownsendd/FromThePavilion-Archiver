from flask import Flask, request, jsonify, render_template
import sqlite3
from PlayerTracker import PlayerTracker

app = Flask(__name__)

@app.route('/')
def index():
    # Render a simple form for entering the playerId
    return render_template('index.html')

@app.route('/get_player_skills', methods=['POST'])
def get_player_skills():
    player_id = request.form['playerId']
    player_tracker = PlayerTracker(player_id)

    player_details = {k: str(v) for k, v in player_tracker.permanent_attributes.items()}
    known_skills = list([int(x) for x in player_tracker.known_skills])
    estimate_spare = list([int(x) for x in player_tracker.estimate_spare])
    estimated_max_training = list([int(x) for x in player_tracker.estimate_max_training])

    return {
        'player_details': dict(player_details),
        'known_skills': known_skills,
        'estimated_spare': estimate_spare,
        'estimated_max_training': estimated_max_training
    }


if __name__ == '__main__':
    app.run(debug=True)

