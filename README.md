# GDS - Fake News Project
Et repository til at samle gruppens forskellige filer og arbejde, som ikke befinder sig i det samlede dokument i Overleaf. 

Fag      : [Grundlæggende Data Science (GDS)](https://absalon.ku.dk/courses/80486)

Projekt  : [Group Fake News Project](https://absalon.ku.dk/courses/80486/assignments/232055)

Gruppe   : [Andy, Alireza, Mads &amp; Omid](https://absalon.ku.dk/groups/215410)

## To Do
***Deadline: 24-2-2025***

(ca. 1 Page)

In the first part of the project, you should work on retrieving, structuring, and cleaning data.

You will be using a subset of the FakeNewsCorpus dataset in your project, which is available from Absalon. You can also find more information about the full datasetLinks to an external site. and find information about how the data is collected, the available fields, etc.

**Task 1**: Your first task is to retrieve a sample of the [FakeNewsCorpus](https://raw.githubusercontent.com/several27/FakeNewsCorpus/master/news_sample.csv) and structure, process, clean it. You should follow the methodology you developed in Exercise 1. When you have finished cleaning, you can start to process the text. [NLTK](https://www.nltk.org/) has built-in support for many common operations. Try the following:

* Tokenize the text.
* Remove stopwords and compute the size of the vocabulary. Compute the reduction rate of the vocabulary size after removing stopwords.
* Remove word variations with stemming and compute the size of the vocabulary. Compute the reduction rate of the vocabulary size after stemming.
Describe which procedures (and which libraries) you used and why they are appropriate.

**Task 2**: Now try to explore the [995K FakeNewsCorpus subset](https://absalon.ku.dk/courses/80486/files/9275000/download?download_frd=1). Make at least three non-trivial observations/discoveries about the data. These observations could be related to outliers, artefacts, or even better: genuinely interesting patterns in the data that could potentially be used for fake-news detection. Examples of simple observations could be how many missing values there are in particular columns - or what the distribution over domains is. Be creative!

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

**Task 3**: Apply your data preprocessing pipeline to the 995,000 rows sampled from the FakeNewsCorpus.

**Task 4**: Split the resulting dataset into a training, validation, and test splits. A common strategy is to uniformly at random split the data 80% / 10% / 10%. You will use the training data to train your baseline and advanced models, the validation data can be used for model selection and hyperparameter tuning, while the test data should only be used in Part 4.

## Completed
- Part 0

## Missing
- Part 1 (Week 8)
- Part 2 (Week 10)
- Part 3 (Week 11)
- Part 4 (Week 12)


- Part 5 (Week 13)
- Submission (Friday 28-3-2025 kl: 16:00, Week 13)
