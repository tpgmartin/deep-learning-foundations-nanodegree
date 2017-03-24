# Lesson 33

## Sentiment Prediction RNN

### Sentiment Prediction

Want to clssify reviews as either positive or negative, only care about last 
output

### Data Preprocessing

Create dictionary `vocab_to_int` maps vocab words to integere, index should 
start at one
Convert the reviews to integers, same shape as reviews list but with integers 
`reviews_ints`

Limit features to 200 characters, will pad reviews with 0's if less than 200 
characters

### Building the RNN

LSTM size: number of units in each layer, the more, the better performance

Use embedding layer instead of one-hot encoding due to size of vocab ~74,000, 
latter would be very inefficient

Check word2vec lesson to recap embedding technique

Compared to feed forward network, RNN has knowledge of individual words in the 
review as well as the sequence they appear in

### Training the Network


