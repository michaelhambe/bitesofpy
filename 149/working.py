#%%
words = ("It's almost Holidays and PyBites wishes You a "
             "Merry Christmas and a Happy 2019").split()

# %%
words

# %%
w2 = sorted(words, key=str.lower)

# %%
w2

# %%
w3 = [w for w in w2 if w[0].isalpha()]+[w for w in w2 if w[0].isnumeric()]

# %%
w3

# %%
words

# %%
