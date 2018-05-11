
# coding: utf-8

# In[60]:


from bs4 import BeautifulSoup

def html_parsing():
   html_file  = open('Anthem.html','r')
   string = html_file.read()
   soup = BeautifulSoup(string, 'lxml')
   text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
   text = text.replace('\n', ' ')
   text_split = text.split('.')
   text_strip = [sentence.strip(' ') for sentence in text_split]
   return text_strip, text


# In[61]:


def stop_word_and_punctuation_removal(s):
    Stop_word = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
    punctuation_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    list_word = []
    for word in s.split(' '):
        if word.lower() not in (Stop_word + punctuation_list):
            list_word.append(word)
    return list_word 
   


# In[63]:


def find_keyword_from_query(query, Bag_of_word):
    keyword_list = []
    refined_list = stop_word_and_punctuation_removal(query)
    for keyword in refined_list:
        if keyword in Bag_of_word:
            keyword_list.append(keyword)
    return keyword_list
    


# In[64]:


def matched_sentence_to_query(list_of_keywords, list_of_sentence):
    match_sentence_list = []
    for keyword in list_of_keywords:
        for sentence in list_of_sentence:
            if keyword in [x.lower() for x in sentence.split(' ')]:
                match_sentence_list.append(sentence)
    return match_sentence_list

