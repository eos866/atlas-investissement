# Atlas de l'investissement – Sénégal

Prototype d'atlas cartographique interactif proposé par **CEGIT** (Centre d'Expertise en Géomatique et Ingénierie Territoriale) pour enrichir le portail [investinsenegal.sn](https://investinsenegal.sn) de l'APIX d'une dimension cartographique.

> **Prototype de démonstration.** Les positions des zones, projets et infrastructures sont indicatives et doivent être validées avec l'APIX et les gestionnaires concernés.

## Fonctionnalités

**Carte interactive**
- Zones économiques (ZES, Zone Franche Industrielle), plateformes régionales APIX et couverture par région
- Projets prioritaires APIX, avec un pictogramme par secteur et un lien vers leur fiche PDF officielle
- Infrastructures : autoroutes, TER, voies ferrées, routes principales et secondaires, aéroports, ports, énergie, grands projets APIX
- Carte thématique des 14 régions à partir des données ANSD : population, densité, croissance, urbanisation, main-d'œuvre, part des jeunes, taille des ménages, pauvreté
- Fiches détaillées au clic, recherche, filtre par secteur, légende repliable
- Fonds de carte au choix : fond simple, orthophotoplan (Esri World Imagery) ou plan OpenStreetMap
- Assistant « Où m'implanter ? » qui classe les sites selon le secteur et les besoins de l'investisseur

**Zones d'activité (données fictives de démonstration)**
- Zonage de chaque zone économique en polygones : commerciale, construction, services, industrie, mixte
- Terrains en polygones, découpés en îlots et desservis par la voirie, avec six statuts : disponible immédiatement, potentiellement disponible, disponible à terme, réservé, occupé, non disponible
- Fiche de chaque terrain : superficie, prix au m², raccordements aux réseaux, occupant
- Formulaire de manifestation d'intérêt pour un lot : demandeur, projet, besoins en réseaux, calendrier ; récapitulatif avec référence, message pré-rempli vers la plateforme APIX et demande en PDF (non transmise automatiquement dans le prototype)
- Viabilisation de la zone : électricité, eau, assainissement, fibre
- Vue 360° : maquette 3D posée sur l'orthophoto réelle, en vue aérienne ou en panorama 360° au sol et depuis un drone (Three.js, chargé à la demande)
- Emplacement des zones ajustable sur l'orthophoto (déplacement, orientation, taille), mémorisé dans le navigateur et exportable en coordonnées
- Superficies calées sur les données de l'APIX : Diamniadio 53 ha, Diass 718 ha (mitoyenne de l'AIBD), Sandiara 100 ha

**Portail « Découvrir les plateformes »**
- Page d'accueil avec les 7 plateformes régionales
- Une page par plateforme : chiffres clés, et quatre rubriques (Territoire, Population, Opportunités, Infrastructures) avec chacune sa carte
- Rapport territorial téléchargeable en PDF

Interface bilingue français / anglais, thèmes clair et sombre, utilisable sur téléphone.

L'interface reprend la palette et la typographie du site investinsenegal.sn (bleu #004A96, orange #EF7900, police Rubik). Le logo de l'APIX n'est pas utilisé : il ne pourra être ajouté qu'avec l'accord de l'agence.

## Lancer l'application

L'application tient dans un seul fichier, `index.html`, sans serveur ni installation. Ouvrez-le dans un navigateur, ou publiez le dépôt avec GitHub Pages :

1. Dans le dépôt GitHub : **Settings › Pages**
2. **Source** : *Deploy from a branch*, branche `main`, dossier `/ (root)`
3. L'application est en ligne quelques minutes plus tard à l'adresse `https://<compte>.github.io/<dépôt>/`

Une connexion internet est nécessaire pour charger Leaflet, jsPDF et les polices depuis leurs CDN.

## Structure du dépôt

```
index.html           Application autonome générée (à publier)
src/atlas.html       Code source (HTML, CSS, JavaScript)
data/regions.json    Limites des 14 régions et de la Gambie (simplifiées)
data/infra.json      Routes principales, secondaires et voies ferrées
build.py             Assemble src/ et data/ en index.html
dist/artifact.html   Variante pour publication en artefact Claude
```

Après toute modification de `src/` ou `data/`, régénérez l'application :

```bash
python3 build.py
```

Les données socio-démographiques, les zones, plateformes, projets et infrastructures ponctuelles sont définies au début du script, dans `src/atlas.html` (objets `SOCIO`, `ZONES`, `PLATS`, `PROJS`, `INFRA_PTS`, `LINES`).

## Sources des données

| Données | Source |
|---|---|
| Population 2013 et 2023 par région | ANSD, RGPH-4 et RGPH-5, via [citypopulation.de](https://citypopulation.de/en/senegal/admin/) |
| Population 2024, urbanisation, structure par âge | ANSD, [Annuaire Population du Sénégal 2024](https://www.vie-publique.sn/docs/0ba03944-322a-430c-a6ce-382b1c2e474b/annuaire-population-du-senegal-2024-ansd.pdf) |
| Ménages | ANSD, [RGPH-5, rapport préliminaire](https://ipar.sn/wp-content/uploads/2024/08/RAPPORT_PRELIMINAIRE_RGPH5PDF_231031_112453.pdf) |
| Taux de pauvreté | ANSD, [EHCVM II 2021-2022](https://www.vie-publique.sn/docs/88cb53b9-e3bd-40f1-9bc8-217c19063e7d/enquete-harmonisee-conditions-vie-menages-ehcvm-ii-senegal-2021-2022-ansd.pdf) |
| Plateformes régionales, projets prioritaires | [APIX – investinsenegal.sn](https://investinsenegal.sn) |
| Limites régionales, routes, voies ferrées | [Natural Earth](https://www.naturalearthdata.com) (domaine public) |
| Orthophotoplan | [Esri World Imagery](https://www.arcgis.com/home/item.html?id=10df2279f9684e4a9f6a7f08febac2a9) – Esri, Maxar, Earthstar Geographics |
| Plan | [OpenStreetMap](https://www.openstreetmap.org/copyright) – © contributeurs OpenStreetMap |

## Bibliothèques utilisées

- [Leaflet](https://leafletjs.com) 1.9.4 – licence BSD-2-Clause
- [Three.js](https://threejs.org) 0.128.0 et OrbitControls – licence MIT (vue 360°)
- [jsPDF](https://github.com/parallax/jsPDF) 2.5.1 et [jsPDF-AutoTable](https://github.com/simonbengtsson/jsPDF-AutoTable) 3.8.2 – licence MIT
- Police Rubik – Google Fonts, licence SIL Open Font License

## Évolutions prévues

- Connexion à l'API du portail Open Data for Africa de l'ANSD pour des données à jour
- Périmètres officiels des zones économiques et catalogue foncier (lots disponibles, viabilisation)
- Données d'infrastructures des gestionnaires (AGEROUTE, Senelec, ANACIM, Port autonome de Dakar) ou OpenStreetMap
- Hébergement de la base sur PostgreSQL/PostGIS avec QGIS Server

---

© CEGIT – [cegitgroup.com](https://cegitgroup.com)
