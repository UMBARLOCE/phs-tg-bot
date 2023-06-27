import re
import string


q = "!qwer.t yu!nm$v jk,hjk."
# w = re.sub("[!|.|,|$]", "", q)
w: str = "".join([i for i in q if i not in (string.punctuation, " ")])
print(w)
