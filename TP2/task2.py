# Documents
D1 = "I love cats"
D2 = "Cats are chill"
D3 = "I am late"

# Your Task: implement context window vectorization
# with window size = 1 (so each window is 3 tokens wide)
# Use <s> and </s> padding flags

def add_padding(tokens):
    # wrap tokens with start and end flags
    pass

def extract_windows(tokens, window_size=1):
    # slide window and collect all (2*window_size+1)-token windows
    pass

def build_vocab(all_windows):
    # collect unique windows, sort alphabetically, assign index
    pass

def vectorize_doc(doc_windows, vocab):
    # return a binary vector: 1 if window in doc, 0 otherwise
    pass

# Run
all_docs = [D1, D2, D3]