# Lesson 23

## Intro to Recurrent Neural Networks

Problem of predicting next character in a sequence

Hidden layer input is both the input at the given timestep and the hidden layer 
input at a previous timestep (can be composed of all previous states). Compare 
to feed-forward networks

### LSTMs

LSTM cell,

* Forget gate
* Update state
* Cell state to hidden output

Fixes gradient problem for RNNs

### RNN Resources

Here are a few great resources for you to learn more about recurrent neural networks. We'll also continue to cover RNNs over the coming weeks.

* [Andrej Karpathy's lecture](https://www.youtube.com/watch?v=iX5V1WpxxkY) on RNNs and LSTMs from CS231n
* [A great blog post](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) by Christopher Olah on how LSTMs work.
* [Building an RNN](http://r2rt.com/recurrent-neural-networks-in-tensorflow-i.html) from the ground up, this is a little more advanced, but has an implementation in TensorFlow.

### Char RNN

