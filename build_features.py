import re

# Read the backup to get the base structure without features
with open('c:/tradeblitz.in/index_backup.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Get the giant journal mockup from index_backup.html
start_journal_mock = text.find('<div class="glass-box mockup" style="padding: 1.5rem; background: #0b0d17;">')
end_journal_mock = text.find('<!-- Equity Curve Mockup -->', start_journal_mock)
end_journal_mock = text.find('</div>', text.find('</svg>', end_journal_mock))
end_journal_mock = text.find('</div>', end_journal_mock + 1)
end_journal_mock = text.find('</div>', end_journal_mock + 1)
journal_mockup = text[start_journal_mock:end_journal_mock + 6]

# Create the features section
features_section = f"""    <section class="features-section" id="features">
        <div class="container">
            <div class="feature-row">
                <div class="feature-content">
                    <span class="feature-num">01</span>
                    <h2 class="feature-title">Fast & Precise Execution</h2>
                    <p class="feature-desc">Enter and exit the market instantly. Automatically calculate risk, lock in
                        your stop-losses, and execute flawlessly without second-guessing.</p>
                    <ul class="feature-list">
                        <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="flex-shrink:0"
                                xmlns="http://www.w3.org/2000/svg">
                                <rect width="24" height="24" rx="6" fill="#10B981" />
                                <path d="M7 12L10.5 15.5L18 8" stroke="white" stroke-width="2.5" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg> Auto-calculate position size</li>
                        <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="flex-shrink:0"
                                xmlns="http://www.w3.org/2000/svg">
                                <rect width="24" height="24" rx="6" fill="#10B981" />
                                <path d="M7 12L10.5 15.5L18 8" stroke="white" stroke-width="2.5" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg> Strict Pre-Trade Execution Gate</li>
                        <li><svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="flex-shrink:0"
                                xmlns="http://www.w3.org/2000/svg">
                                <rect width="24" height="24" rx="6" fill="#10B981" />
                                <path d="M7 12L10.5 15.5L18 8" stroke="white" stroke-width="2.5" stroke-linecap="round"
                                    stroke-linejoin="round" />
                            </svg> Mandatory Strategy Checklist</li>
                    </ul>
                </div>
                <div class="feature-visual">
                    <div class="glass-box mockup">
                        <div class="mockup-header text-green"
                            style="display: flex; align-items: center; justify-content: space-between;">Execute
                            Trade <svg width="20" height="20" viewBox="0 0 24 24" fill="#f97316"
                                stroke="#f97316" stroke-linejoin="round" stroke-linecap="round">
                                <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
                            </svg></div>
                        <div class="mockup-task">Risk: 1% ($100)</div>
                        <div class="mockup-task">Size: 2.5 Lots</div>
                    </div>
                </div>
            </div>

            <div class="feature-row reverse">
                <div class="feature-content">
                    <span class="feature-num">02</span>
                    <h2 class="feature-title">Unbreakable Risk Control</h2>
                    <p class="feature-desc">Stop revenge trading before it happens. Guard your capital with hard-coded
                        platform blocks tailored to your own custom limits.</p>
                    <ul class="feature-list">
                        <li><span style="font-size: 1.3rem; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));">🛡️</span>
                            Custom Max Trades Per Day</li>
                        <li><span style="font-size: 1.3rem; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));">🛡️</span>
                            Max Loss Lockout</li>
                        <li><span style="font-size: 1.3rem; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));">🛡️</span>
                            Account Drawdown Protection</li>
                    </ul>
                </div>
                <div class="feature-visual">
                    <div class="glass-box">
                        <div class="lock-ui"
                            style="background: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239,68,68,0.2); padding: 2rem; border-radius: 12px; text-align: center; box-shadow: inset 0 0 10px rgba(239, 68, 68, 0.1);">
                            <div class="lock-icon"
                                style="font-size: 3.5rem; margin-bottom: 1rem; filter: drop-shadow(0 4px 6px rgba(239, 68, 68, 0.3));">
                                🔒</div>
                            <div class="lock-text"
                                style="color: #ef4444; font-weight: 600; font-size: 1.2rem; line-height: 1.4;">Max Limit
                                Hit.<br>Terminal Locked.</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="feature-row">
                <div class="feature-content">
                    <span class="feature-num">03</span>
                    <h2 class="feature-title">Intelligent AI Journaling</h2>
                    <p class="feature-desc">Let AI review your performance. Visually track your equity over time and
                        receive actionable psychological insights backed by your own data.</p>
                    <ul class="feature-list">
                        <li>⚡ Detailed Manual Trade Logging</li>
                        <li>⚡ Interactive Equity Curve</li>
                        <li>⚡ AI-Driven Coaching & Insights</li>
                    </ul>
                </div>
                <div class="feature-visual">
                    {journal_mockup}
                </div>
            </div>
        </div>
    </section>
"""

# Now we need to remove the routine section from index_backup.html
# because the user prefers the edgeflo design over the tabs entirely!
# "CHANGE ALL THIS AND ADD WHAT HAVE IN DASHBOARD PAGE ADD THAT" -> they want to replace the tabs with the edgeflo sections containing dashboard items.

start_routine = text.find('<!-- NEW INTERACTIVE TABBED SECTION -->')
if start_routine == -1:
    start_routine = text.find('<section class="routine-section"')

# Replace routine with features section!
end_routine = text.find('</section>', start_routine) + 10

new_text = text[:start_routine] + features_section + '\n\n' + text[end_routine:]

with open('c:/tradeblitz.in/index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Restored features section with dashboard mockups into index.html!")
