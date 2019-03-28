#!/usr/bin/env python
# coding: utf-8

# ## Flask API for Hour of CI Answer Bank

# This script sets up an API answer bank for the Hour of CI project so answers can be retrieved for validation purposes without giving direct access to the students learning the material. 

# In[1]:


from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask import Flask,jsonify,json
import hashlib


# ### Flask App

# ####  Answer Catalog
# 

# In[2]:


# Lesson
    # Beginner or advanced
        # quesition

answer_catalog = {
                  # Lesson Indentation
                  "gateway":
                      # Beginner versus advanced indentation (No Adv for gateway)
                     {
                      "beginner":
                         # Indentation for Questions and Answers 
                         {
                          "Q1":'Giving someone directions in person.',
                          "Q2":"Paying for a meal with cash.", 
                          "Q3":"Purchasing a city bus ticket in person",
                          "Q4": "13",
                          "Q5": "88",
                          "Q6": "volume",
                          "Q7": "13",
                          "Q8": "variety",
                          "Q9": "velocity"
                           }
                      },
                # Lesson Indentation
                  "parallel_programming": 
                       # Beginner versus advanced indentation
                      {
                       "beginner":
                          # Indentation for Questions and Answers 
                          {
                          "Q1":'[1,2,3,4,5]',
                          "Q2":"10", 
                          "Q3":"eating cheesecake",
                          "Q4": "1.00",
                          "Q5":"cyberinfrastructure"
                           },
                       "advanced":
                           {
                          "Q1":'seville',
                          "Q2":"35", 
                          "Q3":"eating cheesecake",
                          "Q4": "1.20",
                          "Q5":"cyberinfrastructure"
                           },
                      }
                     }


# ##### Hashed Answer Catalog
# 
# This was done so we could have lists as asnwers since they cannot be a part of the url and need to be hashed. 

# In[3]:


# Reassign not to overwrite the original answer catalog
hash_answer_catalog = answer_catalog

# Loop through three levels of the dictionary to hash the answers and alter the hash_answer_catalog
for i in hash_answer_catalog:
    for j in hash_answer_catalog[i]:
        for h in hash_answer_catalog[i][j]:
            # Make the answers lowercase to make sure this isnt case sensitive
            lower_answer = hash_answer_catalog[i][j][h].lower()
            
            # Hash the answer using the built-in hash function in Python 
            lower_answer=lower_answer.encode('utf-8')
            hash_object = hashlib.sha256(lower_answer)
            hex_dig = hash_object.hexdigest()
            
            
            # Reassign the answer in the hash_answer_catalog
            hash_answer_catalog[i][j][h] = hex_dig

print(hash_answer_catalog)



# In[ ]:


app = Flask(__name__)
api = Api(app)

# Creates a route for each specified hashed answer
class answer_bank(Resource):
    def get(self, lesson, level, q_id, answer):
        if str(hash_answer_catalog[lesson][level][q_id]) == str(answer):
            result = True
        else:
            result = False
        return result

    

@app.route('/ping')
def welcome():
    return render_template('ping_alive.html')  # render a template

# Adds pages with desired routes. Basic at the moment
api.add_resource(answer_bank, '/<lesson>/<level>/<q_id>/<answer>') # Route_1




if __name__ == '__main__':
    # If you try visiting the host manually to test, you have to use 127.0.0.1 or localhost instead of 0.0.0.0
    # For some reason if the API is not working, try switching the port number here and in Valid section of Hourofci script.
     app.run(host='0.0.0.0', port='5011')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




