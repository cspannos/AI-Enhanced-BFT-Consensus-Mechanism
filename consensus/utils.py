import random

def simulate_consensus(nodes, leader):
    """Simple simulation of a consensus round."""
    if leader:
        print(f"Leader Node {leader['id']} proposes a block.")
        votes = [random.choice([True, False]) for _ in nodes]
        print(f"Votes: {votes}")
        if sum(votes) > len(nodes) / 2:
            print("Consensus reached!")
        else:
            print("Consensus failed.")
    else:
        print("No leader to propose a block.")
