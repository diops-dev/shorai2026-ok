# shōrAI — Site web

Site statique multi-pages de **ShōrAI Consulting OÜ**. HTML / CSS / JS pur, sans build runtime.

**Direction artistique** : système de design officiel shōrAI (extrait du handoff Claude Design) — bleu indigo `#02062A`, gradient orange/or `#E94B1F → #FFB44A`, typographie **Sora** (display) + **DM Sans** (corps) + **JetBrains Mono** (labels) + **Noto Serif JP** (kanji 将来). Nav pilule flottante, hero indigo/twilight, cartes glassmorphiques, badges numérotés orange.

Compatible **GitHub Pages** (`diops-dev.github.io` → domaine `shorai-group.com`) puis **Hostinger**.

## Structure

```
shorai-website/
├── index.html                 ← redirige vers /fr/
├── 404.html                   ← page d'erreur (chemins absolus)
├── CNAME                       ← shorai-group.com (GitHub Pages)
├── .nojekyll                   ← désactive Jekyll sur GitHub Pages
├── robots.txt
├── sitemap.xml
├── assets/                     ← logos (wordmark blanc, mark SVG), favicons, kanji
├── css/site.css                ← design system complet « Ma 間 »
├── js/site.js                  ← nav mobile, reveal, FAQ, cookies, formulaire
├── fr/                         ← le site (français — marché principal)
│   ├── index.html              ← Accueil
│   ├── philosophie/
│   ├── expertises/             ← hub + 4 expertises
│   │   ├── strategie-ia/
│   │   ├── transformation-ia-generative/
│   │   ├── gouvernance-et-ethique-ia/
│   │   └── architecture-data-ia/
│   ├── secteurs/               ← hub + 5 secteurs
│   ├── methode/
│   ├── etudes-de-cas/
│   ├── insights/
│   ├── cabinet/                ← cabinet + equipe + manifeste
│   ├── contact/
│   └── legal/                  ← mentions, confidentialité, cookies
└── _build/                     ← générateur Python (NE PAS déployer)
```

> Le dossier `_build/` contient le générateur qui produit les pages. Il n'a pas besoin d'être en ligne (déjà bloqué dans `robots.txt`). Pour modifier les textes ou la structure, éditer les fichiers `_build/gen_*.py` puis relancer `python3 _build/build.py`.

## SEO intégré

- Meta title (≤ 60), meta description (≤ 155), un seul H1 par page.
- Canonical auto-référent + hreflang `fr` / `x-default` sur chaque page.
- Open Graph + Twitter Card.
- JSON-LD : `ProfessionalService` + `WebSite` (accueil), `BreadcrumbList` (toutes pages internes), `Service`, `FAQPage`, `HowTo`, `ContactPage`, `Person`.
- `sitemap.xml` (pages indexables) + `robots.txt`.
- Pages légales sensibles en `noindex, follow`.
- Accessibilité : skip-link, focus visible kintsugi, contrastes WCAG AA (washi sur sumi ≈ 14:1).

## Multilingue (à venir)

Architecture prête pour `/en/`, `/ja/`, `/es/` (cf. `ARBORESCENCE_SEO.md`). Le sélecteur de langue est présent ; les variantes pointent vers `/fr/` tant qu'elles ne sont pas traduites. Quand une langue est ajoutée : créer le sous-dossier, traduire les slugs, et compléter les `hreflang` réciproques dans `_build/gen_common.py`.

## Formulaire de contact (EmailJS)

Le formulaire (`fr/contact/`) fonctionne en **fallback mailto** par défaut. Pour activer l'envoi côté client sans serveur (compatible GitHub Pages / Hostinger statique) :

1. Créer un compte EmailJS, un service et un template.
2. Dans `js/site.js`, renseigner `serviceId`, `templateId`, `publicKey`.
3. Le script utilise alors EmailJS ; sinon il ouvre le client mail de l'utilisateur.

## Déploiement

### GitHub Pages (`diops-dev.github.io`)
1. Pousser le contenu de `shorai-website/` à la racine du dépôt `diops-dev.github.io` (ou dans `/docs` selon la config Pages).
2. Le fichier `CNAME` configure le domaine `shorai-group.com`. `.nojekyll` est présent.
3. Dans le registrar DNS de `shorai-group.com` : enregistrement `A`/`CNAME` vers GitHub Pages.

### Hostinger
1. Uploader le contenu de `shorai-website/` (sauf `_build/`) dans `public_html/` via le gestionnaire de fichiers ou FTP.
2. Le `404.html` et les chemins absolus (`/assets/`, `/css/`, `/fr/`) fonctionnent sur tout hébergement à la racine du domaine.
3. Ajouter une règle de redirection `/` → `/fr/` (déjà gérée par `index.html` côté client).

## À compléter avant mise en ligne

- [ ] Mentions légales : adresse Estonie, n° registre, n° TVA, hébergeur.
- [ ] Clés EmailJS dans `js/site.js`.
- [ ] Images Open Graph (`og:image` 1200×630) — actuellement non définies.
- [ ] Vérifier le lien LinkedIn de l'entreprise.
- [ ] Soumettre `sitemap.xml` à Google Search Console.

---

© 2026 ShōrAI Consulting OÜ · 将来 · shōrai · future
