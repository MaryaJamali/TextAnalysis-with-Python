def text_analysis():
    user_text = input('please type an ENGLISH text: ')
    # Lowercase all text words
    user_text = user_text.lower()
    # Separate words from the text
    text_words = user_text.split()
    stopwords = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'not', 'so', 'if',
                 'to', 'from', 'at', 'by', 'in', 'on', 'that', 'this', 'is', 'am',
                 'are', 'was', 'were', 'be', 'have', 'has', 'do', 'did', 'with',
                 'before', 'after', 'until', 'from', 'to', 'on', 'i', 'he', 'she',
                 'it', 'we', 'they', 'as', 'are', 'at', 'for']
    # List of words without Stopwords
    list_words = []
    for s_w in text_words:
        # All the words that do not exist in Stopwords
        if s_w not in stopwords:
            list_words.append(s_w)
    punctuations = ['.', '%', '  ', '~', '@', ',', '"', "'", '[', ']', '{', '}', ':', ';',
                    '?', '!', '>', '<', '/', '*', '=', '#', '(', ')', '$']
    # Concatenates all words in the list (all punctuation marks are placed as a string)
    punc = ''.join(punctuations)
    # List of words without punctuations
    list_punc = []
    for l_p in list_words:
        # Removing punctuation marks from the beginning and end of the word
        l_p = l_p.strip(punc)
        list_punc.append(l_p)
        # It calculates the number of repetitions of each word in (list_punc) and stores it in the dictionary
    dict_count = {}
    for d_c in list_punc:
        dict_count[d_c] = list_punc.count(d_c)
        # Repeat words in descending order
    sort_words = sorted(dict_count, key=dict_count.get, reverse=True)
# for example: d={'i':2, 'm':1}    s={}   for key in d:   s[key]=d[key]--->s['i']=d['i']=value=2
    sort_dict = {}
    for s_d in sort_words:
        sort_dict[s_d] = dict_count[s_d]
    return sort_dict


print('Number of words in your text: ', text_analysis())
