class Articles:
    '''
    Articles class that stores news articles objects
    '''
    def __init__(self,author,title,description,url,image,date):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date
        
        