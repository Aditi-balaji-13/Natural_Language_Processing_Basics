from util import *

# Add your import statements here
import numpy as np
from concurrent.futures import ThreadPoolExecutor


class InformationRetrieval():

	def __init__(self):
		self.index = None
		self.doc_num = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""
		self.docs = docs
		self.docIDs = docIDs
		self.doc_num = len(docIDs)
		index = {}

		#Fill in code here
		for i, doc in enumerate(self.docs):
			for sentence in doc:
				for word in sentence:
					if word not in index:
						index[word] = {}
					if docIDs[i] not in index[word]:
						index[word][docIDs[i]] = 0
					index[word][docIDs[i]] += 1
                        
                    
        for word in index:
            for i in docIDs:
                if i not in index[word]:
                    index[word][i]

		self.index = index


	


    def rank(self, queries):
        """
        Rank the documents according to relevance for each query

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is a query and
            each sub-sub-list is a sentence of the query
        
    
        Returns
        -------
        list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        """

        #DOC freq ID
        res_key = self.index.items()
        word_doc = list(res_key)
        word_doc = np.array(word_doc)
        
        
        