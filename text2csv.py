#!/usr/bin/python

import pandas as pd
import re
import os


if(len(os.argv) == 2)
	
	file = open(os.argv[1])
	text = file.read()

	email = re.findall(r'([A-Za-z0-9]*@[a-z]*.\w*)',text)

	print(email)
	email_list = pd.DataFrame(email)
	email_list.to_csv('emails.csv')

else
	
	print(f"{os.argv[0] filename.txt}")
