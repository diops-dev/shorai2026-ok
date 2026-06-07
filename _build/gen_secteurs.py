# -*- coding: utf-8 -*-
"""Hub Secteurs + 5 pages enfants — design bleu/orange. i18n via c()."""
from gen_common import page, ARR, c, href, slug_of, rel

_HUB = [
    ("sec_finance", "01"),
    ("sec_industrie", "02"),
    ("sec_retail", "03"),
    ("sec_sante", "04"),
    ("sec_public", "05"),
]


def build_hub():
    rows = ""
    for pk, num in _HUB:
        h = rel(1) + slug_of(pk)
        rows += f'''        <div class="block">
          <span class="block__num">{num}</span>
          <div>
            <a href="{h}" style="text-decoration:none;"><h2 class="block__title">{c(pk + "_hub_title")}</h2></a>
            <p class="block__desc">{c(pk + "_hub_desc")}</p>
          </div>
          <a class="block__link" href="{h}">{c("label_discover")} {ARR}</a>
        </div>\n'''
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("sechub_eyebrow")}</p>
      <h1 class="page-head__title reveal">{c("sechub_h1")}<span class="kanji-suffix">業界</span></h1>
      <p class="page-head__lead reveal">{c("sechub_lead")}</p>
    </header>
    <section class="section section--alt"><div class="shell"><div class="block-grid reveal">
{rows}    </div></div></section>'''
    page("secteurs",
         c("sechub_meta_title"),
         c("sechub_meta_desc"),
         1, body,
         trail=[(c("crumb_home"), "home"), (c("crumb_secteurs"), "secteurs")], active="secteurs")


def _child(pkey):
    enjeux = [
        (c(pkey + "_e1_h"), c(pkey + "_e1_p")),
        (c(pkey + "_e2_h"), c(pkey + "_e2_p")),
        (c(pkey + "_e3_h"), c(pkey + "_e3_p")),
        (c(pkey + "_e4_h"), c(pkey + "_e4_p")),
    ]
    enj = "".join(f'<div><h4>{h}</h4><p>{p}</p></div>' for h, p in enjeux)
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("sec_label")}</p>
      <h1 class="page-head__title reveal" style="font-size:clamp(36px,6vw,76px);">{c(pkey + "_h1")}</h1>
      <p class="page-head__lead reveal">{c(pkey + "_chapeau")}</p>
    </header>

    <section class="section section--alt"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("sec_enjeux_eb")}</p></div></div>
      <div class="feature-list reveal">{enj}</div>
    </div></section>

    <section class="section"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("sec_cas_eb")}</p></div><p class="section__lead">{c(pkey + "_cas")}</p></div>
    </div></section>

    <section class="section section--alt"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("sec_why_eb")}</p></div><p class="section__lead">{c(pkey + "_pourquoi")}</p></div>
      <p class="reveal"><a class="btn btn--grad" href="{rel(2)}{href('contact')}">{c("sec_cta")} {ARR}</a></p>
    </div></section>'''
    page(pkey, c(pkey + "_meta_title"), c(pkey + "_meta_desc"), 2, body,
         trail=[(c("crumb_home"), "home"), (c("crumb_secteurs"), "secteurs"), (c(pkey + "_title"), pkey)], active="secteurs")


def build_children():
    for pk, _ in _HUB:
        _child(pk)
