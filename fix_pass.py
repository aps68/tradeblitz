import glob

for f in glob.glob('*.html'):
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
    except UnicodeDecodeError:
        with open(f, 'r', encoding='utf-16') as fp:
            c = fp.read()
            
    if 'akshaypayakkal@gmail.com' in c:
        c = c.replace('placeholder="akshaypayakkal@gmail.com"', 'placeholder="Admin ID"')
        c = c.replace('placeholder="•••••••••"', 'placeholder="Password"')
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print(f"Updated {f}")
