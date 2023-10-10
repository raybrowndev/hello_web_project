# Given Names Route Design Recipe


## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# # Request:
# GET /names?add=Eddie

# # This route should return a list of pre-defined names, plus the name given.

# # Expected response (2OO OK):
# Julia, Alice, Karim, Eddie

```

## 2. Create Examples as Tests


```python
EXAMPLE

"""
when: i request the path /names
and: i use the method get
the: i return a 200 response and the list of predefined names
[Julia, Alice, Karim]
"""

GET /names 
Expected response (200 OK):
Expected response [Julia, Alice, Karim]:


"""
when: i request the path /names?add=Alice
and: i use the method GET
then: i return a 200 response and the predefined names and the added name
[Julia, Alice, Karim, Eddie]
"""

GET /names?add=Eddie
Expected response (200 OK):
Expected response [Julia, Alice, Karim, Eddie]:

```

## 3. Test-drive the Route

```python

def test_get_predefined_names(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ['Julia', 'Alice', 'Karim']


def test_get_predefined_names_and_added_names(web_client):
    response = web_client.post('/names?add=Eddie', data={'add': "Eddie"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ['Julia', 'Alice', 'Karim', 'Eddie']

```