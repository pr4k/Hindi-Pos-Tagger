import nltk
from nltk.corpus import indian
from nltk.tag import tnt
import string


nltk.download("punkt")
nltk.download("indian")


def train():

    taggedSet = "hindi.pos"
    wordSet = indian.sents(taggedSet)
    count = 0
    print(wordSet[0])
    for sen in wordSet:
        count = count + 1
        sen = "".join(
            [
                " " + i if not i.startswith("'") and i not in string.punctuation else i
                for i in sen
            ]
        ).strip()
        print(count, sen, "sentences")
    print("Total sentences in the tagged file are", count)

    trainPerc = 0.9

    trainRows = int(trainPerc * count)
    testRows = trainRows + 1

    data = indian.tagged_sents(taggedSet)
    train_data = data[:trainRows]
    test_data = data[testRows:]

    print("Training dataset length: ", len(train_data))
    print("Testing dataset length: ", len(test_data))

    pos_tagger = tnt.TnT()
    pos_tagger.train(train_data)
    print("Accuracy: ", pos_tagger.evaluate(test_data))
    return pos_tagger


def tagger(pos_tagger, sentenceToBeTagged):

    tokenized = nltk.word_tokenize(sentenceToBeTagged)

    return pos_tagger.tag(tokenized)


if __name__ == "__main__":
    pos_tagger = train()
    sentence_to_be_tagged = "३९ गेंदों में दो चौकों और एक छक्के की मदद से ३४ रन बनाने वाले परोरे अंत तक आउट नहीं हुए ।"
    print(tagger(pos_tagger, sentence_to_be_tagged))
