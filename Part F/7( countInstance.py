class WebBrowser:
    connected = True
    count_instances = 0

    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False
        WebBrowser.count_instances += 1


print(WebBrowser.count_instances)
chrome = WebBrowser('facebook.com')
firefox = WebBrowser('google.com')
print(WebBrowser.count_instances)
