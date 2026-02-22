import re

with open('c:/tradeblitz.in/journal.html', 'r', encoding='utf-8') as f:
    journal = f.read()

with open('c:/tradeblitz.in/dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()

if 'chart.js' not in dash:
    dash = dash.replace('</head>', '    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>\n</head>')

# get the whole journal tabs grid
match_grid = re.search(r'(<div class="dashboard-grid".*?>\s*<!-- Log Trade Form -->.*?)</div>\s*</div>\s*</div>\s*</section>', journal, re.DOTALL)
if match_grid:
    grid_content = match_grid.group(1)
    
    dash_tab_journal_pattern = r'<!-- Tab Content 4 -->\s*<div class="tab-content" id="tab-journal">.*?</div>\s*</div>\s*</div>'
    dash = re.sub(dash_tab_journal_pattern, '<!-- Tab Content 4 -->\n<div class="tab-content" id="tab-journal" style="width:100%">\n<div style="margin-bottom:2rem;"><h3>Trade Journal ??</h3><p>Log your trades, document your setups, and track your psychology.</p></div>\n' + grid_content + '</div>\n</div>\n</div>', dash, flags=re.DOTALL)

js_match = re.search(r'(<script>\s*// Set default date to today.*?renderLogs\(\);\s*</script>)', journal, re.DOTALL)
if js_match:
    js_content = js_match.group(1)
    if 'renderLogs()' not in dash:
        dash = dash.replace('</body>', js_content + '\n</body>')

with open('c:/tradeblitz.in/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash)
