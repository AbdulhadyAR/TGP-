class Character:
    def __init__(self, name, level=1, max_health=100, power=10):
        self.name = name
        self.level = level
        self.max_health = max_health
        self.health = max_health
        self.power = power

    def attack(self, target):
        """Basic attack reduces target's health."""
        print(f"{self.name} attacks {target.name} for {self.power} damage!")
        target.take_damage(self.power)

    def take_damage(self, amount):
        """Reduce health but not below zero."""
        self.health = max(0, self.health - amount)
        print(f"{self.name} takes {amount} damage! (Health: {self.health}/{self.max_health})")

    def level_up(self):
        """Increase level, power, and health."""
        self.level += 1
        self.max_health += 20
        self.power += 5
        self.health = self.max_health
        print(f"{self.name} leveled up! Level: {self.level}, Health: {self.max_health}, Power: {self.power}")

    def get_status(self):
        """Display current stats."""
        return f"{self.name} | Level: {self.level} | Health: {self.health}/{self.max_health} | Power: {self.power}"


class Warrior(Character):
    def __init__(self, name, level=1, max_health=120, power=12, max_rage=100):
        super().__init__(name, level, max_health, power)
        self.rage = 0
        self.max_rage = max_rage

    def attack(self, target):
        """Warrior attack builds rage."""
        super().attack(target)
        self.rage = min(self.max_rage, self.rage + 15)
        print(f"{self.name} builds rage! (Rage: {self.rage}/{self.max_rage})")

    def power_smash(self, target):
        """Special attack that consumes rage."""
        if self.rage >= 50:
            damage = self.power * 2
            self.rage -= 50
            print(f"{self.name} uses Power Smash on {target.name} for {damage} damage!")
            target.take_damage(damage)
        else:
            print(f"{self.name} doesn’t have enough rage for Power Smash! ({self.rage}/{self.max_rage})")

    def get_status(self):
        base_status = super().get_status()
        return f"{base_status} | Rage: {self.rage}/{self.max_rage}"


class Mage(Character):
    def __init__(self, name, level=1, max_health=80, power=8, max_mana=120):
        super().__init__(name, level, max_health, power)
        self.mana = max_mana
        self.max_mana = max_mana

    def cast_spell(self, target):
        """Mages cast powerful spells that cost mana."""
        mana_cost = 30
        if self.mana >= mana_cost:
            damage = self.power * 3
            self.mana -= mana_cost
            print(f"{self.name} casts a spell on {target.name} for {damage} damage! ({self.mana}/{self.max_mana} mana left)")
            target.take_damage(damage)
        else:
            print(f"{self.name} doesn’t have enough mana to cast a spell! ({self.mana}/{self.max_mana})")

    def meditate(self):
        """Restore mana."""
        restored = 25
        self.mana = min(self.max_mana, self.mana + restored)
        print(f"{self.name} meditates and restores mana. ({self.mana}/{self.max_mana})")

    def get_status(self):
        base_status = super().get_status()
        return f"{base_status} | Mana: {self.mana}/{self.max_mana}"
