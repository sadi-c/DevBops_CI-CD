# Primary Key = BlogName
    You can upload blogs, add comments, and view photos on the

# Using DevBops_blog
    Columns are : "BlogName", "BlogDate", "BlogTime", "UserName", "BlogContent", "BlogLocation", "BlogComment"
    BlogCommnet should be a dictionary, key is the userid, value is their comments
    
# Response template:
    return {
    "Result": False or True,
    "Error": None or errorMessage,
     "Description": "",
    "BlogID": None or blogID
    }

    
