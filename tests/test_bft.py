import pytest
from consensus.bft import AIEnhancedBFT
from models.ai_model import train_model

def test_leader_selection():
    model = train_model()
    nodes = [
        {'id': 1, 'features': [99, 0, 10, 100], 'stake': 100},
        {'id': 2, 'features': [50, 10, 100, 50], 'stake': 50},
    ]
    bft = AIEnhancedBFT(nodes, model)
    leader = bft.select_leader()
    assert leader['id'] == 1, "Leader selection failed!"
