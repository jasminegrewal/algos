# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:25:56 2017

@author: jasmine
"""
from collections import defaultdict

def groupAnagrams(strings):
    anagrams, groups = defaultdict(list), []
    for word in strings:
        sorted_str = ("").join(sorted(word))            
        print(sorted_str)
        anagrams[sorted_str].append(word)
        print (anagrams)
    for anagram in anagrams.values():
        print (anagram)
        groups.append(anagram)
    print (anagrams)
    return groups


if __name__ == "__main__":
    groups = groupAnagrams(["cat", "dog", "act", "mac","amc"])
    print (groups)
