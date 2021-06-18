# NLP_DocEmbeddings

This is an exploratory project to establish the similarity of documents compared to a reference class.
Class1 (=relevant) and Class0 (=irrelevant) documents are compared to a reference text (=extract from a Class1 document not present in the dataset)

Doc_Embeddings.ipynb: Main script. 
Reads in documents
Cleans the text
Calculates the cosine similarity of each document compared to the reference text
Visualises document similarity

read_file.py:
Function that accesses the text from pdf, scanned pdf, word and html documents

clean_text.py
Function that removes stop words, corpus-specific stop words, non-English words, and lemmatizes the text

Documents:
Folder with the list of corpus-specific stop words (useless words.docx) and informative non-English words that we don't want to remove (informative_words.docx)

Data visualisation: Folder containing the output of the main script, i.e. the visualisation of document embeddings.
