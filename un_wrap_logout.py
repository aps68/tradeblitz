import glob
import re

for f in glob.glob('*.html'):
    if f == 'admin.html':
        continue
    try:
        with open(f, 'r', encoding='utf-8') as file:
            c = file.read()
    except Exception:
        continue
    
    # Replace the empty div wrapper with just the logout button
    pattern = r'<div style="display: flex; gap: 1rem; align-items: center;">\s*<a href="index.html" class="btn-nav">Log Out</a>\s*</div>'
    new_c = re.sub(pattern, '<a href="index.html" class="btn-nav">Log Out</a>', c)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_c)
    print(f"Updated {f}")
