# Lesson 19

## Convolutional Networks

### Intuition

For a given image, split levels of detail layer by layer.

Convolutional neural network (CNN) will be composed of separate layers, each 
layer might capture a different level in the hierarchy of objects. We don't 
tell the CNN how to look for features in the image, the CNN just learnigns from 
the training set.

### Filters

Image with width, height, and 'depth' (initially derived from colour channels). 
Use a filter to split image up into smaller patches.

The amount by which the filter slides is referred to as the 'stride'. This is a 
hyperparameter.

CNN is able to learn local structure/patterns by grouping together adjacent 
pixels.

Common to have multiple filters, different filters pick up different qualities 
of a patch. The amount of filters in a convolutional layer is called the filter 
depth. The number of neurons that connect to a given patch is tuned by our 
filter depth.

Valid padding: filter just go to edge of image, so filter is (dim.-1) * (dim.-1)
Same padding: pad filtered image, so filter has same dimensions to input image

### Parameters

Share parameters across all patches in a given input layer.

Padding input image with border of zeros means that we do not decrease the 
image width or height moving between layers.

Dimensionality: Given our input layer has a volume of `W`, our filter has a 
volume `(height * width * depth)` of `F`, we have a stride of `S`, and a 
padding of `P`, the following formula gives us the volume of the next layer: 
`(W−F+2P)/S+1`.

For a given convolutional layer output shape

`new_height = (input_height - filter_height + 2 * P)/S + 1`
`new_width = (input_width - filter_width + 2 * P)/S + 1`
`depth = number of filters`

[Padding in tensorflow](https://www.tensorflow.org/api_guides/python/nn#Convolution)

Number of parameters for a convolutional layer without parameter sharing:

(dim. output shape) * (number of weights + 1)

number of weights = dim. of filter shapes

Number of parameters for a convolutional layer **with** parameter sharing:

(number of neurons in the filter + bias neuron) * (number of channels in the output layer)

number of channels in the output layer = depth of output shape

### Visualising CNNs

[CNN trained on ImageNet](http://www.matthewzeiler.com/pubs/arxive2013/eccv2014.pdf)

[Deep visualisation toolbox](https://www.youtube.com/watch?v=ghEmQSxT6tw)

### Explore the Design Space

A pooling layer is generally used to
* Decrease the size of the output
* Prevent overfitting

For a pooling layer the output depth is the same as the input depth. 
Additionally, the pooling operation is applied individually for each depth 
slice.

[Pooling](https://en.wikipedia.org/wiki/Convolutional_neural_network#Pooling_layer)

Max pooling
* Often more accurate
* more expensive - convolutons run at lower stride
* More hyperparameters, pooling size, pooling stride

Average pooling

### Tensorflow Max Pooling

```
conv_layer = tf.nn.conv2d(input, weight, strides=[1, 2, 2, 1], padding='SAME')
conv_layer = tf.nn.bias_add(conv_layer, bias)
conv_layer = tf.nn.relu(conv_layer)
# Apply Max Pooling
conv_layer = tf.nn.max_pool(
    conv_layer,
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding='SAME')
```

Recently, pooling layers have fallen out of favor. Some reasons are:
* Recent datasets are so big and complex we're more concerned about 
underfitting.
* Dropout is a much better regularizer.
* Pooling results in a loss of information. Think about the max pooling 
operation as an example. We only keep the largest of n numbers, thereby 
disregarding `n-1` numbers completely.

### 1x1 Convolutions

Effectively running a mini neural network inbetween convolutions

Mathematically inexpensive

### Inception Module

At each layer of convolutional network use composition of convolutions and 
concatenate them

### CNN in TensorFlow

[Max pooling](https://cs231n.github.io/convolutional-networks/)
