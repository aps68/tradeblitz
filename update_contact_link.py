import glob

files = glob.glob('*.html')

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            c = file.read()
    except Exception:
        continue
    
    # Replace the standard contact link
    c = c.replace('<a href="mailto:krishnadevps123@gmail.com">Contact Us</a>', '<a href="contact.html">Contact Us</a>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)
    print(f"Updated {f}")
