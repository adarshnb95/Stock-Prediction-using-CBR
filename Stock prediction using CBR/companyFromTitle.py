from newspaper import Article

url = 'https://www.engadget.com/2017/04/11/microsoft-finally-pulls-the-plug-on-vista/'

def find(url,company):
	article = Article(url)
	article.download()
	article.parse()
	article.nlp()
	text = article.keywords
	print(type(text))
	if company.lower() in article.keywords:
		return True, text
	else:
		return False, []

#print(find(url,'Microsoft'))
