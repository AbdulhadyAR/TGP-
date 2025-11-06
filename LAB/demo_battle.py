
from characters import Character, Warrior, Mage

def main():
    # Create heroes
    arthur = Warrior("Arthur")
    merlin = Mage("Merlin")

    # Create a generic enemy
    goblin = Character("Goblin", level=1, max_health=60, power=6)

    print("\n=== Battle Start ===\n")

    arthur.attack(goblin)
    merlin.cast_spell(goblin)
    goblin.attack(arthur)

    arthur.power_smash(goblin)
    merlin.meditate()
    merlin.cast_spell(goblin)

    print("\n=== Status Check ===")
    print(arthur.get_status())
    print(merlin.get_status())
    print(goblin.get_status())


if __name__ == "__main__":
    main()
