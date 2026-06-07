# -*- coding: utf-8 -*-
"""Runner: build all pages in all languages + root redirect + robots + sitemap."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import gen_common
from gen_common import OUT, SITE, LANGS, SLUGS
import gen_core, gen_expertises, gen_secteurs, gen_rest

def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# ---- Build all pages, for each language ----
for lang in LANGS:
    gen_common.LANG = lang
    gen_core.build_home(); gen_core.build_philosophie(); gen_core.build_methode()
    gen_expertises.build_hub(); gen_expertises.build_children()
    gen_secteurs.build_hub(); gen_secteurs.build_children()
    gen_rest.build_cabinet(); gen_rest.build_equipe(); gen_rest.build_manifeste()
    gen_rest.build_cas(); gen_rest.build_insights(); gen_rest.build_contact()
    gen_rest.build_legal()

# 404 is language-neutral (FR copy) — built once.
gen_common.LANG = "fr"
gen_rest.build_404()

# ---- Root redirect → /fr/ ----
write("index.html", f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>shōrAI — Conseil IA pour PME et ETI</title>
  <meta http-equiv="refresh" content="0; url=/fr/">
  <link rel="canonical" href="{SITE}/fr/">
  <link rel="alternate" hreflang="fr" href="{SITE}/fr/">
  <link rel="alternate" hreflang="en" href="{SITE}/en/">
  <link rel="alternate" hreflang="es" href="{SITE}/es/">
  <link rel="alternate" hreflang="pt" href="{SITE}/pt/">
  <link rel="alternate" hreflang="x-default" href="{SITE}/fr/">
  <meta name="robots" content="noindex, follow">
  <script>location.replace("/fr/");</script>
</head>
<body><p>Redirection vers <a href="/fr/">shorai-group.com/fr/</a>…</p></body>
</html>
''')

# ---- robots.txt ----
disallow = ""
for lang in LANGS:
    disallow += f"Disallow: /{lang}/{SLUGS[lang]['legal_mentions']}\n"
    disallow += f"Disallow: /{lang}/{SLUGS[lang]['legal_cookies']}\n"
write("robots.txt", f'''User-agent: *
Allow: /

Disallow: /_build/
{disallow}
Sitemap: {SITE}/sitemap.xml
''')

# ---- sitemap.xml (multilingual, indexable pages only) ----
# page_key -> (priority, changefreq); legal/mentions & cookies are noindex → excluded.
PAGES = [
    ("home", "1.0", "weekly"),
    ("philosophie", "0.7", "monthly"),
    ("expertises", "0.9", "monthly"),
    ("exp_strategie", "0.8", "monthly"),
    ("exp_transfo", "0.8", "monthly"),
    ("exp_gouvernance", "0.8", "monthly"),
    ("exp_archi", "0.8", "monthly"),
    ("secteurs", "0.9", "monthly"),
    ("sec_finance", "0.7", "monthly"),
    ("sec_industrie", "0.7", "monthly"),
    ("sec_retail", "0.7", "monthly"),
    ("sec_sante", "0.7", "monthly"),
    ("sec_public", "0.7", "monthly"),
    ("methode", "0.8", "monthly"),
    ("cas", "0.6", "monthly"),
    ("insights", "0.7", "weekly"),
    ("cabinet", "0.6", "monthly"),
    ("equipe", "0.5", "monthly"),
    ("manifeste", "0.5", "monthly"),
    ("contact", "0.8", "monthly"),
    ("legal_confidentialite", "0.3", "yearly"),
]
LASTMOD = "2026-06-03"

def alt_links(page_key):
    out = ""
    for lng in LANGS:
        s = SLUGS[lng][page_key]
        out += f'    <xhtml:link rel="alternate" hreflang="{lng}" href="{SITE}/{lng}/{s}"/>\n'
    s_fr = SLUGS["fr"][page_key]
    out += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/fr/{s_fr}"/>\n'
    return out

urls = ""
for page_key, prio, freq in PAGES:
    alts = alt_links(page_key)
    for lng in LANGS:
        s = SLUGS[lng][page_key]
        urls += f'''  <url>
    <loc>{SITE}/{lng}/{s}</loc>
    <lastmod>{LASTMOD}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
{alts}  </url>
'''
write("sitemap.xml", f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{urls}</urlset>
''')

# ---- GitHub Pages helpers ----
write(".nojekyll", "")
write("CNAME", "shorai-group.com\n")

print("BUILD OK")
