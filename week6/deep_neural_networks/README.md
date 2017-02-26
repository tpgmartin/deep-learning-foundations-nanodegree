# Lesson 18 

## Deep Neural Networks

[TensorFlow examples](https://github.com/aymericdamien/TensorFlow-Examples)

### Save and Restore TensorFlow Models

[`tf.train.Saver`](https://www.tensorflow.org/api_docs/python/tf/train/Saver)

Since `tf.train.Saver.restore()` sets all the TensorFlow Variables, you don't 
need to call `tf.global_variables_initializer()`.

### Regularization

Early termination: prevent over-fitting

Regularization: L2 Regularization, add another term to loss function to 
penalizes large weights. Structure of network does not need to change.

L2 norm is just sum of squares of individual weights

### Dropout

Randomly remove fraction of data from activation - network forced to learn 
different redundant representation to make itself overall more robust

Average activation: zero out dropout activation, multiply remaining activations 
by two. This ensure remaining activation is properly scaled.

[Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)

[`tf.nn.dropout()`](https://www.tensorflow.org/api_docs/python/tf/nn/dropout)

During training, a good starting value for `keep_prob` is 0.5.

During testing, use a `keep_prob` value of 1.0 to keep all units and maximize 
the power of the model.