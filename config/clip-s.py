import ml_collections
import imp
import os

# Import the base configuration
base = imp.load_source("base", os.path.join(os.path.dirname(__file__), "base.py"))

def get_config():
    config = base.get_config()

    # Use the new reward function
    config.reward_fn = "clip_score"

    return config
