import pytest
from models.ai_model import train_model

def test_model_training():
    model = train_model()
    assert model is not None, "Model training failed!"
