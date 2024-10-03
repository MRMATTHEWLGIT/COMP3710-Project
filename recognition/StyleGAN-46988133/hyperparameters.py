"""
hyperparameters.py created by Matthew Lockett 46988133
"""
# The root directory for where the ADNI dataset is stored
# See torchvision ImageFolder class for the required dataset structure 
ROOT = r"C:\Users\Mathew\AD_NC"

# The IMAGE_SIZExIMAGE_SIZE pixel dimension of the images loaded into the model
IMAGE_SIZE = 256

# The number of channels of the images loaded into the model (1 = Greyscale)
NUM_CHANNELS = 1

# The total number of images trained on the model at any given time
BATCH_SIZE = 128