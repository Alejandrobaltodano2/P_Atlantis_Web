from sklearn.feature_extraction.text import TfidfVectorizer #  Libreria que  Calcula los valores tf-idf
from sklearn.metrics.pairwise import cosine_similarity #Calcule la similitud del coseno 
from nltk.corpus import stopwords #palabras vacias 
import nltk # procesamiento del lenguaje natural
import string #cadenas 



class Chatbot:
    lista_respuesta=''
    def __init__(self,lista:list) -> None:
        self.lista=lista
    def listaRespuestas(self):
        for e in self.lista:
            self.lista_respuesta+=e.respuesta+'\n'

    def Preprocesamiento_del_texto(self):
        self.listaRespuestas()
        self.lista_respuesta=self.lista_respuesta.lower()
        self.sent_tokens=nltk.sent_tokenize(self.lista_respuesta)
        self.wortd_tokens = nltk.word_tokenize(self.lista_respuesta)
        self.lemmer = nltk.stem.WordNetLemmatizer()
    
    def LemTokens(self,tokens):
        return [self.lemmer.lemmatize(token) for token in tokens]

    def LemNormalize(self,texto):
        remover_signos_puntacion = dict((ord(punct),None) for punct in string.punctuation)
        return  self.LemTokens(nltk.word_tokenize(texto.lower().translate(remover_signos_puntacion)))

    def Responder(self,pregunta_usuario):
        self.Preprocesamiento_del_texto()
        self.sent_tokens.append(pregunta_usuario)
        self.tfidfvec = TfidfVectorizer(tokenizer=self.LemNormalize,stop_words=stopwords.words('spanish'))
        self.tfidf=self.tfidfvec.fit_transform(self.sent_tokens)
        self.vals=cosine_similarity(self.tfidf[-1],self.tfidf)
        self.idx = self.vals.argsort()[0][-2]
        self.flat=self.vals.flatten()           
        self.flat.sort()
        self.req_tfidf = self.flat[-2]
        if self.req_tfidf==0:
            return -1
        else :
            self.sent_tokens.remove(pregunta_usuario)

            return self.idx