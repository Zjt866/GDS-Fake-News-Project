# GDS - Fake News Project
Et repository til at samle gruppens forskellige filer og arbejde, som ikke befinder sig i det samlede dokument i Overleaf. 

Fag      : [Grundlæggende Data Science (GDS)](https://absalon.ku.dk/courses/80486)

Projekt  : [Group Fake News Project](https://absalon.ku.dk/courses/80486/assignments/232055)

Gruppe   : [Andy, Alireza, Mads &amp; Omid](https://absalon.ku.dk/groups/215410)

## To Do
### Part 1
***Deadline: 24-2-2025***

***(ca. 1 Page)***

In the first part of the project, you should work on retrieving, structuring, and cleaning data.

You will be using a subset of the FakeNewsCorpus dataset in your project, which is available from Absalon. You can also find more information about the [full dataset](https://github.com/several27/FakeNewsCorpus) and find information about how the data is collected, the available fields, etc.

**Task 1**: Your first task is to retrieve a sample of the [FakeNewsCorpus](https://raw.githubusercontent.com/several27/FakeNewsCorpus/master/news_sample.csv) and structure, process, clean it. You should follow the methodology you developed in Exercise 1. When you have finished cleaning, you can start to process the text. [NLTK](https://www.nltk.org/) has built-in support for many common operations. Try the following:

* Tokenize the text.
* Remove stopwords and compute the size of the vocabulary. Compute the reduction rate of the vocabulary size after removing stopwords.
* Remove word variations with stemming and compute the size of the vocabulary. Compute the reduction rate of the vocabulary size after stemming.
Describe which procedures (and which libraries) you used and why they are appropriate.

**Task 2**: Apply your data preprocessing pipeline to the 995,000 rows sampled from the FakeNewsCorpus.
  (Datacleaning, Tokenization, Stopword removel, Stemming)

**Task 3**: Now try to explore the [995K FakeNewsCorpus subset](https://absalon.ku.dk/courses/80486/files/9275000/download?download_frd=1). Make at least three non-trivial observations/discoveries about the data. These observations could be related to outliers, artefacts, or even better: genuinely interesting patterns in the data that could potentially be used for fake-news detection. Examples of simple observations could be how many missing values there are in particular columns - or what the distribution over domains is. Be creative!

1. Describe how you ended up representing the FakeNewsCorpus dataset (for instance with a Pandas dataframe). Argue for why you chose this design.
2. Did you discover any inherent problems with the data while working with it?
3. Report key properties of the data set - for instance through statistics or visualization.

The exploration can include (but need not be limited to):

1. counting the number of URLs in the content
2. counting the number of dates in the content
3. counting the number of numeric values in the content
4. determining the 100 more frequent words that appear in the content
5. plot the frequency of the 10000 most frequent words (any interesting patterns?)
6. run the analysis in point 4 and 5 both before and after removing stopwords and applying stemming: do you see any difference?

**Task 4**: Split the resulting dataset into a training, validation, and test splits. A common strategy is to uniformly at random split the data 80% / 10% / 10%. You will use the training data to train your baseline and advanced models, the validation data can be used for model selection and hyperparameter tuning, while the test data should only be used in Part 4.

### Part 2
***Deadline: 9-3-2025***

***(ca. 1 Page)***

You should create one or more reasonable baselines for your Fake News predictor. These should be simple models that you can use to benchmark your more advanced models against. You should aim to train a binary classification model that can predict whether an article is *reliable* or *fake*.

**Task 0**: Briefly discuss how you grouped the labels into two groups. Are there any limitations that could arise from the decisions you made when grouping the labels?

**Task 1**: Start by implementing and training a simple logistic regression classifier using a fixed vocabulary of the 10,000 most frequent words extracted from the content field, as the input features. You do not need to apply TF-IDF weighting to the features. It should take no more than five minutes to fit this model on a modern laptop, and you should expect to achieve an F1 score of ~94% on your test split. Write in your report the performance that you achieve with your implementation of this model, and remember to report any hyper-parameters used for the training process.

**Task 2**: Consider whether it would make sense to include meta-data features as well. If so, which ones, and why? If relevant, report the performance when including these additional features and compare it to the first baselines. Discuss whether these results match your expectations.

**Task 3**: Apply your data preprocessing pipeline to the extra reliable data you scraped during Graded Exercise 2 and add this to the training data and observe how this changes the performance of your simple model. Discuss whether you will continue to use this extra reliable data for the Advanced Model.

For the remainder of the project, we will limit ourselves to main-text data only (i.e. no meta-data). This makes it easier to do the cross-domain experiment in Part 4 (which does not have the same set of meta-data fields).

## Completed
- Part 0

## Missing
- Part 1 (Week 8)
- Part 2 (Week 10)
- Part 3 (Week 11)
- Part 4 (Week 12)


- Part 5 (Week 13)
- Submission (Friday 28-3-2025 kl: 16:00, Week 13)
