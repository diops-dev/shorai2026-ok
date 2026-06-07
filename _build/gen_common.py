# -*- coding: utf-8 -*-
"""shōrAI static site generator — chrome (head, nav, footer) + i18n architecture.
   Design system: bleu indigo + orange/or (du fichier design Claude Design).

   i18n: build.py sets gen_common.LANG before each language pass and loops over
   LANGS. Content strings in gen_*.py are FR for all languages (placeholder) for
   now — only the architecture is internationalised here. Chrome labels live in
   UI[lang]; URL slugs live in SLUGS[lang][page_key]. Both are filled with the FR
   values in every language as placeholders, ready to translate.
"""
import os, html, json

SITE = "https://shorai-group.com"
OUT = os.path.join(os.path.dirname(__file__), "..")

# ---- i18n globals -----------------------------------------------------------
LANGS = ["fr", "en", "es", "pt"]
LANG = "fr"  # mutated by build.py for each pass

OG_LOCALE = {"fr": "fr_FR", "en": "en_US", "es": "es_ES", "pt": "pt_PT"}
HTML_LANG = {"fr": "fr", "en": "en", "es": "es", "pt": "pt"}

# Slugs per language, keyed by stable page_key. FR slugs are used as placeholders
# for every language; translate per language later (e.g. SLUGS["en"]["expertises"]
# = "expertise/").
_FR_SLUGS = {
    "home": "",
    "philosophie": "philosophie/",
    "methode": "methode/",
    "expertises": "expertises/",
    "exp_strategie": "expertises/strategie-ia/",
    "exp_transfo": "expertises/transformation-ia-generative/",
    "exp_gouvernance": "expertises/gouvernance-et-ethique-ia/",
    "exp_archi": "expertises/architecture-data-ia/",
    "secteurs": "secteurs/",
    "sec_finance": "secteurs/finance-assurance/",
    "sec_industrie": "secteurs/industrie-manufacturing/",
    "sec_retail": "secteurs/retail-distribution/",
    "sec_sante": "secteurs/sante-life-sciences/",
    "sec_public": "secteurs/secteur-public/",
    "cabinet": "cabinet/",
    "equipe": "cabinet/equipe/",
    "manifeste": "cabinet/manifeste/",
    "cas": "etudes-de-cas/",
    "insights": "insights/",
    "contact": "contact/",
    "legal_mentions": "legal/mentions-legales/",
    "legal_confidentialite": "legal/politique-de-confidentialite/",
    "legal_cookies": "legal/politique-cookies/",
}
_EN_SLUGS = {
    "home": "",
    "philosophie": "philosophy/",
    "methode": "method/",
    "expertises": "expertise/",
    "exp_strategie": "expertise/ai-strategy/",
    "exp_transfo": "expertise/generative-ai-transformation/",
    "exp_gouvernance": "expertise/ai-governance-compliance/",
    "exp_archi": "expertise/data-architecture-delivery/",
    "secteurs": "industries/",
    "sec_finance": "industries/finance-insurance/",
    "sec_industrie": "industries/industry-manufacturing/",
    "sec_retail": "industries/retail-distribution/",
    "sec_sante": "industries/healthcare-life-sciences/",
    "sec_public": "industries/public-sector/",
    "cabinet": "firm/",
    "equipe": "firm/team/",
    "manifeste": "firm/manifesto/",
    "cas": "case-studies/",
    "insights": "insights/",
    "contact": "contact/",
    "legal_mentions": "legal/legal-notice/",
    "legal_confidentialite": "legal/privacy-policy/",
    "legal_cookies": "legal/cookie-policy/",
}
_ES_SLUGS = {
    "home": "",
    "philosophie": "filosofia/",
    "methode": "metodo/",
    "expertises": "servicios/",
    "exp_strategie": "servicios/estrategia-ia/",
    "exp_transfo": "servicios/transformacion-ia-generativa/",
    "exp_gouvernance": "servicios/gobernanza-cumplimiento-ia/",
    "exp_archi": "servicios/arquitectura-datos-delivery/",
    "secteurs": "sectores/",
    "sec_finance": "sectores/finanzas-seguros/",
    "sec_industrie": "sectores/industria-manufactura/",
    "sec_retail": "sectores/retail-distribucion/",
    "sec_sante": "sectores/salud-ciencias-vida/",
    "sec_public": "sectores/sector-publico/",
    "cabinet": "gabinete/",
    "equipe": "gabinete/equipo/",
    "manifeste": "gabinete/manifiesto/",
    "cas": "casos/",
    "insights": "insights/",
    "contact": "contacto/",
    "legal_mentions": "legal/aviso-legal/",
    "legal_confidentialite": "legal/politica-privacidad/",
    "legal_cookies": "legal/politica-cookies/",
}
_PT_SLUGS = {
    "home": "",
    "philosophie": "filosofia/",
    "methode": "metodo/",
    "expertises": "servicos/",
    "exp_strategie": "servicos/estrategia-ia/",
    "exp_transfo": "servicos/transformacao-ia-generativa/",
    "exp_gouvernance": "servicos/governanca-conformidade-ia/",
    "exp_archi": "servicos/arquitetura-dados-delivery/",
    "secteurs": "setores/",
    "sec_finance": "setores/financas-seguros/",
    "sec_industrie": "setores/industria-manufatura/",
    "sec_retail": "setores/retalho-distribuicao/",
    "sec_sante": "setores/saude-ciencias-vida/",
    "sec_public": "setores/setor-publico/",
    "cabinet": "gabinete/",
    "equipe": "gabinete/equipa/",
    "manifeste": "gabinete/manifesto/",
    "cas": "casos/",
    "insights": "insights/",
    "contact": "contacto/",
    "legal_mentions": "legal/aviso-legal/",
    "legal_confidentialite": "legal/politica-privacidade/",
    "legal_cookies": "legal/politica-cookies/",
}
SLUGS = {"fr": dict(_FR_SLUGS), "en": _EN_SLUGS, "es": _ES_SLUGS, "pt": _PT_SLUGS}

# Chrome / UI labels per language. FR placeholder in all four languages.
_FR_UI = {
    "skip": "Aller au contenu",
    "brand_aria": "shōrAI — accueil",
    "nav_expertises": "Expertises",
    "nav_secteurs": "Secteurs",
    "nav_methode": "Méthode",
    "nav_cas": "Cas clients",
    "nav_insights": "Insights",
    "nav_cabinet": "Cabinet",
    "nav_cta": "Prendre RDV",
    "menu_label": "Menu",
    "menu_close": "Fermer",
    "lang_aria": "Choisir la langue",
    "crumbs_aria": "Fil d'Ariane",
    "crumbs_sep": "/",
    "footer_tag": "Conseil en stratégie IA pour PME &amp; ETI.<br>De l'audit terrain à l'automatisation. 将来.",
    "footer_exp": "Expertises",
    "footer_sec": "Secteurs",
    "footer_sec_all": "Tous les secteurs",
    "footer_cabinet": "Cabinet",
    "footer_cabinet_link": "Le cabinet",
    "footer_methode": "Méthode",
    "footer_manifeste": "Manifeste",
    "footer_copyright": "© 2026 ShōrAI Consulting · Tous droits réservés",
    "footer_kanji": "将来 · shōrai · future",
    "footer_legal": "Mentions légales",
    "footer_privacy": "Confidentialité",
    "footer_cookies": "Cookies",
    "cookie_aria": "Préférences cookies",
    "cookie_text": "Nous utilisons des cookies analytiques anonymisés pour comprendre l'usage du site. Pas de publicité, pas de tracking tiers.",
    "cookie_accept": "Accepter",
    "cookie_refuse": "Refuser",
    "cookie_more": "En savoir plus",
}
_EN_UI = {
    "skip": "Skip to content",
    "brand_aria": "shōrAI — home",
    "nav_expertises": "Expertise",
    "nav_secteurs": "Industries",
    "nav_methode": "Method",
    "nav_cas": "Case studies",
    "nav_insights": "Insights",
    "nav_cabinet": "Firm",
    "nav_cta": "Book a call",
    "menu_label": "Menu",
    "menu_close": "Close",
    "lang_aria": "Choose language",
    "crumbs_aria": "Breadcrumb",
    "crumbs_sep": "/",
    "footer_tag": "AI strategy consulting for SMEs &amp; mid-market companies.<br>From field audit to automation. 将来.",
    "footer_exp": "Expertise",
    "footer_sec": "Industries",
    "footer_sec_all": "All industries",
    "footer_cabinet": "Firm",
    "footer_cabinet_link": "The firm",
    "footer_methode": "Method",
    "footer_manifeste": "Manifesto",
    "footer_copyright": "© 2026 ShōrAI Consulting · All rights reserved",
    "footer_kanji": "将来 · shōrai · future",
    "footer_legal": "Legal notice",
    "footer_privacy": "Privacy",
    "footer_cookies": "Cookies",
    "cookie_aria": "Cookie preferences",
    "cookie_text": "We use anonymised analytics cookies to understand how the site is used. No advertising, no third-party tracking.",
    "cookie_accept": "Accept",
    "cookie_refuse": "Decline",
    "cookie_more": "Learn more",
}
_ES_UI = {
    "skip": "Saltar al contenido",
    "brand_aria": "shōrAI — inicio",
    "nav_expertises": "Servicios",
    "nav_secteurs": "Sectores",
    "nav_methode": "Método",
    "nav_cas": "Casos",
    "nav_insights": "Insights",
    "nav_cabinet": "Gabinete",
    "nav_cta": "Reservar cita",
    "menu_label": "Menú",
    "menu_close": "Cerrar",
    "lang_aria": "Elegir idioma",
    "crumbs_aria": "Ruta de navegación",
    "crumbs_sep": "/",
    "footer_tag": "Consultoría en estrategia de IA para pymes y empresas medianas.<br>De la auditoría de campo a la automatización. 将来.",
    "footer_exp": "Servicios",
    "footer_sec": "Sectores",
    "footer_sec_all": "Todos los sectores",
    "footer_cabinet": "Gabinete",
    "footer_cabinet_link": "El gabinete",
    "footer_methode": "Método",
    "footer_manifeste": "Manifiesto",
    "footer_copyright": "© 2026 ShōrAI Consulting · Todos los derechos reservados",
    "footer_kanji": "将来 · shōrai · future",
    "footer_legal": "Aviso legal",
    "footer_privacy": "Privacidad",
    "footer_cookies": "Cookies",
    "cookie_aria": "Preferencias de cookies",
    "cookie_text": "Utilizamos cookies analíticas anonimizadas para entender el uso del sitio. Sin publicidad, sin rastreo de terceros.",
    "cookie_accept": "Aceptar",
    "cookie_refuse": "Rechazar",
    "cookie_more": "Más información",
}
_PT_UI = {
    "skip": "Ir para o conteúdo",
    "brand_aria": "shōrAI — início",
    "nav_expertises": "Serviços",
    "nav_secteurs": "Setores",
    "nav_methode": "Método",
    "nav_cas": "Casos",
    "nav_insights": "Insights",
    "nav_cabinet": "Gabinete",
    "nav_cta": "Marcar reunião",
    "menu_label": "Menu",
    "menu_close": "Fechar",
    "lang_aria": "Escolher idioma",
    "crumbs_aria": "Trilho de navegação",
    "crumbs_sep": "/",
    "footer_tag": "Consultoria em estratégia de IA para PME e empresas de média dimensão.<br>Da auditoria no terreno à automatização. 将来.",
    "footer_exp": "Serviços",
    "footer_sec": "Setores",
    "footer_sec_all": "Todos os setores",
    "footer_cabinet": "Gabinete",
    "footer_cabinet_link": "O gabinete",
    "footer_methode": "Método",
    "footer_manifeste": "Manifesto",
    "footer_copyright": "© 2026 ShōrAI Consulting · Todos os direitos reservados",
    "footer_kanji": "将来 · shōrai · future",
    "footer_legal": "Aviso legal",
    "footer_privacy": "Privacidade",
    "footer_cookies": "Cookies",
    "cookie_aria": "Preferências de cookies",
    "cookie_text": "Utilizamos cookies analíticos anonimizados para compreender a utilização do site. Sem publicidade, sem rastreio de terceiros.",
    "cookie_accept": "Aceitar",
    "cookie_refuse": "Recusar",
    "cookie_more": "Saber mais",
}
UI = {"fr": dict(_FR_UI), "en": _EN_UI, "es": _ES_UI, "pt": _PT_UI}

# Editorial content per language, keyed by stable string id. Defined in content.py
# to keep this module focused on chrome/i18n plumbing.
from content import CONTENT

CONTACT = {
    "email": "info@shorai-group.com",
    "phone": "+33 6 33 59 87 74",
    "phone_tel": "+33633598774",
    "calendar": "https://calendar.app.google/Mib5EFdjDi21g46s8",
}

EXPERTISES = [
    ("01", "Stratégie IA", "exp_strategie", "Vision, feuille de route, go/no-go."),
    ("02", "Transformation IA générative", "exp_transfo", "Du pilote à la production."),
    ("03", "Gouvernance & conformité", "exp_gouvernance", "AI Act, RGPD, éthique opérationnelle."),
    ("04", "Architecture data & delivery", "exp_archi", "Socle, MLOps, run encadré."),
]
SECTEURS = [
    ("01", "Finance & assurance", "sec_finance", "Risque, KYC, conformité ACPR."),
    ("02", "Industrie & manufacturing", "sec_industrie", "Maintenance prédictive, qualité."),
    ("03", "Retail & distribution", "sec_retail", "Pricing, fidélisation, stocks."),
    ("04", "Santé & life sciences", "sec_sante", "Diagnostic, parcours, conformité."),
    ("05", "Secteur public", "sec_public", "Usager, souveraineté, RGPD."),
]

# Arrow used inline in content
ARR = '<span class="arrow" aria-hidden="true">→</span>'


def t(key):
    """Chrome label for the current language."""
    return UI[LANG][key]


def c(key):
    """Editorial content string for the current language (see content.py)."""
    return CONTENT[LANG][key]


def slug_of(page_key):
    """URL slug (no language prefix) for a page in the current language."""
    return SLUGS[LANG][page_key]


def href(page_key):
    """Relative href (from /{LANG}/) to a page in the current language."""
    return SLUGS[LANG][page_key]


def rel(depth):   # back to /{LANG}/
    return "../" * depth
def aprefix(depth):  # back to site root (assets/css/js)
    return "../" * (depth + 1)


def hreflangs(page_key):
    """Reciprocal hreflang <link> tags for a page across all languages."""
    lines = []
    for lng in LANGS:
        s = SLUGS[lng][page_key]
        lines.append(f'  <link rel="alternate" hreflang="{lng}" href="{SITE}/{lng}/{s}">')
    # x-default → French
    s_fr = SLUGS["fr"][page_key]
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{SITE}/fr/{s_fr}">')
    return "\n".join(lines)


def head(title, desc, page_key, depth, og_type="website", jsonld=None,
         robots="index, follow, max-image-preview:large, max-snippet:-1"):
    ap = aprefix(depth)
    slug = SLUGS[LANG][page_key]
    canon = f"{SITE}/{LANG}/{slug}"
    jl = ""
    if jsonld:
        jl = "\n".join(f'  <script type="application/ld+json">{j}</script>' for j in jsonld)
    return f'''<!DOCTYPE html>
<html lang="{HTML_LANG[LANG]}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <link rel="canonical" href="{canon}">
{hreflangs(page_key)}
  <meta name="robots" content="{robots}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{canon}">
  <meta property="og:site_name" content="shōrAI">
  <meta property="og:locale" content="{OG_LOCALE[LANG]}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(title)}">
  <meta name="twitter:description" content="{html.escape(desc)}">
  <meta name="theme-color" content="#02062A">
  <link rel="icon" type="image/png" sizes="32x32" href="{ap}assets/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="{ap}assets/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{ap}assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="{ap}css/site.css">
{jl}
</head>
<body>
  <a href="#main" class="skip-link" style="position:absolute;left:-9999px;top:0;z-index:300;background:var(--brand-orange-500);color:#fff;padding:12px 20px;">{t('skip')}</a>
'''


def lang_switcher(page_key):
    """Language selector: links to the same page in each language, active = plain text."""
    parts = []
    for lng in LANGS:
        label = lng.upper()
        if lng == LANG:
            parts.append(f'<span class="nav__lang nav__lang--active" aria-current="true">{label}</span>')
        else:
            s = SLUGS[lng][page_key]
            parts.append(f'<a class="nav__lang" href="/{lng}/{s}" hreflang="{lng}">{label}</a>')
    sep = '<span class="nav__lang-sep" aria-hidden="true"> · </span>'
    return f'<div class="nav__langs" aria-label="{t("lang_aria")}">{sep.join(parts)}</div>'


def nav(depth, page_key, active=""):
    r = rel(depth); ap = aprefix(depth)
    def link(label, hk, key):
        cls = ' class="active--page"' if key == active else ''
        return f'<a href="{r}{href(hk)}"{cls}>{label}</a>'
    return f'''  <nav class="nav">
    <div class="nav__inner">
      <a class="nav__brand" href="{r}" aria-label="{t('brand_aria')}">
        <img src="{ap}assets/mark-color.png" alt="" width="34" height="34"><span>shōrAI</span>
      </a>
      <div class="nav__links">
        {link(t('nav_expertises'), "expertises", "expertises")}
        {link(t('nav_secteurs'), "secteurs", "secteurs")}
        {link(t('nav_methode'), "methode", "methode")}
        {link(t('nav_cas'), "cas", "cas")}
        {link(t('nav_insights'), "insights", "insights")}
        {link(t('nav_cabinet'), "cabinet", "cabinet")}
      </div>
      {lang_switcher(page_key)}
      <a class="nav__cta" href="{r}{href('contact')}">{t('nav_cta')} <span aria-hidden="true">→</span></a>
      <button class="nav__burger" aria-label="{t('menu_label')}" aria-controls="mobileMenu">
        <svg width="22" height="22" viewBox="0 0 22 22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><line x1="3" y1="7" x2="19" y2="7"></line><line x1="3" y1="15" x2="19" y2="15"></line></svg>
      </button>
    </div>
  </nav>

  <div class="mobile-menu" id="mobileMenu">
    <button class="mobile-menu__close" aria-label="{t('menu_close')}">✕</button>
    <a href="{r}{href('expertises')}">{t('nav_expertises')}</a>
    <a href="{r}{href('secteurs')}">{t('nav_secteurs')}</a>
    <a href="{r}{href('methode')}">{t('nav_methode')}</a>
    <a href="{r}{href('cas')}">{t('nav_cas')}</a>
    <a href="{r}{href('insights')}">{t('nav_insights')}</a>
    <a href="{r}{href('cabinet')}">{t('nav_cabinet')}</a>
    {lang_switcher(page_key)}
    <a class="mobile-menu__cta" href="{r}{href('contact')}">{t('nav_cta')} →</a>
  </div>
'''


def crumbs(depth, trail):
    """trail = list of (label, page_key_or_None). None => current/leaf."""
    r = rel(depth)
    sep = f'<li class="sep" aria-hidden="true">{t("crumbs_sep")}</li>'
    items = []
    for i, (label, pk) in enumerate(trail):
        if pk is None or i == len(trail) - 1:
            items.append(f'<li aria-current="page">{label}</li>')
        else:
            items.append(f'<li><a href="{r}{href(pk)}">{label}</a></li>')
    ld_items = []
    for i, (label, pk) in enumerate(trail):
        entry = {"@type": "ListItem", "position": i + 1, "name": label}
        if pk is not None:
            entry["item"] = f"{SITE}/{LANG}/{SLUGS[LANG][pk]}"
        ld_items.append(entry)
    ld = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld_items}, ensure_ascii=False)
    return f'''  <nav class="crumbs shell" aria-label="{t('crumbs_aria')}">
    <ol>{sep.join(items)}</ol>
  </nav>
  <script type="application/ld+json">{ld}</script>
'''


def footer(depth):
    r = rel(depth); ap = aprefix(depth)
    exp = "\n".join(f'            <li><a href="{r}{href(hk)}">{c("foot_" + hk)}</a></li>' for _, _, hk, _ in EXPERTISES)
    sec = "\n".join(f'            <li><a href="{r}{href(hk)}">{c("foot_" + hk)}</a></li>' for _, _, hk, _ in SECTEURS[:4])
    return f'''  <footer class="footer">
    <div class="footer__bg"></div>
    <div class="shell">
      <div class="footer__inner">
        <div>
          <div class="footer__brand">
            <img src="{ap}assets/mark-color.png" alt="" width="32" height="32"><span>shōrAI</span>
          </div>
          <p class="footer__tag">{t('footer_tag')}</p>
        </div>
        <div class="footer__col">
          <h5>{t('footer_exp')}</h5>
          <ul>
{exp}
          </ul>
        </div>
        <div class="footer__col">
          <h5>{t('footer_sec')}</h5>
          <ul>
{sec}
            <li><a href="{r}{href('secteurs')}">{t('footer_sec_all')}</a></li>
          </ul>
        </div>
        <div class="footer__col">
          <h5>{t('footer_cabinet')}</h5>
          <ul>
            <li><a href="{r}{href('cabinet')}">{t('footer_cabinet_link')}</a></li>
            <li><a href="{r}{href('methode')}">{t('footer_methode')}</a></li>
            <li><a href="{r}{href('manifeste')}">{t('footer_manifeste')}</a></li>
            <li><a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></li>
          </ul>
        </div>
      </div>
      <div class="footer__bottom">
        <span>{t('footer_copyright')}</span>
        <span class="footer__kanji">{t('footer_kanji')}</span>
        <span><a href="{r}{href('legal_mentions')}">{t('footer_legal')}</a> · <a href="{r}{href('legal_confidentialite')}">{t('footer_privacy')}</a> · <a href="{r}{href('legal_cookies')}">{t('footer_cookies')}</a></span>
      </div>
    </div>
  </footer>

  <div class="cookie" id="cookie" role="dialog" aria-label="{t('cookie_aria')}">
    <p>{t('cookie_text')}</p>
    <div class="cookie__row">
      <button class="accept" data-cookie="accept">{t('cookie_accept')}</button>
      <button class="refuse" data-cookie="refuse">{t('cookie_refuse')}</button>
      <a href="{r}{href('legal_cookies')}">{t('cookie_more')}</a>
    </div>
  </div>

  <script src="{ap}js/site.js" defer></script>
'''


def page(page_key, title, desc, depth, body, trail=None, og_type="website", jsonld=None,
         robots="index, follow, max-image-preview:large, max-snippet:-1", active=""):
    """Render one page for the current LANG. Output path = {LANG}/{slug}index.html."""
    slug = SLUGS[LANG][page_key]
    path = f"{LANG}/{slug}index.html"
    doc = head(title, desc, page_key, depth, og_type=og_type, jsonld=jsonld, robots=robots)
    doc += nav(depth, page_key, active=active)
    if trail is not None:
        doc += crumbs(depth, trail)
    doc += f'  <main id="main">\n{body}\n  </main>\n'
    doc += footer(depth)
    doc += "</body>\n</html>\n"
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(doc)
    return path
