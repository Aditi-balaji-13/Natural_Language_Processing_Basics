from util import *

# Add your import statements here




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
						index[word] == {}
					if docIDs[i] not in index[word]:
						index[word][docIDs[i]] == 0
					index[word][docIDs[i]] += 1
                        
            

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

		doc_IDs_ordered = []
		
		for i,query in enumerate(queries):
			quer_ind = {}
			for sentence in query:
				for word in sentence:
					if word not in quer_ind:
						quer_ind[word] = 0
					else:
						quer_ind[word] += 1
			df = {}
			for word in self.index:
				df[word] = 1+np.log((1+self.doc_num)/(self.doc_num-self.index[word].values().count(0)+1))
			dot={}
			mag={}
			cosine={}
			for doc in self.docIDs:
				dot[doc]=0
				mag[doc]=0
			qmag=0
			for word in quer_ind and word not in self.index:
				df[word] = 1+ np.log(1+self.doc_num)
				qmag+=(df[word]*quer_ind[word])**2
			for word in self.index:	
				f=True
				for doc in self.docIDs:
					if word in quer_ind:
						dot[doc]+=(df[word]**2)*quer_ind[word]*self.index[word][doc]
						if(f):
							qmag+=(df[word]*quer_ind[word])**2
							f=False
					mag[doc]+=(df[word]*self.index[word][doc])**2
			qmag=np.sqrt(qmag)
			for doc in self.docIDs:
				cosine[doc]=dot[doc]/(qmag*np.sqrt(mag[doc]))
			doc_IDs_ordered.append(sorted(cosine,key=cosine.get,reverse=True))

            		

          

		
		return doc_IDs_ordered




