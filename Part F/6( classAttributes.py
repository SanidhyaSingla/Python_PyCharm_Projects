class WebBrowser:
    connected = True

    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False


chrome = WebBrowser('facebook.com')
firefox = WebBrowser('google.com')

print(chrome.__dict__)
print(firefox.__dict__)

# Check class attributes
print(chrome.connected)
print(firefox.connected)

# Change attribute for instance only
chrome.connected = False
print(chrome.__dict__)
print(chrome.connected)

print(firefox.__dict__)
print(firefox.connected)

# Change attribute for all instances
WebBrowser.connected = False
print(chrome.connected)
print(firefox.connected)
