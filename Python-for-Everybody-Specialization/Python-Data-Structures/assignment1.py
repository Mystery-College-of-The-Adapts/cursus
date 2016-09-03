
text = "X-DSPAM-Confidence:    0.8475";
spaceindex = text.find(" ")
num = text[spaceindex:].lstrip(" ")
print float(num)