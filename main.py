from models.ai_model import train_model, load_model
from consensus.bft import AIEnhancedBFT, simulate_consensus

def main():
    # Train or load the AI model
    model = train_model()  # Or load_model() if the model is pre-trained
    
    # Define the nodes participating in consensus
    nodes = [
        {'id': 1, 'features': [99, 0, 10, 100], 'stake': 100},
        {'id': 2, 'features': [50, 10, 100, 50], 'stake': 50},
        {'id': 3, 'features': [90, 1, 15, 200], 'stake': 200},
        {'id': 4, 'features': [20, 20, 200, 10], 'stake': 10},
    ]
    
    # Initialize BFT with AI model
    bft = AIEnhancedBFT(nodes, model)
    leader = bft.select_leader()

    # Simulate the consensus process
    simulate_consensus(nodes, leader)

if __name__ == "__main__":
    main()
