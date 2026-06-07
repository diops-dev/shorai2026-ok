# -*- coding: utf-8 -*-
"""Cabinet, Études de cas, Insights, Contact, Légales, 404 — design bleu/orange. i18n via c()."""
import json, os
from gen_common import page, ARR, CONTACT, SITE, OUT, c, href, slug_of, rel


def build_cabinet():
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("cab_eyebrow")}</p>
      <h1 class="page-head__title reveal">{c("cab_h1")}</h1>
      <p class="page-head__lead reveal">{c("cab_lead")}</p>
    </header>

    <section class="section section--alt"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("cab_s1_eb")}</p></div><p class="section__lead">{c("cab_s1_lead")}</p></div>
      <div class="two-col reveal"><div></div><div>
        <p>{c("cab_s1_p1")}</p>
      </div></div>
    </div></section>

    <section class="section"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("cab_s2_eb")}</p></div></div>
      <div class="feature-list reveal">
        <div><h4>{c("cab_s2_f1_h")}</h4><p>{c("cab_s2_f1_p")}</p></div>
        <div><h4>{c("cab_s2_f2_h")}</h4><p>{c("cab_s2_f2_p")}</p></div>
        <div><h4>{c("cab_s2_f3_h")}</h4><p>{c("cab_s2_f3_p")}</p></div>
        <div><h4>{c("cab_s2_f4_h")}</h4><p>{c("cab_s2_f4_p")}</p></div>
      </div>
    </div></section>

    <section class="section section--alt"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("cab_s3_eb")}</p></div></div>
      <ol class="editorial-list reveal">
        <li><span class="num">24h</span><div><span class="it-title">{c("cab_s3_i1")}</span></div></li>
        <li><span class="num">72h</span><div><span class="it-title">{c("cab_s3_i2")}</span></div></li>
        <li><span class="num">·</span><div><span class="it-title">{c("cab_s3_i3_t")}</span><p class="it-desc">{c("cab_s3_i3_d")}</p></div></li>
        <li><span class="num">·</span><div><span class="it-title">{c("cab_s3_i4_t")}</span><p class="it-desc">{c("cab_s3_i4_d")}</p></div></li>
      </ol>
      <p class="reveal" style="margin-top:40px;"><a class="cta-primary" href="{rel(1)}{slug_of('equipe')}">{c("cab_cta")} {ARR}</a></p>
    </div></section>'''
    page("cabinet",
         c("cab_meta_title"),
         c("cab_meta_desc"),
         1, body,
         trail=[(c("crumb_home"), "home"), (c("crumb_cabinet"), "cabinet")], active="cabinet")


def build_equipe():
    person_ld = json.dumps({"@context": "https://schema.org", "@type": "Organization",
        "name": "shōrAI", "department": {"@type": "Organization", "name": c("eq_dept_name")},
        "description": c("eq_ld_desc")}, ensure_ascii=False)
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("eq_eyebrow")}</p>
      <h1 class="page-head__title reveal">{c("eq_h1")}</h1>
      <p class="page-head__lead reveal">{c("eq_lead")}</p>
    </header>

    <section class="section section--alt"><div class="shell">
      <div class="reveal" style="border-top:1px solid rgba(11,18,71,0.10); padding-top:44px; max-width:760px;">
        <h2 style="font-family:var(--font-display); font-weight:600; font-size:clamp(28px,3.5vw,44px); letter-spacing:-0.03em; margin:0 0 6px;">{c("eq_dept_name")}</h2>
        <p style="color:var(--brand-orange-500); font-weight:600; margin:0 0 4px;">{c("eq_dept_role")}</p>
        <p class="muted ital" style="margin:0 0 24px;">{c("eq_dept_tags")}</p>
        <p style="color:var(--ink-600); font-size:18px; line-height:1.7;">{c("eq_dept_body")}</p>
      </div>
    </div></section>

    <section class="section"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("eq_s2_eb")}</p></div><p class="section__lead">{c("eq_s2_lead")}</p></div>
      <div class="two-col reveal"><div></div><div>
        <p>{c("eq_s2_p1")}</p>
        <p style="margin-top:24px;"><a class="cta-primary" href="{rel(2)}{slug_of('manifeste')}">{c("eq_cta")} {ARR}</a></p>
      </div></div>
    </div></section>'''
    page("equipe",
         c("eq_meta_title"),
         c("eq_meta_desc"),
         2, body,
         trail=[(c("crumb_home"), "home"), (c("crumb_cabinet"), "cabinet"), (c("eq_crumb"), "equipe")], jsonld=[person_ld], active="cabinet")


def build_manifeste():
    beliefs = [c("man_b1"), c("man_b2"), c("man_b3"), c("man_b4"),
               c("man_b5"), c("man_b6"), c("man_b7"), c("man_b8")]
    blocks = "\n".join(f'        <p class="reveal" style="font-family:var(--font-display); font-weight:500; font-size:clamp(22px,3vw,34px); line-height:1.3; letter-spacing:-0.02em; color:var(--ink-900); max-width:26ch; margin:0 0 40px;">{b}</p>' for b in beliefs)
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("man_eyebrow")}</p>
      <h1 class="page-head__title reveal">{c("man_h1")}</h1>
    </header>
    <section class="section section--alt"><div class="shell">
{blocks}
        <p class="reveal muted" style="margin-top:32px; border-top:1px solid rgba(11,18,71,0.10); padding-top:32px;">ShōrAI Consulting</p>
        <p class="reveal" style="margin-top:40px;"><a class="cta-primary" href="{rel(2)}{href('contact')}">{c("man_cta")} {ARR}</a></p>
    </div></section>'''
    page("manifeste",
         c("man_meta_title"),
         c("man_meta_desc"),
         2, body,
         trail=[(c("crumb_home"), "home"), (c("crumb_cabinet"), "cabinet"), (c("man_crumb"), "manifeste")], active="cabinet")


def build_cas():
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("cas_eyebrow")}</p>
      <h1 class="page-head__title reveal">{c("cas_h1")}</h1>
      <p class="page-head__lead reveal">{c("cas_lead")}</p>
    </header>

    <section class="section section--alt"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("cas_fmt_eb")}</p></div></div>
      <div class="feature-list reveal">
        <div><h4>{c("cas_fmt_f1_h")}</h4><p>{c("cas_fmt_f1_p")}</p></div>
        <div><h4>{c("cas_fmt_f2_h")}</h4><p>{c("cas_fmt_f2_p")}</p></div>
        <div><h4>{c("cas_fmt_f3_h")}</h4><p>{c("cas_fmt_f3_p")}</p></div>
        <div><h4>{c("cas_fmt_f4_h")}</h4><p>{c("cas_fmt_f4_p")}</p></div>
        <div><h4>{c("cas_fmt_f5_h")}</h4><p>{c("cas_fmt_f5_p")}</p></div>
        <div><h4>{c("cas_fmt_f6_h")}</h4><p>{c("cas_fmt_f6_p")}</p></div>
      </div>
    </div></section>

    <section class="section"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("cas_c1_eb")}</p><h2 class="section__title">{c("cas_c1_title")}</h2></div></div>
      <ol class="editorial-list reveal">
        <li><span class="num">01</span><div><span class="it-title">{c("cas_row1_t")}</span><p class="it-desc">{c("cas_ph_context")}</p></div></li>
        <li><span class="num">02</span><div><span class="it-title">{c("cas_row2_t")}</span><p class="it-desc">{c("cas_ph_problem")}</p></div></li>
        <li><span class="num">03</span><div><span class="it-title">{c("cas_row3_t")}</span><p class="it-desc">{c("cas_ph_approach")}</p></div></li>
        <li><span class="num">04</span><div><span class="it-title">{c("cas_row4_t")}</span><p class="it-desc">{c("cas_ph_result")}</p></div></li>
        <li><span class="num">05</span><div><span class="it-title">{c("cas_row5_t")}</span><p class="it-desc">{c("cas_ph_blind")}</p></div></li>
        <li><span class="num">06</span><div><span class="it-title">{c("cas_row6_t")}</span><p class="it-desc">{c("cas_ph_next")}</p></div></li>
      </ol>
    </div></section>

    <section class="section section--alt"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("cas_c2_eb")}</p><h2 class="section__title">{c("cas_c2_title")}</h2></div></div>
      <ol class="editorial-list reveal">
        <li><span class="num">01</span><div><span class="it-title">{c("cas_row1_t")}</span><p class="it-desc">{c("cas_ph_context")}</p></div></li>
        <li><span class="num">02</span><div><span class="it-title">{c("cas_row2_t")}</span><p class="it-desc">{c("cas_ph_problem")}</p></div></li>
        <li><span class="num">03</span><div><span class="it-title">{c("cas_row3_t")}</span><p class="it-desc">{c("cas_ph_approach2")}</p></div></li>
        <li><span class="num">04</span><div><span class="it-title">{c("cas_row4_t")}</span><p class="it-desc">{c("cas_ph_result")}</p></div></li>
        <li><span class="num">05</span><div><span class="it-title">{c("cas_row5_t")}</span><p class="it-desc">{c("cas_ph_blind")}</p></div></li>
        <li><span class="num">06</span><div><span class="it-title">{c("cas_row6_t")}</span><p class="it-desc">{c("cas_ph_next")}</p></div></li>
      </ol>
    </div></section>

    <section class="section"><div class="shell">
      <div class="reveal" style="max-width:640px;">
        <p class="eyebrow">{c("cas_other_eb")}</p>
        <p class="section__lead" style="margin-top:16px;">{c("cas_other_lead")}</p>
        <p style="margin-top:24px;"><a class="btn btn--grad" href="{rel(1)}{href('contact')}">{c("cas_other_cta")} {ARR}</a></p>
      </div>
    </div></section>'''
    page("cas",
         c("cas_meta_title"),
         c("cas_meta_desc"),
         1, body,
         trail=[(c("crumb_home"), "home"), (c("cas_crumb"), "cas")], active="cas")


def build_insights():
    articles = [c("ins_a1"), c("ins_a2"), c("ins_a3"), c("ins_a4"), c("ins_a5")]
    art_rows = "\n".join(f'''        <li><span class="num">{i+1:02d}</span><div><span class="it-title">{a}</span><p class="it-desc muted ital">{c("ins_soon")}</p></div></li>''' for i, a in enumerate(articles))
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("ins_eyebrow")}</p>
      <h1 class="page-head__title reveal">{c("ins_h1")}</h1>
      <p class="page-head__lead reveal">{c("ins_lead")}</p>
    </header>

    <section class="section section--alt"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("ins_s1_eb")}</p></div></div>
      <div class="feature-list reveal">
        <div><h4>{c("ins_s1_f1_h")}</h4><p>{c("ins_s1_f1_p")}</p></div>
        <div><h4>{c("ins_s1_f2_h")}</h4><p>{c("ins_s1_f2_p")}</p></div>
      </div>
    </div></section>

    <section class="section"><div class="shell">
      <div class="section__head reveal"><div><p class="eyebrow">{c("ins_s2_eb")}</p></div></div>
      <ol class="editorial-list reveal">
{art_rows}
      </ol>
      <p class="reveal" style="margin-top:40px;"><a class="cta-primary" href="{rel(1)}{href('contact')}">{c("ins_cta")} {ARR}</a></p>
    </div></section>'''
    page("insights",
         c("ins_meta_title"),
         c("ins_meta_desc"),
         1, body,
         trail=[(c("crumb_home"), "home"), (c("ins_crumb"), "insights")], active="insights")


def build_contact():
    contact_ld = json.dumps({"@context": "https://schema.org", "@type": "ContactPage",
        "name": c("con_ld_name"),
        "mainEntity": {"@type": "Organization", "name": "shōrAI",
            "contactPoint": {"@type": "ContactPoint", "contactType": "sales",
                "email": CONTACT["email"],
                "availableLanguage": ["French", "English", "Spanish", "Portuguese"]}}}, ensure_ascii=False)
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("con_eyebrow")}</p>
      <h1 class="page-head__title reveal">{c("con_h1")}</h1>
      <p class="page-head__lead reveal">{c("con_lead")}</p>
    </header>

    <section class="section section--alt"><div class="shell">
      <div class="contact reveal">
        <div class="contact__left">
          <ul class="contact__bullets">
            <li>{c("con_b1")}</li>
            <li>{c("con_b2")}</li>
            <li>{c("con_b3")}</li>
          </ul>
          <div class="contact__details">
            <div class="contact__detail"><span class="contact__detail-label">{c("con_d_email")}</span><a class="contact__detail-value" href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></div>
            <div class="contact__detail"><span class="contact__detail-label">{c("con_d_phone")}</span><span class="contact__detail-value">{c("con_d_phone_v")}</span></div>
            <div class="contact__detail"><span class="contact__detail-label">{c("con_d_avail")}</span><span class="contact__detail-value">{c("con_d_avail_v")}</span></div>
            <div class="contact__detail"><span class="contact__detail-label">{c("con_d_cover")}</span><span class="contact__detail-value">{c("con_d_cover_v")}</span></div>
          </div>
        </div>

        <form id="contactForm" class="form" novalidate>
          <div class="form__row">
            <div class="form__field"><label for="f-name">{c("con_f_name")}</label><input id="f-name" name="name" required placeholder="{c("con_f_name_ph")}"></div>
            <div class="form__field"><label for="f-company">{c("con_f_company")}</label><input id="f-company" name="company" placeholder="Acme SA"></div>
          </div>
          <div class="form__row">
            <div class="form__field"><label for="f-email">{c("con_f_email")}</label><input id="f-email" name="email" type="email" required placeholder="{c("con_f_email_ph")}"></div>
            <div class="form__field"><label for="f-phone">{c("con_f_team")}</label>
              <select id="f-phone" name="phone"><option value="">{c("con_f_choose")}</option><option>10–49</option><option>50–249</option><option>250–1000</option><option>1000+</option></select></div>
          </div>
          <div class="form__field"><label for="f-msg">{c("con_f_msg")}</label><textarea id="f-msg" name="message" required placeholder="{c("con_f_msg_ph")}" rows="4"></textarea></div>
          <label class="form__consent" style="display:flex; gap:10px; align-items:flex-start; font-size:13px; color:var(--ink-500);"><input type="checkbox" name="consent" required style="margin-top:3px; accent-color:var(--brand-orange-500);"> {c("con_f_consent")}</label>
          <button type="submit" class="form__submit">{c("con_f_submit")} →</button>
          <p id="formMsg" class="form__msg" style="font-size:13px;"></p>
          <p style="font-size:13px; color:var(--ink-400);">{c("con_f_note")}</p>
        </form>
      </div>
    </div></section>

    <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>'''
    page("contact",
         c("con_meta_title"),
         c("con_meta_desc"),
         1, body,
         trail=[(c("crumb_home"), "home"), (c("con_crumb"), "contact")], jsonld=[contact_ld])


def _legal(pkey, title, meta_title, meta_desc, inner, robots):
    body = f'''    <header class="page-head shell">
      <p class="eyebrow reveal">{c("legal_eyebrow")}</p>
      <h1 class="page-head__title reveal" style="font-size:clamp(32px,5vw,60px);">{title}</h1>
    </header>
    <section class="section section--alt"><div class="shell measure reveal" style="color:var(--ink-600); font-size:17px; line-height:1.7;">
{inner}
    </div></section>'''
    page(pkey, meta_title, meta_desc, 2, body,
         trail=[(c("crumb_home"), "home"), (title, pkey)], robots=robots)


def build_legal():
    h2 = 'style="font-family:var(--font-display); font-weight:600; font-size:24px; color:var(--ink-900); margin:32px 0 12px;"'
    _legal("legal_mentions", c("lm_title"),
        c("lm_meta_title"), c("lm_meta_desc"),
        f'''      <h2 {h2}>{c("lm_h_editor")}</h2>
      <p>{c("lm_editor")}</p>
      <h2 {h2}>{c("lm_h_director")}</h2><p>{c("lm_director")}</p>
      <h2 {h2}>{c("lm_h_host")}</h2><p>{c("lm_host")}</p>
      <h2 {h2}>{c("lm_h_contact")}</h2><p><a style="color:var(--brand-blue-700);" href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></p>
      <h2 {h2}>{c("lm_h_ip")}</h2><p>{c("lm_ip")}</p>''',
        robots="noindex, follow")

    _legal("legal_confidentialite", c("lc_title"),
        c("lc_meta_title"), c("lc_meta_desc"),
        f'''      <p>{c("lc_intro")}</p>
      <ol class="editorial-list" style="margin-top:32px;">
        <li><span class="num">01</span><div><span class="it-title">{c("lc_i1_t")}</span><p class="it-desc">{c("lc_i1_d")}</p></div></li>
        <li><span class="num">02</span><div><span class="it-title">{c("lc_i2_t")}</span><p class="it-desc">{c("lc_i2_d")}</p></div></li>
        <li><span class="num">03</span><div><span class="it-title">{c("lc_i3_t")}</span><p class="it-desc">{c("lc_i3_d")}</p></div></li>
        <li><span class="num">04</span><div><span class="it-title">{c("lc_i4_t")}</span><p class="it-desc">{c("lc_i4_d")}</p></div></li>
        <li><span class="num">05</span><div><span class="it-title">{c("lc_i5_t")}</span><p class="it-desc">{c("lc_i5_d")}</p></div></li>
        <li><span class="num">06</span><div><span class="it-title">{c("lc_i6_t")}</span><p class="it-desc">info@shorai-group.com</p></div></li>
        <li><span class="num">07</span><div><span class="it-title">{c("lc_i7_t")}</span><p class="it-desc">{c("lc_i7_d")}</p></div></li>
      </ol>''',
        robots="index, follow")

    _legal("legal_cookies", c("lk_title"),
        c("lk_meta_title"), c("lk_meta_desc"),
        f'''      <p>{c("lk_intro")}</p>
      <div class="feature-list" style="margin-top:24px;">
        <div><h4>{c("lk_f1_h")}</h4><p>{c("lk_f1_p")}</p></div>
        <div><h4>{c("lk_f2_h")}</h4><p>{c("lk_f2_p")}</p></div>
      </div>
      <p style="margin-top:24px;">{c("lk_more")}</p>''',
        robots="noindex, follow")


def build_404():
    doc = '''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page introuvable — 404 | shōrAI</title>
  <meta name="description" content="Cette page n'existe pas, ou plus. Retour à l'accueil shōrAI.">
  <meta name="robots" content="noindex, follow">
  <meta name="theme-color" content="#02062A">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="/css/site.css">
</head>
<body>
  <nav class="nav"><div class="nav__inner">
    <a class="nav__brand" href="/fr/" aria-label="shōrAI"><img src="/assets/mark-color.png" alt="" width="34" height="34"><span>shōrAI</span></a>
    <a class="nav__cta" href="/fr/contact/">Prendre RDV <span aria-hidden="true">→</span></a>
  </div></nav>
  <main id="main">
    <section class="section" style="min-height:70vh; display:flex; align-items:center; padding-top:160px;">
      <div class="shell">
        <p class="eyebrow" style="color:var(--brand-orange-500);">Erreur 404</p>
        <h1 class="page-head__title" style="margin:24px 0;">Page introuvable</h1>
        <p class="page-head__lead">Cette page n'existe pas, ou plus. Le silence Ma 間 a parfois ses raisons.</p>
        <p style="margin-top:32px;"><a class="btn btn--grad" href="/fr/">Retour à l'accueil <span class="arrow" aria-hidden="true">→</span></a></p>
      </div>
    </section>
  </main>
  <footer class="footer"><div class="footer__bg"></div><div class="shell"><div class="footer__bottom" style="border-top:0;">
    <span>© 2026 ShōrAI Consulting · <a href="/fr/legal/mentions-legales/">Mentions légales</a></span>
    <span class="footer__kanji">将来 · shōrai · future</span>
  </div></div></footer>
</body>
</html>
'''
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(doc)
