from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define the tier dictionary
tier_dict = {
    "The Hellfire Hellborne": "S",
    "The Summoned Hellborne": "S",
    "The Exalted Hellborne": "S",
    "The Surging Hellborne": "S",
    "The Exalted Hordes": "A",
    "The Surging Elite": "A",
    "The Exalted Elite": "A",
    "The Burning Rain": "A",
    "The Unstoppable Elite": "A",
    "The Invigorating Hellborne": "B",
    "The Draining Spires": "B",
    "The Exalted Council": "B",
    "The Wanderer Enfeebled": "B",
    "The Wanderer Exhausted": "B",
    "The Wanderer Withered": "B",
    "The Aether Rush": "C",
    "The Teeming Masses": "C",
    "The Bursting Masses": "C",
    "The Stalking Devil": "C",
    "The Gorging Masses": "D",
    "The Insatiable Spires": "D",
    "The Corrupting Spires": "D",
    "The Bursting Fiends": "D",
}

tier_ranking = {"S": 1, "A": 2, "B": 3, "C": 4, "D": 5}

@app.route("/", methods=["GET", "POST"])
def index():
    best_choice = None
    choices = []

    if request.method == "POST":
        choice1 = request.form.get("choice1").strip()
        choice2 = request.form.get("choice2").strip()
        choice3 = request.form.get("choice3").strip()

        choices = [choice1, choice2, choice3]
        valid_choices = [c for c in choices if c in tier_dict]

        if valid_choices:
            best_choice = min(valid_choices, key=lambda c: tier_ranking[tier_dict[c]])

    return render_template("index.html", best_choice=best_choice, choices=choices)

@app.route("/suggestions", methods=["GET"])
def suggestions():
    query = request.args.get("query", "").lower()
    suggestions = [choice for choice in tier_dict if choice.lower().startswith(query)]
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(debug=True)
    
