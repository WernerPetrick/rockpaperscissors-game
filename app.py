from flask import Flask, render_template, request
import random

app = Flask(__name__)

standard_theme = ['Rock', 'Paper', 'Scissors']
elemental_theme = ['Fire', 'Water', 'Plant']
fantasy_theme = ['Wizard', 'Goblin', 'Dragon']

rock = {
    "title": "Rock",
    "enemy" : "Scissors",
    "weakness" : "Paper",
    "image" : "../static/assets/rock.jpg"
}

paper = {
    "title": "Paper",
    "enemy" : "Rock",
    "weakness" : "Scissors",
    "image" : "../static/assets/paper.jpg"
}

scissors = {
    "title": "Scissors",
    "enemy" : "Paper",
    "weakness" : "Rock",
    "image" : "../static/assets/scissors.jpg"
}

wizard = {
    "title": "Wizard",
    "enemy" : "Goblin",
    "weakness" : "Dragon",
    "image" : "../static/assets/wizard.jpg"
}

goblin = {
    "title": "Goblin",
    "enemy" : "Dragon",
    "weakness" : "Wizard",
    "image" : "../static/assets/goblin.jpg"
}

dragon = {
    "title": "Dragon",
    "enemy" : "Wizard",
    "weakness" : "Goblin",
    "image" : "../static/assets/dragon.jpg"
}

fire = {
    "title": "Fire",
    "enemy" : "Plant",
    "weakness" : "Water",
    "image" : "../static/assets/fire.jpg"
}

water = {
    "title": "Water",
    "enemy" : "Fire",
    "weakness" : "Plant",
    "image" : "../static/assets/water.jpg"
}

plant = {
    "title": "Plant",
    "enemy" : "Water",
    "weakness" : "Fire",
    "image" : "../static/assets/plant.jpg"
}

def computer_choice(current_theme):
    
    weapons = ['Rock', 'Paper', 'Scissors']
    
    print("Selected theme is: ", current_theme)
    
    if current_theme == 'standard':
        weapons = standard_theme
    elif current_theme == 'elemental':
        weapons = elemental_theme
    elif current_theme == 'fantasy':
        weapons = fantasy_theme
        
    pc_weapon_choice = random.choice(weapons)
    
    return pc_weapon_choice

@app.route("/", methods=['GET','POST'])
def index():
    
    return render_template("index.html")


@app.route("/user_choice", methods=['POST'])
def user_choice():
    
    incoming_data = request.form.to_dict()
    selected_weapon = incoming_data.get('selected_weapon')

    selected_theme = request.form.get("theme")
    pc_weapon = computer_choice(selected_theme)
    victorious = 0
    
    if selected_weapon == pc_weapon:
        victorious = None
    elif selected_weapon == 'Rock' and pc_weapon == 'Scissors':
        victorious = True
    elif selected_weapon == 'Paper' and pc_weapon == 'Rock':
        victorious = True
    elif selected_weapon == 'Scissors' and pc_weapon == 'Paper':
        victorious = True
    elif selected_weapon == 'Rock' and pc_weapon == 'Paper':
        victorious = False
    elif selected_weapon == 'Paper' and pc_weapon == 'Scissors':
        victorious = False
    elif selected_weapon == 'Scissors' and pc_weapon == 'Rock':
        victorious = False
    else:
        victorious = None
    
    return render_template("results.html", user_choice = selected_weapon, pc_choice = pc_weapon, win_condition = victorious)

@app.route("/theme_changer", methods=['POST'])
def theme_changer():
    selected_theme = request.form.get("theme")
    
    if selected_theme == 'elemental':
        return render_template("game-type.html",
            first_character=fire["title"], first_enemy=fire["enemy"], first_weakness=fire["weakness"], first_image=fire["image"],
            second_character=water["title"], second_enemy=water["enemy"], second_weakness=water["weakness"], second_image=water["image"],
            third_character=plant["title"], third_enemy=plant["enemy"], third_weakness=plant["weakness"], third_image=plant["image"]
        )
    elif selected_theme == 'fantasy':
        return render_template("game-type.html",
            first_character=wizard["title"], first_enemy=wizard["enemy"], first_weakness=wizard["weakness"], first_image=wizard["image"],
            second_character=goblin["title"], second_enemy=goblin["enemy"], second_weakness=goblin["weakness"], second_image=goblin["image"],
            third_character=dragon["title"], third_enemy=dragon["enemy"], third_weakness=dragon["weakness"], third_image=dragon["image"]
        )
    else:
        return render_template("game-type.html",
            first_character=rock["title"], first_enemy=rock["enemy"], first_weakness=rock["weakness"], first_image=rock["image"],
            second_character=paper["title"], second_enemy=paper["enemy"], second_weakness=paper["weakness"], second_image=paper["image"],
            third_character=scissors["title"], third_enemy=scissors["enemy"], third_weakness=scissors["weakness"], third_image=scissors["image"]
        )

if __name__ == "__main__":
    app.run(debug=True)
