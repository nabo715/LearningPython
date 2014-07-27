text = "X-DSPAM-Confidence:    0.8475";
strt_pos = text.find('.')
new_text = text[strt_pos-1:]
conv_text = float(new_text)
print conv_text
