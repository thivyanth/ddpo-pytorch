import ml_collections
import imp
import os

# Import clip-s configuration
clip_s = imp.load_source("clip_s", os.path.join(os.path.dirname(__file__), "clip-s.py"))

def get_config():
    config = clip_s.get_config()

    # Change the pretrained model if needed
    config.pretrained.model = "runwayml/stable-diffusion-v1-5"

    # Reduce number of epochs for faster training
    config.num_epochs = 10
    config.use_lora = True
    config.save_freq = 1
    config.num_checkpoint_limit = 5

    # Reduce batch size and number of batches per epoch to fit laptop GPU memory
    config.sample.batch_size = 1
    config.sample.num_batches_per_epoch = 1

    # Reduce training batch size and gradient accumulation steps for faster training
    config.train.batch_size = 1
    config.train.gradient_accumulation_steps = 1

    # Prompting
    config.prompt_fn = "imagenet_animals"
    config.prompt_fn_kwargs = {}

    # Use the new reward function
    config.reward_fn = "clip_score"

    # Per-prompt stat tracking
    config.per_prompt_stat_tracking = {
        "buffer_size": 16,
        "min_count": 16,
    }

    return config
