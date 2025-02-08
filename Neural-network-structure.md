# The model structure
<img src="https://github.com/user-attachments/assets/71cdb685-54b0-4833-922d-530d217b1139" width="800" height="400">

The program takes inputs and outputs the probability it will be ACE or not. There are 12 distinct inputs and only one output that being did it result in an Ace.

With 1 meaning it has a 100% chance of being an ace and 0 being 
0% chance it is ace. Therefore values outside this range are invalid, which means we need to design our model such that it only outputs values between 0 and 1. we can achieve this by having the activation function for our output layer being a sigmoid function. It compresses any real number to a value into a value between 0 and 1.

Another problem is the input layer and all the neurons for that matter can only have a numerical value. In our database we have strings surface,serve_side,hitter_hand,receiver_hand. You could run a SQL querry to changes these to numerical values for example being the hitter_hand being right handed could have a value of 1, and it being left will have 0. Where this gets problematic is that for somethings like surface it can be hard,clay or grass with there being 3 options. We could implement a similar system, or create seperate inputs for the three possible values.
