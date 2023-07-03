import keyword


def count_keywords(text):
    keywords = keyword.kwlist
    count = 0
    for word in text.split():
        if word in keywords:
            count += 1
    return count


# Example usage:
text = '''
This is an example text that contains keywords like False, None, True, and, as, assert, async, await, break, class, continue,
def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise,
return, try, while, with, yield.
'''
keyword_count = count_keywords(text)
print("Number of keywords:", keyword_count)
