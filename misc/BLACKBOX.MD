# Practical Black-Box Attacks against Deep Learning Systems using Adversarial Examples
- March 2017

## Abstract

Strategy Attacked state-of-the-art deep neural networks (DNNs)

1. MetaMind of Salesforce
- misclassification rate of 84.24%
2. model hosted by Amazon
- misclassification rate: 96.19%
3. model hosted by Google
- misclassification rate: 88.94%

* misclassification rate: rate of misclassifying generated adversarial examples

- Black-box attack strategy is capable of evading defense stategies previously
found to make adversarial example crafting harder

## Introduction

### Assumption about Adversary:
- Adversary has no information about the structure or parameters of the DNN
- Does not have access to any large dataset used to train the DNN to be attacked
- Only capability is to observe labels assigned by DNN for chosen inputs
like an "oracle"

### Properties of blackbox attack
- limited to observing output class labels given input
- number of labels required is limited
- approach scales to different classifier types

### Disclosure
- The researchers discloses attacks to MetaMind, Amazon, Google,
No damage was caused as they demonstrated control of models created for
their own account.

## Threat Model
- TargetDNN (oracle) - multi-class DNN classifier - which outputs probability
of vectors where each vector component encodes the DNN's belief/ confidence
level of the input being part of the predefined classes
- For demonstration -> classify handwritten digits and traffic signs

### Adversarial Capabilities
- TargentDNN aka the Oracle
- Access to DNN's output probability label vector O'(x) for any input x
by querying the oricle.

### Adversarial Goal
- Produce minimally altered version of any input x, the adversarial sample,
misclassified by oracle o. Attack on oracle's output integrity
- Add minimal perturbation to evade human detection
- Finding minimal perturbation is not trivial

## Black-box Attack Strategy
- Learn a substitute DNN approximating the target using a dataset constructed with synthetic inputs and labels observed from the oracle (target network).
- Adversarial examples are then crafted using this substitue
- Adversarial examples transfer between architectures so we expect the target DNN to misclassify them
- To be able to train a substitute model without a real labeled dataset, we use the target DNN as an oracle to construct a synthetic data set.
- The inputs are synthetically generated and the outputs are labels observed from the oracle netowrk
- The attacker builds an approximation F of the model ) learned by the oracle
- The substitute network F is then used to craft adversarial samples misclassified by F.
- As long as the transferability property holds between F and O, the adversarial samples crafted for F will also be misclassified by O

###Two-fold strategy

1. Substitute Model Training: The attacker queries the oracle network 0 with synthetic inputs collected by "Jacobian-based heuristic" to build a model F approximating the model O's decision bounderies.

2. Adversarial Sample Crafting - the attacker uses substitue network F to craft adversarial samples, which are then misclassified by oracle O due to the transferability of adversarial samples

### Substitude model training

### Challenges

1. We will be selecting an architecture for substitute without knowledge of the targetd oracle's architecture

2. Limit number of queries made to the oracle,
so not suspicious

### Synthetic data technique
- To limit number of queries
- Sysnthetic data generation technique
= (Jacobian-based data augmentation)
- Technique is not designed to maximize the substitute
DNN's accuracy but rather to ensure that it approximates the oracle's decision boundaries with few label queries

### Substitute architecure
- Not the most limiting, because we have some partial knowledge of oracles input and output
- (input) -> images -> (convolution)
- (input) -> (text) -> RNN / LSTM
- (output) -> Classification

### Generating  Synthetic data set
- heuristic - based on identifying direction in which the model's output is varying around the initial set of training points around an initial set of training points.
- Augment the synthetic data tweaked given the identified direction
- "Jacobian based Data Augmentation"

# Substitute DNN Training Algorithm
- Initial collection using a small set of input reprensentation. If targetted oracle 0 classifies handwritten digits, adverary collects 10 images of each digit.

2. Architecture selection. Use high-level knowledge of classification task (convolutional neural networks, approprate for vision)

3. Substitute Training
```
Repeat iterably for more accurate substitute

1. Labeling
QUery label probability distribution
outputs given synthetic inputs
this becomes output training set

2. Training
Train architecutre using subsitute training set

3. Augmentation
Adversary applies augmentation techniqe
to produce larger subsitute training set
with more synthetic data points. This new training set better represents the model's decision boundaries

```

# Adversarial Sample Crafting
1. goodfellow algorithm - fast gradient sign method
- Fast
2. papernot algorithm
- source-target misclassification attacks
- Adversaries seek to take samples from any legitimate source to any chosen target class
- Choose input components forming some perturbation
in the direction of target value
- Reduced perturbation than goodfellow algorithm
- Greater computing cost than goodfellow algorithm

# Validation of the attack

- Metamind DNN, Minsit, 84.24% misclassfied adversarial examples
- German traffic signs 64.24% misclassfied adversarial examples




# Metrics of Adversarial Sample Crafting
- Success rate: proportion of  adversarial samples
misclassified by substitute DNN
- Goal is to verify whether these samples are misclassified by oracle or not
- Transferability of adversarial samples refers to the oracle misclassifcation rate of the adversarial sample crafted using the substitute DNN

# Calibration
- Substitute DNN architecture (number of layes, size, activation function, type) has limited impact on adversarial sample transferability,
- Increasing the number of epochs, after the substitute DNN has reached an asymptotic accuracy, does not improve adversarial sample transferability.
- At comparable input perturbation magnitude, the Goodfellow and Papernot algorithms have similar transferability rates


# Reducing Oracle Querying
- reservoir sampling
- J. S. Vitter, “Random sampling with a reservoir,” ACM Transactions on Mathematical Software (TOMS), vol. 11, no. 1, pp. 37–57, 1985.
- Reservoir sampling is a class of algorithms that randomly select κ samples from a list of samples.
- e use reservoir sampling to select a limited number of new inputs κ when performing a Jacobian-based dataset augmentation

# Results
```
Metamind Oracle attack
- 60k training , and 10k test images handwritten
- 28x28
- Uploaded 50k samples
- Handgrafted 100 samples

-  Instead of learning a substitute DNN with optimal accuracy, the adversary is interested in learning a substitute capable of mimicking the oracle decision boundaries.

 - 43 traffic signs
 - 35k training images, 4k for validation set
 - 10k for test set

Amazon oracle: To train a classifier on Amazon Machine Learning,6, we uploaded a CSV version of the MNIST dataset to a S3 bucket. We then loaded the data, selected the multi-class model type, and keept default configuration settings. The process took a few minutes and produced a classifier achieving a  92.17 %
 test set accuracy. We cannot improve the accuracy due to the automated nature of training. We then activate real-time predictions to query the model for labels from our machine with the provided API. Although probabilities are returned, we discard them and retain only the most likely label—as stated in our threat model (Section 3).

Google oracle: The procedure to train a classifier on Google’s Cloud Prediction API7 is similar to Amazon’s. We upload the CSV file with the MNIST training data to Google Cloud Storage. We then train a model using the Prediction API. The only property we can specify is the expected multi-class nature of our model. We then evaluate the resulting model on the MNIST test set. The API reports an accuracy of 92%  on this test set for the model trained
```

# Other info
```
The only limitation on the substitute is that it must implement a differentiable function, to allow for synthetic data generation with the Jacobian. The attack does not either make any assumption about the target oracle: for instance, the oracle does not necessarily have to be differentiable.
```
