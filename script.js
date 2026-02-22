document.addEventListener('DOMContentLoaded', () => {
    // If visiting the main homepage/index, clear the session (log out)
    if (window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || window.location.pathname === '') {
        localStorage.removeItem('tradeblitz_user_email');
    }

    // Navbar Scroll Effect
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Simple Form Submission via Web3Forms API
    const form = document.getElementById('waitlistForm');
    const msg = document.getElementById('formMsg');

    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            let email = form.querySelector('input[type="email"]').value;

            if (email) {
                email = email.toLowerCase().trim();

                // Loading state
                const btn = form.querySelector('button');
                const originalText = btn.textContent;
                btn.textContent = 'Processing...';
                btn.disabled = true;
                msg.innerHTML = "";

                // Access the global array from approved_emails.js to prevent CORS issues on local desktop files
                let approvedEmails = [];
                if (window.APPROVED_EMAILS_TEXT) {
                    approvedEmails = window.APPROVED_EMAILS_TEXT.split('\n').map(e => e.trim().toLowerCase()).filter(e => e.length > 0);
                } else if (window.APPROVED_EMAILS) {
                    approvedEmails = window.APPROVED_EMAILS.map(e => e.toLowerCase().trim());
                }

                // Check if user is already approved
                if (approvedEmails.includes(email)) {
                    msg.innerHTML = `Welcome back! <strong>${email}</strong> has been verified. Logging in...`;
                    msg.style.color = '#10B981';

                    // Save email to localStorage so we can link trades to the user!
                    localStorage.setItem('tradeblitz_user_email', email);

                    form.reset();
                    btn.textContent = 'Redirecting... 🚀';
                    btn.style.background = '#10B981';

                    setTimeout(() => {
                        window.location.href = "prep.html";
                    }, 1200);
                    return; // Stop execution
                }

                // If not approved, send to waitlist via Web3Forms
                try {
                    // Send data to Web3Forms
                    const response = await fetch('https://api.web3forms.com/submit', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                        },
                        body: JSON.stringify({
                            // IMPORTANT: Replace this with the actual Access Key sent to your email
                            access_key: "46f78f72-911d-458e-8aef-6125321e53cc",
                            email: email,
                            subject: "New TradeBlitz Waitlist Registration!",
                            from_name: "TradeBlitz Waitlist"
                        })
                    });

                    if (response.status === 200) {
                        msg.innerHTML = `Success! <strong>${email}</strong> is on the waitlist. You will be notified when approved.`;
                        msg.style.color = '#f59e0b';

                        form.reset();
                        btn.textContent = 'Pending Approval ⏳';
                        btn.style.background = '#f59e0b';
                        btn.disabled = false;

                        // We do NOT redirect to dashboard or set localStorage here 
                        // because they are not approved yet.
                    } else {
                        msg.innerHTML = "Error: Please check if the Access Key is correct in script.js!";
                        msg.style.color = '#EF4444';
                        btn.textContent = originalText;
                        btn.disabled = false;
                    }
                } catch (error) {
                    console.error(error);
                    msg.innerHTML = "Something went wrong! Please try again.";
                    msg.style.color = '#EF4444';
                    btn.textContent = originalText;
                    btn.disabled = false;
                }
            }
        });
    }

    // Smooth Scrolling for Anchor Links
    document.querySelectorAll('.nav-links a, .btn-secondary, .btn-primary').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            if (this.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Reveal Elements on Scroll
    const revealElements = document.querySelectorAll('.problem-card, .feature-row');

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const revealPoint = 150;

        revealElements.forEach(el => {
            const revealTop = el.getBoundingClientRect().top;
            if (revealTop < windowHeight - revealPoint) {
                el.style.opacity = "1";
                el.style.transform = "translateY(0)";
            }
        });
    };

    // Initial setup for reveal
    revealElements.forEach(el => {
        el.style.opacity = "0";
        el.style.transform = "translateY(50px)";
        el.style.transition = "all 0.8s ease-out";
    });

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Trigger once on load

    // Interactive Tab Logic
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    let currentTabIndex = 0;
    let tabInterval;

    function switchTab(index) {
        if (tabBtns.length === 0) return;

        // Remove active class from all buttons and contents
        tabBtns.forEach(b => b.classList.remove('active'));
        tabContents.forEach(c => c.classList.remove('active'));

        // Add active class to current button
        tabBtns[index].classList.add('active');

        // Show corresponding content
        const targetId = 'tab-' + tabBtns[index].getAttribute('data-tab');
        document.getElementById(targetId).classList.add('active');

        currentTabIndex = index;
    }

    tabBtns.forEach((btn, index) => {
        btn.addEventListener('click', () => {
            switchTab(index);
            resetTabInterval(); // reset timer on manual interaction
        });
    });

    function startTabInterval() {
        if (tabBtns.length > 0) {
            tabInterval = setInterval(() => {
                let nextIndex = (currentTabIndex + 1) % tabBtns.length;
                switchTab(nextIndex);
            }, 3000);
        }
    }

    function resetTabInterval() {
        clearInterval(tabInterval);
        startTabInterval();
    }

    startTabInterval();
});
