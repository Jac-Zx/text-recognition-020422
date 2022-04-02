#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask


# In[ ]:


from textblob import TextBlob


# In[ ]:


app = Flask(__name__)


# In[ ]:


from flask import request, render_template
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        s = TextBlob(text).sentiment
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




