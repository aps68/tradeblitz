import glob

files = glob.glob('*.html')

bgm_html = """
    <!-- Ambient BGM Player -->
    <audio id="bgmAudio" loop preload="auto">
        <source src="background.mp3" type="audio/mpeg">
    </audio>
    <button id="bgmToggle" title="Toggle Ambient Music" style="position: fixed; bottom: 20px; left: 20px; z-index: 9999; background: rgba(11, 13, 23, 0.8); border: 1px solid rgba(255,255,255,0.1); padding: 12px; border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; cursor: pointer; backdrop-filter: blur(10px); transition: 0.3s; color: #64748b;">
        <svg id="bgmIcon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
            <line id="muteLine1" x1="23" y1="9" x2="17" y2="15"></line>
            <line id="muteLine2" x1="17" y1="9" x2="23" y2="15"></line>
        </svg>
    </button>

    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const audio = document.getElementById("bgmAudio");
            const toggleBtn = document.getElementById("bgmToggle");
            const icon = document.getElementById("bgmIcon");
            
            audio.volume = 0.4; // Default half volume

            // Restore time & play state across pages
            const savedTime = localStorage.getItem("tradeblitz_bgm_time");
            const isPlaying = localStorage.getItem("tradeblitz_bgm_playing") === "true";
            
            if (savedTime) audio.currentTime = parseFloat(savedTime);

            function setPlayingUI() {
                icon.innerHTML = '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>';
                toggleBtn.style.color = "#10b981";
                toggleBtn.style.borderColor = "rgba(16, 185, 129, 0.3)";
                toggleBtn.style.boxShadow = "0 0 10px rgba(16, 185, 129, 0.2)";
            }
            
            function setMutedUI() {
                icon.innerHTML = '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line>';
                toggleBtn.style.color = "#ef4444";
                toggleBtn.style.borderColor = "rgba(239, 68, 68, 0.3)";
                toggleBtn.style.boxShadow = "none";
            }

            if (isPlaying) {
                // Browsers might block this, but we try
                audio.play().then(() => setPlayingUI()).catch(e => setMutedUI());
            } else {
                setMutedUI();
            }
            
            // Save time continuously so jumping pages feels seamless
            setInterval(() => {
                if (!audio.paused) {
                    localStorage.setItem("tradeblitz_bgm_time", audio.currentTime);
                }
            }, 1000);
            
            toggleBtn.addEventListener("click", () => {
                if (audio.paused) {
                    audio.play();
                    setPlayingUI();
                    localStorage.setItem("tradeblitz_bgm_playing", "true");
                } else {
                    audio.pause();
                    setMutedUI();
                    localStorage.setItem("tradeblitz_bgm_playing", "false");
                }
            });
            
            // Try playing anyway on first interaction if they left it playing
            document.body.addEventListener("click", () => {
                if (localStorage.getItem("tradeblitz_bgm_playing") === "true" && audio.paused) {
                    audio.play();
                    setPlayingUI();
                }
            }, { once: true });
        });
    </script>
</body>"""

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            c = file.read()
    except Exception:
        continue
    
    if "bgmAudio" in c:
        continue # Already added
        
    c = c.replace('</body>', bgm_html)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)
    print(f"Injected BGM into {f}")
