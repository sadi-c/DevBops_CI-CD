import boto3
from boto3.dynamodb.conditions import Attr, Key


# Using DevBops_blog
# Columns are : "BlogName", "BlogDate", "BlogTime", "UserName", "BlogContent", "BlogLocation", "BlogComment"
# BlogCommnet should be a dictionary, key is the userid, value is their comments
# Response template:
# Using DevBops_blog
# Columns are : "BlogName", "BlogDate", "BlogTime", "UserName", "BlogContent", "BlogLocation", "BlogComment"
# BlogCommnet should be a dictionary, key is the userid, value is their comments
###Response template:
# return {
#                "Result": False or True,
#                "Error": None or errorMessage,
#                "Description": "",
#                "BlogID": None or blogID
#            }
class Blog:
    def __init__(self):
        self.__Tablename__ = "DevBops_blog"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "blogName"
        self.Primary_key = "blogName"
        self.columns = ["BlogDate", "BlogTime", "UserName", "BlogContent", "BlogLocation", "BlogComment"]
        self.table = self.DB.Table(self.__Tablename__)

    def put(self, BlogName, BlogDate, BlogTime, UserName, BlogContent, BlogLocation, BlogComment):

        # cehck if blog exists, if exists, then immediately return false
        if (self.check_blog_exists(BlogName)):
            # immediately return false
            return {
                "Result": False,
                "Error": "Blog cannot be created",
                "Description": "Blog name already exists",
                "BlogName": None
            }

        # all_items = self.table.scan()
        # last_primary_key = len(all_items['Items']) +1

        response = self.table.put_item(
            Item={
                self.Primary_Column_Name: BlogName,
                # self.columns[0]: BlogName,
                self.columns[0]: BlogDate,
                self.columns[1]: BlogTime,
                self.columns[2]: UserName,
                self.columns[3]: BlogContent,
                self.columns[4]: BlogLocation,
                self.columns[5]: BlogComment
            }
        )
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return {
                "Result": True,
                "Error": None,
                "Description": "Blog was created succesfully",
                "BlogName": BlogName

            }
        else:
            return  {
                "Result": False,
                "Error": "Database error",
                "Description": "Database error",
                "BlogName": None
            }

    def check_blog_exists(self, BlogName):
        response = self.table.scan(
            FilterExpression=Attr("blogName").eq(BlogName)
        )
        if response["Items"]:
            # We found blog already exists
            return True
        else:
            return False

    def update_blog(self, BlogName, New_BlogDate, New_BlogTime, New_BlogContent, New_BlogLocation):

        response = self.table.scan(
            FilterExpression=Attr("blogName").eq(BlogName)
        )
        if response["Items"]:
            # ###### TODO: use update_item insetad of put_item
            # self.Primary_key = response["Items"][0]["blogID"]
            # self.Primary_key = response["Items"][0]["blogName"]
            res = self.table.update_item(
                Key={
                    'blogName': BlogName,

                },
                UpdateExpression="set BlogDate=:d, BlogTime=:t, BlogLocation=:l, BlogContent=:c",
                ExpressionAttributeValues={
                    # ':n': New_BlogName,
                    ':d': New_BlogDate,
                    ':t': New_BlogTime,
                    ':l': New_BlogLocation,
                    ':c': New_BlogContent
                }
                # ReturnValues="UPDATED_NEW"

            )
            # return res
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return {
                    "Result": True,
                    "Error": None,
                    "Description": "Blog was updated succesfully",

                    "BlogName": None
                }
            else:
                return {
                    "Result": False,
                    "Error": "Database error",
                    "Description": "Database error",
                    "BlogName": None
                }
        else:
            return {
                "Result": False,
                "Error": "Blog not found",
                "Description": "Cannot updated",
                "BlogName": None
            }

    def delete(self, BlogName):
        response = self.table.scan(
            FilterExpression=Attr("blogName").eq(BlogName)
        )
        if response["Items"]:
            self.Primary_key = response["Items"][0]["blogName"]
            res = self.table.delete_item(
                Key={
                    self.Primary_Column_Name: self.Primary_key
                }
            )
            return {
                "Result": True,
                "Error": None,
                "Description": "Blog was deleted"
            }
        else:
            return {
                "Result": False,
                "Error": "Blog does not exists",
                "Description": "Error"
            }

    def view(self):
        res = self.table.scan()

        return {
            "Result": True,
            "Error": None,
            "Description": "All blog from database",
            "BlogDB": res['Items']
        }
        # return res['Items']

    def add_comment(self, BlogName, New_Comment, UserName):
        response = self.table.scan(
            FilterExpression=Attr("blogName").eq(BlogName)
        )
        if response["Items"]:

            # {"user1": "comment", "user2": "comment"}

            # ###### TODO: use update_item insetad of put_item
            # self.Primary_key = response["Items"][0]["blogID"]
            # self.Primary_key = response["Items"][0]["blogName"]
            res = self.table.update_item(
                Key={
                    'blogName': BlogName,

                },

                # UpdateExpression="set BlogComment= list_append(BlogComment, :i)",

                UpdateExpression="SET BlogComment.#username = :comment",
                ExpressionAttributeNames={
                    "#username": UserName
                },
                ExpressionAttributeValues={
                    ":comment": New_Comment
                }

            )
            # return res
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return {
                    "Result": True,
                    "Error": None,
                    "Description": "Comment was updated succesfully",

                    "BlogName": None
                }
            else:
                return {
                    "Result": False,
                    "Error": "Database error",
                    "Description": "Database error",
                    "BlogName": None
                }
        else:
            return {
                "Result": False,
                "Error": "Blog not found",
                "Description": "Cannot add comment",
                "BlogName": None
            }

    def getAllUserBlog(self, username):
        response = self.table.scan()['Items']
        lst = []
        if len(response) > 0:
            for d in response:
                if d['UserName'] == username:
                    lst.append(d)
            return {
                "Result": True,
                "Error": None,
                "Description": "All blog this user created",
                "BlogsDB": lst
            }
        else:
            return {
                "Result": False,
                "Error": "No blogs for this user",
                "Description": "This user haven't post any blogs yet.",
                "BlogsDB": lst
            }


if __name__ == "__main__":
    blog = Blog()
    # for create new post
    # res = blog.put(BlogName="BlogService", BlogDate="OCT 10,2020", BlogTime="1 PM", UserName="Sadika", BlogContent="Almost There",  BlogLocation="NY",BlogComment={})
    # res = blog.put(BlogName="Saturday Live", BlogDate="OCT 10,2020", BlogTime="10 AM", UserName="Dolma", BlogContent="We are Live Today",  BlogLocation="NY",BlogComment={})
    # res = blog.put(BlogName="Three", BlogDate="OCT 9,2020", BlogTime="10 AM", UserName="Chandler", BlogContent="Making new",  BlogLocation="NY",BlogComment={})
    # for update post
    # res = blog.update_blog(BlogName="Saturday Live", New_BlogDate='OCT 09, 2020', New_BlogTime='5 PM', New_BlogContent='update workingV1',  New_BlogLocation="NY")

    # for delete
    # res = blog.delete("Saturday")

    # for view
    # res = blog.view()

    # for comment
    # res=blog.add_comment("Learning","Comment1","Sadika")
    # res=blog.add_comment("Saturday Live","Comment3","Dolma")
    # res=blog.add_comment("Saturday Live","NewComment","Sadika")
    # res=blog.add_comment("Saturday Live","Comment2","Chandler")

    print(blog.getAllUserBlog('zxcvzcxv'))

# print (res)
