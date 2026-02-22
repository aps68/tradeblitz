import glob

files = ["dashboard.html", "prep.html", "execute.html", "journal.html", "chat.html", "index.html"]

old_nav = """            <div style="display: flex; gap: 1rem; align-items: center;">
                <a href="index.html" class="btn-nav">Log Out</a>
                <button onclick="document.getElementById('adminModal').style.display='flex'" class="btn-nav" style="background: rgba(245, 158, 11, 0.1); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.3); padding: 0.8rem 1.5rem; cursor: pointer; margin: 0;">Admin</button>
            </div>"""

new_nav = """            <div style="display: flex; gap: 1rem; align-items: center;">
                <a href="index.html" class="btn-nav">Log Out</a>
            </div>"""

old_footer = """            <div class="footer-links">
                <a href="#">Privacy Policy</a>
                <a href="#">Terms of Service</a>
                <a href="mailto:hello@tradeblitz.in">Contact Us</a>
            </div>"""

new_footer = """            <div class="footer-links">
                <a href="#">Privacy Policy</a>
                <a href="#">Terms of Service</a>
                <a href="mailto:hello@tradeblitz.in">Contact Us</a>
                <a href="#" onclick="event.preventDefault(); document.getElementById('adminModal').style.display='flex'">Admin</a>
            </div>"""

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
    except Exception:
        continue
    c = c.replace(old_nav, new_nav)
    c = c.replace(old_footer, new_footer)
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)
    print(f"Updated {f}")
