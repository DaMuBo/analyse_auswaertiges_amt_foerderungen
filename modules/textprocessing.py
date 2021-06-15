import re
import spacy
from sklearn.preprocessing import FunctionTransformer

nlp = spacy.load('en_core_web_md')
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS

def preprocessor(text):
    if isinstance((text), (str)):
        text = re.sub('<[^>]*>', '', text)
        text = re.sub('[\d]+', '', text.lower())
        text = re.sub('"', '', text.lower())
        return text
    if isinstance((text), (list)):
        return_list = []
        for i in range(len(text)):
            temp_text = re.sub('<[^>]*>', '', text[i])
            temp_text = re.sub('[\d]+', '', temp_text.lower())
            return_list.append(temp_text)
        return(return_list)
    else:
        pass
    
def normalizer(text):
    #text = text.lower()
    tokenizer = nlp.Defaults.create_tokenizer(nlp)
    tokens = tokenizer(text)
    lemma_list = []
    for token in tokens:
        if token.is_stop is False:
            token_preprocessed = preprocessor(token.lemma_)
            if token_preprocessed != '':
                 lemma_list.append(token_preprocessed)
    tokens = lemma_list
    return tokens
        

def pipelinize(function, active=True):
    def list_comprehend_a_function(list_or_series, active=True):
        if active:
            return [function(i) for i in list_or_series]
        else: # if it's not active, just pass it right back
            return list_or_series
    return FunctionTransformer(list_comprehend_a_function, validate=False, kw_args={'active':active})
    