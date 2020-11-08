# NLTK-hindi-POS-tagging

This project is created as an Assignment for WSM Course.

## Problem Statement:

The task given was to create a Pos(Part-of-speech) Tagger for Hindi Language.

## Solution Proposed:

Our Solution contains the use of Open-Source And widely used library NLTK.

### Brief Description of the Solution:

The whole solution is divided into two parts;

- Training the Pos tagger to detect Hindi Part of speech
- Predicting the tags for a new phrase or sentence.

##### Training of the Pos Tagger

We use `indian` Corpus provided by NLTK, to train our tagger.
The whole dataset contains 540 records out of which we use **** 90% * dataset i.e 486 records to train and remaining to evaluate the accuracy

Our Model performs with `81.11 %` accuracy on test dataset.

##### Prediction of Tags

Once the model is trained, the tagger is passed to a seperate function which takes care of prediction of tags, given a sentence.

## Team Mates:

- Mohit Khora [kami9coder](https://github.com/kami9coder)
- Pratiksha Samal
- Jaswant Reddy
- Prakhar Kaushik [pr4k](https://github.com/pr4k)
 
 ## Special Mention

 We would like to thank our professor and mentor ** Mr Rakesh Chandra Balabantaray ** sir for all the guidance and motivation provided throughout the project.
