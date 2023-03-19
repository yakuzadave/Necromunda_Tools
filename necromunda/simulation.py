class CombatSimulator:
    def __init__(self, gangs):
        self.gangs = gangs

    def simulate_combat(self):
        results = {}
        for i, gang1 in enumerate(self.gangs[:-1]):
            for gang2 in self.gangs[i+1:]:
                result = self.fight(gang1, gang2)
                results[(gang1, gang2)] = result
        return results

    def fight(self, gang1, gang2):
        # Implement the logic for a single fight between two gangs
        # For now, let's return a random winner
        import random
        return random.choice([gang1, gang2])

