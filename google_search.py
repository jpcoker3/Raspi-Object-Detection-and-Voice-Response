"""
    pip install googlesearch-python
"""

from googlesearch import search
from pprint import pprint as print

def top_description(query):
    #grab the description of the top result
    results = list(search(query, advanced=True))
    return results[0].description

def full_search(query):
    #return all of the data from the search
    results = list(search(query, advanced=True))
    return results

#testing function
if __name__ == '__main__':
    query = input("What would you like to search for? ")
    
    results = top_description(query)
    
    print(results)
