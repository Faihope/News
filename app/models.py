class Articles:
    '''
    Articles class that stores news articles objects
    '''
    def __init__(self,id,author,title,description,url,image,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date
        
class Source:
    '''
    Source class to define News source Objects 
    '''
    
    def __init__(self,id,name,description,url,category,language,country):
        self.id= id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language =language
        self.country =country
        
      