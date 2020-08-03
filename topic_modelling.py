from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd
import numpy as np
import mglearn

foo = ["The color of animals is by no means a matter of chance", "it depends on many considerations","in the majority of cases tends to protect the animal from danger by rendering it less conspicuous"
"Perhaps it may be said that if coloring is mainly protective there ought to be but few brightly colored animals"]

vect=CountVectorizer(ngram_range=(1,1),stop_words='english')

def func(topics, feature_names, sorting, topics_per_chunk=6,n_words=20):
	topic_words = []
	for i in range(0, len(topics), topics_per_chunk):
		these_topics = topics[i: i + topics_per_chunk]
		len_this_chunk = len(these_topics)
		for i in range(n_words):
			try:
				topic_words.append(list(feature_names[sorting[these_topics, i]]))
			except:
				print("Error")
		print("\n")
	return topic_words
	
def getTopics(text):
	dtm=vect.fit_transform(text)
	pd.DataFrame(dtm.toarray(),columns=vect.get_feature_names())
	lda=LatentDirichletAllocation(n_components=5)
	lda.fit_transform(dtm)
	lda_dtf=lda.fit_transform(dtm)
	sorting=np.argsort(lda.components_)[:,::-1]
	features=np.array(vect.get_feature_names())
	topics = func(topics=range(5), feature_names=features,
	sorting=sorting, topics_per_chunk=5, n_words=10)
	return topics
	# summary = []
	# for topic in range(5):
	# 	curr_topic = np.argsort(lda_dtf[:,topic])[::-1]
	# 	for i in curr_topic[:4]:
	# 		print(".".join(text[i].split(".")[:2]))
	# 		summary.append(".".join(text[i].split(".")[:2]) + "\n")

if __name__ == '__main__':
	getTopics(foo)