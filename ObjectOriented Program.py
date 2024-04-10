class TextAnalysis:
    # Whenever we want to code object_oriented, we need the def __init__(self) method.
    def __init__(self, user_text):
        self.user_text = user_text
        # Lowercase all text words
        self.user_text = user_text.lower()

    def stopword(self):
        # Separate words from the text
        text_word = self.user_text.split()
        stopwords = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'not', 'so', 'if',
                     'to', 'from', 'at', 'by', 'in', 'on', 'that', 'this', 'is', 'am',
                     'are', 'was', 'were', 'be', 'have', 'has', 'do', 'did', 'with',
                     'before', 'after', 'until', 'from', 'to', 'on', 'i', 'he', 'she',
                     'it', 'we', 'they', 'as', 'are', 'at', 'for']
        # List of words without Stopwords
        list_words = []
        for s_w in text_word:
            # All the words that do not exist in Stopwords
            if s_w not in stopwords:
                list_words.append(s_w)
        # Returns the value
        return list_words

# When creating a class method, you no longer need self as the first argument,
# and you use cls(class self), which refers to the class itself.
    @classmethod
    def punctuation(cls, list_words):
        punctuations = ['.', '  ', '%', '@', ',', '"', "'", '[', ']', '{', '}', ':', ';',
                        '?', '!', '>', '<', '/', '*', '=', '#', '(', ')', '$', '~']
        # Concatenates all words in the list (all punctuation marks are placed as a string)
        punc = ''.join(punctuations)
        # List of words without punctuations
        list_punc = []
        for l_p in list_words:
            # Removing punctuation marks from the beginning and end of the word
            l_p = l_p.strip(punc)
            list_punc.append(l_p)
        return list_punc

    @classmethod
    def wordcount(cls, list_punc):
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


# Define an object
user1 = input('please type an ENGLISH text: ')
# Calling the TextAnalysis function
input_text = TextAnalysis(user1)
# Using the stopword method
input_text1 = input_text.stopword()
print('words without stopwords: ', input_text1)
# Using the punctuation method
input_text2 = input_text.punctuation(input_text1)
print('words without punctuations: ', input_text2)
# Using the word count method
input_text3 = input_text.wordcount(input_text2)
print('Your main words count: ', input_text3)

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
