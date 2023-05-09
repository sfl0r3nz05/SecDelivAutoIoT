"""
import socket
from flask import Flask,jsonify
app_port = 5000

# Get Hostname
hostname = socket.gethostname()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        msg="Hello there, this is a test, You have just hit the container: "+ hostname+ " on port: "+str(app_port)
    )
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(app_port), debug=True)
	
"""
# Rock, Paper and Scissors Game with Python
import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break
