#!/usr/bin/python

import pandas as pd
import re

file = open('sample.txt')
text = file.read()

email = re.findall(r'([A-Za-z0-9]*@[a-z]*.\w*)',text)

print(email)
email_list = pd.DataFrame(email)
email_list.to_csv('emails.csv')