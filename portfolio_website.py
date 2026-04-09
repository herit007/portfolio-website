import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="DataCraft — Portfolio",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Session state ───────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"
if "active_project" not in st.session_state:
    st.session_state.active_project = None

# ── Project data ────────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "id": "upi_dashboard",
        "title": "UPI Transaction Analysis Dashboard",
        "tagline": "Analyzing digital payment growth and trends",
        "description": (
            "An interactive Power BI dashboard built to explore UPI transaction data,"
            "highlighting growth trends, app performance, and yearly comparisons."
        ),
        "tech": ["Power BI", "Data Visualization"],
        "insights": [
            "PhonePe leads in transaction volume, showing strong dominance in the UPI ecosystem.",
            "Year-over-year growth in UPI usage highlights rapid digital payment adoption.",
            "Transaction trends show consistent upward movement across multiple years."
        ],
        "image_url": "upi_dashboard.png",
        "color": "#6366f1",
    },

    {
        "id": "currency_dashboard",
        "title": "Currency Exchange Rate Dashboard",
        "tagline": "Tracking INR exchange trends across currencies",
        "description": (
            "A Power BI dashboard analyzing INR exchange rates across multiple currencies, "
            "including trend forecasting, ranking, and comparative insights."
        ),
        "tech": ["Power BI", "Data Visualization"],
        "insights": [
            "KWD ranks highest in average exchange rate among selected currencies.",
            "Exchange rate trends show steady growth with forecasted upward movement.",
            "YoY change indicates slight decline (-3.88%), highlighting short-term fluctuations."
        ],
        "image_url": "currency_dashboard.png",
        "color": "#10b981",
    },

    {
        "id": "hr_dashboard",
        "title": "HR Analytics Dashboard",
        "tagline": "Employee distribution and performance insights",
        "description": (
            "An Excel-based dashboard analyzing employee distribution across departments, "
            "cities, and performance levels with interactive filters."
            "Useful for HR teams to understand workforce dynamics."
        ),
        "tech": ["Excel", "Data Visualization"],
        "insights": [
            "Finance department has the highest employee count among all departments.",
            "Employee distribution across cities is relatively balanced with slight variations.",
            "Performance score trends show fluctuations across different levels."
        ],
        "image_url": "hr_dashboard.png",
        "color": "#f59e0b",

    },

    {
        "id": "Retail_Sales_Dashboard",
        "title": "Retail Sales Dashboard",
        "tagline": "Business Intelligence & Customer Insights",
        "description": (
            "An interactive dashboard analyzing retail sales performance, customer behavior, and product trends."
            "Designed to help businesses track KPIs, identify growth opportunities, and understand churn patterns."
        ),
        "tech": ["Power BI", "Data Visualization"],
        "insights": [
           "Sales show strong peaks in February and June, followed by a sharp decline in mid-year indicating seasonal demand patterns.",
            "Customer churn rate is significantly high (~36%), suggesting retention strategies need improvement.",
            "Electronics category dominates revenue (~81%), making it the primary driver of business performance.",
            "Mumbai and Delhi contribute the highest sales, highlighting key geographic markets.",
            "High-value products like laptops and mobiles generate most of the revenue despite fewer orders."
        ],
        "image_url": "retail_sales_dashboard.png",
        "color": "#ec4899",
    },

    {
        "id": "student_performance",
        "title": "Student Performance & Analysis Dashboard",
        "tagline": "Academic performance and student insights",
        "description": "An interactive dashboard analyzing student performance, attendance trends, subject-wise scores, and demographic filters.",
        "tech": ["Power BI"],
        "image_url": "student_performance_dashboard.png",
        "color": "#1e40af",
        "insights": [
            "Tracked total students, attendance percentage, and average score using KPI cards.",
            "Analyzed subject-wise average scores to compare academic performance.",
            "Visualized monthly attendance trends to identify fluctuations over time.",
            "Segmented students by section and gender for deeper analysis.",
            "Compared exam performance across subjects and exam types.",
            "Identified top-performing students based on attendance and score metrics."
        ]
    },

    {
        "id": "sales_customer",
        "title": "Sales & Customer Intelligence Dashboard",
        "tagline": "Customer behavior and sales performance insights",
        "description": "An interactive dashboard analyzing sales trends, customer behavior, product performance, and revenue distribution.",
        "tech": ["Power BI"],
        "image_url": "sales_customer_dashboard.png",
        "color": "#0ea5e9",
        "insights": [
            "Tracked total sales and units sold to evaluate business growth.",
            "Analyzed category-wise performance including furniture, office supplies, and technology.",
            "Identified top-selling subcategories such as accessories and binders.",
            "Compared total orders, returns, and revenue to measure efficiency.",
            "Observed monthly sales trends to detect seasonal patterns."
        ]
    },

    {
        "id": "company_report",
        "title": "Company HR Analytics Dashboard",
        "tagline": "Employee insights and performance overview",
        "description": "An interactive dashboard showing employee count, salary distribution, department analysis, and regional insights.",
        "tech": ["Power BI"],
        "insights": [
            "Identified department-wise employee distribution, highlighting Marketing and Finance as the largest teams.",
            "Analyzed salary allocation across departments to understand cost concentration and budget usage.",
            "Compared active vs inactive employees to track workforce engagement and attrition patterns.",
            "Observed regional performance trends, with the West region contributing the highest overall metrics.",
            "Tracked monthly trends to identify fluctuations in company performance over time."
        ],
        "image_url": "company_report.png",
        "color": "#3b82f6",
    },

    {
        "id": "sales_report",
        "title": "Sales Performance Track Dashboard",
        "tagline": "Sales trends and profit insights",
        "description": "A dynamic dashboard analyzing sales, profit, product performance, and regional distribution with interactive filters.",
        "tech": ["Power BI"],
        "insights": [
            "Identified top-performing products like Paseo contributing the highest sales revenue.",
            "Analyzed sales distribution across segments, with Government and Small Business leading.",
            "Compared profit margins across segments to evaluate business efficiency.",
            "Observed country-wise profit contribution, with France and Germany as top contributors.",
            "Tracked overall sales, units sold, and profit to understand business growth trends."
        ],
        "image_url": "sales_report.png",
        "color": "#a855f7",
    },
    
    {
        "id": "sales_analysis",
        "title": "Sales Analysis Dashboard",
        "tagline": "Sales trends and regional performance insights",
        "description": "A dashboard analyzing monthly sales trends, regional distribution, and product-wise performance.",
        "tech": ["Power BI"],
        "image": "sales_dashboard.png",
        "color": "#0ea5e9",
        "insights": [
            "Analyzed monthly sales growth trends to identify fluctuations.",
            "Compared sales performance across regions (Central, East, West, North, South).",
            "Identified top-performing product categories.",
            "Evaluated contribution of each region to total sales.",
            "Compared Books vs Electronics sales performance.",
            "Highlighted seasonal sales patterns and growth rate changes."
        ]
    },

    {
        "id": "student_behavior",
        "title": "Student Behavior & Performance Dashboard",
        "tagline": "Behavior analysis and academic performance insights",
        "description": "An interactive dashboard combining student behavior analysis with academic performance tracking.",
        "tech": ["Power BI"],
        "image": "student_behavior_dashboard.png",
        "color": "#f97316",
        "insights": [
            "Tracked behavior patterns such as disruptive, late, and participative actions.",
            "Analyzed performance across subjects and sections.",
            "Visualized student distribution by gender and section.",
            "Compared academic performance across different terms.",
            "Identified trends between behavior and performance.",
            "Highlighted areas for student improvement and engagement."
        ]
    },
]

# ── Global CSS ──────────────────────────────────────────────────────────────────
def inject_css():
    st.markdown(
        """
        <style>
        /* ── Reset & base ── */
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

        html, body, [data-testid="stAppViewContainer"] {
            background-color: #0d0d0f !important;
            color: #e2e2e6 !important;
            font-family: 'DM Sans', sans-serif !important;
        }

        /* Hide Streamlit chrome */
        #MainMenu, footer, header { visibility: hidden; }
        [data-testid="stSidebar"] { display: none; }
        [data-testid="collapsedControl"] { display: none; }
        .stDeployButton { display: none; }

        /* Remove default top padding */
        .block-container {
            padding-top: 0 !important;
            padding-bottom: 2rem !important;
            max-width: 1100px !important;
        }

        /* ── Navbar ── */
        .navbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 18px 0 18px 0;
            border-bottom: 1px solid #1e1e24;
            margin-bottom: 0;
        }
        .navbar-brand {
            font-size: 1.15rem;
            font-weight: 600;
            letter-spacing: -0.02em;
            color: #ffffff;
        }
        .navbar-brand span {
            color: #6366f1;
        }
        .nav-links {
            display: flex;
            gap: 6px;
        }
        .nav-btn {
            display: inline-block;
            padding: 7px 18px;
            border-radius: 8px;
            font-size: 0.875rem;
            font-weight: 500;
            cursor: pointer;
            border: 1px solid transparent;
            text-decoration: none;
            transition: all 0.15s ease;
            color: #a0a0b0;
            background: transparent;
        }
        .nav-btn:hover { color: #ffffff; background: #1a1a22; }
        .nav-btn.active { color: #ffffff; background: #1a1a22; border-color: #2a2a36; }

        /* ── Hero ── */
        .hero {
            padding: 72px 0 60px 0;
            border-bottom: 1px solid #1a1a22;
        }
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.78rem;
            font-weight: 500;
            color: #6366f1;
            background: rgba(99,102,241,0.1);
            border: 1px solid rgba(99,102,241,0.2);
            border-radius: 100px;
            padding: 4px 12px;
            margin-bottom: 24px;
            letter-spacing: 0.02em;
            text-transform: uppercase;
        }
        .hero-title {
            font-size: clamp(2rem, 4vw, 2.75rem);
            font-weight: 600;
            line-height: 1.15;
            letter-spacing: -0.03em;
            color: #ffffff;
            margin: 0 0 18px 0;
        }
        .hero-sub {
            font-size: 1.05rem;
            color: #7a7a8e;
            line-height: 1.6;
            max-width: 520px;
            margin: 0 0 32px 0;
        }
        .hero-pills {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 8px;
        }
        .pill {
            font-size: 0.8rem;
            font-weight: 500;
            color: #9090a8;
            background: #16161e;
            border: 1px solid #232330;
            border-radius: 6px;
            padding: 5px 12px;
            font-family: 'DM Mono', monospace;
        }

        /* ── Section heading ── */
        .section-heading {
            font-size: 1.35rem;
            font-weight: 600;
            letter-spacing: -0.02em;
            color: #ffffff;
            margin: 0 0 6px 0;
        }
        .section-sub {
            font-size: 0.9rem;
            color: #6a6a7e;
            margin: 0 0 28px 0;
        }

        /* ── Project cards ── */
        .project-card {
            background: #111116;
            border: 1px solid #1e1e28;
            border-radius: 14px;
            padding: 28px;
            transition: border-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
            height: 100%;
        }
        .project-card:hover {
            border-color: #2e2e40;
            transform: translateY(-2px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        }
        .card-accent {
            width: 32px;
            height: 3px;
            border-radius: 2px;
            margin-bottom: 16px;
        }
        .card-title {
            font-size: 1rem;
            font-weight: 600;
            color: #f0f0f6;
            margin: 0 0 6px 0;
            letter-spacing: -0.01em;
        }
        .card-tagline {
            font-size: 0.8rem;
            color: #5a5a72;
            font-weight: 500;
            margin: 0 0 14px 0;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        .card-desc {
            font-size: 0.875rem;
            color: #7a7a90;
            line-height: 1.65;
            margin: 0 0 20px 0;
        }
        .card-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 22px;
        }
        .tech-tag {
            font-size: 0.72rem;
            font-weight: 500;
            color: #6060788;
            background: #18181f;
            border: 1px solid #252530;
            border-radius: 5px;
            padding: 3px 9px;
            font-family: 'DM Mono', monospace;
            color: #808098;
        }

        /* ── Streamlit button overrides ── */
        .stButton > button {
            background: #16161e !important;
            color: #c8c8dc !important;
            border: 1px solid #2a2a38 !important;
            border-radius: 8px !important;
            padding: 8px 18px !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
            font-family: 'DM Sans', sans-serif !important;
            transition: all 0.15s ease !important;
            width: auto !important;
        }
        .stButton > button:hover {
            background: #1e1e2a !important;
            border-color: #3a3a50 !important;
            color: #ffffff !important;
        }

        /* Nav button overrides */
        .nav-stbtn .stButton > button {
            background: transparent !important;
            border: none !important;
            color: #8080a0 !important;
            padding: 7px 16px !important;
            border-radius: 8px !important;
        }
        .nav-stbtn .stButton > button:hover {
            background: #1a1a22 !important;
            color: #ffffff !important;
        }
        .nav-stbtn-active .stButton > button {
            background: #1a1a22 !important;
            border: 1px solid #2a2a36 !important;
            color: #ffffff !important;
        }

        /* Back button */
        .back-btn .stButton > button {
            background: transparent !important;
            border: 1px solid #252530 !important;
            color: #8080a0 !important;
            padding: 6px 16px !important;
            font-size: 0.82rem !important;
        }
        .back-btn .stButton > button:hover {
            background: #16161e !important;
            color: #c0c0d8 !important;
        }

        /* ── Project detail page ── */
        .detail-badge {
            display: inline-flex;
            gap: 6px;
            flex-wrap: wrap;
            margin: 12px 0 28px 0;
        }
        .detail-title {
            font-size: clamp(1.5rem, 3vw, 2.1rem);
            font-weight: 600;
            letter-spacing: -0.03em;
            color: #ffffff;
            margin: 8px 0 0 0;
        }
        .detail-tagline {
            font-size: 0.875rem;
            color: #5a5a72;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 500;
            margin: 6px 0 0 0;
        }
        .detail-desc {
            font-size: 0.95rem;
            color: #7a7a90;
            line-height: 1.7;
            margin: 20px 0 30px 0;
            max-width: 640px;
        }
        .insight-item {
            display: flex;
            gap: 12px;
            align-items: flex-start;
            padding: 14px 18px;
            background: #111116;
            border: 1px solid #1e1e28;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .insight-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            margin-top: 7px;
            flex-shrink: 0;
        }
        .insight-text {
            font-size: 0.875rem;
            color: #9090a8;
            line-height: 1.6;
        }
        .divider {
            border: none;
            border-top: 1px solid #1a1a22;
            margin: 32px 0;
        }

        /* ── About section ── */
        .about-card {
            background: #111116;
            border: 1px solid #1e1e28;
            border-radius: 14px;
            padding: 32px;
        }
        .about-name {
            font-size: 1.1rem;
            font-weight: 600;
            color: #f0f0f6;
            margin: 0 0 4px 0;
        }
        .about-role {
            font-size: 0.85rem;
            color: #5a5a72;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            font-weight: 500;
            margin: 0 0 16px 0;
        }
        .about-bio {
            font-size: 0.875rem;
            color: #7a7a90;
            line-height: 1.7;
            margin: 0;
        }
        .contact-row {
            display: flex;
            gap: 12px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        .contact-link {
            font-size: 0.8rem;
            font-weight: 500;
            color: #6366f1;
            text-decoration: none;
            font-family: 'DM Mono', monospace;
        }
        .contact-link:hover { text-decoration: underline; }

        .project-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        object-fit: contain;
        background: #0b0b12;
        
        /* ── Stray Streamlit margins ── */
        div[data-testid="stVerticalBlock"] > div { gap: 0rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# ── Navigation helpers ──────────────────────────────────────────────────────────
def go_home():
    st.session_state.page = "home"
    st.session_state.active_project = None

def go_projects():
    st.session_state.page = "projects"
    st.session_state.active_project = None

def go_project(pid):
    st.session_state.page = "project_detail"
    st.session_state.active_project = pid

# ── Navbar component ────────────────────────────────────────────────────────────
def render_navbar():
    c_brand, c_space, c_home, c_proj = st.columns([2, 4, 1, 1.2])
    with c_brand:
        st.markdown(
            '<div class="navbar-brand" style="padding-top:10px;">◈ Data<span>Craft</span></div>',
            unsafe_allow_html=True,
        )
    is_home = st.session_state.page in ("home",)
    is_proj = st.session_state.page in ("projects", "project_detail")
    with c_home:
        cls = "nav-stbtn-active" if is_home else "nav-stbtn"
        st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
        if st.button("Home", key="nav_home"):
            go_home()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with c_proj:
        cls = "nav-stbtn-active" if is_proj else "nav-stbtn"
        st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
        if st.button("Projects", key="nav_projects"):
            go_projects()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('<hr style="border:none;border-top:1px solid #1a1a22;margin:0 0 0 0;">', unsafe_allow_html=True)

# ── Home page ───────────────────────────────────────────────────────────────────
def render_home():
    # Hero
    st.markdown(
        """
        <div class="hero">
            <div class="hero-badge">◈ &nbsp; Data Analytics Portfolio</div>
            <h1 class="hero-title">Turning raw data into<br>decisions that matter.</h1>
            <h2 class="hero-sub">Skills</h2>
            <div class="hero-pills">
                <span class="pill">Python</span>
                <span class="pill">SQL</span>
                <span class="pill">Numpy</span>
                <span class="pill">Pandas</span>
                <span class="pill">Matplotlib</span>
                <span class="pill">Seaborn</span>
                <span class="pill">Excel</span>
                <span class="pill">Power Bi</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Featured projects (first 2)
    st.markdown('<div style="height:44px;"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-heading">Featured Projects</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">A selection of recent work.</p>', unsafe_allow_html=True)

    cols = st.columns(2, gap="medium")
    for i, proj in enumerate(PROJECTS[:2]):
        with cols[i]: 
            with st.container():  # 🔥 THIS FIXES EVERYTHING
                _render_card(proj)
                
    st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
    if st.button("View all projects →", key="home_all"):
        go_projects()
        st.rerun()

    # About
    st.markdown('<div style="height:52px;"></div>', unsafe_allow_html=True)
    st.markdown('<hr style="border:none;border-top:1px solid #1a1a22;margin:0 0 32px 0;">', unsafe_allow_html=True)
    st.markdown('<p class="section-heading">About</p>', unsafe_allow_html=True)
    st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="about-card">
            <p class="about-name">Herit Tanna</p>
            <p class="about-role">Data Analyst | Dashboard Developer</p>
            <p class="about-bio">
                I focus on turning raw data into clear, interactive dashboards that help uncover 
                meaningful insights. My work revolves around data visualization, trend analysis, 
                and building intuitive dashboards using tools like Power BI and Excel.
            </p>
            <p class="about-bio">
                I enjoy exploring datasets, identifying patterns, and presenting them in a way 
                that makes decision-making easier and more effective.
            </p>
            <div class="contact-row">
                <a class="contact-link" href="https://mail.google.com/mail/?view=cm&fs=1&to=blender740@gmail.com" target="_blank">blender740@gmail.com</a>
                <a class="contact-link" href="https://github.com/herit007" target="_blank">github/herit007</a>
                <a class="contact-link" href="https://www.linkedin.com/in/tanna-herit-38b679387/" target="_blank">linkedin/herit</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="about-card" style="opacity:0.85;">
    <p class="about-name">Disclaimer</p>

    <p class="about-bio">
        The dashboards and insights presented in this portfolio are for analytical 
        and demonstration purposes only.
    </p>

    <p class="about-bio">
        Some datasets used may be simulated or AI-generated and may not reflect 
        real-world or production-level accuracy.
    </p>

    <p class="about-bio">
        Any decisions made based on these insights are the responsibility of the user. 
        I am not liable for any losses, damages, or outcomes resulting from their use.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="height:48px;"></div>', unsafe_allow_html=True)

# ── Projects page ───────────────────────────────────────────────────────────────
def render_projects():
    st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-heading">All Projects</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub"></p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    for i, proj in enumerate(PROJECTS):
        with (col1 if i % 2 == 0 else col2):
            with st.container():  # 🔥 ADD THIS HERE TOO
                _render_card(proj)
            st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)

    st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)

# ── Card renderer ───────────────────────────────────────────────────────────────
def _render_card(proj):
    tech_tags = " ".join([f"`{t}`" for t in proj["tech"]])

    with st.container():

        # 🔥 LOAD & RESIZE IMAGE
        img = Image.open(proj["image_url"])
        img = img.resize((800, 400))  # 👈 SAME SIZE FOR ALL

        # 🔥 CARD STYLE
        st.markdown(
            """
            <div style="
                background:#0b0b12;
                border:1px solid #1e1e28;
                border-radius:16px;
                overflow:hidden;
                margin-bottom:20px;
            ">
            """,
            unsafe_allow_html=True
        )

        # ✅ SHOW RESIZED IMAGE
        st.image(img, use_container_width=True)

        # ✅ CONTENT
        st.markdown(
            f"""
            <div style="padding:20px;">
                <div style="width:40px;height:4px;background:{proj['color']};margin-bottom:10px;border-radius:2px;"></div>
                <p style="color:#9ca3af;font-size:12px;margin:0;">{proj['tagline']}</p>
                <h3 style="color:white;margin:5px 0;">{proj['title']}</h3>
                <p style="color:#9ca3af;font-size:14px;">{proj['description']}</p>
                <p style="color:#6b7280;font-size:12px;">{tech_tags}</p>
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button("View Project →", key=f"card_{proj['id']}"):
        go_project(proj["id"])
        st.rerun()

# ── Project detail page ─────────────────────────────────────────────────────────
def render_project_detail():
    pid = st.session_state.active_project
    proj = next((p for p in PROJECTS if p["id"] == pid), None)
    if proj is None:
        st.error("Project not found.")
        return

    # Back
    st.markdown('<div style="height:28px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("← Back to Projects", key="back_btn"):
        go_projects()
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)

    # Title area
    tech_tags = "".join(f'<span class="tech-tag">{t}</span>' for t in proj["tech"])
    st.markdown(
        f"""
        <div style="border-left: 3px solid {proj['color']}; padding-left: 20px;">
            <p class="detail-tagline">{proj['tagline']}</p>
            <h1 class="detail-title">{proj['title']}</h1>
        </div>
        <p class="detail-desc">{proj['description']}</p>
        <div class="card-tech" style="margin-bottom:32px;">{tech_tags}</div>
        """,
        unsafe_allow_html=True,
    )

    # Dashboard image
    st.image(
        proj["image_url"],
        use_container_width=True,
        caption=f"{proj['title']} — Dashboard Preview",
    )

    st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)
    st.markdown(
        '<p style="font-size:0.95rem;font-weight:600;color:#e0e0ec;margin-bottom:14px;">Key Insights</p>',
        unsafe_allow_html=True,
    )

    for insight in proj["insights"]:
        st.markdown('<div style="height:28px;"></div>', unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="insight-item">
                <div class="insight-dot" style="background:{proj['color']};"></div>
                <p class="insight-text">{insight}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("""
            <div style="
            font-size:0.75rem;
            color:#6a6a7e;
            border-top:1px solid #1a1a22;
            padding-top:16px;
            max-width:600px;
            ">
            *Insights are for analytical purposes only. Some data may be simulated or AI-generated.
            No guarantees of business outcomes are implied.*
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div style="height:48px;"></div>', unsafe_allow_html=True)

# ── Main router ─────────────────────────────────────────────────────────────────
def main():
    inject_css()
    render_navbar()

    page = st.session_state.page
    if page == "home":
        render_home()
    elif page == "projects":
        render_projects()
    elif page == "project_detail":
        render_project_detail()
    else:
        render_home()

if __name__ == "__main__":
    main()
