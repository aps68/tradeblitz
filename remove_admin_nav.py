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
    
    # Remove the Admin button from the navbar
    pattern = r'<button[^>]*>Admin</button>'
    new_c = re.sub(pattern, '', c)
    
    # Keep the button in the footer
    # Also fix any empty divs that might have resulted
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_c)
    print(f"Updated {f}")
