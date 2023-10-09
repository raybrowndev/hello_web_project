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

def test_sort_names_one_name(web_client):
    response = web_client.post('/sort-names', data={'names': "John"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "John"

"""
When: I make a POST request to /sort-names
And: I send a string containing comma-seperates names
Then: I get a 200 response and string containing comma seperated names sort alphabetically
STRING WITH TWO NAMES IN CORRECT ORDER - RETURN SAME INPUT 
"""

def test_sort_names_two_names(web_client):
    response = web_client.post('/sort-names', data={'names': "John,Mary"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "John,Mary"

"""
When: I make a POST request to /sort-names
And: I send a string containing comma-seperates names
Then: I get a 200 response and string containing comma seperated names sort alphabetically
STRING WITH TWO NAMES IN REVERSE ORDER 
"""
def test_sort_names_two_names_reverse(web_client):
    response = web_client.post('/sort-names', data={'names': "Mary,John"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "John,Mary"

"""
When: I make a POST request to /sort-names
And: I send a string containing comma-seperates names
Then: I get a 200 response and string containing comma seperated names sort alphabetically
STRING MULTIPLE NAMES IN RANDOM ORDER - "Alice,Joe,Julia,Kieran,Zoe"
"""

def test_sort_names_multiple_names_random(web_client):
    response = web_client.post('/sort-names', data={'names': "Joe,Alice,Zoe,Julia,Kieran"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Julia,Kieran,Zoe"