"""Génère index.html du portfolio (lcabart21.github.io)."""
from datetime import date
import html

GH = "https://github.com/lcabart21/"

DOMAINS = ["Tableur et reporting", "SQL et modélisation", "Python et analyse", "Business intelligence",
           "Data engineering", "Statistiques et ML", "IA générative"]

# (id, date, domaine, titre court, dépôt)
TIMELINE = [
    ("perso", date(2025, 5, 15), 2, "Coûts d'assurance santé", "perso-us-medical-insurance"),
    ("p2", date(2025, 10, 15), 0, "Ventes e-commerce", "oc-p2-analyse-ventes-ecommerce"),
    ("p3", date(2025, 11, 15), 1, "Base assurance habitation", "oc-p3-analyse-sql"),
    ("p4", date(2026, 1, 15), 2, "Sous-nutrition mondiale", "oc-p4-analyse-fao-sous-nutrition"),
    ("p5", date(2026, 3, 15), 1, "Marché immobilier", "oc-p5-marche-immobilier-sql"),
    ("p6", date(2026, 5, 15), 2, "BottleNeck, version initiale", "oc-p6-bottleneck-analyse-stock-ventes"),
    ("p7", date(2026, 7, 8), 3, "Portefeuille projets Sanitoral", "oc-p7-dashboard-powerbi-sanitoral"),
    ("p8", date(2026, 7, 22), 4, "Pipeline dbt et Snowflake", "oc-p8-pipeline-dbt-snowflake"),
    ("p9", date(2026, 9, 3), 5, "Streaming musical", "oc-p9-tendances-streaming-musical"),
    ("p10", date(2026, 9, 10), 3, "Accès à l'eau potable", "oc-p10-dashboard-eau-potable"),
    ("p11", date(2026, 9, 14), 5, "Export de poulet bio", "oc-p11-etude-marche-clustering"),
    ("p12", date(2026, 9, 30), 5, "Faux billets", "oc-p12-detection-faux-billets"),
    ("p13", date(2026, 10, 12), 6, "BottleNeck avec l'IA", "oc-p13-bottleneck-ia"),
]

FEATURED = [
    dict(id="p13", repo="oc-p13-bottleneck-ia", img="p13.jpg",
         alt="Nuage de points prix de vente contre prix d'achat : un seul produit s'écarte de la diagonale",
         title="Reprendre une analyse avec l'IA, sans lui faire confiance aveuglément",
         meta="Projet 13, octobre 2026. Python, pandas, pandera, scikit-learn, Claude.",
         contexte="Mon analyse P6 des ventes et du stock d'un caviste en ligne devait servir à la direction, aux achats et à la logistique.",
         besoin="Fiabiliser les indicateurs et distinguer les erreurs de prix des grands crus légitimement chers.",
         demarche="J'ai utilisé l'IA comme relecteur, avec deux variantes de prompt notées sur une grille fixée à l'avance. J'ai comparé pandera et Great Expectations sur les mêmes règles, puis cinq méthodes de détection d'anomalies. Aucune proposition de l'IA n'a été adoptée sans être exécutée sur les vraies données.",
         resultats="8 erreurs de calcul corrigées. Le prompt structuré en trouvait 8 sur 8, le prompt naïf 6, et son code plantait. Une seule anomalie de prix remonte, et c'est la vraie : Isolation Forest en signalait 22.",
         impact="Les équipes reçoivent des indicateurs justes et une liste de corrections courte. La démarche est documentée et reproductible, avec un mini-plan de formation pour les métiers.",
         limites="La période des ventes n'est pas connue (hypothèse : 12 mois). L'expérience IA repose sur une seule exécution par prompt."),
    dict(id="p12", repo="oc-p12-detection-faux-billets", img="p12.jpg",
         alt="Courbe du rappel et de la précision selon le seuil de décision",
         title="Détecter les faux billets à partir de six mesures",
         meta="Projet 12, septembre 2026. scikit-learn, pipelines, validation croisée.",
         contexte="Un organisme de lutte contre le faux-monnayage scanne les billets et relève six dimensions géométriques.",
         besoin="Prédire si un billet est faux, en priorité sans en laisser passer : un faux non détecté retourne en circulation.",
         demarche="J'ai imputé les valeurs manquantes sans utiliser la cible, puis comparé quatre modèles en validation croisée. J'ai choisi le seuil sur les prédictions hors-pli, en donnant deux fois plus de poids au rappel, et livré un script de prédiction.",
         resultats="98,4 % des faux détectés sur le jeu de test, et 97,6 % des alertes sont justes. J'ai retenu la régression logistique pour ses probabilités fiables et ses coefficients explicables.",
         impact="Un outil utilisable tel quel sur un billet ou un fichier, avec une procédure de ré-entraînement quand les contrefaçons évoluent.",
         limites="Deux faux ont les dimensions de vrais billets : il faudrait d'autres mesures (couleur, texture) pour les attraper."),
    dict(id="p10", repo="oc-p10-dashboard-eau-potable", img="p10.jpg",
         alt="Page nationale du tableau de bord Power BI pour l'Éthiopie",
         title="Choisir où une ONG doit investir dans l'accès à l'eau",
         meta="Projet 10, septembre 2026. Power BI, Power Query, DAX.",
         contexte="Une ONG obtiendra un financement à investir dans un seul domaine (création de services, modernisation ou conseil), dans un pays à choisir.",
         besoin="Descendre du monde au continent puis au pays, en excluant les pays trop instables.",
         demarche="J'ai écrit un blueprint qui relie chaque besoin à une mesure, puis fait valider un mockup. J'ai corrigé six anomalies de données dans Power Query, construit un modèle en étoile et pondéré les moyennes par la population.",
         resultats="778 millions de personnes sans accès basique en 2017, dont la moitié en Afrique. Pour l'Éthiopie, les trois indicateurs d'arbitrage désignent la création de services en zone rurale.",
         impact="Un outil de décision qui justifie un pays et un domaine, plutôt qu'une simple description.",
         limites="La mortalité n'est disponible que pour 2016 et les données s'arrêtent en 2017."),
    dict(id="p11", repo="oc-p11-etude-marche-clustering", img="p11.jpg",
         alt="Carte du monde colorée selon six familles de pays",
         title="Trouver les premiers marchés export d'une PME de volaille bio",
         meta="Projet 11, septembre 2026. ACP, classification hiérarchique, k-means, API Banque mondiale.",
         contexte="Une PME 100 % française veut exporter ses poulets bio, sans pays présélectionné.",
         besoin="Proposer au comité de direction des groupes de pays à étudier en priorité.",
         demarche="J'ai décrit 166 pays avec 13 indicateurs, résumés en quatre axes par une ACP. Une classification hiérarchique fixe six familles, que k-means affine. J'ai vérifié la stabilité des groupes, puis classé les pays sous plusieurs pondérations.",
         resultats="Une famille cible, l'Europe développée. Quatre pays pour démarrer : Allemagne, Pays-Bas, Royaume-Uni et Danemark. L'Allemagne reste en tête quelle que soit la pondération.",
         impact="Une feuille de route en deux phases, du frais en Europe au congelé pour le grand export, et une décision attendue : lancer l'étude de marché sur ces quatre pays.",
         limites="Données de 2017, sans indicateur de demande bio ni de barrières douanières."),
    dict(id="p8", repo="oc-p8-pipeline-dbt-snowflake", img="p8.jpg",
         alt="Graphique de la part de femmes chez les inscrits comparée à la population",
         title="Mesurer qui n'accède pas aux formations data",
         meta="Projet 8, juillet 2026. dbt, Snowflake, SQL.",
         contexte="Une direction pédagogique veut objectiver le profil des inscrits à ses parcours data entre 2022 et 2025.",
         besoin="Savoir qui s'inscrit, et surtout qui manque à l'appel par rapport à la population française.",
         demarche="J'ai construit un pipeline dbt en couches (staging, intermediate, marts), avec 29 tests à chaque exécution. J'ai créé un indice de représentation lisible par un public non technique, à périmètre comparable avec l'INSEE.",
         resultats="Les femmes sont sous-représentées (indice 0,65) sans amélioration en quatre ans. L'Île-de-France pèse deux fois son poids démographique. Les 20-24 ans passent de 1,3 % à 8,6 % des inscrits.",
         impact="Des constats chiffrés pour orienter les actions d'accessibilité et d'égalité des chances.",
         limites="Le chargement des données INSEE reste manuel et les effectifs baissent de 44 % sur la période."),
]

OTHERS = [
    ("p9", "Septembre 2026", "Streaming musical : ce qui fait un hit, et la Pop à 6 mois",
     "Le genre explique 27 % de la popularité, le son rien. La prévision Prophet est jugée face à un modèle naïf, qui gagne sur l'erreur ponctuelle : je l'écris.", "Python, tests non paramétriques, Prophet"),
    ("p7", "Juillet 2026", "Suivi de portefeuille projets pour trois niveaux de direction",
     "Des alertes à 15 % d'écart, et une cause structurelle trouvée : la phase de test des projets IT dépasse son budget de 472 % en moyenne.", "Power BI, Power Query, DAX"),
    ("p6", "Mai 2026", "BottleNeck : stock et ventes d'un caviste en ligne",
     "Version initiale, conservée pour montrer la progression : ses huit erreurs sont corrigées dans le projet 13.", "Python, pandas"),
    ("p5", "Mars 2026", "DataImmo : base des ventes immobilières et 12 analyses",
     "Une base normalisée et des requêtes avec CTE et fonctions de fenêtre. Paris est à 12 091 €/m², et les ventes progressent de 3,7 % entre les deux premiers trimestres 2020.", "SQL, SQLite, modélisation"),
    ("p4", "Janvier 2026", "Sous-nutrition dans le monde",
     "La nourriture disponible suffirait pour 132 % de la population mondiale, mais 7,1 % des habitants sont sous-alimentés. C'est un problème de répartition.", "Python, pandas"),
    ("p3", "Novembre 2025", "Base de contrats d'assurance habitation",
     "Dictionnaire de données, schéma relationnel et 12 requêtes métier sur environ 31 000 contrats.", "SQL, SQLite"),
    ("p2", "Octobre 2025", "Rapport marketing mensuel d'un e-commerce",
     "Les ventes sont multipliées par 10, mais la conversion passe de 11 % à 5 %. Trois axes d'action sont proposés.", "Excel, storytelling"),
    ("perso", "Mai 2025", "Coûts d'assurance santé aux États-Unis",
     "Projet personnel : un fumeur paie en moyenne 3,8 fois plus. Mes premiers pas en Python.", "Python, pandas, plotly"),
]

SKILLS = [
    ("Cadrer un besoin métier", ["p7", "p10", "p11", "p13"]),
    ("Nettoyer et contrôler la qualité des données", ["p4", "p6", "p8", "p9", "p10", "p11", "p13"]),
    ("SQL et modélisation relationnelle", ["p3", "p5", "p8"]),
    ("Python et pandas", ["perso", "p4", "p6", "p9", "p11", "p12", "p13"]),
    ("Statistiques et tests", ["p9", "p12"]),
    ("Machine learning", ["p11", "p12", "p13"]),
    ("Power BI et DAX", ["p7", "p10"]),
    ("Data engineering (dbt, Snowflake)", ["p8"]),
    ("Restituer et recommander", ["p2", "p4", "p7", "p9", "p10", "p11", "p12", "p13"]),
    ("Utiliser l'IA de façon critique", ["p13"]),
]
COLS = ["perso", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11", "p12", "p13"]
COL_LABEL = {"perso": "Perso", **{c: c[1:] for c in COLS if c != "perso"}}
REPO = {t[0]: t[4] for t in TIMELINE}

e = html.escape


def timeline_svg():
    W, H, L, R, T, B = 940, 330, 170, 20, 24, 44
    d0, d1 = date(2025, 4, 1), date(2026, 11, 15)
    span = (d1 - d0).days
    x = lambda d: L + (d - d0).days / span * (W - L - R)
    y = lambda i: T + i * ((H - T - B) / (len(DOMAINS) - 1))
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="tl-title tl-desc">',
           '<title id="tl-title">Mes projets dans le temps, par domaine</title>',
           '<desc id="tl-desc">Treize projets entre mai 2025 et octobre 2026, qui passent du tableur et du SQL '
           'à la business intelligence, au machine learning puis à l\'IA générative.</desc>']
    for i, dom in enumerate(DOMAINS):
        out.append(f'<line class="grid" x1="{L}" x2="{W - R}" y1="{y(i):.1f}" y2="{y(i):.1f}"/>')
        out.append(f'<text class="dom" x="{L - 14}" y="{y(i) + 4:.1f}" text-anchor="end">{e(dom)}</text>')
    for yy, mm, lab in [(2025, 6, "juin 2025"), (2025, 10, "oct. 2025"), (2026, 2, "fév. 2026"), (2026, 6, "juin 2026"), (2026, 10, "oct. 2026")]:
        xx = x(date(yy, mm, 1))
        out.append(f'<line class="tick" x1="{xx:.1f}" x2="{xx:.1f}" y1="{T - 8}" y2="{H - B + 8}"/>')
        out.append(f'<text class="month" x="{xx:.1f}" y="{H - 14}" text-anchor="middle">{lab}</text>')
    pts = sorted(TIMELINE, key=lambda t: t[1])
    path = " ".join(f"{'M' if k == 0 else 'L'}{x(t[1]):.1f},{y(t[2]):.1f}" for k, t in enumerate(pts))
    out.append(f'<path class="trail" d="{path}"/>')
    for pid, d, dom, label, repo in pts:
        cls = "pt feat" if pid in {f["id"] for f in FEATURED} else "pt"
        href = f"#{pid}" if pid in {f["id"] for f in FEATURED} else f"{GH}{repo}"
        name = "projet personnel" if pid == "perso" else f"projet {pid[1:]}"
        out.append(f'<a href="{href}" class="{cls}"><title>{e(label)} ({name})</title>'
                   f'<circle cx="{x(d):.1f}" cy="{y(dom):.1f}" r="{8 if "feat" in cls else 6}"/></a>')
    out.append("</svg>")
    return "\n".join(out)


def featured_html():
    rows = []
    for f in FEATURED:
        rows.append(f'''
<article class="case" id="{f["id"]}">
  <div class="case-head">
    <h3>{e(f["title"])}</h3>
    <p class="meta">{e(f["meta"])}</p>
  </div>
  <figure><img src="assets/{f["img"]}" alt="{e(f["alt"])}" loading="lazy" width="1100"></figure>
  <dl class="story">
    <dt>Contexte</dt><dd>{e(f["contexte"])}</dd>
    <dt>Besoin métier</dt><dd>{e(f["besoin"])}</dd>
    <dt>Démarche</dt><dd>{e(f["demarche"])}</dd>
    <dt>Résultats</dt><dd>{e(f["resultats"])}</dd>
    <dt>Impact</dt><dd>{e(f["impact"])}</dd>
    <dt>Limites</dt><dd>{e(f["limites"])}</dd>
  </dl>
  <p class="repo-link"><a href="{GH}{f["repo"]}">Voir le code et les livrables sur GitHub</a></p>
</article>''')
    return "\n".join(rows)


def others_html():
    rows = []
    for pid, when, title, txt, stack in OTHERS:
        rows.append(f'''<li id="{pid}">
  <p class="when">{e(when)}</p>
  <div><h3><a href="{GH}{REPO[pid]}">{e(title)}</a></h3><p>{e(txt)}</p><p class="stack">{e(stack)}</p></div>
</li>''')
    return "\n".join(rows)


def matrix_html():
    head = "".join(f'<th scope="col"><a href="{GH}{REPO[c]}">{COL_LABEL[c]}</a></th>' for c in COLS)
    body = []
    for skill, projs in SKILLS:
        cells = "".join(f'<td>{"<span class=\"dot\" aria-label=\"oui\"></span>" if c in projs else ""}</td>' for c in COLS)
        body.append(f'<tr><th scope="row">{e(skill)}</th>{cells}</tr>')
    return f'<table class="matrix"><caption>Projets qui mobilisent chaque compétence (numéro du projet OpenClassrooms)</caption><thead><tr><th scope="col">Compétence</th>{head}</tr></thead><tbody>{"".join(body)}</tbody></table>'


CSS = r"""
:root{--paper:#F5F7F6;--ink:#17233B;--muted:#56627A;--line:#D5DBE3;--accent:#1F6F5C;--dot:#E0A43A;--panel:#FFFFFF;
--serif:"Newsreader",Georgia,serif;--sans:"Public Sans",system-ui,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--paper:#121A26;--ink:#E7ECF3;--muted:#A3AFC2;--line:#2C3A4F;--accent:#5CC2A6;--dot:#F0B95A;--panel:#18222F}}
*{box-sizing:border-box}
html{scroll-behavior:smooth}@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 var(--sans);-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-underline-offset:3px}
a:focus-visible{outline:3px solid var(--dot);outline-offset:3px;border-radius:2px}
.wrap{max-width:1040px;margin:0 auto;padding:0 24px}
nav{position:sticky;top:0;z-index:5;background:var(--paper);border-bottom:1px solid var(--line)}
nav .wrap{display:flex;gap:28px;align-items:center;height:56px;overflow-x:auto;white-space:nowrap}
nav strong{font-family:var(--serif);font-size:20px;font-weight:600;margin-right:auto}
nav a{color:var(--ink);text-decoration:none;font-size:15px}nav a:hover{color:var(--accent)}
h1,h2,h3{font-family:var(--serif);font-weight:500;letter-spacing:-.01em;line-height:1.15}
header.hero{padding-top:64px;padding-bottom:24px}
.hero h1{font-size:clamp(40px,6vw,68px);margin:0 0 18px;max-width:14ch}
.hero .lede{font-size:21px;line-height:1.5;color:var(--muted);max-width:60ch;margin:0 0 10px}
.hero .lede b{color:var(--ink);font-weight:600}
.hero .links{display:flex;gap:22px;flex-wrap:wrap;margin:22px 0 0;font-weight:600}
.chart{margin:40px 0 8px;overflow-x:auto}
.chart svg{min-width:720px;width:100%;height:auto;display:block}
.chart .grid{stroke:var(--line);stroke-width:1}
.chart .tick{stroke:var(--line);stroke-dasharray:2 4}
.chart .dom{font:14px var(--sans);fill:var(--muted)}
.chart .month{font:13px var(--sans);fill:var(--muted)}
.chart .trail{fill:none;stroke:var(--ink);stroke-opacity:.35;stroke-width:1.5}
.chart .pt circle{fill:var(--panel);stroke:var(--ink);stroke-width:2}
.chart .pt.feat circle{fill:var(--dot);stroke:var(--ink)}
.chart a:hover circle,.chart a:focus circle{fill:var(--accent);stroke:var(--accent)}
.chart-note{font-size:14px;color:var(--muted);margin:0 0 24px}
main>section{padding-top:56px;padding-bottom:56px;border-top:1px solid var(--line)}
section>h2{font-size:clamp(30px,4vw,40px);margin:0 0 10px}
section>.intro{color:var(--muted);max-width:62ch;margin:0 0 36px;font-size:18px}
.case{padding:0 0 56px;margin-bottom:56px;border-bottom:1px solid var(--line);display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);grid-template-areas:'head head' 'story fig' 'link fig';gap:12px 48px;scroll-margin-top:72px}
.case-head{grid-area:head}.story{grid-area:story}.case figure{grid-area:fig;position:sticky;top:76px}.repo-link{grid-area:link}
.case:last-child{border-bottom:0;margin-bottom:0;padding-bottom:0}
.case h3{font-size:clamp(25px,3vw,32px);margin:0 0 6px;max-width:30ch}
.case .meta{color:var(--muted);margin:0 0 14px;font-size:15px}
.case figure{margin:0;align-self:start}
.case img{width:100%;height:auto;border:1px solid var(--line);border-radius:6px;background:#fff}
.story{margin:0;display:grid;grid-template-columns:8.5em 1fr;gap:10px 18px}
.story dt{font-weight:600;font-size:15px;padding-top:2px}
.story dd{margin:0;max-width:60ch}
.repo-link{margin:8px 0 0;font-weight:600}
.others{list-style:none;margin:0;padding:0}
.others li{display:grid;grid-template-columns:10em 1fr;gap:20px;padding:20px 0;border-top:1px solid var(--line);scroll-margin-top:72px}
.others li:first-child{border-top:0}
.others .when{margin:0;color:var(--muted);font-size:15px;padding-top:4px}
.others h3{font-size:22px;margin:0 0 6px}.others h3 a{color:var(--ink)}.others h3 a:hover{color:var(--accent)}
.others p{margin:0;max-width:66ch}.others .stack{color:var(--muted);font-size:15px;margin-top:6px}
.matrix-wrap{overflow-x:auto}
.matrix{border-collapse:collapse;width:100%;min-width:760px;font-size:15px}
.matrix caption{text-align:left;color:var(--muted);padding-bottom:12px;caption-side:top}
.matrix th,.matrix td{padding:9px 6px;border-bottom:1px solid var(--line);text-align:center}
.matrix thead th{font-weight:600}.matrix thead a{color:var(--ink);text-decoration:none}.matrix thead a:hover{color:var(--accent)}
.matrix tbody th{text-align:left;font-weight:500;padding-right:16px}
.matrix thead th:first-child{text-align:left}
.dot{display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--accent)}
.veille{display:grid;grid-template-columns:1fr 1fr;gap:40px 56px}
.veille h3{font-size:24px;margin:0 0 12px}
.steps{margin:0;padding-left:1.4em}.steps li{margin:0 0 12px;padding-left:4px}.steps li::marker{font-family:var(--serif);font-weight:600;color:var(--accent)}
.steps b{display:block}
.subs{list-style:none;margin:0;padding:0}
.subs li{padding:8px 0;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;gap:16px}
.subs li span:last-child{color:var(--muted);text-align:right}
.wins{grid-column:1/-1;background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:28px 32px}
.wins ul{margin:0;padding-left:1.2em}.wins li{margin:0 0 10px;max-width:80ch}
.next{grid-column:1/-1;color:var(--muted);max-width:75ch;margin:0}
.about{display:grid;grid-template-columns:1.3fr 1fr;gap:40px}
.about p{max-width:62ch;margin:0 0 14px}
.facts{margin:0;display:grid;grid-template-columns:auto 1fr;gap:8px 18px;align-content:start}
.facts dt{color:var(--muted)}.facts dd{margin:0}
footer{border-top:1px solid var(--line);padding:28px 0 48px;color:var(--muted);font-size:15px}
@media (max-width:760px){
 body{font-size:16px}.wrap{padding:0 16px}
 header.hero{padding-top:40px;padding-bottom:12px}.hero .lede{font-size:19px}
 nav .wrap{gap:18px}
 .chart{direction:rtl}.chart svg{direction:ltr;min-width:600px}
 .case{grid-template-columns:1fr;grid-template-areas:'head' 'fig' 'story' 'link'}.case figure{position:static}
 .story{grid-template-columns:1fr;gap:2px}.story dd{margin-bottom:10px}
 .others li{grid-template-columns:1fr;gap:4px}
 .veille,.about{grid-template-columns:1fr}
 .wins{padding:22px 20px}
}
@media print{
 nav{display:none}.chart{overflow:visible;direction:ltr}.chart svg{min-width:0}.case figure{position:static}
 .case{break-inside:auto}.case-head,.others li,.matrix tr,.wins,.steps li{break-inside:avoid}h2,h3{break-after:avoid}
 main>section{padding-top:28px;padding-bottom:28px}
 a{color:var(--ink)}body{background:#fff}
}
"""

PAGE = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Leo Cabart, data analyst</title>
<meta name="description" content="Portfolio de Leo Cabart, data analyst Client Insights à Paris : projets d'analyse, de business intelligence, de machine learning et d'IA générative.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Public+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<nav aria-label="Sections"><div class="wrap"><strong>Leo Cabart</strong>
<a href="#projets">Projets</a><a href="#autres">Autres projets</a><a href="#competences">Compétences</a><a href="#veille">Veille</a><a href="#profil">Profil</a></div></nav>
<main>
<header class="hero wrap">
<h1>Des chiffres justes, puis une décision.</h1>
<p class="lede">Je suis <b>data analyst Client Insights</b> chez Louis Vuitton, à Paris. Je transforme des données clients et ventes en indicateurs fiables et en recommandations que les équipes métier peuvent appliquer.</p>
<p class="lede">Je travaille au quotidien avec BigQuery, Power BI et Python. Ce portfolio rassemble treize projets, du tableur à l'IA générative.</p>
<p class="links"><a href="#projets">Voir les projets</a><a href="https://github.com/lcabart21">GitHub</a></p>
<div class="chart" aria-describedby="chart-note">{timeline_svg()}</div>
<p class="chart-note" id="chart-note">Chaque point est un projet. Les points jaunes sont détaillés plus bas ; les autres renvoient au code sur GitHub.</p>
</header>

<section id="projets" class="wrap" aria-labelledby="h-projets">
<h2 id="h-projets">Projets détaillés</h2>
<p class="intro">Cinq projets choisis pour la variété des problèmes et des méthodes. Chacun suit le même fil : contexte, besoin, démarche, résultats, impact et limites.</p>
{featured_html()}
</section>

<section id="autres" class="wrap" aria-labelledby="h-autres">
<h2 id="h-autres">Autres projets</h2>
<p class="intro">Du plus récent au plus ancien. Chaque dépôt contient un README sur le même modèle, les livrables et, quand c'est possible, de quoi rejouer l'analyse.</p>
<ul class="others">
{others_html()}
</ul>
</section>

<section id="competences" class="wrap" aria-labelledby="h-comp">
<h2 id="h-comp">Compétences et preuves</h2>
<p class="intro">Chaque compétence renvoie aux projets qui la démontrent. Les colonnes portent le numéro du projet OpenClassrooms et mènent au dépôt.</p>
<div class="matrix-wrap">{matrix_html()}</div>
</section>

<section id="veille" class="wrap" aria-labelledby="h-veille">
<h2 id="h-veille">Ma veille</h2>
<p class="intro">Les outils de la data changent tous les mois. Je suis des communautés de praticiens qui partagent ce qui marche et ce qui casse, et je ne teste que ce qui répond à un problème que j'ai réellement.</p>
<div class="veille">
<div>
<h3>Le système</h3>
<ol class="steps">
<li><b>Lire</b>Deux à trois fois par semaine, je parcours une sélection de communautés Reddit sur mes outils et mon métier.</li>
<li><b>Garder</b>Ce qui m'intéresse part dans les favoris de l'application, pour y revenir au calme.</li>
<li><b>Trier</b>Je teste en priorité ce qui touche à un problème rencontré au travail. Le reste attend.</li>
<li><b>Tester</b>J'essaie sur un cas réel, à petite échelle, avant d'adopter.</li>
<li><b>Adopter</b>Si le test est concluant, l'outil ou la pratique entre dans mon quotidien.</li>
</ol>
</div>
<div>
<h3>Les sources</h3>
<ul class="subs">
<li><span>r/BigQuery</span><span>Mon entrepôt de données au quotidien</span></li>
<li><span>r/PowerBI</span><span>DAX, modélisation, nouveautés</span></li>
<li><span>r/analytics, r/dataanalysis</span><span>Pratiques du métier</span></li>
<li><span>r/dataengineering</span><span>Pipelines, dbt, qualité des données</span></li>
<li><span>r/datascience</span><span>Méthodes statistiques et ML</span></li>
<li><span>r/dataisbeautiful</span><span>Idées de visualisation</span></li>
<li><span>r/ClaudeAI, r/ClaudeHomies</span><span>Usages de l'IA générative</span></li>
</ul>
</div>
<div class="wins">
<h3>Ce que ma veille a déjà changé</h3>
<ul>
<li>J'ai découvert l'extension BigQuery pour VS Code. J'interroge désormais l'entrepôt en local, sans passer par la console web, et je peux travailler mes requêtes avec un assistant IA dans le même outil.</li>
<li>Des astuces DAX repérées dans les discussions ont été testées directement dans mes rapports Power BI avant d'être adoptées.</li>
<li>Dans le projet 13, la veille a orienté les choix : pandera plutôt que Great Expectations, une détection d'anomalies robuste par catégorie plutôt qu'un modèle complexe, des prompts structurés plutôt que naïfs. Chaque option a été testée sur les données avant d'être retenue.</li>
</ul>
</div>
<p class="next"><b>Prochaine étape.</b> Reddit donne des retours d'expérience, mais pas toujours des sources vérifiables. J'ajoute donc les notes de version officielles de BigQuery et le blog des mises à jour mensuelles de Power BI, pour confirmer ce que je lis avant de l'appliquer.</p>
</div>
</section>

<section id="profil" class="wrap" aria-labelledby="h-profil">
<h2 id="h-profil">Profil</h2>
<div class="about">
<div>
<p>Au sein de l'équipe Client Insights EMEA de Louis Vuitton, je travaille sur l'analyse de la clientèle : fidélisation, ciblage de campagnes clienteling, tableaux de bord de suivi pour les boutiques.</p>
<p>J'aime les problèmes où la donnée est imparfaite et où il faut d'abord vérifier avant de conclure. Je documente ce que je garde, ce que j'écarte et pourquoi, pour que les équipes puissent reprendre l'outil sans moi.</p>
</div>
<dl class="facts">
<dt>Poste</dt><dd>Data analyst, Client Insights EMEA, Louis Vuitton</dd>
<dt>Formation</dt><dd>Data Analyst, OpenClassrooms (titre RNCP niveau 6)</dd>
<dt>Outils</dt><dd>BigQuery (SQL), Power BI (DAX), Python, Dataiku, dbt</dd>
<dt>Ville</dt><dd>Paris</dd>
<dt>Code</dt><dd><a href="https://github.com/lcabart21">github.com/lcabart21</a></dd>
</dl>
</div>
</section>
</main>
<footer><div class="wrap">Leo Cabart, 2026. Les projets OpenClassrooms reposent sur des données publiques ou fictives fournies pour l'exercice.</div></footer>
</body>
</html>
"""

if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    open(out, "w", encoding="utf-8").write(PAGE)
    print("written", out, len(PAGE))
