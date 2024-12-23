# Number of past frames/actions we provide
# Beware that there's a hard limit coming from the dataset
BUFFER_SIZE = 9
# Given by the paper
ZERO_OUT_ACTION_CONDITIONING_PROB = 0.1

HEIGHT = 240
WIDTH = 320

# CFG ratio
CFG_GUIDANCE_SCALE = 1.5

# Default number of inference steps for diffusion
DEFAULT_NUM_INFERENCE_STEPS = 10

# Conditional Image noise parameters
# Those values are the same as in the paper
MAX_NOISE_LEVEL = 0.7
NUM_BUCKETS = 10

# Repo name for dumping model artifacts
REPO_NAME = "arnaudstiegler/sd-model-gameNgen"

# When not using frame conditioning, we use this prompt
VALIDATION_PROMPT = "video game doom image, high quality, 4k, high resolution"

# Datasets
TRAINING_DATASET_DICT = {
    "small": "arnaudstiegler/vizdoom-episode",
    "large": "arnaudstiegler/vizdoom-episode-large",
}

# Model Architecture
MODEL_PRETRAINED_PATH = "CompVis/stable-diffusion-v1-4"
ACTION_EMBEDDING_DIM = 768
CONV_KERNEL_SIZE = (3, 3)
CONV_STRIDE = (1, 1)
CONV_PADDING = (1, 1)
UNET_CHANNELS = 320

# Training Parameters
VALIDATION_INFERENCE_STEPS = 30
DEFAULT_TRAIN_BATCH_SIZE = 12
DEFAULT_NUM_TRAIN_EPOCHS = 2
DEFAULT_LEARNING_RATE = 2e-5
DEFAULT_LR_WARMUP_STEPS = 500

# Image Processing
IMG_INTERPOLATION = "bilinear"
IMG_NORMALIZATION_MEAN = [0.5]
IMG_NORMALIZATION_STD = [0.5]
