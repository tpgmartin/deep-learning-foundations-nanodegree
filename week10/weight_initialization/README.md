# Lesson 32

## Weight Initialization

If all the weights are the same, all the gradient will be the same, and it will 
be difficult for the network to adjust weights once it has an output.

Instead pick unique random weights with a uniform distribution
Validation accuracy is much higher if weights between -1 and +1

General rule, pick weights between range 1/sqrt(n) where n is number of inputs 
to a given neuron

Normal distribution generally outperforms selecting weights randomly from a 
uniform distribution

Using truncated normal distribution has similar performance to regular normal 
distribution. In general better to use truncated normal to avoid selecting 
larger weights

### Additional Material

* [Understanding the difficulty of training deep feedforward neural networks](http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf)
* [Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification](https://arxiv.org/pdf/1502.01852v1.pdf)
* [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/pdf/1502.03167v2.pdf)
