from rake_nltk import Rake
import re

# Convert csv to string for when you pull from the actual csv of Trumps tweets
# https://stackoverflow.com/questions/3305926/python-csv-string-to-array


def keywordExtraction():
    r = Rake()

    # Opens file, reads contents and stores in string 'data'
    with open("pulledTweets.txt", 'r', encoding="utf8") as file:
        data = file.read()
        print("Read file")

    print("Removing links from text")
    refinedTweets = re.sub(r'https?:\/\/.*[\r\n]*', '', data, flags=re.MULTILINE)
    print("Links removed")

    text_file = open("refinedTweets.txt", "w", encoding="utf8")
    text_file.write(refinedTweets + '\n')

    # Extracts keywords from data file and ranks them
    print("Extracting keywords")
    extracted = r.extract_keywords_from_text(refinedTweets)
    print("Keywords extracted")

    # Creates list of ranked keywords
    print("Ranking keywords")
    ranked_phrases = r.get_ranked_phrases()
    print("Keywords ranked")

    # Creates file named ranked_phrases and adds the ranked keywords
    text_file = open("ranked_phrases.txt", "w", encoding="utf8")
    for ele in ranked_phrases:
        text_file.write(ele + '\n')
    text_file.close()

    print("Phrases added to file.")
