#!/usr/bin/python3

import pandas as pd
import re
import sys


if(len(sys.argv) == 2):
	
	file = open(sys.argv[1])
	text = file.read()

	email = re.findall(r'([A-Za-z0-9]*@[a-z]*.\w*)',text)

	print(email)
	email_list = pd.DataFrame(email)
	email_list.to_csv('emails.csv')

else:
	
	print(f"Usage : {sys.argv[0] filename.txt}")
