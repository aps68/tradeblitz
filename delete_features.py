import re

with open('c:/tradeblitz.in/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the static features section containing the "01", "02", "03" screenshots
# Since the user wants to remove the sections shown in the screenshot entirely
start_idx = text.find('<section class="features-section" id="features">')
end_idx = text.find('</section>', start_idx) + 10  # include </section>

if start_idx != -1 and end_idx != -1:
    text = text[:start_idx] + text[end_idx:]
    with open('c:/tradeblitz.in/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Deleted features section")
else:
    print("Could not find section")
