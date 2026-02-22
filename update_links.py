import glob

files = ["dashboard.html", "prep.html", "execute.html", "journal.html", "chat.html", "index.html"]

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
    except Exception:
        continue

    # Update Privacy Policy
    # We look for something like <a href="#">Privacy Policy</a>
    c = c.replace('<a href="#">Privacy Policy</a>', '<a href="privacy.html">Privacy Policy</a>')
    
    # Update Terms of Service
    c = c.replace('<a href="#">Terms of Service</a>', '<a href="terms.html">Terms of Service</a>')
    
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)
    print(f"Updated {f}")
