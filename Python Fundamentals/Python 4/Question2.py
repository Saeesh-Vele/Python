class Book:
    reviews = []
    def __init__ (self , title , author):
        self.title = title
        self.author = author
        
    @classmethod
    def new_review(cls , review):
        cls.reviews.append(review)
        
    @classmethod
    def count_reviews(cls):
        print(f"The number of reviews is {len(cls.reviews)}")
        
    @classmethod
    def display_reviews(cls):
        print(cls.reviews)
        
    
Book.new_review("Hi")
Book.new_review("Bro")
Book.count_reviews()
Book.display_reviews()