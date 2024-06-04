import json     
from mongoengine.errors import NotUniqueError

from models import Author, Quote

if "__name__"=="__maim__":
    with open("author.json", encoding="utf-8") as ath:
        data = json.load(ath)
        for el in data:
            try:
                author = Author(
                    fullname = el.get("fullname"),
                    born_date=el.get("born_date"),
                    born_location=el.get("born_location"),
                    description=el.get("description")
                )
                
                author.save()
            except NotUniqueError:
                print(f"The author already exists {el.get('fullname')}")    
                
    with open ("quotes.json", encoding="uft-8") as qu:
        data = json.load(qu)
        
        for el in data:
            author, *_ = Author.objects(fullname = el.get("author"))
            
            quote = Quote(quote=el.get("quote"), tags=el.get("tags"), author=author)
            
            quote.save()