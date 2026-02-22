import re

with open('c:/tradeblitz.in/dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

correct_mockup_html = """<!-- Tab Content 4 -->
                    <div class="tab-content" id="tab-journal">
                        <div class="tab-info">
                            <h3>Trade Journal 📖</h3>
                            <p>Log your trades, document your setups, and track your psychology.</p>
                        </div>
                        <div class="tab-image">
                            <div class="glass-box mockup" style="padding: 1.5rem; background: #0b0d17;">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                                    <div style="font-weight: 800; color: #fff; font-size: 1.2rem; display: flex; align-items: center; gap: 0.5rem;"><span style="font-size: 1.5rem;">📊</span> Recent Logs</div>
                                    <div style="display: flex; gap: 0.5rem; align-items: center;">
                                        <div style="background: rgba(16, 185, 129, 0.2); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.4); padding: 0.3rem 0.6rem; border-radius: 6px; font-weight: 700; font-size: 0.75rem;">📥 Save CSV</div>
                                        <div style="color: #64748b; font-size: 0.75rem; background: #12141f; padding: 0.3rem 0.6rem; border-radius: 6px;">Total: <strong style="color:#fff;">1</strong></div>
                                    </div>
                                </div>
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                                    <div style="background: #12141f; padding: 1.2rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); text-align: center;">
                                        <div style="color: #94a3b8; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; margin-bottom: 0.8rem;">Win Rate</div>
                                        <div style="width: 80px; height: 80px; border-radius: 50%; border: 6px solid #10b981; display: flex; align-items: center; justify-content: center; margin: 0 auto; box-shadow: inset 0 0 10px rgba(16,185,129,0.2);">
                                            <span style="color: #fff; font-weight: 800; font-size: 1.3rem;">100%</span>
                                        </div>
                                    </div>
                                    <div style="background: #12141f; padding: 1.2rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); display: flex; flex-direction: column; justify-content: center; gap: 0.8rem;">
                                        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8; font-size: 0.75rem; font-weight: 700;">TOTAL TRADES</span><span style="color: #fff; font-weight: 800; font-size: 0.9rem;">1</span></div>
                                        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8; font-size: 0.75rem; font-weight: 700;">TOTAL P&L</span><span style="color: #10b981; font-weight: 800; font-size: 0.9rem;">+$100.00</span></div>
                                        <div style="display: flex; justify-content: space-between;"><span style="color: #94a3b8; font-size: 0.75rem; font-weight: 700;">WINS / LOSSES</span><span style="color: #fff; font-weight: 600; font-size: 0.9rem;"><span style="color:#10b981">1</span> / <span style="color:#ef4444">0</span></span></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>"""

# Find the start of the injected tab-journal block
start_idx = html.find('<!-- Tab Content 4 -->')
# Find the closing </section> tag which tells us where to stop deleting
end_idx = html.find('</section>', start_idx)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + correct_mockup_html + '\n                    ' + html[end_idx:]

# Remove the script that was injected
script_start = html.find('<script>\n        // Set default date to today')
if script_start != -1:
    script_end = html.find('</script>', script_start)
    if script_end != -1:
        # include the closing script tag in the removal
        html = html[:script_start] + html[script_end + 9:]

# Remove empty injected chart.js script from head
html = html.replace('    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>\n', '')

with open('c:/tradeblitz.in/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)
