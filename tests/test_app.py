# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""
When: I make a POST request to /count_vowels
And: I send "AEioUBcDfG" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_upper_and_lowercase(web_client):
    response = web_client.post('/count_vowels', data={'text': 'AEioUBcDfG'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "AEioUBcDfG"'


"""
When: I make a POST request to /sort-names
And: I send a string containing comma-seperates names
Then: I get a 200 response and string containing comma seperated names sort alphabetically
EMPTY STRING
"""
def test_post_sort_names_empty_string(web_client):
    response = web_client.post('/sort-names', data={'names': ""})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""

"""
When: I make a POST request to /sort-names
And: I send a string containing comma-seperates names
Then: I get a 200 response and string containing comma seperated names sort alphabetically
STRING WITH ONE NAME
"""

def test_post_sort_names_one_name(web_client):
    response = web_client.post('/sort-names', data={'names': "John"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "John"

"""
When: I make a POST request to /sort-names
And: I send a string containing comma-seperates names
Then: I get a 200 response and string containing comma seperated names sort alphabetically
STRING WITH TWO NAMES IN CORRECT ORDER - RETURN SAME INPUT 
"""

def test_post_sort_names_two_names(web_client):
    response = web_client.post('/sort-names', data={'names': "John,Mary"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "John,Mary"

"""
When: I make a POST request to /sort-names
And: I send a string containing comma-seperates names
Then: I get a 200 response and string containing comma seperated names sort alphabetically
STRING WITH TWO NAMES IN REVERSE ORDER 
"""
def test_post_sort_names_two_names_reverse(web_client):
    response = web_client.post('/sort-names', data={'names': "Mary,John"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "John,Mary"

"""
When: I make a POST request to /sort-names
And: I send a string containing comma-separated names
Then: I get a 200 response and string containing comma separated names sorted alphabetically
STRING MULTIPLE NAMES IN RANDOM ORDER - "Alice,Joe,Julia,Kieran,Zoe"
"""

def test_post_sort_names_multiple_names_random(web_client):
    response = web_client.post('/sort-names', data={'names': "Joe,Alice,Zoe,Julia,Kieran"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Julia,Kieran,Zoe"

"""
When: I make a GET request to /names
And: I do not provide an `add` parameter
Then: I get a response of the pre-defined names sorted in alphabetical order
"""
def test_get_names_without_add_parameter(web_client):
    response = web_client.get('/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Julia, Karim"

"""
When: I make a GET request to /names
And: I provide "Eddie" for the value of the `add` parameter
Then: I get a response containing "Eddie" in correct alphabetical order
"""
def test_get_names_with_one_additional_name(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Eddie, Julia, Karim"

"""
When: I make a GET request to /names
And: I provide "Leo" for the value of the `add` parameter
Then: I get a response containing "Leo" in correct alphabetical order
"""
def test_get_names_with_one_additional_name_2(web_client):
    response = web_client.get('/names?add=Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Julia, Karim, Leo"

"""
When: I make a GET request to /names
And: I provide "Eddie,Leo" for the value of the `add` parameter
Then: I get a response of "Alice, Eddie, Julia, Karim, Leo"
"""
def test_get_names_with_two_additional_names(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Eddie, Julia, Karim, Leo"

"""
When: I make a GET request to /names
And: I provide "Leo,Eddie" for the value of the `add` parameter
Then: I get a response of "Alice, Eddie, Julia, Karim, Leo"
"""
def test_get_names_with_two_additional_names_2(web_client):
    response = web_client.get('/names?add=Leo,Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Eddie, Julia, Karim, Leo"

"""
When: I make a GET request to /names
And: I provide already existing pre-defined names
Then: I get a response containing repeated names (as it's possible for two people to have the same first name)
"""
def test_get_names_with_repeated_predefined_names(web_client):
    response = web_client.get('/names?add=Karim,Alice')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice, Alice, Julia, Karim, Karim"
