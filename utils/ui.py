from html import escape
import streamlit as st


def apply_global_styles() -> None:
    """Apply the global application design system."""

    st.html(
        """
        <style>
            :root {
                --app-primary: #38BDF8;
                --app-primary-light: #7DD3FC;
                --app-background: #07111F;
                --app-surface: #101C2E;
                --app-surface-light: #17263B;
                --app-border: rgba(148, 163, 184, 0.20);
                --app-text: #F8FAFC;
                --app-muted: #94A3B8;
            }

            .stApp {
                background:
                    radial-gradient(
                        circle at 90% 5%,
                        rgba(56, 189, 248, 0.08),
                        transparent 28%
                    ),
                    radial-gradient(
                        circle at 5% 50%,
                        rgba(59, 130, 246, 0.06),
                        transparent 24%
                    ),
                    var(--app-background);
            }

            .block-container {
                max-width: 1480px;
                padding-top: 1rem;
                padding-bottom: 3rem;
            }

            [data-testid="stHeader"] {
                background: transparent;
            }

            section[data-testid="stSidebar"] {
                background:
                    linear-gradient(
                        180deg,
                        rgba(15, 29, 48, 0.99),
                        rgba(7, 17, 31, 0.99)
                    );
                border-right: 1px solid var(--app-border);
            }

            .app-hero {
                position: relative;
                overflow: hidden;
                padding: 2.4rem 2rem 2rem;
                margin-bottom: 1rem;
                border: 1px solid rgba(56, 189, 248, 0.28);
                border-radius: 24px;
                background:
                    radial-gradient(
                        circle at 80% 20%,
                        rgba(56, 189, 248, 0.22),
                        transparent 35%
                    ),
                    linear-gradient(
                        135deg,
                        rgba(15, 29, 48, 0.99),
                        rgba(21, 40, 65, 0.96)
                    );
                box-shadow: 0 22px 55px rgba(0, 0, 0, 0.28);
                text-align: center;
            }

            .app-hero::before {
                content: "";
                position: absolute;
                width: 230px;
                height: 230px;
                top: -140px;
                left: -90px;
                border-radius: 50%;
                background: rgba(56, 189, 248, 0.10);
            }

            .hero-eyebrow {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 0.38rem 0.9rem;
                margin-bottom: 1.05rem;
                border: 1px solid rgba(56, 189, 248, 0.40);
                border-radius: 999px;
                background: rgba(56, 189, 248, 0.10);
                color: var(--app-primary-light);
                font-size: 0.77rem;
                font-weight: 750;
                letter-spacing: 0.10rem;
                text-transform: uppercase;
            }

            .hero-title-row {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0.85rem;
                width: 100%;
            }

            .hero-icon {
                font-size: clamp(2.1rem, 4vw, 3.4rem);
                line-height: 1;
            }

            .hero-title {
                margin: 0;
                color: var(--app-text);
                font-size: clamp(2rem, 4vw, 3.5rem);
                font-weight: 800;
                line-height: 1.15;
                letter-spacing: -0.04em;
            }

            .hero-subtitle {
                max-width: 850px;
                margin: 1rem auto 0;
                color: var(--app-muted);
                font-size: 1.05rem;
                line-height: 1.7;
                text-align: center;
            }

            .hero-rule {
                width: 70px;
                height: 3px;
                margin: 1.35rem auto 0;
                border-radius: 999px;
                background:
                    linear-gradient(
                        90deg,
                        transparent,
                        var(--app-primary),
                        transparent
                    );
            }

            .nav-caption {
                margin: 0.2rem 0 0.55rem;
                color: #64748B;
                font-size: 0.75rem;
                font-weight: 700;
                letter-spacing: 0.08rem;
                text-align: center;
                text-transform: uppercase;
            }

            div[data-testid="stPageLink"] {
                width: 100%;
            }

            div[data-testid="stPageLink"] a {
                display: flex;
                min-height: 46px;
                align-items: center;
                justify-content: center;
                padding: 0.65rem 0.8rem;
                border: 1px solid rgba(148, 163, 184, 0.18);
                border-radius: 12px;
                background: rgba(15, 29, 48, 0.78);
                color: #CBD5E1;
                font-weight: 650;
                text-align: center;
                transition:
                    transform 0.18s ease,
                    border-color 0.18s ease,
                    background 0.18s ease;
            }

            div[data-testid="stPageLink"] a:hover {
                transform: translateY(-2px);
                border-color: rgba(56, 189, 248, 0.55);
                background: rgba(56, 189, 248, 0.10);
                color: #FFFFFF;
            }

            div[data-testid="stPageLink"] a[aria-current="page"] {
                border-color: rgba(56, 189, 248, 0.75);
                background:
                    linear-gradient(
                        135deg,
                        rgba(14, 116, 144, 0.52),
                        rgba(37, 99, 235, 0.42)
                    );
                color: #FFFFFF;
                box-shadow: 0 8px 20px rgba(14, 165, 233, 0.15);
            }

            .section-heading {
                margin: 1.8rem 0 1.1rem;
            }

            .section-title {
                margin: 0;
                color: var(--app-text);
                font-size: 1.55rem;
                font-weight: 760;
                letter-spacing: -0.02em;
            }

            .section-description {
                margin: 0.35rem 0 0;
                color: var(--app-muted);
                font-size: 0.94rem;
                line-height: 1.6;
            }

            .kpi-card {
                height: 100%;
                min-height: 145px;
                padding: 1.3rem;
                border: 1px solid var(--app-border);
                border-radius: 17px;
                background:
                    linear-gradient(
                        145deg,
                        rgba(23, 38, 59, 0.96),
                        rgba(12, 25, 43, 0.98)
                    );
                box-shadow: 0 12px 30px rgba(0, 0, 0, 0.18);
                transition:
                    transform 0.18s ease,
                    border-color 0.18s ease;
            }

            .kpi-value-compact {
                max-width: 100%;
                font-size: clamp(1rem, 1.5vw, 1.45rem);
                line-height: 1.35;
                overflow-wrap: anywhere;
                word-break: break-word;
                white-space: normal;
            }

            .kpi-card:hover {
                transform: translateY(-3px);
                border-color: rgba(56, 189, 248, 0.48);
            }

            .kpi-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 1rem;
            }

            .kpi-label {
                color: var(--app-muted);
                font-size: 0.78rem;
                font-weight: 750;
                letter-spacing: 0.05rem;
                text-transform: uppercase;
            }

            .kpi-icon {
                font-size: 1.55rem;
            }

            .kpi-value {
                margin-top: 0.65rem;
                color: var(--app-text);
                font-size: 1.8rem;
                font-weight: 820;
                line-height: 1.2;
            }

            .kpi-helper {
                margin-top: 0.4rem;
                color: #64748B;
                font-size: 0.8rem;
            }

            .empty-state {
                padding: 2.5rem 1.5rem;
                border: 1px dashed rgba(148, 163, 184, 0.35);
                border-radius: 18px;
                background: rgba(15, 29, 48, 0.55);
                color: var(--app-muted);
                text-align: center;
            }

            .empty-state-icon {
                margin-bottom: 0.7rem;
                font-size: 2.5rem;
            }

            .app-footer {
                margin-top: 3.5rem;
                padding: 1.35rem;
                border-top: 1px solid rgba(148, 163, 184, 0.14);
                color: #64748B;
                font-size: 0.80rem;
                text-align: center;
            }

            div[data-testid="stDataFrame"] {
                border: 1px solid rgba(148, 163, 184, 0.14);
                border-radius: 14px;
                overflow: hidden;
            }

            @media (max-width: 800px) {
                .app-hero {
                    padding: 1.7rem 1rem;
                }

                .hero-title-row {
                    flex-direction: column;
                    gap: 0.35rem;
                }

                .hero-subtitle {
                    font-size: 0.94rem;
                }

                .kpi-card {
                    min-height: auto;
                }
            }
        </style>
        """
    )


def page_header(
    title: str,
    subtitle: str,
    icon: str,
    eyebrow: str,
) -> None:
    """Render the shared professional page header."""

    header_html = (
        '<section class="app-hero">'
        f'<div class="hero-eyebrow">{escape(eyebrow)}</div>'
        '<div class="hero-title-row">'
        f'<span class="hero-icon">{escape(icon)}</span>'
        f'<h1 class="hero-title">{escape(title)}</h1>'
        '</div>'
        f'<p class="hero-subtitle">{escape(subtitle)}</p>'
        '<div class="hero-rule"></div>'
        '</section>'
    )

    st.html(header_html)


def section_header(
    title: str,
    description: str = "",
) -> None:
    """Render a reusable section heading."""

    description_html = ""

    if description:
        description_html = (
            f'<p class="section-description">{escape(description)}</p>'
        )

    st.html(
        '<div class="section-heading">'
        f'<h2 class="section-title">{escape(title)}</h2>'
        f'{description_html}'
        '</div>'
    )


def page_footer() -> None:
    """Render the application footer."""

    st.html(
        '<footer class="app-footer">'
        'Sales Analytics Dashboard&nbsp;&nbsp;•&nbsp;&nbsp;'
        'Built with Streamlit and Python&nbsp;&nbsp;•&nbsp;&nbsp;'
        'Version 1.0'
        '</footer>'
    )


def style_plotly_figure(figure, height: int = 420):
    """Apply consistent styling to a Plotly figure."""

    figure.update_layout(
        template="plotly_dark",
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=25, r=25, t=60, b=35),
        legend_title_text="",
        font=dict(family="Arial", size=13),
    )

    return figure