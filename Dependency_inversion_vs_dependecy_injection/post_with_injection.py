class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class PostService:
    def __init__(self, database):
        self.database = database

    def create_post(self, post):
        # Database logic to create a post
        self.database.create(post)

    def get_post(self, post_id):
        # Database logic to retrieve a post by ID
        return self.database.get(post_id)

class Database:
    def create(self, data):
        print("Creating data:", data)

    def get(self, data_id):
        print("Retrieving data with ID:", data_id)

# Dependency Injection
db = Database()
post_service = PostService(database=db)

# Creating a new post
new_post = Post("Sample Title", "This is the content of the post.")
post_service.create_post(new_post)

# Retrieving a post
retrieved_post = post_service.get_post(1)



"""
Is example mein, PostService class ko Database object se inject kiya gaya hai. Dependency Injection se PostService ko pata hota hai ki wo kis Database object ko use karna hai. Isse aap future mein agar database implementation change karna chahte hain toh sirf Database class mein changes karke PostService class ko asar nahi padega.

Dependency Injection se aap bina kisi direct dependency ko class mein create kiye bina, code ke different parts ko easily replace aur test kar sakte hain.

"""