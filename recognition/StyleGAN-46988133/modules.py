"""
modules.py created by Matthew Lockett 46988133
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import hyperparameters as hp

class MappingNetwork(nn.Module):
    """
    Within a StyleGAN model, the Mapping Network is used to transform a latent space vector z
    (a vector of random noise) into an intermediate latent vector w. The intermediate latent space
    vector is used to provide more control over the images features when compared to a normal GAN 
    model.

    REF: This class was inspired by code generated by ChatGPT-4o via the following prompt:
    REF: Prompt: Can you show me code for a StyleGan model and break down each section so that I can understand it?
    """
    
    def __init__(self):
        """
        An instance of the MappingNetwork StyleGAN model.
        """
        super(MappingNetwork, self).__init__()

        layers = []
        layers.append(PixelNorm())
        # For each layer complete a pass of one fully connected neural network and save
        for i in range(hp.MAPPING_LAYERS):
            layers.append(fully_connected(hp.LATENT_SIZE, hp.LATENT_SIZE))

        # Store all fully connected layers sequentially
        self.mapping = nn.Sequential(*layers)


    def forward(self, z):
        """
        Performs a forward pass on an input latent space vector, and turns it into
        an intermediate latent space vector w.
        
        Param: z: A latent space vector
        Return: The intermediate latent space vector w
        """
        return self.mapping(z)
    

def fully_connected(in_channels, out_channels):
    """
    Represents one fully connected layer of a standard neural network with leaky
    ReLu activations.

    Param: in_channels: The size of the input vector to this layer
    Param: out_channels: The size of the output vector this layer creates
    Return: A sequential model of one fully connected layer 
    REF: This function was inspired by code generated by ChatGPT-4o via the following prompt:
    REF: Prompt: Can you show me code for a StyleGan model and break down each section so that I can understand it?
    """
    return nn.Sequential(
        nn.Linear(in_channels, out_channels),
        nn.LeakyReLU(hp.LRELU_SLOPE_ANGLE)
    )

class PixelNorm(nn.Module):
    """
    Used to perform pixel normalisation on a vectorised image or latent space vector. The vector
    is normalised relative to it's own mean and variance.

    REF: This code was inspired by the following website:
    REF: https://blog.paperspace.com/implementation-stylegan-from-scratch/
    """

    def __init__(self):
        """
        An instance of the PixelNorm class.
        """
        super(PixelNorm, self).__init__()
        self.epsilon = hp.EPSILON # Used to avoid divison by zero

    def forward(self, x):
        """
        Normalises the input vector x, reltaive to it's own mean and variance. 

        Param: x: The input vector to be normalised.
        Return: A normalised output vector.
        """
        return x / torch.sqrt(torch.mean(x ** 2, dim=1, keepdim=True) + self.epsilon) 



