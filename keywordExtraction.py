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
    removeLinks = re.sub(r'^https?:\/\/.*[\r\n]*', " ", data)
    print("Links removed")

    print("Removing non letters from text")
    result = re.sub(r'[^a-zA-Z,]', " ", removeLinks)
    print("Non letters removed")

    # Extracts keywords from data file and ranks them
    print("Extracting keywords")
    extracted = r.extract_keywords_from_text(result)
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
