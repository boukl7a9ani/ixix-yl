import folium
import random
import webbrowser

# List of monuments with their descriptions, locations, and coordinates
monuments = {
    "Eiffel Tower": {
        "description": "La Tour Eiffel est une grande tour métallique située à Paris, France. Elle est un symbole mondial de la France.",
        "location": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris",
        "coordinates": (48.8584, 2.2945)
    },
    "Louvre Museum": {
        "description": "Le musée du Louvre est le plus grand musée d'art du monde et un monument emblématique de Paris.",
        "location": "Rue de Rivoli, 75001 Paris",
        "coordinates": (48.8606, 2.3376)
    },
    "Notre-Dame Cathedral": {
        "description": "La cathédrale Notre-Dame de Paris est une cathédrale gothique située sur l'île de la Cité.",
        "location": "6 Parvis Notre-Dame - Pl. Jean-Paul II, 75004 Paris",
        "coordinates": (48.8529, 2.3500)
    },
    "Sacré-Cœur Basilica": {
        "description": "La basilique du Sacré-Cœur est une église située au sommet de la colline de Montmartre.",
        "location": "35 Rue du Chevalier de la Barre, 75018 Paris",
        "coordinates": (48.8867, 2.3431)
    },
    "Arc de Triomphe": {
        "description": "L'Arc de Triomphe est un monument historique situé sur la place Charles de Gaulle, à l'extrémité ouest des Champs-Élysées.",
        "location": "Place Charles de Gaulle, 75008 Paris",
        "coordinates": (48.8738, 2.2950)
    }
}

# Function to ask trivia questions
def ask_trivia_question(monument):
    correct_answer = monument
    other_choices = random.sample([m for m in monuments.keys() if m != correct_answer], 3)
    choices = random.sample([correct_answer] + other_choices, 4)
    
    print(f"Quel monument est situé à l'adresse suivante : {monuments[monument]['location']} ?")
    
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    
    try:
        answer = int(input("Entrez le numéro de votre réponse : "))
        if choices[answer - 1] == correct_answer:
            print("Bonne réponse !\n")
        else:
            print(f"Mauvaise réponse ! La bonne réponse était {correct_answer}.\n")
    except (ValueError, IndexError):
        print("Réponse invalide. Veuillez entrer un numéro valide.\n")

# Function to display the monument information
def display_monuments():
    print("Bienvenue à Paris! Voici les monuments que vous pouvez explorer :")
    for idx, monument in enumerate(monuments.keys(), 1):
        print(f"{idx}. {monument}")
    
# Function to get monument details
def get_monument_info(choice):
    monument_name = list(monuments.keys())[choice - 1]
    info = monuments[monument_name]
    print(f"\nMonument: {monument_name}")
    print(f"Description: {info['description']}")
    print(f"Emplacement: {info['location']}")
    print(f"Coordonnées géographiques: {info['coordinates']}\n")
    
    # Show the map of the monument
    show_map(monument_name)

# Function to show the map with the monument location
def show_map(monument_name):
    location = monuments[monument_name]['coordinates']
    monument_map = folium.Map(location=location, zoom_start=15)
    folium.Marker(location, popup=monument_name).add_to(monument_map)
    
    # Save the map to an HTML file and open it in the browser
    map_filename = f"{monument_name.replace(' ', '_')}_map.html"
    monument_map.save(map_filename)
    webbrowser.open(map_filename)

# Main game loop
def play_game():
    while True:
        display_monuments()
        try:
            choice = int(input("Choisissez un monument (1-5) ou entrez 0 pour quitter : "))
            if choice == 0:
                print("Merci d'avoir joué! À bientôt!")
                break
            elif 1 <= choice <= len(monuments):
                monument_name = list(monuments.keys())[choice - 1]
                get_monument_info(choice)
                # Ask a trivia question after showing the monument info
                ask_trivia_question(monument_name)
            else:
                print("Choix invalide. Essayez encore.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

# Start the game
if __name__ == "__main__":
    play_game()
