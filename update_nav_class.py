import glob

files = ["dashboard.html", "prep.html", "execute.html", "journal.html", "chat.html"]

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            c = file.read()
    except Exception:
        continue
    
    # Let's add the Trading Class link to the nav links right before AI Chat
    if '<a href="tradingclass.html"' in c:
        continue # already added
        
    c = c.replace('<a href="chat.html">AI Chat</a>', '<a href="tradingclass.html">Trading Class</a>\n                <a href="chat.html">AI Chat</a>')
    c = c.replace('<a href="chat.html" class="active" style="color: #fff;">AI Chat</a>', '<a href="tradingclass.html">Trading Class</a>\n                <a href="chat.html" class="active" style="color: #fff;">AI Chat</a>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)
    print(f"Updated {f}")
