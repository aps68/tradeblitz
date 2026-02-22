import re

with open('c:/tradeblitz.in/dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()

with open('c:/tradeblitz.in/index.html', 'r', encoding='utf-8') as f:
    index = f.read()

# Find the journal tab in dashboard
start_dash = dash.find('<div class="tab-content" id="tab-journal">')
end_dash = dash.find('</section>', start_dash)
tab_content = dash[start_dash:end_dash].strip()
idx1 = tab_content.rfind('</div>')
tab_content = tab_content[:idx1 + 6]

# Find the journal tab in index
start_index = index.find('<div class="tab-content" id="tab-journal">')
# Look for the last element in the old code block in index.html to find end
end_index = index.find('</div>', index.find('<div class="mockup-task">Setup: A+ Breakout</div>'))
end_index = index.find('</div>', end_index + 1) # closes mockup task
end_index = index.find('</div>', end_index + 1) # closes mockup header
print("tab content length:", len(tab_content))

new_index = index[:start_index] + tab_content + '\n' + index[end_index + 6:]

with open('c:/tradeblitz.in/index.html', 'w', encoding='utf-8') as f:
    f.write(new_index)

print('Copied tab-journal block to index.html!')
