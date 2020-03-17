from textblob import TextBlob
from textblob import classifiers
from textblob.classifiers import NaiveBayesClassifier


def SA():
    trainingData = [
        ('Tom Holland is a terrible spiderman.', 'neg'),
        ('a terrible Javert (Russell Crowe) ruined Les Miserables for me...', 'neg'),
        ('The Dark Knight Rises is the greatest superhero movie ever!', 'pos'),
        ('Fantastic Four should have never been made.', 'neg'),
        ('Wes Anderson is my favorite director!', 'pos'),
        ('Captain America 2 is pretty awesome.', 'pos'),
        ('Lets pretend "Batman and Robin" never happened..', 'neg'),
        ('I love this sandwich.', 'pos'),
        ('this is an amazing place!', 'pos'),
        ('I feel very good about these beers.', 'pos'),
        ('this is my best work.', 'pos'),
        ("what an awesome view", 'pos'),
        ('I do not like this restaurant', 'neg'),
        ('I am tired of this stuff.', 'neg'),
        ("I can't deal with this", 'neg'),
        ('he is my sworn enemy!', 'neg'),
        ('my boss is horrible.', 'neg')
    ]
    testingData = [
        ('Superman was never an interesting character.', 'neg'),
        ('Fantastic Mr Fox is an awesome film!', 'pos'),
        ('Dragonball Evolution is simply terrible!!', 'neg'),
        ('the beer was good.', 'pos'),
        ('I do not enjoy my job', 'neg'),
        ("I ain't feeling dandy today.", 'neg'),
        ("I feel amazing!", 'pos'),
        ('Gary is a friend of mine.', 'pos'),
        ("I can't believe I'm doing this.", 'neg')
    ]

    cl = NaiveBayesClassifier(trainingData)
    cl.show_informative_features(10)
    DemoInput = input("Please provide a test input: ")
    print(cl.classify(DemoInput))
