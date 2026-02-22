import glob

files = glob.glob('*.html')

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            c = file.read()
    except Exception:
        continue
    
    # Replace the standard contact link
    c = c.replace('mailto:hello@tradeblitz.in', 'mailto:krishnadevps123@gmail.com')
    # Replace raw email text (like in privacy policy)
    c = c.replace('hello@tradeblitz.in', 'krishnadevps123@gmail.com')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)
    print(f"Updated {f}")
