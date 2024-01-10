def rand_paragraph(fake, nb_sentences=3, variable_nb_sentences=True, ext_word_list=None):
    """
    Generate a random paragraph.
    Args:
        fake (Faker): The Faker instance to use.
        nb_sentences: Number of sentences in the paragraph.
        variable_nb_sentences: If True, the number of sentences can vary around nb_sentences.
        ext_word_list: Optional; an external list of words to use.
    """
    return fake.paragraph(nb_sentences=nb_sentences, variable_nb_sentences=variable_nb_sentences, ext_word_list=ext_word_list)

def rand_paragraphs(fake, nb=3, ext_word_list=None):
    """
    Generate a list of random paragraphs.
    Args:
        fake (Faker): The Faker instance to use.
        nb: Number of paragraphs to generate.
        ext_word_list: Optional; an external list of words to use.
    """
    return fake.paragraphs(nb=nb, ext_word_list=ext_word_list)

def rand_sentence(fake, nb_words=6, variable_nb_words=True, ext_word_list=None):
    """
    Generate a random sentence.
    Args:
        fake (Faker): The Faker instance to use.
        nb_words: Number of words in the sentence.
        variable_nb_words: If True, the number of words can vary around nb_words.
        ext_word_list: Optional; an external list of words to use.
    """
    return fake.sentence(nb_words=nb_words, variable_nb_words=variable_nb_words, ext_word_list=ext_word_list)

def rand_sentences(fake, nb=3, ext_word_list=None):
    """
    Generate a list of random sentences.
    Args:
        fake (Faker): The Faker instance to use.
        nb: Number of sentences to generate.
        ext_word_list: Optional; an external list of words to use.
    """
    return fake.sentences(nb=nb, ext_word_list=ext_word_list)

def rand_word(fake, ext_word_list=None):
    """
    Generate a random word.
    Args:
        fake (Faker): The Faker instance to use.
        ext_word_list: Optional; an external list of words to use.
    """
    return fake.word(ext_word_list=ext_word_list)

def rand_words(fake, nb=3, ext_word_list=None):
    """
    Generate a list of random words.
    Args:
        fake (Faker): The Faker instance to use.
        nb: Number of words to generate.
        ext_word_list: Optional; an external list of words to use.
    """
    return fake.words(nb=nb, ext_word_list=ext_word_list)

def rand_text(fake, max_nb_chars=200, ext_word_list=None):
    """
    Generate a random text string.
    Args:
        fake (Faker): The Faker instance to use.
        max_nb_chars: Maximum number of characters in the text.
        ext_word_list: Optional; an external list of words to use.
    """
    return fake.text(max_nb_chars=max_nb_chars, ext_word_list=ext_word_list)