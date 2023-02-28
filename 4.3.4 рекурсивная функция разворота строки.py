def rec_str(text):
    if len(text) == 0:
        return ''
    else:
        return text[-1] + rec_str(text[:-1])

print(rec_str('test'))
