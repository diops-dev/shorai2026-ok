# -*- coding: utf-8 -*-
"""Hub Expertises + 4 pages enfants — design bleu/orange. i18n via c()."""
import json
from gen_common import page, ARR, c, href, slug_of, rel

def _faq_block(items):
    faq = f'''    <section class="section section--alt"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("faq_eyebrow")}</p><h2 class="section__title">{c("faq_title")}</h2></div></div>
      <div class="faq">'''
    for q, a in items:
        faq += f'''
        <div class="faq__item">
          <button class="faq__q" aria-expanded="false">{q}<span class="faq__icon" aria-hidden="true">+</span></button>
          <div class="faq__a"><div class="faq__a-inner">{a}</div></div>
        </div>'''
    faq += '\n      </div></div></section>'
    ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]},
        ensure_ascii=False)
    return faq, ld


def build_hub():
    blocks = [
        ("exp_strategie", "01"),
        ("exp_transfo", "02"),
        ("exp_gouvernance", "03"),
        ("exp_archi", "04"),
    ]
    rows = ""
    for pk, num in blocks:
        h = rel(1) + slug_of(pk)
        rows += f'''        <div class="block">
          <span class="block__num">{num}</span>
          <div>
            <a href="{h}" style="text-decoration:none;"><h2 class="block__title">{c(pk + "_hub_title")}</h2></a>
            <p class="block__desc">{c(pk + "_hub_desc")}</p>
            <p class="block__aside">{c(pk + "_hub_aside")}</p>
          </div>
          <a class="block__link" href="{h}">{c("label_discover")} {ARR}</a>
        </div>\n'''
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("exphub_eyebrow")}</p>
      <h1 class="page-head__title reveal">{c("exphub_h1")}<span class="kanji-suffix">技</span></h1>
      <p class="page-head__lead reveal">{c("exphub_lead")}</p>
    </header>
    <section class="section section--alt">
      <div class="shell">
        <div class="block-grid reveal">
{rows}        </div>
        <div class="banner reveal">
          <div class="banner__text"><span class="banner__big">72h</span><span class="banner__desc">{c("exphub_banner")}</span></div>
          <a href="{rel(1)}{href('contact')}">{c("exphub_banner_cta")} {ARR}</a>
        </div>
      </div>
    </section>'''
    page("expertises",
         c("exphub_meta_title"),
         c("exphub_meta_desc"),
         1, body,
         trail=[(c("crumb_home"), "home"), (c("crumb_expertises"), "expertises")], active="expertises")


def _child(pkey, sections, faq=None, related=None):
    """sections: list of html strings. related: list of page_keys."""
    secs = "\n".join(sections)
    rel_html = ""
    if related:
        links = []
        for rk in related:
            links.append(f'<a class="cta-secondary" href="{rel(2)}{slug_of(rk)}" style="margin-right:32px;">{c("rel_" + rk)} {ARR}</a>')
        items = "".join(links)
        rel_html = f'''    <section class="section"><div class="shell"><div class="reveal"><p class="eyebrow">{c("rel_eyebrow")}</p><div style="display:flex; flex-wrap:wrap; gap:14px 0; margin-top:16px;">{items}</div></div></div></section>'''
    faq_html, faq_ld = ("", None)
    if faq:
        faq_html, faq_ld = _faq_block(faq)
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c(pkey + "_eyebrow")}</p>
      <h1 class="page-head__title reveal">{c(pkey + "_h1")}</h1>
      <p class="page-head__lead reveal">{c(pkey + "_sub")}</p>
    </header>
{secs}
{faq_html}
    <section class="section"><div class="shell"><p class="reveal"><a class="btn btn--grad" href="{rel(2)}{href('contact')}">{c(pkey + "_cta")} {ARR}</a></p></div></section>
{rel_html}'''
    service_ld = json.dumps({"@context": "https://schema.org", "@type": "Service",
        "name": c(pkey + "_title"), "provider": {"@type": "Organization", "name": "shōrAI"},
        "areaServed": "FR", "description": c(pkey + "_meta_desc")}, ensure_ascii=False)
    jl = [service_ld] + ([faq_ld] if faq_ld else [])
    page(pkey, c(pkey + "_meta_title"), c(pkey + "_meta_desc"), 2, body,
         trail=[(c("crumb_home"), "home"), (c("crumb_expertises"), "expertises"), (c(pkey + "_title"), pkey)],
         jsonld=jl, active="expertises")


def _sec(eyebrow, title, lead, inner, alt=False):
    cls = "section section--alt" if alt else "section"
    head = f'<div class="section__head reveal"><div><p class="eyebrow">{eyebrow}</p>' + (f'<h2 class="section__title">{title}</h2>' if title else '') + f'</div>' + (f'<p class="section__lead">{lead}</p>' if lead else '') + '</div>'
    return f'    <section class="{cls}"><div class="shell">{head}{inner}</div></section>'


def _features(items):
    rows = "".join(f'<div><h4>{h}</h4><p>{p}</p></div>' for h, p in items)
    return f'<div class="feature-list reveal">{rows}</div>'


def build_children():
    # --- 01 Stratégie IA ---
    _child("exp_strategie",
        [
        _sec(c("exp_strategie_s1_eb"), c("exp_strategie_s1_t"), c("exp_strategie_s1_l"), "", alt=True),
        _sec(c("exp_strategie_s2_eb"), "", "", _features([
            (c("exp_strategie_f1_h"), c("exp_strategie_f1_p")),
            (c("exp_strategie_f2_h"), c("exp_strategie_f2_p")),
            (c("exp_strategie_f3_h"), c("exp_strategie_f3_p")),
            (c("exp_strategie_f4_h"), c("exp_strategie_f4_p")),
            (c("exp_strategie_f5_h"), c("exp_strategie_f5_p")),
        ])),
        _sec(c("exp_strategie_s3_eb"), c("exp_strategie_s3_t"), "",
             f'''<ol class="editorial-list reveal">
                <li><span class="num">01</span><div><span class="it-title">{c("exp_strategie_ph1_t")}</span><p class="it-desc">{c("exp_strategie_ph1_d")}</p></div></li>
                <li><span class="num">02</span><div><span class="it-title">{c("exp_strategie_ph2_t")}</span><p class="it-desc">{c("exp_strategie_ph2_d")}</p></div></li>
                <li><span class="num">03</span><div><span class="it-title">{c("exp_strategie_ph3_t")}</span><p class="it-desc">{c("exp_strategie_ph3_d")}</p></div></li>
                <li><span class="num">04</span><div><span class="it-title">{c("exp_strategie_ph4_t")}</span><p class="it-desc">{c("exp_strategie_ph4_d")}</p></div></li>
             </ol>''', alt=True),
        _sec(c("exp_strategie_s4_eb"), "", "",
             f'''<div class="proof reveal"><div class="proof__grid">
                <div class="proof__cell"><p class="lbl">{c("exp_strategie_pr1_l")}</p><p>{c("exp_strategie_pr1_p")}</p></div>
                <div class="proof__cell"><p class="lbl">{c("exp_strategie_pr2_l")}</p><p>{c("exp_strategie_pr2_p")}</p></div>
                <div class="proof__cell"><p class="lbl">{c("exp_strategie_pr3_l")}</p><p>{c("exp_strategie_pr3_p")}</p></div>
             </div></div>'''),
        ],
        faq=[
            (c("exp_strategie_faq1_q"), c("exp_strategie_faq1_a")),
            (c("exp_strategie_faq2_q"), c("exp_strategie_faq2_a")),
            (c("exp_strategie_faq3_q"), c("exp_strategie_faq3_a")),
        ],
        related=["exp_gouvernance", "methode"])

    # --- 02 Transformation IA générative ---
    _child("exp_transfo",
        [
        _sec(c("exp_transfo_s1_eb"), c("exp_transfo_s1_t"), c("exp_transfo_s1_l"), "", alt=True),
        _sec(c("exp_transfo_s2_eb"), "", "", _features([
            (c("exp_transfo_f1_h"), c("exp_transfo_f1_p")),
            (c("exp_transfo_f2_h"), c("exp_transfo_f2_p")),
            (c("exp_transfo_f3_h"), c("exp_transfo_f3_p")),
            (c("exp_transfo_f4_h"), c("exp_transfo_f4_p")),
        ])),
        _sec(c("exp_transfo_s3_eb"), c("exp_transfo_s3_t"), c("exp_transfo_s3_l"), "", alt=True),
        ],
        related=["exp_archi", "exp_strategie"])

    # --- 03 Gouvernance & conformité ---
    _child("exp_gouvernance",
        [
        _sec(c("exp_gouvernance_s1_eb"), c("exp_gouvernance_s1_t"), c("exp_gouvernance_s1_l"), "", alt=True),
        _sec(c("exp_gouvernance_s2_eb"), "", "", _features([
            (c("exp_gouvernance_f1_h"), c("exp_gouvernance_f1_p")),
            (c("exp_gouvernance_f2_h"), c("exp_gouvernance_f2_p")),
            (c("exp_gouvernance_f3_h"), c("exp_gouvernance_f3_p")),
            (c("exp_gouvernance_f4_h"), c("exp_gouvernance_f4_p")),
            (c("exp_gouvernance_f5_h"), c("exp_gouvernance_f5_p")),
        ])),
        _sec(c("exp_gouvernance_s3_eb"), "", "",
             f'<blockquote class="pullquote reveal" style="max-width:46ch; font-size:clamp(20px,2.4vw,28px);">{c("exp_gouvernance_case")}</blockquote>', alt=True),
        ],
        related=["exp_strategie", "methode"])

    # --- 04 Architecture data & delivery ---
    _child("exp_archi",
        [
        _sec(c("exp_archi_s1_eb"), c("exp_archi_s1_t"), c("exp_archi_s1_l"), "", alt=True),
        _sec(c("exp_archi_s2_eb"), "", "", _features([
            (c("exp_archi_f1_h"), c("exp_archi_f1_p")),
            (c("exp_archi_f2_h"), c("exp_archi_f2_p")),
            (c("exp_archi_f3_h"), c("exp_archi_f3_p")),
            (c("exp_archi_f4_h"), c("exp_archi_f4_p")),
        ])),
        _sec(c("exp_archi_s3_eb"), c("exp_archi_s3_t"), c("exp_archi_s3_l"), "", alt=True),
        ],
        related=["exp_transfo", "exp_gouvernance"])
