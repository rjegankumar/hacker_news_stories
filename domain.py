import read
import pandas as pd

def split_str(s):
	if type(s) == float or s.find('.') == -1:
		return s
	split_s = s.split('.', maxsplit=1)[1]
	if split_s.find('.') == -1 or split_s.find('co.') == 0 or split_s.find('com.') == 0:
		return s
	else:
		return split_s

if __name__=="__main__":
	hn = read.load_data()	
	hn['domain_url'] = hn['url'].apply(split_str)
	hn_domains = hn['domain_url'].value_counts(sort=True)
	pd.set_option('display.max_rows',100)
	print(hn_domains.head(100))
	
