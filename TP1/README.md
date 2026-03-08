# line 10
use `string.punctuation` bcz it saves you from typing all those marks

# line 13
instead of separate if statements for symbols and punctuation, use one `elif`
or just check if the char is in both lists at once

# line 30
using regex `re.sub` is good, but make sure you understand the lookbehind `(?<!\d)`

# line 47
building strings with `+=` inside a loop is discouraged
use a list and then `.join()` for better performance

# line 56
manually replacing `"i'm"` only works for one case
use a dict for contractions if you want to handle `"don't"`, `"can't"`, etc

# it feels like you wrote the simple parts and asked an `ai` to do the rest
# no need for `ai` when the task is this simple. try to actually code next time
