from json import load, dumps
from nltk.tokenize import word_tokenize

# a dictionary where the words will be the key and their ids will be the values
lexicon = {}

# unique integral ids to give to each word
id = 1

# open the json file containing all of the articles
with open("dataset.json", "r") as dataset:
    # loads the file into a list
    articles = load(dataset)
    # loops through the articles
    for article in articles:
        # stores the words of the title and the content in a list
        title = word_tokenize(article["title"])
        content = word_tokenize(article["content"])
        '''iterates through each word, gives it an ID, stores it in the lexicon dictionary 
        if it is not already there, and increments the ID counter by 1 '''
        for word in title:
            if not word in lexicon:
                lexicon[word] = id
                id += 1
        for word in content:
            if not word in lexicon:
                lexicon[word] = id
                id += 1


with open("lexicon.json", "w") as Lexicon:
    Lexicon.write(dumps(lexicon))
        

