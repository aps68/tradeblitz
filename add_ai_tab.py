import os
import re

files_to_update = ['index.html', 'dashboard.html']

ai_tab_button = '<button class="tab-btn" data-tab="ai">AI SUPPORT</button>'

ai_tab_content = """

                    <!-- Tab Content - AI Support -->
                    <div class="tab-content" id="tab-ai">
                        <div class="tab-info" style="padding-top: 1rem;">
                            <h3 style="font-size: 2.8rem; letter-spacing: -1px; margin-bottom: 1rem;">TradeBlitz AI Support 🤖</h3>
                            <p style="font-size: 1.15rem; color: #94a3b8; line-height: 1.6; max-width: 450px;">Struggling with a setup? Mindset getting foggy? Talk to your personal trading assistant.</p>
                        </div>
                        <div class="tab-image">
                            <div class="glass-box mockup" style="padding: 2rem; background: #0b0d17; display: flex; flex-direction: column; gap: 2rem; border: 1px solid rgba(59, 130, 246, 0.2); box-shadow: 0 0 20px rgba(59, 130, 246, 0.05);">
                                <div style="display: flex; gap: 1rem; align-items: flex-start;">
                                    <div style="font-size: 1.5rem; background: rgba(59, 130, 246, 0.2); padding: 0.5rem; border-radius: 50%;">🤖</div>
                                    <div style="background: #12141f; padding: 1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); color: #e2e8f0; font-size: 0.95rem; line-height: 1.5; border-top-left-radius: 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                                        Hello! I am TradeBlitz AI. I am here to help you analyze your setups and master your trading psychology. Notice your emotions shifting? Fire away!
                                    </div>
                                </div>
                                <div style="display: flex; gap: 1rem; align-items: flex-start; flex-direction: row-reverse;">
                                    <div style="font-size: 1.5rem; background: rgba(245, 158, 11, 0.2); padding: 0.5rem; border-radius: 50%;">👤</div>
                                    <div style="background: rgba(59, 130, 246, 0.15); padding: 1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(59, 130, 246, 0.3); color: #e2e8f0; font-size: 0.95rem; line-height: 1.5; border-top-right-radius: 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                                        I just took two big losses in a row and I want to double my size. What should I do?
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>"""

for f in files_to_update:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            c = file.read()
    except Exception:
        continue
        
    if 'data-tab="ai"' in c:
        continue
        
    # Append the button
    c = c.replace('<button class="tab-btn" data-tab="journal">JOURNAL</button>', '<button class="tab-btn" data-tab="journal">JOURNAL</button>\n                    ' + ai_tab_button)
    
    # We need to inject the tab-content cleanly.
    # The end of tab-journal is the <circle cx="100" cy="0" r="2" fill="#0f111a" stroke="#3b82f6" stroke-width="1.5"></circle> ... block.
    # Because whitespace can be flaky, I will do a regex sub or replace a known smaller block.
    
    target = '</svg>\n                                </div>\n                            </div>\n                        </div>\n                    </div>'
    
    if target in c:
        c = c.replace(target, target + ai_tab_content)
    else:
        print(f"Failed to find target block in {f}")
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)
    print(f"Updated {f}")
