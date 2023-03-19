from necromunda.gang import Gang, Fighter
from necromunda.game import Game, Campaign
from necromunda.simulation import CombatSimulator

def main():
    # Create gangs, games, and a campaign
    gang1 = Gang("Gang 1", "Goliath")
    gang2 = Gang("Gang 2", "Escher")
    gang3 = Gang("Gang 3", "Orlock")

    fighter1 = Fighter("Fighter 1", {"M": 4, "WS": 3, "BS": 3, "S": 4, "T": 4, "W": 1, "I": 4, "A": 1, "Ld": 8}, [], [])
    fighter2 = Fighter("Fighter 2", {"M": 4, "WS": 3, "BS": 3, "S": 4, "T": 4, "W": 1, "I": 4, "A": 1, "Ld": 8}, [], [])

    gang1.add_fighter(fighter1)
    gang2.add_fighter(fighter2)

    game1 = Game([gang1, gang2, gang3])

    campaign = Campaign("Campaign 1")
    campaign.add_game(game1)

    # Run combat simulation
    simulator = CombatSimulator([gang1, gang2, gang3])
    results = simulator.simulate_combat()

    # Print the results
    for (g1, g2), winner in results.items():
        print(f"{g1.name} vs {g2.name}: Winner is {winner.name}")

if __name__ == "__main__":
    main()
