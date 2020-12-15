import os
import nltk
nltk.download('all')

#Sentence Tokenizer
from nltk.tokenize import sent_tokenize
Para = "Borrowing from Para=the management literature, Kaplan and Haenlein classify artificial intelligence into three different types of AI systems: analytical, human-inspired, and humanized artificial intelligence. Analytical AI has only characteristics consistent with cognitive intelligence; generating a cognitive representation of the world and using learning based on past experience to inform future decisions. Human-inspired AI has elements from cognitive and emotional intelligence; understanding human emotions, in addition to cognitive elements, and considering them in their decision making.Humanized AI shows characteristics of all types of competencies (i.e., cognitive, emotional, and social intelligence), is able to be self-conscious and is self-aware in interactions with others."
Para_tokens=sent_tokenize(Para)
Para_tokens
len(Para_tokens)
Para_tokens[2]


#Word Tokenizer
from nltk.tokenize import word_tokenize
Para1="I won't let you go"
word_tokenize(Para1)

#Tree Bank Tokenizer
from nltk.tokenize import TreebankWordTokenizer
Type2=TreebankWordTokenizer()
Type2.tokenize(Para1)

#Word Punctutation Tokenizer
from nltk.tokenize import WordPunctTokenizer
Type3=WordPunctTokenizer()
Type3.tokenize(Para1)

#RegExp_Tokenizer
from nltk.tokenize import regexp_tokenize
word_tokenize(Para1)
regexp_tokenize(Para1, "[\d]+")
regexp_tokenize(Para1, "[\w]+")
regexp_tokenize(Para1, "[\w]")

#Reg exp tokenizer
from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer("[\w']+")
tokenizer.tokenize(Para1)

#Stop word Tokenizer
from nltk.corpus import stopwords
SW=stopwords.words('english')
SW
len(SW)
sw_para="what are you doing exactly right now? I wanted to get to my office."
sw_para
from nltk.tokenize import word_tokenize
sw_para_tokens=word_tokenize(sw_para)
sw_para_tokens
len(sw_para_tokens)
filterArr=[item for item in sw_para_tokens if item not in SW]
filterArr

#Sample Usecase
from nltk.tokenize import word_tokenize
AI="Borrowing from the management literature, Kaplan and Haenlein classify artificial intelligence into three different types of AI systems: analytical, human-inspired, and humanized artificial intelligence. Analytical AI has only characteristics consistent with cognitive intelligence; generating a cognitive representation of the world and using learning based on past experience to inform future decisions. Human-inspired AI has elements from cognitive and emotional intelligence; understanding human emotions, in addition to cognitive elements, and considering them in their decision making.Humanized AI shows characteristics of all types of competencies (i.e., cognitive, emotional, and social intelligence), is able to be self-conscious and is self-aware in interactions with others."
AI
type(AI)

#Word tokenizer
from nltk.tokenize import word_tokenize
AI_tokens=word_tokenize(AI)
AI_tokens

