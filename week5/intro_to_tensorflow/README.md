# Introduction to Tensor Flow

## Hello, Tensor World!

TensorFlow's API is built around the idea of a computational graph.

A "TensorFlow Session" is an environment for running a graph. The session is in 
charge of allocating the operatiosn to GPUs/CPUs

## TensorFlow Math

[TensorFlow math](https://www.tensorflow.org/api_guides/python/math_ops)

## Minising Cross Entropy

Find loss: average cross-entropy across training set, want to minimise this

Minimisation with gradient descent

## Normalized Inputs And Initial Weights

Well conditioned problem makes it easy for optimiser to proceed

* Weight initialisation: Generate weights from Gaussian distribution, start with 
small sigma to begin with

* initialisation of the logic classifier

* Optimisation, through gradient descent

## Measuring Performance

Verification: use a small subset of training data to check classifier, have 
completely separate test set

## Stochastic Gradient Descent

Gradient descent does not scale well due to loss function

Compute average loss for random subset of training data - have to take more 
frequent, but smaller steps "Stochastic Gradient Descent"

SGD has lots of issues in practice

## Momentum And Learning Rate Decay

Helping SGD

* Inputs, mean = 0
* Equal variance (small)

Initial weights

* Random
* Mean = 0
* Equal variance (small)

Momentum: keep running average of gradient

Learning rate decay: learning rate should decrease over time

## Parameter Hyperspace

How quick you learn (i.e. learning rate) does not indicate how well you learn, 
a higher learning rate may plateau earlier than a slower learning rate for the 
same data

SGD "Black Magic" lots of hyper-parameters

Remember: Keep calm and lower your learning rate

ADAGRAD: Modification of SGD

## Mini-batching

Mini-batching is a technique for training on subsets of the dataset instead of 
all the data at one time. This provides the ability to train a model, even if a 
computer lacks the memory to store the entire dataset.

Mini-batching is computationally inefficient, since you can't calculate the loss 
simultaneously across all samples. However, this is a small price to pay in 
order to be able to run the model at all.

It's also quite useful combined with SGD. The idea is to randomly shuffle the 
data at the start of each epoch, then create the mini-batches. For each 
mini-batch, you train the network weights with gradient descent. Since these 
batches are random, you're performing SGD with each batch.

## Epochs

An epoch is a single forward and backward pass of the whole dataset. This is 
used to increase the accuracy of the model without requiring more data.
