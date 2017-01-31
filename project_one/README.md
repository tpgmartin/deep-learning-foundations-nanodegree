# Week One

Gradient descent to minimise cost funciton

## Intro to Neural Networks

Perceptrons are individual nodes of a neural network 

Bias: Adding or subtracting to the line will move the line up or down
Weights: Changing the weights will affect the slope of the line

## Gradient Descent

Want the network's prediction error to be as small as possible by adjusting 
the weights. Find weights that minimisee the squared error.

## Multilayer Perceptrons

Allow solutions to nonlinear datasets
More layers allow solutions to more complex problems

## Anaconda

Create new working environment

`conda create -n <env-name> python3`

e.g. What command would you use to create an environment named data installed 
with Python 3.5, numpy, and pandas?

`conda create -n data python=3.5 numpy pandas`

Activate

`source activate <env-name>`

You can save the packages to a YAML file with 

`conda env export > environment.yaml`

To create an environment from an environment file use 

`conda env create -f environment.yaml`

List environments

`conda env list`

Best practice to create separate environments for Python2 and Python3

When sharing your code on GitHub, it's good practice to make an environment 
file and include it in the repository.

usually include a pip `requirements.txt` file using `pip freeze` for people not 
using conda.

## Jupyter notebook

[Running a notebook server](https://jupyter-notebook.readthedocs.io/en/latest/public_server.html)

[Built-in magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

Convert notebook to html

`jupyter nbconvert --to html notebook.ipynb`

Convert to slideshow

`jupyter nbconvert notebook.ipynb --to slides`


