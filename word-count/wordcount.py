from collections import defaultdict
import re

def word_count(words_str):
  word_lst = _prepare_valid_word_lst(words_str)
    
  wc = defaultdict(int)
  for word in word_lst: wc[word] += 1
  return wc

def _prepare_valid_word_lst(words_str):
  lowered_words_str = words_str.lower()
  rmvd_punct_and_ws = re.sub(r"\W+", " ", lowered_words_str).rstrip()
  wrd_lst = re.split(r"\W|_", rmvd_punct_and_ws)
  return wrd_lst
