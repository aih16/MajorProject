def sentimentAnalysis():
    print("Sentiment Analysis")

    with open("extractThis.txt", 'r') as file:
        data = file.read().replace('\n', '')

    sentences = nltk.tokenize.sent_tokenize(data)