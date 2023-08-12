from drivers import Browser,ChromeBrowser,FireFoxBrowser


class BrowserFactory:
    def __init__(self):
        self.last_browser = None

    def get_browser(self, name):
        self.last_browser = name
        if name == 'chrome':
            return ChromeBrowser()
        elif name == 'firefox':
            return FireFoxBrowser()
        else:
            raise Exception('wrong browser type')

our_browser_factory = BrowserFactory()
chrome1 = our_browser_factory.get_browser('chrome')
chrome2 = our_browser_factory.get_browser('chrome')
ff = our_browser_factory.get_browser('firefox')
print()