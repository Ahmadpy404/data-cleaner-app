import streamlit as st
import pandas as pd

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_csv("practice.csv", skipinitialspace=True)

# -------------------------------
# Cleaning Function
# -------------------------------
def clean_data(df):
    df = df.copy()
    df = df.drop_duplicates()

    if 'Age' in df.columns:
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
        df['Age'] = df['Age'].fillna(df['Age'].mean())

    if 'Salary' in df.columns:
        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
        df['Salary'] = df['Salary'].fillna(df['Salary'].median())

    if 'Email' in df.columns:
        df['Email'] = df['Email'].fillna("noemail@example.com")
        df['Email'] = df['Email'].str.lower().str.strip()

    if 'Name' in df.columns:
        df['Name'] = df['Name'].str.strip().str.title()

    if 'Join_Date' in df.columns:
        df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')
        df['Join_Date'] = df['Join_Date'].dt.strftime("%Y-%m-%d")

    return df

cleaned_df = clean_data(df)

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Data Cleaning Showcase",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0A0A0F;
    color: #E8E6F0;
}

.stApp {
    background: #0A0A0F;
}

/* ── Remove default padding ── */
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── Hero Banner ── */
.hero-wrapper {
    position: relative;
    overflow: hidden;
    background: #0A0A0F;
    padding: 70px 80px 60px 80px;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}

.hero-grid {
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(139,92,246,0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(139,92,246,0.08) 1px, transparent 1px);
    background-size: 50px 50px;
    animation: gridPan 20s linear infinite;
}

@keyframes gridPan {
    0%   { background-position: 0 0; }
    100% { background-position: 50px 50px; }
}

.hero-glow {
    position: absolute;
    top: -120px; left: -120px;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(139,92,246,0.18) 0%, transparent 70%);
    pointer-events: none;
    animation: pulse 6s ease-in-out infinite;
}

.hero-glow-2 {
    position: absolute;
    bottom: -100px; right: -100px;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(56,189,248,0.12) 0%, transparent 70%);
    pointer-events: none;
    animation: pulse 8s ease-in-out infinite reverse;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50%       { transform: scale(1.1); opacity: 0.7; }
}

.hero-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: #8B5CF6;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.hero-label::before {
    content: '';
    display: inline-block;
    width: 28px; height: 1px;
    background: #8B5CF6;
}

.hero-title {
    font-family: 'DM Sans', sans-serif;
    font-size: clamp(44px, 6vw, 80px);
    font-weight: 800;
    line-height: 1.0;
    letter-spacing: -0.03em;
    color: #FFFFFF;
    margin-bottom: 10px;
}

.hero-title span {
    background: linear-gradient(135deg, #8B5CF6 0%, #38BDF8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    font-size: 16px;
    font-weight: 300;
    color: rgba(232,230,240,0.55);
    max-width: 520px;
    line-height: 1.7;
    margin-top: 16px;
}

.badge-row {
    display: flex;
    gap: 10px;
    margin-top: 32px;
    flex-wrap: wrap;
}

.badge {
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.3);
    border-radius: 100px;
    padding: 6px 14px;
    font-size: 12px;
    font-weight: 500;
    color: #C4B5FD;
    letter-spacing: 0.02em;
}

/* ── Section Wrapper ── */
.section {
    padding: 56px 80px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}

.section-tag {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 0.35em;
    text-transform: uppercase;
    color: #38BDF8;
    margin-bottom: 12px;
}

.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #FFFFFF;
    letter-spacing: -0.02em;
    margin-bottom: 4px;
}

.section-desc {
    font-size: 14px;
    color: rgba(232,230,240,0.45);
    margin-bottom: 28px;
    font-weight: 300;
}

/* ── Pipeline Steps ── */
.pipeline-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin-top: 8px;
}

.step-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 22px 20px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s ease, transform 0.2s ease;
}

.step-card:hover {
    border-color: rgba(139,92,246,0.4);
    transform: translateY(-2px);
}

.step-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #8B5CF6, #38BDF8);
    opacity: 0.7;
}

.step-number {
    font-family: 'Syne', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.2em;
    color: rgba(139,92,246,0.6);
    margin-bottom: 10px;
}

.step-icon {
    font-size: 26px;
    margin-bottom: 10px;
    display: block;
}

.step-title {
    font-family: 'Syne', sans-serif;
    font-size: 14px;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 6px;
}

.step-desc {
    font-size: 12px;
    color: rgba(232,230,240,0.45);
    line-height: 1.6;
}

/* ── Metrics Bar ── */
.metrics-row {
    display: flex;
    gap: 20px;
    margin-bottom: 36px;
    flex-wrap: wrap;
}

.metric-tile {
    flex: 1;
    min-width: 160px;
    background: linear-gradient(135deg, rgba(139,92,246,0.10) 0%, rgba(56,189,248,0.05) 100%);
    border: 1px solid rgba(139,92,246,0.22);
    border-radius: 18px;
    padding: 24px 22px;
    text-align: left;
}

.metric-label {
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: rgba(232,230,240,0.40);
    margin-bottom: 10px;
}

.metric-value {
    font-family: 'DM Sans', sans-serif;
    font-size: 34px;
    font-weight: 800;
    background: linear-gradient(135deg, #8B5CF6 0%, #38BDF8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
}

.metric-unit {
    font-size: 13px;
    font-weight: 300;
    color: rgba(232,230,240,0.40);
    margin-top: 4px;
}

/* ── Dataframe Overrides ── */
.stDataFrame {
    border-radius: 14px !important;
    overflow: hidden !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

iframe[title="st.dataframe"] {
    border-radius: 14px !important;
}

/* ── Download Button ── */
.stDownloadButton > button {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    background: linear-gradient(135deg, #8B5CF6 0%, #38BDF8 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 100px !important;
    padding: 12px 32px !important;
    letter-spacing: 0.02em !important;
    cursor: pointer !important;
    transition: opacity 0.2s ease, transform 0.2s ease !important;
    box-shadow: 0 4px 20px rgba(139,92,246,0.35) !important;
    margin-top: 24px !important;
}

.stDownloadButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}

/* ── Footer ── */
.footer {
    padding: 36px 80px;
    display: flex;
    align-items: center;
    gap: 12px;
    color: rgba(232,230,240,0.2);
    font-size: 12px;
    font-weight: 300;
}

.footer-dot {
    width: 4px; height: 4px;
    border-radius: 50%;
    background: rgba(139,92,246,0.5);
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-grid"></div>
    <div class="hero-glow"></div>
    <div class="hero-glow-2"></div>
    <div style="position:relative; z-index:2;">
        <div class="hero-label">Portfolio Project</div>
        <div class="hero-title">Data <span>Cleaning</span><br>Pipeline</div>
        <div class="hero-sub">
            A production-grade data wrangling workflow — deduplication,
            type coercion, imputation, and standardisation all in one clean pass.
        </div>
        <div class="badge-row">
            <span class="badge">Python</span>
            <span class="badge">Pandas</span>
            <span class="badge">Streamlit</span>
            <span class="badge">Data Engineering</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════
# PIPELINE STEPS
# ═══════════════════════════════════════════
st.markdown("""
<div class="section">
    <div class="section-tag">Methodology</div>
    <div class="section-title">Cleaning Pipeline</div>
    <div class="section-desc">Five deterministic transformations applied in sequence.</div>
    <div class="pipeline-grid">
        <div class="step-card">
            <div class="step-number">STEP 01</div>
            <span class="step-icon">♻️</span>
            <div class="step-title">Deduplication</div>
            <div class="step-desc">Exact-row duplicates removed to ensure referential integrity across the dataset.</div>
        </div>
        <div class="step-card">
            <div class="step-number">STEP 02</div>
            <span class="step-icon">🔢</span>
            <div class="step-title">Type Coercion</div>
            <div class="step-desc">Age and Salary columns cast to numeric; malformed entries coerced to NaN gracefully.</div>
        </div>
        <div class="step-card">
            <div class="step-number">STEP 03</div>
            <span class="step-icon">📐</span>
            <div class="step-title">Imputation</div>
            <div class="step-desc">Missing Age filled with column mean; missing Salary filled with median to resist outliers.</div>
        </div>
        <div class="step-card">
            <div class="step-number">STEP 04</div>
            <span class="step-icon">✏️</span>
            <div class="step-title">Standardisation</div>
            <div class="step-desc">Names title-cased and stripped; emails lowercased with a safe default for nulls.</div>
        </div>
        <div class="step-card">
            <div class="step-number">STEP 05</div>
            <span class="step-icon">📅</span>
            <div class="step-title">Date Formatting</div>
            <div class="step-desc">Join dates parsed with error tolerance and normalised to ISO 8601 (YYYY-MM-DD).</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════
# RAW DATA
# ═══════════════════════════════════════════
st.markdown("""
<div class="section">
    <div class="section-tag">Input</div>
    <div class="section-title">Raw Dataset</div>
    <div class="section-desc">Unprocessed data straight from the CSV — duplicates, nulls, and inconsistencies intact.</div>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div style="padding: 0 80px 56px 80px;">', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════
# CLEANED DATA
# ═══════════════════════════════════════════
st.markdown("""
<div class="section">
    <div class="section-tag">Output</div>
    <div class="section-title">Cleaned Dataset</div>
    <div class="section-desc">Post-pipeline result — consistent types, no nulls, standardised text and dates.</div>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div style="padding: 0 80px 56px 80px;">', unsafe_allow_html=True)
    st.dataframe(cleaned_df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════
# INSIGHTS
# ═══════════════════════════════════════════
avg_age    = round(cleaned_df['Age'].mean(), 1)
avg_salary = round(cleaned_df['Salary'].mean(), 0)
total_rows = len(cleaned_df)
dupes_removed = len(df) - len(df.drop_duplicates())

st.markdown(f"""
<div class="section">
    <div class="section-tag">Insights</div>
    <div class="section-title">Post-Clean Metrics</div>
    <div class="section-desc">Key statistics extracted from the cleaned dataset.</div>
    <div class="metrics-row">
        <div class="metric-tile">
            <div class="metric-label">Average Age</div>
            <div class="metric-value">{avg_age}</div>
            <div class="metric-unit">years</div>
        </div>
        <div class="metric-tile">
            <div class="metric-label">Average Salary</div>
            <div class="metric-value">{int(avg_salary):,}</div>
            <div class="metric-unit">USD / year</div>
        </div>
        <div class="metric-tile">
            <div class="metric-label">Clean Records</div>
            <div class="metric-value">{total_rows}</div>
            <div class="metric-unit">rows retained</div>
        </div>
        <div class="metric-tile">
            <div class="metric-label">Duplicates Removed</div>
            <div class="metric-value">{dupes_removed}</div>
            <div class="metric-unit">rows dropped</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════
# DOWNLOAD
# ═══════════════════════════════════════════
st.markdown("""
<div class="section" style="border-bottom: none;">
    <div class="section-tag">Export</div>
    <div class="section-title">Download Results</div>
    <div class="section-desc">Get the fully cleaned dataset as a CSV file.</div>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div style="padding: 0 80px 0 80px;">', unsafe_allow_html=True)
    csv = cleaned_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇  Download Cleaned CSV",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════
st.markdown("""
<div class="footer">
    <span>Data Cleaning Showcase</span>
    <div class="footer-dot"></div>
    <span>Built with Python & Streamlit</span>
    <div class="footer-dot"></div>
    <span>Portfolio Project</span>
</div>
""", unsafe_allow_html=True)