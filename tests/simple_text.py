import protatoquests

def test():
    response = protatoquests.get("https://www.google.com")
    response.raise_for_status()
    print(response.text)
    assert "https://www.google.com" in response.text