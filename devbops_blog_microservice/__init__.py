from flask import Flask, request
from devbops_blog_microservice.awsmanager import Blog
blog = Blog()
app = Flask(__name__)
### Blog 
### Comment
### Viewing 


@app.route('/createBlog', methods=['POST'])
def create():
    res = request.json
    blogname = res['BlogName']
    blogdate = res['BlogDate']
    blogtime = res['BlogTime']
    username = res['UserName']
    blogcontent = res['BlogContent']
    # blogimage = res['BlogImage']
    bloglocation = res['BlogLocation']
    #blogcomment = res['BlogComment']
    res = blog.put(BlogName=blogname, BlogDate=blogdate, BlogTime=blogtime, UserName=username, BlogContent=blogcontent,BlogLocation=bloglocation, BlogComment={})
    #print(res) ## only here for debugging
    return res
@app.route('/update', methods=['POST'])
def updateBlog():
    res = request.json
    blogname = res['BlogName']
    blogdate = res['New_BlogDate']
    blogtime = res['New_BlogTime']
    blogcontent = res['New_BlogContent']
    # blogimage = res['New_BlogImage']
    bloglocation = res['New_BlogLocation']
    res = blog.update_blog(BlogName=blogname, New_BlogDate=blogdate, New_BlogTime=blogtime, New_BlogContent=blogcontent,  New_BlogLocation=bloglocation)
    return res
@app.route('/delete', methods=['POST'])
def deleteBlog():
    req = request.json
    BlogName = req['BlogName']
    res = blog.delete(BlogName)
    return res
### NEED TO WORK ON COMMENT ###
@app.route('/comment', methods=["POST"])
def comment():
    req = request.json
    BlogName = req['BlogName']
    comment = req['Comment']
    username = req['UserName']
    res = blog.add_comment(BlogName=BlogName, New_Comment=comment, UserName=username) # Does this work?
    return res
    ## generate a commentID by using UUID
    #commentID = UUID()
    #each blog content a unique ID
    #return  commentIDclear
   # return "OK"
@app.route('/view', methods=["GET"])
def viewing():
    res = blog.view()
    return res

@app.route('/history', methods=['POST'])
def history():
    req = request.json
    username = req['UserName']
    res = blog.getAllUserBlog(username)
    return res


if __name__ == '__main__':
    app.run(debug=True)