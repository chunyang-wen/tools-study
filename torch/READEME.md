### Please refer to pytorch repo to install requirements

+ Anaconda
+ torchvision: use pip to install

### PyTorch

Code from here:

[Tutorials](http://pytorch.org/tutorials/)


### Typical training procedure

+ Define the neural network that has some learnable parameters(or weights)
+ Iterate over a dataset of inputs
+ Process input through the network
+ Compute the loss (how far is the output from being correct)
+ Propagate gradients back into the network's parameters
+ Update the weights of the network, typically using a simple update rule:

`weight = weight + learning_rate * gradient`
