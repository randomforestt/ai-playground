# Towards Evaluating the Robustness of Neural Networks 22 March 2017
- demonstrate that defensive distillation does not significantly increase the robustness of neural networks by introducing three new attack algorithms that are successful on both distilled and undistilled neural networks with 100 %probability
- We evaluate our attacks on three standard datasets: MNIST, a digit-recognition task (0-9); CIFAR-10, a small-image recognition task, also with 10 classes; and ImageNet, a large-image recognition task with 1000 classes.
- one extreme example for the ImageNet classification task, we can cause the Inception v3 [45] network to incorrectly classify images by changing only the lowest order bit of each pixel. Such changes are impossible to detect visually.
- http://nicholas.carlini.com/code/nn_robust_attacks
- introduce three new attacks for the
- L0, L2, and L∞  distance metrics. Our attacks are significantly more effective than previous approaches. Our L0 attack is the first published attack that can cause targeted misclassification on the ImageNet dataset.
- Propose using high-confidence adversarial examples in a simple transferability test to evaluate defenses, and show this test breaks defensive distillation.
- We systematically evaluate the choice of the objective function for finding adversarial examples, and show that the choice can dramatically impact the efficacy of an attack.
```
Therefore, any defense that is able to provide robustness against adversarial examples must
somehow break this transferabilityproperty; otherwise, we could run our attack algorithm on 
an easy-to-attack model, and then transfer those adversarial examples to the hard-to-attack model.

Even though defensive distillation is not robust to our stronger attacks, we demonstrate a 
second break of distillation by transferring attacks from a standard model to a defensively distilled model.

We accomplish this by finding high-confidence adversarial examples, which we define as adversarial examples 
that are strongly misclassified by the original model. Instead of looking for an adversarial example that 
just barely changes the classification from the source to the target, we want one where the target is much 
more likely than any other label.
```

# The Limitations of Deep Learning in Adversarial Settings - 2015
- Introduces a class of algorithms to craft adversarial samples
based on the mapping between the output and inputs of DNN
- This algorithm applied to computer vision (handwritten digits)
can reliably produce samples correctly classified by human subjects but misclassified in specific targets by a DNN with a 97% adversarial success rate while only modifying on average 4.02% of the input features per sample
- Algorithm: You need knowledge of architecture (weights, and biases), to build
a saliency map to know which inputs has a significant impact to the output when perturbed


# Interesting To Check out

##  Malware Detection:
- G. E. Dahl, J. W. Stokes, L. Deng, and D. Yu. Large-scale malware classification using random projections and neural networks. In Acoustics, Speech and Signal Processing (ICASSP), 2013 IEEE International Conference on, pages 3422–3426. IEEE, 2013
- Grosse, K., Papernot, N., Manoharan, P., Backes, M., and McDaniel, P. Adversarial perturbations against deep neural networks for malware classification. arXiv preprint arXiv:1606.04435 (2016).
- entirely defeats its purpose: an adversary who is able to make only slight modifications to a malware file that cause it to remain malware, but become classified as benign, has entirely defeated the malware classifiaction

## Financial Fraud Detection
E. Knorr. How paypal beats the bad guys with machine learning. http://www.infoworld.com/article/2907877/machine-learning/how-paypal-reduces-fraud-with-machine-learning.html, 2015.

## Explore DNN properties that could be used to craft adversarial samples
- Simply put, these techniques exploit gradients computed by network training algorithms: instead of using these gradients to update network parameters as would normally be done, gradients are used to update the original input itself, which is subsequently misclassified by DNNs.
- I. J. Goodfellow, J. Shlens, and C. Szegedy. Explaining and harnessing adversarial examples. In Proceedings of the 2015 International Conference on Learning Representations. Computational and Biological Learning Society, 2015.
- A. Nguyen, J. Yosinski, and J. Clune. Deep neural networks are easily fooled: High confidence predictions for unrecognizable images. In In Computer Vision and Pattern Recognition (CVPR 2015). IEEE, 2015.
- C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow, and R. Fergus. Intriguing properties of neural networks. In Proceedings of the 2014 International Conference on Learning Representations. Computational and Biological Learning Society, 2014.
- Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I., and Fergus, R. Intriguing properties of neural networks. ICLR (2013)

## It is possible to generate audio that sounds like speech to. machine learning algorithms but not to humans
- http://www.hiddenvoicecommands.com
- Carlini, N., Mishra, P., Vaidya, T., Zhang, Y., Sherr, M., Shields, C., Wagner, D., and Zhou, W. Hidden voice commands. In 25th USENIX Security Symposium (USENIX Security 16), Austin, TX (2016).
- Example: y playing a video with a hidden voice command, it may be possible to cause a smart phone to visit a malicious webpage to cause a drive-by download.

## adversarial examples are possible in the physical world
- Kurakin, A., Goodfellow, I., and Bengio, S. Adversarial examples in the physical world. arXiv preprint arXiv:1607.02533 (2016).

# Various attempts at constructing defenses that increase the robustness of a neural network defined as a measure of how easy it is to find adversarial examples that are close to their original input
- Gu, S., and Rigazio, L. Towards deep neural network architectures robust to adversarial examples. arXiv preprint arXiv:1412.5068 (2014)
- Bastani, O., Ioannou, Y., Lampropoulos, L., Vytiniotis, D., Nori, A., and Criminisi, A. Measuring neural net robustness with constraints. arXiv preprint arXiv:1605.07262 (2016).
- Bastani, O., Ioannou, Y., Lampropoulos, L., Vytiniotis, D., Nori, A., and Criminisi, A. Measuring neural net robustness with constraints. arXiv preprint arXiv:1605.07262 (2016).
- Shaham, U., Yamada, Y., and Negahban, S. Understanding adversarial training: Increasing local stability of neural nets through robust optimization. arXiv preprint arXiv:1511.05432 (2015).
- Papernot, N., McDaniel, P., Wu, X., Jha, S., and Swami, A. Distillation as a defense to adversarial perturbations against deep neural networks. IEEE Symposium on Security and Privacy (2016).

## The existence of adversarial examples has inspired research on how to harden neural networks against these kinds of attacks. Many early attempts to secure neural networks failed or provided only marginal robustness improvements
- Gu, S., and Rigazio, L. Towards deep neural network architectures robust to adversarial examples. arXiv preprint arXiv:1412.5068 (2014).
- Bastani, O., Ioannou, Y., Lampropoulos, L., Vytiniotis, D., Nori, A., and Criminisi, A. Measuring neural net robustness with constraints. arXiv preprint arXiv:1605.07262 (2016).
- Huang, R., Xu, B., Schuurmans, D., and Szepesvári, C. Learning with a strong adversary. CoRR, abs/1511.03034 (2015).
- Shaham, U., Yamada, Y., and Negahban, S. Understanding adversarial training: Increasing local stability of neural nets through robust optimization. arXiv preprint arXiv:1511.05432 (2015).


# Adversarial Examples

### Attacking Machine Learning with Adversarial Examples
  - https://blog.openai.com/adversarial-example-research/

### Robust Adversarial Examples - JULY 17, 2017
  - https://blog.openai.com/robust-adversarial-inputs/

### Adversarial Machine Learning Tutorial
  - https://aaai18adversarial.github.io/

### Hacking the Brain With Adversarial Images
  - Researchers from Google Brain show that adversarial images can trick both humans and computers, and the implications are scary
  - Eva Ackerman
  - https://spectrum.ieee.org/the-human-os/robotics/artificial-intelligence/hacking-the-brain-with-adversarial-images

### Slight Street Sign Modifications Can Completely Fool Machine Learning Algorithms
    - Minor changes to street sign graphics can fool machine learning algorithms into thinking the signs say something completely different
    - Eva Ackerman
    - https://spectrum.ieee.org/cars-that-think/transportation/sensors/slight-street-sign-modifications-can-fool-machine-learning-algorithms

### Intriguing properties of neural networks - last revised 19 Feb 2014
  - https://arxiv.org/pdf/1312.6199.pdf

### Practical Black-Box Attacks against Machine Learning - last revised 19 Mar 2017
  - https://arxiv.org/abs/1602.02697

### Robust Physical-World Attacks on Deep Learning Models last revised 10 Apr 2018
  - https://arxiv.org/abs/1707.08945

### Adversarial Attacks on Neural Network Policies
  - https://arxiv.org/abs/1702.02284

### 'How neural networks learn' - Part II: Adversarial Examples - Arxiv Insights
  - https://www.youtube.com/watch?v=4rFOkpI0Lcg

### Tricking Neural Networks: Create your own Adversarial Examples
10 Jan 2018 | Daniel Geng and Rishi Veerapaneni
 - https://ml.berkeley.edu/blog/2018/01/10/adversarial-examples/

### DELVING INTO TRANSFERABLE ADVERSARIAL EXAMPLES AND BLACK-BOX ATTACKS
 - https://arxiv.org/pdf/1611.02770.pdf

### The limitations of deep learning
 - https://blog.keras.io/the-limitations-of-deep-learning.html
 - https://blog.keras.io/the-future-of-deep-learning.html

### Cody Marie Wild: Know Your Adversary: Understanding Adversarial Examples
 - https://towardsdatascience.com/know-your-adversary-understanding-adversarial-examples-part-1-2-63af4c2f5830
 - https://towardsdatascience.com/the-modeler-strikes-back-defense-strategies-against-adversarial-attacks-9aae07b93d00

### The Deep Flaw In All Neural Networks
 - https://www.i-programmer.info/news/105-artificial-intelligence/8064-the-deep-flaw-in-all-neural-networks.html

### Ian Goodfellow, Research Scientist, Google - RE•WORK Deep Learning Summit 2015
 - https://www.youtube.com/watch?v=Pq4A2mPCB0Y


# Attack Algorithms

## Fast Gradient Sign and Iterative Gradient Sign
```
designed primarily to be fast instead of producing very close adversarial examples. 
Given an image x, the fast gradient sign method sets

x′ = x − ϵ⋅ sign (∇loss F,t(x))

where ϵ is chosen to be sufficiently small so as to be undetectable, 
and t is the target label.

Intuitively, for each pixel, the fast gradient sign method uses the gradient 
of the loss function to determine in which direction the pixel’s intensity should
be changed (whether it should be increased or decreased) to minimize the loss
function; then, it shifts all pixels simultaneously.

Kurakin et al. introduce a simple refinement of the fast gradient sign method
Iterative gradient sign was found to produce superior results to fast gradient sig

```
- Goodfellow, I. J., Shlens, J., and Szegedy, C. Explaining and harnessing adversarial examples. arXiv preprint arXiv:1412.6572 (2014).
- Kurakin, A., Goodfellow, I., and Bengio, S. Adversarial examples in the physical world. arXiv preprint arXiv:1607.02533 (2016).

# Jacobian-based Saliency Map Attack (JSMA).
```
At a high level, the attack is a greedy algorithm that picks pixels to
modify one at a time, increasing the target classification on each iteration. T
hey use the gradient

∇Z(x)l

to compute a saliency map, which models the impact each pixel has on the 
resulting classification. A large value indicates that changing it will significantly 
increase the likelihood of the model labeling the image as the target class l. Given the saliency map, 
it picks the most important pixel and modify it to increase the likelihood of class l
. This is repeated until either more than a set threshold of pixels are modified which
makes the attack detectable, or it succeeds in changing the classification.
```
- Papernot, N., McDaniel, P., Jha, S., Fredrikson, M., Celik, Z. B., and Swami, A. The limitations of deep learning in adversarial settings. In 2016 IEEE European Symposium on Security and Privacy (EuroS&P) (2016), IEEE, pp. 372–387.

## Deepfool
```
an untargeted attack technique optimized for the L2
 distance metric. It is efficient.

The authors construct Deepfool by imagining that the neural networks are totally linear, 
with a hyperplane separating each class from another. From this, they analytically derive 
the optimal solution to this simplified problem, and construct the adversarial example.

Then, since neural networks are not actually linear, they take a step towards 
that solution, and repeat the process a second time. The search terminates 
when a true adversarial example is found.

The exact formulation used is rather sophisticated; interested readers should refer to the original work .
```
- Moosavi-Dezfooli, S.-M., Fawzi, A., and Frossard, P. Deepfool: a simple and accurate method to fool deep neural networks. arXiv preprint arXiv:1511.04599 (2015).


# Defensive Distillation
- Papernot, N., McDaniel, P., Wu, X., Jha, S., and Swami, A. Distillation as a defense to adversarial perturbations against deep neural networks. IEEE Symposium on Security and Privacy (2016).
- Initial analysis proved to be very promising: defensive distillation defeats existing attack algorithms and reduces their success probability from  95% to 0.5 %
- One case study demonstrates that defensive distillation does not actually eliminate adversarial examples.
- https://www.arxiv-vanity.com/papers/1608.04644/
```
To defensively distill a neural network, begin by first training a network with identical
architecture on the training data in a standard manner. When we compute the softmax while
training this network, replace it with a more-smooth version of the softmax (by dividing the 
logits by some constant
T
). At the end of training, generate the soft training labels by evaluating this
network on each of the training instances and taking the output labels of the network.

Then, throw out the first network and use only the soft training labels. With those,
train a second network where instead of training it on the original training labels, 
use the soft labels. This trains the second model to behave like the first model, and t
he soft labels convey additional hidden knowledge learned by the first model.

The key insight here is that by training to match the first network, we will hopefully 
avoid over-fitting against any of the training data. If the reason that neural networks 
exist is because neural networks are highly non-linear and have “blind spots” [46] w
here adversarial examples lie, then preventing this type of over-fitting might remove those blind spots.

In fact, as we will see later, defensive distillation does not remove adversarial examples.
One potential reason this may occur is that others [11] have argued the reason adversarial 
examples exist is not due to blind spots in a highly non-linear neural network, 
but due only to the locally-linear nature of neural networks. This so-called linearity hypothesis 
appears to be true [47], and under this explanation it is perhaps less surprising that distillation 
does not increase the robustness of neural networks.

Distillation was initially proposed as an approach to reduce a large model (the teacher) 
down to a smaller distilled model [19]. At a high level, distillation works by first training 
the teacher model on the training set in a standard manner. Then, we use the teacher to label 
each instance in the training set with soft labels (the output vector from the teacher network). 
For example, while the hard label for an image of a hand-written digit 7
 will say it is classified as a seven, the soft labels might say it has a  80%
chance of being a seven and a 20% chance of being a one. Then, we train the distilled 
model on the soft labels from the teacher, rather than on the hard labels from the training set.
Distillation can potentially increase accuracy on the test set as well as the rate at which
the smaller model learns to predict the hard labels [19, 30].

Defensive distillation uses distillation in order to increase the robustness of a
neural network, but with two significant changes. First, both the teacher model and the 
distilled model are identical in size — defensive distillation does not result in smaller models.
Second, and more importantly, defensive distillation uses a large distillation temperature 
(described below) to force the distilled model to become more confident in its predictions.

Recall that, the softmax function is the last layer of a neural network. Defensive distillation 
modifies the softmax function to also include a temperature constant T:

Defensive distillation proceeds in four steps:

1. Train a network, the teacher network, by setting the temperature of the softmax to
T during the training phase.

2. Compute soft labels by apply the teacher network to each instance in the training set,
again evaluating the softmax at temperature T.

3. Train the distilled network (a network with the same shape as the teacher network) on the soft labels,
using softmax at temperature T.

4. Finally, when running the distilled network at test time (to classify new inputs), use temperature 1
.
```

## TRANSFERABILITY
## A Well-known property that adversarial examples on one model are often also adversarial on another model.
- Features are transferable between deep neural networks,
- Recent work has shown that an adversarial example for one model will often transfer to be an adversarial on a different model, even if they are trained on different sets of training data
- Any defense must demonstrate it is able to break the transferability property
- Adversarial samples can indeed be misclassified across models
```

- Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I., and Fergus, R. 
Intriguing properties of neural networks. ICLR (2013).

- Goodfellow, I. J., Shlens, J., and Szegedy, C. Explaining and harnessing adversarial examples. 
arXiv preprint arXiv:1412.6572 (2014).
C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow, and R. Fergus.

Intriguing properties of neural networks. 
In Proceedings of the 2014 International Conference on Learning Representations. 
Computational and Biological Learning Society, 2014.

Papernot, N., McDaniel, P., and Goodfellow, I. Transferability in machine learning: 
from phenomena to black-box attacks using adversarial samples.
arXiv preprint arXiv:1605.07277 (2016).

```

# To create defenses - perform two evaluation approaches
```
Use a powerful attack (such as the ones proposed in this paper) to evaluate the 
robustness of the secured model directly. Since a defense that prevents our 
L2 attack will prevent our other attacks, defenders should make sure to establish 
robustness against the L2 distance metric.

Demonstrate that transferability fails by constructing high-confidence adversarial
examples on a unsecured model and showing they fail to transfer to the secured model.
```
