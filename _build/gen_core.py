# -*- coding: utf-8 -*-
"""Accueil, Philosophie, Méthode — design bleu/orange. i18n via c()."""
import json
from gen_common import page, ARR, CONTACT, SITE, EXPERTISES, slug_of, href, rel, c

def build_home():
    org_ld = json.dumps({
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": "shōrAI", "alternateName": "shōrAI Group", "legalName": "ShōrAI Consulting",
        "url": SITE + "/", "description": c("home_ld_desc"),
        "foundingDate": "2025",
        "knowsAbout": ["Artificial Intelligence Strategy", "Generative AI", "AI Governance", "AI Act Compliance", "Data Architecture"],
        "contactPoint": {"@type": "ContactPoint", "contactType": "customer service",
            "email": CONTACT["email"],
            "availableLanguage": ["French", "English", "Spanish", "Portuguese"]},
        "areaServed": [{"@type": "Place", "name": "France"}, {"@type": "Place", "name": "Europe"}]
    }, ensure_ascii=False)
    website_ld = json.dumps({"@context": "https://schema.org", "@type": "WebSite", "name": "shōrAI", "url": SITE + "/"}, ensure_ascii=False)

    titles = [c("home_exp1_title"), c("home_exp2_title"), c("home_exp3_title"), c("home_exp4_title")]
    descs = [c("home_exp1_desc"), c("home_exp2_desc"), c("home_exp3_desc"), c("home_exp4_desc")]
    exp_rows = ""
    for i, (num, _t, pkey, _) in enumerate(EXPERTISES):
        exp_rows += f'''        <li>
          <span class="num">0{i+1}</span>
          <div><a href="{slug_of(pkey)}" style="text-decoration:none;"><span class="it-title">{titles[i]}</span></a>
          <p class="it-desc">{descs[i]}</p></div>
        </li>\n'''

    body = f'''    <!-- HERO -->
    <section class="hero" id="top" style="background-image:url('../assets/bg-hero.jpg'); background-size:cover; background-position:center;">
      <div class="hero__scrim"></div>
      <div class="hero__watermark" aria-hidden="true"><img class="mark-spin" src="../assets/mark-color.png" alt=""></div>
      <div class="shell hero__content">
        <div>
          <span class="hero__eyebrow">{c("home_hero_eyebrow")}</span>
          <h1 style="font-size:clamp(44px, 6.4vw, 104px);">{c("home_hero_h1")}</h1>
          <p class="hero__lead">{c("home_hero_lead")}</p>
          <div class="hero__ctas">
            <a class="hero__primary" href="{href('methode')}">{c("home_hero_cta1")} <span aria-hidden="true">→</span></a>
            <a class="hero__ghost" href="{href('contact')}">{c("home_hero_cta2")}</a>
          </div>
        </div>
        <div class="hero__stats">
          <div class="hero__stat"><div class="hero__stat-value">72h</div><div class="hero__stat-label">{c("home_stat1_label")}</div></div>
          <div class="hero__stat"><div class="hero__stat-value">72h</div><div class="hero__stat-label">{c("home_stat2_label")}</div></div>
          <div class="hero__stat"><div class="hero__stat-value">24h</div><div class="hero__stat-label">{c("home_stat3_label")}</div></div>
        </div>
      </div>
      <div class="hero__kanji">shōrai · future</div>
    </section>

    <!-- 01 CONSTAT -->
    <section class="section section--alt">
      <div class="shell">
        <div class="section__head reveal">
          <div><p class="eyebrow">{c("home_s1_eyebrow")}</p><h2 class="section__title">{c("home_s1_title")}</h2></div>
          <p class="section__lead">{c("home_s1_lead")}</p>
        </div>
        <ol class="editorial-list reveal">
          <li><span class="num">01</span><div><span class="it-title">{c("home_s1_i1")}</span></div></li>
          <li><span class="num">02</span><div><span class="it-title">{c("home_s1_i2")}</span></div></li>
          <li><span class="num">03</span><div><span class="it-title">{c("home_s1_i3")}</span></div></li>
          <li><span class="num">04</span><div><span class="it-title">{c("home_s1_i4")}</span></div></li>
        </ol>
        <blockquote class="pullquote reveal" style="margin-top:56px;">{c("home_s1_quote")}</blockquote>
      </div>
    </section>

    <!-- 02 PROMESSE -->
    <section class="section">
      <div class="shell">
        <div class="section__head reveal">
          <div><p class="eyebrow">{c("home_s2_eyebrow")}</p><h2 class="section__title">{c("home_s2_title")}</h2></div>
          <p class="section__lead">{c("home_s2_lead")}</p>
        </div>
        <div class="two-col reveal">
          <div></div>
          <div>
            <p>{c("home_s2_p1")}</p>
            <p>{c("home_s2_p2")}</p>
            <p style="margin-top:28px;"><a class="cta-primary" href="{href('methode')}">{c("home_s2_cta")} {ARR}</a></p>
          </div>
        </div>
      </div>
    </section>

    <!-- 03 EXPERTISES -->
    <section class="section section--alt" id="services">
      <div class="shell">
        <div class="section__head reveal">
          <div><p class="eyebrow">{c("home_s3_eyebrow")}</p><h2 class="section__title">{c("home_s3_title")}</h2></div>
          <p class="section__lead">{c("home_s3_lead")}</p>
        </div>
        <ol class="editorial-list reveal">
{exp_rows}        </ol>
        <p class="reveal" style="margin-top:32px;"><a class="cta-secondary" href="{href('expertises')}">{c("home_s3_cta")} {ARR}</a></p>
      </div>
    </section>

    <!-- 04 MÉTHODE -->
    <section class="section" id="methode">
      <div class="shell">
        <div class="section__head reveal">
          <div><p class="eyebrow">{c("home_s4_eyebrow")}</p><h2 class="section__title">{c("home_s4_title")}</h2></div>
          <p class="section__lead">{c("home_s4_lead")}</p>
        </div>
        <ol class="editorial-list reveal">
          <li><span class="num">01</span><div><span class="it-title">{c("home_s4_i1_t")}</span><p class="it-desc">{c("home_s4_i1_d")}</p></div></li>
          <li><span class="num">02</span><div><span class="it-title">{c("home_s4_i2_t")}</span><p class="it-desc">{c("home_s4_i2_d")}</p></div></li>
          <li><span class="num">03</span><div><span class="it-title">{c("home_s4_i3_t")}</span><p class="it-desc">{c("home_s4_i3_d")}</p></div></li>
        </ol>
        <p class="reveal" style="margin-top:32px;"><a class="cta-secondary" href="{href('methode')}">{c("home_s4_cta")} {ARR}</a></p>
      </div>
    </section>

    <!-- QUOTE -->
    <section class="quote">
      <div class="quote__bg" style="background-image:url('../assets/bg-quote.jpg'); background-size:cover; background-position:center;"></div>
      <div class="quote__inner shell">
        <div class="quote__romaji">shōrai · future</div>
        <blockquote class="quote__text">{c("home_quote")}</blockquote>
        <div class="quote__attr">{c("home_quote_attr")}</div>
      </div>
    </section>

    <!-- CONTACT -->
    <section class="section section--alt" id="contact">
      <div class="shell">
        <div class="section__head reveal">
          <div><p class="eyebrow">{c("home_s5_eyebrow")}</p><h2 class="section__title">{c("home_s5_title")}</h2></div>
          <p class="section__lead">{c("home_s5_lead")}</p>
        </div>
        <div class="two-col reveal">
          <div class="contact__coords">
            <span class="contact__line"><span class="contact__dot"></span><a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></span>
          </div>
          <div>
            <p>{c("home_s5_p1")}</p>
            <p style="margin-top:28px;"><a class="btn btn--grad" href="{href('contact')}">{c("home_s5_cta")} {ARR}</a></p>
          </div>
        </div>
      </div>
    </section>'''
    page("home",
         c("home_meta_title"),
         c("home_meta_desc"),
         0, body, trail=None, jsonld=[org_ld, website_ld])


def build_philosophie():
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("phi_eyebrow")}</p>
      <h1 class="page-head__title reveal">{c("phi_h1")}<span class="kanji-suffix">道</span></h1>
      <p class="page-head__lead reveal">{c("phi_lead")}</p>
    </header>

    <section class="section section--alt">
      <div class="shell">
        <div class="section__head reveal">
          <div><p class="eyebrow">{c("phi_s1_eyebrow")}</p><h2 class="section__title">{c("phi_s1_title")}</h2></div>
          <p class="section__lead">{c("phi_s1_lead")}</p>
        </div>
        <div class="two-col reveal"><div></div><div>
          <p>{c("phi_s1_p1")}</p>
          <p>{c("phi_s1_p2")}</p>
        </div></div>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <div class="reveal"><p class="eyebrow">{c("phi_s2_eyebrow")}</p></div>
        <div class="feature-list reveal" style="margin-top:24px;">
          <div><h4>Shibui 渋い</h4><p>{c("phi_shibui")}</p></div>
          <div><h4>Kanso 簡素</h4><p>{c("phi_kanso")}</p></div>
          <div><h4>Seijaku 静寂</h4><p>{c("phi_seijaku")}</p></div>
          <div><h4>Fukinsei 不均整</h4><p>{c("phi_fukinsei")}</p></div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="shell">
        <blockquote class="pullquote pullquote--center reveal">{c("phi_quote")}</blockquote>
        <p class="reveal" style="text-align:center; margin-top:40px;"><a class="cta-primary" href="{rel(1)}{href('methode')}">{c("phi_cta")} {ARR}</a></p>
      </div>
    </section>'''
    page("philosophie",
         c("phi_meta_title"),
         c("phi_meta_desc"),
         1, body,
         trail=[(c("crumb_home"), "home"), (c("phi_crumb"), "philosophie")])


def build_methode():
    howto_ld = json.dumps({
        "@context": "https://schema.org", "@type": "HowTo",
        "name": c("met_ld_name"), "description": c("met_ld_desc"),
        "step": [
            {"@type": "HowToStep", "position": 1, "name": c("met_step1_n"), "text": c("met_step1_t")},
            {"@type": "HowToStep", "position": 2, "name": c("met_step2_n"), "text": c("met_step2_t")},
            {"@type": "HowToStep", "position": 3, "name": c("met_step3_n"), "text": c("met_step3_t")}
        ]
    }, ensure_ascii=False)
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("met_eyebrow")}</p>
      <h1 class="page-head__title reveal">{c("met_h1")}<span class="kanji-suffix">間</span></h1>
      <p class="page-head__lead reveal">{c("met_lead")}</p>
    </header>

    <section class="section section--alt">
      <div class="shell">
        <div class="reveal"><p class="eyebrow">{c("met_phases_eyebrow")}</p></div>
        <ol class="editorial-list reveal" style="margin-top:24px;">
          <li><span class="num">01</span><div><span class="it-title">{c("met_p1_t")}</span><p class="it-desc">{c("met_p1_d")}</p></div></li>
          <li><span class="num">02</span><div><span class="it-title">{c("met_p2_t")}</span><p class="it-desc">{c("met_p2_d")}</p></div></li>
          <li><span class="num">03</span><div><span class="it-title">{c("met_p3_t")}</span><p class="it-desc">{c("met_p3_d")}</p></div></li>
        </ol>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <div class="section__head reveal">
          <div><p class="eyebrow">{c("met_rule_eyebrow")}</p><h2 class="section__title">{c("met_rule_title")}</h2></div>
          <p class="section__lead">{c("met_rule_lead")}</p>
        </div>
        <div class="feature-list reveal">
          <div><h4>{c("met_rule_f1_h")}</h4><p>{c("met_rule_f1_p")}</p></div>
          <div><h4>{c("met_rule_f2_h")}</h4><p>{c("met_rule_f2_p")}</p></div>
          <div><h4>{c("met_rule_f3_h")}</h4><p>{c("met_rule_f3_p")}</p></div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="shell">
        <div class="section__head reveal">
          <div><p class="eyebrow">{c("met_nap_eyebrow")}</p><h2 class="section__title">{c("met_nap_title")}</h2></div>
          <p class="section__lead">{c("met_nap_lead")}</p>
        </div>
        <div class="proof reveal">
          <div class="proof__grid">
            <div class="proof__cell"><p class="lbl">{c("met_nap_l1")}</p><p style="font-family:var(--font-mono); font-size:14px;">{c("met_nap_formula")}</p></div>
            <div class="proof__cell"><p class="lbl">{c("met_nap_l2")}</p><p>{c("met_nap_example")}</p></div>
            <div class="proof__cell"><p class="lbl">{c("met_nap_l3")}</p><p>{c("met_nap_notcounted")}</p></div>
          </div>
        </div>
        <p class="reveal" style="margin-top:40px;"><a class="btn btn--grad" href="{rel(1)}{href('contact')}">{c("met_cta")} {ARR}</a></p>
      </div>
    </section>'''
    page("methode",
         c("met_meta_title"),
         c("met_meta_desc"),
         1, body,
         trail=[(c("crumb_home"), "home"), (c("met_crumb"), "methode")], jsonld=[howto_ld], active="methode")
