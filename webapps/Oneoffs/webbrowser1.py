import webbrowser
webbrowser.get(using='chrome')
url = 'http://docs.python.org/'
# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)
webbrowser.open(url, new=0, autoraise=True)
