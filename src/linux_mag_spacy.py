import spacy


class LinuxMagSpacy(object):
    """
    Jouons avec Spacy pour explorer le Natural Language Processing.
    """

    def __init__(self):
        self.__nlp = spacy.load("fr")

    def extract_information(self, sentence):
        doc = self.__nlp(sentence)
        print([(word.text, word.pos_) for word in doc])


if __name__ == "__main__":
    linux_mag_spacy = LinuxMagSpacy()
    linux_mag_spacy.extract_information("Bonjour le monde de Linux Mag")
