import re

# Original input text
a = ("Graph is a non-linear data structure like tree data structure. "
     "The limitation of tree is, it can only represent hierarchical data. "
     "For situations where nodes or vertices are randomly connected with each other other, "
     "we use Graph. Example situations where we use graph data structure are, a social network, "
     "a computer network, a network of locations used in GPS and many more examples where "
     "different nodes or vertices are connected without any hierarchic or constraint on structure.")
clean_string=a.replace(",",",,,")
clean_string = clean_string.replace(" ", ",")

clean_string = re.sub(r'([!@#$%^&*()\-_+=\[\]{}\\|;:\'"./<>?`~])', r',\1,', clean_string)

clean_string = re.sub(r',+', ',', clean_string)

print("Cleaned String:\n", clean_string)

li = clean_string.split(',')
print("\nSplit List:\n", li)

nli = list(set(li))
print("\nUnique List:\n", nli)

m = ""
for i in li:
    m += f"@{li.index(i)}"

print(m)


indexes = m.split('@')[1:]  # remove leading empty part
decoded_words = [li[int(i)] for i in indexes]
decoded_text = " ".join(decoded_words)
print("\nDecoded Words:\n", decoded_text)
