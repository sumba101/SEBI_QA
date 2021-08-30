Case files data could be downloaded from here:

https://iiitaphyd-my.sharepoint.com/:f:/g/personal/deepti_saravanan_research_iiit_ac_in/EhsLi4zKPwtHlhV5QhlqN7gBXQB9wIq0Yyqtyl09e6062w?e=PTe8wn

Case - Data from case files
Misc - Data from Informal Guidance and Concept Papers

Files - Description :

(Let X -> Case / Misc)

X_DF - Document frequecy values of tokens for tdidf calculation

X_tfidf - tfidf values of tokens

X_filenames - filenames of the corresponding pdf files in the data directory

X_queries - List of queries generated

X_total_vocab - list of word tokens

X_text - list of sentences from file

reg_topics.pkl - list of list of topics extracted from SEBI sub-regulations -> [[reg1_topic1, reg1_topic2,...],[reg2_topic1, reg2_topic2,...]...]

cleanedregtopics48.pkl - list of list of topics extracted from regulatory documents -> [[doc1_topic1, doc1_topic2,...],[doc2_topic1, doc2_topic2,...]...]

cleanedreguations48.pkl - list of list of sub-regulations from 48 regulatory documents -> [[doc1_reg1, doc1_reg2,...], [doc2_reg1, doc2_reg2]...]

glossary.json - dictionary of unique tokens corresponding to each regulatory documents. Keys -> tokens and values -> index of the regulatory document according to the list in main code. -> {token0:[0], token1:[0], token2:[1],...}

mainvocab.pkl - list of word tokens from sub-regulations.

vocabdef.pkl - list of WordNet definitions of words corresponding to the words in mainvocab.pkl
