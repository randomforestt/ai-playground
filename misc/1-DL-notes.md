# TODO: Understand General Adversarial Network

1. [Stefan Hosein - Demystifying General Adversarial Nets (Data Camp)](https://datacamp.com/community/tutorials/generative-adversarial-networks)

2. [An intuitive introduction to Generative Adversarial Networks (Thalles Silva)](https://medium.freecodecamp.org/an-intuitive-introduction-to-generative-adversarial-networks-gans-7a2264a81394)

3. [Skymind: A Beginner's Guide to Generative Adversarial Networks (GANs)](https://skymind.ai/wiki/generative-adversarial-network-gan)

4. [Generative Adversarial Networks (GANs) - Computerphile - Rob Miles](https://www.youtube.com/watch?v=Sw9r8CL98N0&t=67s)

5. [Two Hour Lecture from Fast AI about GANS](http://course.fast.ai/lessons/lesson12.html)


# Autoencoders
- unsupervised machine learning algorithm.
- Trained to attempt to copy its input to its output
- Input is the same as output
- Takes data in some original (high-dimensional) space
- Project data into a new smaller dimension space (new representation) from which it can then be
relatively accurately restored.
- Dimensionality reduction, new representation, lower dimenstional representation of your input data
- Some features may be redundant or correlated, resulting in wasted processing time
and overfitting your model (too many parameters), ideal only to include features we need
- Compressed data (unsupervised)
- Internal Architecture:
```
Input --> encoder network ---> bottleneck --> decoder network ---> Output
```
- Bottleneck also called latent space representation or compressed feature vector
- Auto encoders work by compressing the input into a "latent-space representation" and then
reconstructs the output from this representation
- Data compression algorithm
- Somewhat like principal component analysis (PCA)
  - technique used to emphasize variation and bring out strong patterns in a dataset. It's often used to make data easy to explore and visualize.[Setosa.io PCA Explained Visually](http://setosa.io/ev/principal-component-analysis/)
- Properties:
  - Data Specific
    - only able to compress data similar to what they have been trained on
    - autoencoder trained on human faces wont perform well with images of modern buildings
    - MP3, JPG, ZIP are compression algorithms are better in their specific use cases
    - MP3 for example hold assumptions about sound in general not specific types of sound
  - Lossy
    - Decompressed outputs will be degrated compared to original inputs usually
- Example applications
  - Data denoising: map noisy images to clean images (remove noise)
  - dimensionality reduction
  - Semantic Segmentation
  - [Other examples can be use cases: Sky Mind Article](https://skymind.ai/wiki/deep-autoencoder)
- DAta specific learned compression
- a class of neural networks that can learn to compress data completely unsupervised

## [Autoencoder Tutorial Machine Learning With Keras](https://www.youtube.com/watch?v=uCaPP4blYAg)
- An simple example of an autoencoder in keras (video) by John G. Fisher

# [Variational Autoencoders - John G. Fisher](https://www.youtube.com/watch?v=9zKuYvjFFS8)
- Example: denoising auto encoder
  - dataset: Input: Original image + noise -> Output: Original Image
- Example: Neural Inpainting
  - data set: Original image - parts of image (replace with white pixels for example) -> Output: Original Image
  - You can remove watermarks in images!
  - Remove parked car
- Disentanged VAE
  - Example: Given a face, you can rotate it!
    - Change something on your latent space then the face is rotated but nothing else changes (same person!)
    - If you do the same in normal VAE the face rotates but also changes!
    - Goal: Have some kind of a network that can extract very useful causal features
      from a very high dimensional space then use those features for some task that it is trying to learn. And the hope is then that those learned features will also generalize
      to domains outside of your training data
      - Application to reinforcement learning: In the end we want to train agents that are able to understand the world by compressing a whole lot of information and then learning useful behavior on that latent space

# Deep-Belief Networks
-A stack of "restricted boltamann machines (RBM)"  in which each RBM eachlayer communicates with both the previous and subsequent layers. The nodes of any single layer don’t communicate with each other laterally.
## [Sky Mind Article has links to other resources about RBMs](https://skymind.ai/wiki/restricted-boltzmann-machine)


# Inceptionism
- Inceptionism is an attempt to make neural networks give up their secrets by showing us what they see. It creates some amazing artwork along the way.

# TODO: READ

- [Conv Nets: A Modular Perspective](http://colah.github.io/posts/2014-07-Conv-Nets-Modular/)
- [Exploring Models and Data for Image Question
Answering](https://arxiv.org/pdf/1505.02074.pdf)
