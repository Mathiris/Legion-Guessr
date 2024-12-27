import csv
import random
from flask import Flask, render_template

app = Flask(__name__)

def load_personalities():
    """Charge toutes les personnalités depuis le fichier CSV."""
    with open('personnalites.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

# Charger toutes les personnalités au démarrage du serveur
all_personalities = load_personalities()

def get_random_person():
    global all_personalities
    """Renvoie une personnalité aléatoire qui n'a pas encore été devinée."""
    chosen_person = random.choice(all_personalities)
    all_personalities.remove(chosen_person)
    # Si toutes les personnalités ont été devinées, réinitialiser la liste
    if not all_personalities:
        all_personalities = load_personalities()
    return chosen_person

@app.route('/')
def index():
    person = get_random_person()
    full_name = f"{person['prenom']} {person['nom']}".strip()
    has_legion_honneur = person['a_legion_honneur'].lower() == 'true'

    return render_template('index.html', name=full_name, has_legion_honneur=has_legion_honneur)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
