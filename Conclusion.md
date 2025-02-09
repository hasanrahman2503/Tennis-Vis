<img src="https://github.com/user-attachments/assets/71cdb685-54b0-4833-922d-530d217b1139" width="800" height="400">
# How we can use our model?
We can use our model to evaluate a players moves, see how favourably or unfavourably the model views it. Next we can try alter some of the paramters e.g.(ball_bounce_v) if increasing it significantly improved the outcome from the model, that could be an area of improvment. With the reverse also being true.

Some of the data has missing values for example entry 1214 has missing data, which will distrupt any model. Since the relative frequency of missing data is rare enough we can ingore these results without much consquences, but we should be vigilant when ignoring erroneous data as it can skew our results e.g(If its disproproportional in where the data is missing).


$$\text{Well fitted model} \neq \text{A good model}$$

Is our model any good? We know that it can successfully minimise the cost function but is it actually good at predicting aces, or is it just memorising answers. One way to test this is to give our model data on games it has never been trained on to see how well it performs.
