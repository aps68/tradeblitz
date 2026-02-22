import re

with open('c:/tradeblitz.in/index_backup.html', 'r', encoding='utf-8') as f:
    backup_html = f.read()

with open('c:/tradeblitz.in/index.html', 'r', encoding='utf-8') as f:
    current_html = f.read()

# Extract the Execution mockup from current_html
exec_start = current_html.find('<div class="glass-box mockup">', current_html.find('Execute With Precision'))
exec_end = current_html.find('</div>\n                </div>', exec_start)
exec_end = current_html.rfind('</div>', 0, exec_end)
exec_end = current_html.rfind('</div>', 0, exec_end) + 6
exec_mockup = current_html[exec_start:exec_end]

# Extract the Journal mockup from current_html
journal_start = current_html.find('<div class="glass-box mockup"', current_html.find('Intelligent AI Journaling'))
journal_end = current_html.find('<!-- Equity Curve Mockup -->', journal_start)
# We need the whole visual for journal
visual_start = current_html.find('<div class="feature-visual">', current_html.find('Intelligent AI Journaling'))
visual_end = current_html.find('</div>\n            </div>', visual_start)
journal_full_mockup = current_html[visual_start + 28 : visual_end].strip()

# Now extract the routine-section from backup_html
routine_start = backup_html.find('<!-- NEW INTERACTIVE TABBED SECTION -->')
if routine_start == -1:
    routine_start = backup_html.find('<section class="routine-section"')
routine_end = backup_html.find('</section>', routine_start) + 10
routine_section = backup_html[routine_start:routine_end]

# Now let's inject our custom mockups into the routine_section
# In backup_html, tab-execute's image is around "Execute Trade"
old_exec_start = routine_section.find('<div class="glass-box mockup">', routine_section.find('id="tab-execute"'))
old_exec_end = routine_section.find('</div>', routine_section.find('<div class="mockup-task">Size: 2.5 Lots</div>')) + 6
old_exec_end = routine_section.find('</div>', old_exec_end) + 6
routine_section = routine_section[:old_exec_start] + exec_mockup + routine_section[old_exec_end:]

# In backup_html, tab-journal's image is around "Recent Logs"
old_journal_start = routine_section.find('<div class="glass-box mockup"', routine_section.find('id="tab-journal"'))
old_journal_end = routine_section.find('</div>', routine_section.find('WINS / LOSSES'))
# there are many divs, let's just replace the entire tab-image inner content
ti_start = routine_section.find('<div class="tab-image">', routine_section.find('id="tab-journal"')) + 23
ti_end = routine_section.find('</div>\n                    </div>\n\n                </div>', ti_start)
routine_section = routine_section[:ti_start] + '\n' + journal_full_mockup + '\n                        ' + routine_section[ti_end:]


# We will also add some CSS margin to make the graph fit well nicely.
routine_section = routine_section.replace('style="padding: 1.5rem; background: #0b0d17;"', 'style="padding: 1.5rem; background: #0b0d17; width: 100%;"')

# Now completely replace features-section in current_html with our new routine_section
feat_start = current_html.find('<section class="features-section"')
feat_end = current_html.find('</section>', feat_start) + 10

new_html = current_html[:feat_start] + routine_section + current_html[feat_end:]

# Remove empty display:flex artifacts if any
with open('c:/tradeblitz.in/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully replaced features with row-wise tabs containing dashboard components!")
