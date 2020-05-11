# MajorProject - Trump Tweets vs The Markets

## Windows

###Author: Aidan Hogden

### Installation
1. Install PyCharm IDE or any other terminal capable of importing the relevant libraries.

2. If using PyCharm or similar IDE, install the relevant libraries that are being imported, these being:
- textblob
- nltk
- rake_nltk
- pandas
- sklearn
- numpy
    
### Execution
Run the main.py file calling the the below functions for the following purpose:
- SA() for preprocessing, keyword extraction and sentiment analysis.
- CountVector() or TF-IDF() for Feature Extraction depending on which one you require.
- GNB, MNB or LogiR for Gaussian NB, Multinomial NB or Logistic Regression model market prediction.

### Structure
All files can be found in the main MajorProject directory, all data sets and needed information that is stored in either CSV or TXT format can be found in the datasets directory and all depreciated code can be found in the OldCode directory. 
