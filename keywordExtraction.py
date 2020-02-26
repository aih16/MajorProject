from rake_nltk import Rake


def keywordExtraction():
    r = Rake()

    # Opens file, reads data and stores as string 'data'
    with open("extractThis.txt", 'r') as file:
        data = file.read().replace('\n', '')

    # Extracts keywords from data file and ranks them
    r.extract_keywords_from_text(data)

    # Creates list of ranked keywords
    ranked_phrases = r.get_ranked_phrases()

    # Creates file named ranked_phrases and adds the ranked keywords
    text_file = open("ranked_phrases.txt", "w")
    for ele in ranked_phrases:
        text_file.write(ele + '\n')
    text_file.close()

    print("Phrases added to file.")
