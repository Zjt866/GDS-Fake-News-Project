## **Task 2:** Now try to explore the 995K FakeNewsCorpus subset. 
## Make at least three non-trivial observations/discoveries about the data. 
## These observations could be related to outliers, artefacts, or even better: genuinely interesting patterns in the data that could potentially be used for fake-news detection. 
## Examples of simple observations could be how many missing values there are in particular columns - or what the distribution over domains is. Be creative!

### Describe how you ended up representing the FakeNewsCorpus dataset (for instance with a Pandas dataframe). Argue for why you chose this design.
#### - Did you discover any inherent problems with the data while working with it?
#### - Report key properties of the data set - for instance through statistics or visualization.
### The exploration can include (but need not be limited to):

#### - Counting the number of URLs in the content
#### - Counting the number of dates in the content
#### - Counting the number of numeric values in the content
#### - Determining the 100 more frequent words that appear in the content
#### - Plot the frequency of the 10000 most frequent words (any interesting patterns?)
#### - Run the analysis in point 4 and 5 both before and after removing stopwords and applying stemming: do you see any difference?

## Data representation

[Reasoning for choice of dataframe]


```python
import pandas as pd
import re

file = "995,000_rows.csv"
# I've not put the read function to avoid exploding my laptop
```

### Brainstorm for possible interesting non-trivial observations/discoveries to analyse.

##### 1. Similarities of the fake news in their word frequency and noting which words are most prevalent.
##### 2. Charachter length of the fake news.
##### 3. POS (Parts of Speech).
###### 3.1 Frequency of nouns, verbs, etc.
##### 4. Frequency of  names (i.e. frequency of 'Trump' or 'Hillary').
##### 5. Frequency of links (urls).
##### 6. Frequency of quotes (citater). 
##### 7. Frequency of dates (dato).
##### 8. The positivity/negativity.
##### 9. Averge of length of words used in titles. (i.e. supercalifragilistic or alert)
##### 10. Use of capital letters in titles. (BREAKING NEWS! or Breaking News!)
##### 11. Readability index (lixtal).
##### 12. Use of complex words.
##### 13. Use of emotional words
##### 13. Frequency of numbers
##### 14. Length of numbers
##### 15. Frequency of Author names.
##### 16. Use of exclamation/question mark.


```python

```
