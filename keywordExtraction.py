from rake_nltk import Rake


def keywordExtraction():
    r = Rake()

    # Extracts keywords and ranks them
    r.extract_keywords_from_text("Keyword extraction is not that difficult after all. There are many libraries that can help you with keyword extraction. Rapid automatic keyword extraction is one of those.")

    # Creates list of ranked keywords
    ranked_phrases = r.get_ranked_phrases()

    # Creates file named ranked_phrases and adds the ranked keywords
    text_file = open("ranked_phrases.txt", "w")
    for ele in ranked_phrases:
        text_file.write(ele+'\n')
    text_file.close()

    print("Phrases added to file.")
