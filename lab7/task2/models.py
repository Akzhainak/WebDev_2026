class Character:
    def __init__(self, name, quality, weapon, region):
        self.name = name
        self.quality = quality
        #self.element = element
        self.weapon = weapon
        self.region = region

    def get_action(self):
        return f"{self.name} is exploring the world of Teyvat."

    def __str__(self):
        return (f"Character: {self.name}\n"
                f"Quality: {'*' * self.quality}\n"
                #f"Element: {self.element}\n"
                f"Weapon: {self.weapon}\n"
                f"Region: {self.region}")

class PlayableCharacter(Character):
    def __init__(self, name, quality,  weapon, region, banner_type):
        super().__init__(name, quality,  weapon, region)
        self.banner_type = banner_type

    def get_action(self):
        return f"{self.name} uses stamina to sprint and attack!"

    def check_banner(self):
        return f"This character is available in the {self.banner_type} banner."

class Boss(Character):
    def __init__(self, name,  region, drops):
        super().__init__(name, 5,  "Universal", region)
        self.drops = drops

    def get_action(self):
        return f"{self.name} enters the rage phase and uses an ultimate ability!"

    def get_drops(self):
        return f"Rewards for defeating {self.name}: {', '.join(self.drops)}"