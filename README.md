# Algorics Assesment
Python3.7 should be installed and added to PATH
```
$ python --version
Python 3.7.3
```
**Install virtualenv using pip**

    $ pip install virtualenv 
   
 First create a virtual environment for the project.
 
    virtualenv -p python3.7 venv or virtualenv venv
       . $ venv/bin/activate (Linux)
       . $ venv/Scripts/activate (windows)

 **Install dependencies**
```
   $ pip install -r requirements.txt
```
 **Run App using below command**
      
       $ python run .py
        
**API end Point**
**1. fetch all the record using below end point**
- **Input:** pass the page_no and row_size input via query string parameter (row_size decide      number of record in ecah page and page_no for fetch record of particular page) 
- **Method**: [GET]
- **endpoint:** http://127.0.0.1:5000/record?page_no=2&row_size=3 (we can change page_no and row size)
---    

**2.Given a title as input, return all the attributes of that song**
- **Input:** pass the title of the song using query string parameter 
- **Method**: [GET]
- **endpoint:** http://127.0.0.1:5000/songs?title=3AM (invoke this method in Browser , we can also change the title)
---
**2.User should be able to rate a song using star rating**

- **Input:** pass the id and rating of the song using query string parameter (id is use to fetch the particular song to provide rating)
- **Method**: [POST]
- **endpoint:** http://127.0.0.1:5000/rating?id=14p5EKgbPx4U3P1j5JNHeh&rating=3 (here we are giving 3 rating , we can change the id of the song and rating)
---
**Run Unit Test Cases using below command**
            
    $ python -m unittest

You should see the following failing output
    
    .....
    ----------------------------------------------------------------------
    Ran 5 tests in 0.007s
        
    OK

**Run Linter script using below command**
            
    $ sh scripts/lint.sh

You should see the following failing output
 
    --------------------------------------------------------------------
    Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


    --------------------------------------------------------------------
    Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


    --------------------------------------------------------------------
    Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

    

    
