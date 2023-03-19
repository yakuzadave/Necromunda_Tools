class Fighter:
    def __init__(self, name, stats, equipment, skills):
        self.name = name
        self.stats = stats
        self.equipment = equipment
        self.skills = skills

    def update_stat(self, stat, value):
        if stat in self.stats:
            self.stats[stat] = value
        else:
            raise ValueError(f"Stat '{stat}' not found.")

    def add_stat(self, stat, value):
        if stat not in self.stats:
            self.stats[stat] = value
        else:
            raise ValueError(f"Stat '{stat}' already exists.")

    def update_equipment(self, old_item, new_item):
        try:
            index = self.equipment.index(old_item)
            self.equipment[index] = new_item
        except ValueError:
            raise ValueError(f"Equipment '{old_item}' not found.")

    def add_equipment(self, item):
        if item not in self.equipment:
            self.equipment.append(item)
        else:
            raise ValueError(f"Equipment '{item}' already exists.")

    def remove_equipment(self, item):
        try:
            self.equipment.remove(item)
        except ValueError:
            raise ValueError(f"Equipment '{item}' not found.")

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
        else:
            raise ValueError(f"Skill '{skill}' already exists.")

    def remove_skill(self, skill):
        try:
            self.skills.remove(skill)
        except ValueError:
            raise ValueError(f"Skill '{skill}' not found.")



class Gang:
    def __init__(self, name, faction, fighters=None):
        self.name = name
        self.faction = faction
        self.fighters = fighters or []

    def add_fighter(self, fighter):
        self.fighters.append(fighter)

    def remove_fighter(self, fighter):
        self.fighters.remove(fighter)
