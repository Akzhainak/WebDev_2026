from models import Character, PlayableCharacter, Boss

def main():
    traveler = Character("Traveler", 5, "Adaptive", "Sword", "Unknown")
    kazuha = PlayableCharacter("Kazuha", 5, "Anemo", "Sword", "Inazuma", "Event")
    raiden_boss = Boss("Magatsu Mitake Narukami no Mikoto", "Electro", "Inazuma", 
                       ["Mudrah of the Malefic General", "Tears of the Calamitous God"])

    characters_list = [traveler, kazuha, raiden_boss]

    print("--- List Iteration and Polymorphism ---\n")
    for char in characters_list:
        print(f"Object: {char.name}")
        print(f"Action: {char.get_action()}")
        print("-" * 30)

    print("\n--- Unique Methods and __str__ ---")
    print(kazuha)
    print(kazuha.check_banner())
    
    print("\n" + raiden_boss.get_drops())

if __name__ == "__main__":
    main()