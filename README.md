# Initiation Tableau Public
## Warm up (10 minutes)
* Télécharger tableau public
## Presentation of Tableau by Alexandre (time?)
## First step with Tableau (30 minutes)
* Working in pair
    * Get traffic accidents data for the Geneva Canton (in csv format). You can get a first idea of the data online: https://www.etat.ge.ch/geoportail/pro/?mapresources=CATALOGUE&visiblelayerindexes={%22CATALOGUE%22:[8139]}
    * Look at the data in a text editor
    * Import the data in Tableau
    * (30 minutes) Explore the data. For example:
        * Can you display the data on a map?
        * Can you display the number of accidents for each hour?
    * (30 minutes) prepare a quick presentation (3 minutes by group) about these data using Tableau Public
    * You are now in charge of the firefighter unit of Geneva, and you would like to learn from data to handle injuries more quickly while being more cost efficient.
      * Define a first strategy based on this data
      * Do you have all the data you need? What can the data provider do to help you become more data driven?


### Tips
* Location coordonates are provided in the CH1903+ / LV95 system. You can transform them to WGS 84 by taking two points for which you know coordinates in both systems and by taking the approximation that the transformation is linear. For example, given two points in Geneva:
https://map.geo.admin.ch/?lang=fr&topic=ech&bgLayer=ch.swisstopo.pixelkarte-farbe&layers=ch.swisstopo.zeitreihen,ch.bfs.gebaeude_wohnungs_register,ch.bav.haltestellen-oev,ch.swisstopo.swisstlm3d-wanderwege&layers_visibility=false,false,false,false&layers_timestamp=18641231,,,&E=2501012.71&N=1118072.85&zoom=11.843333333333332
https://map.geo.admin.ch/?lang=fr&topic=ech&bgLayer=ch.swisstopo.pixelkarte-farbe&layers=ch.swisstopo.zeitreihen,ch.bfs.gebaeude_wohnungs_register,ch.bav.haltestellen-oev,ch.swisstopo.swisstlm3d-wanderwege&layers_visibility=false,false,false,false&layers_timestamp=18641231,,,&E=2497281.51&N=1121171.99&zoom=9.709999999999994
We can create columns:
  * longitude = 6.15588 + ([N]-1121183)/(1118136.1-1121183) * (6.10761-6.15588)
  * latitude = 46.20738 + ([E]-2497325.5)/(2500999.9-2497325.5) * (46.23423-46.20738)
* You can create new fields. For example, you can compute the number of physical injuries in a new column, naming it "Nb Physical Injuries"
 [Nb Blesses Legers]+[Nb Blesses Graves]+[Nb Tues]

# Introduction to programmation

Brainstorming avec des post-its : Qu'est-ce que vous connaissez comme langages ? Classer sur un tableau à deux axes :
* Facilité de prise en main
* Capacité à créer des gros projets
* Un mot sur chaque

TP0 : introduction à la programmation
TP1 : Dataset de Titanic loadé. Combien de lignes ? De colones ? Un peu d'exploration / de viz
TP2 : Quelle chance de survie ? à la mano.
TP3 : Random Forest

* Loaded dataset
What can you say about the data?
Length? Number of features?

# Introduction to data Science

## To go further
### Demonstration by the teacher
* Answer the question: how many injuries will I have during the coming permanence?
    * How precise if this model?
* Do the example with Random Forest
* We could take data from other cantons to have stronger statistics
* We could even go a bit further and wonder if we should change the time for the duty shift to have a better ratio figherfighter / injuries

## Hands on with the Titanic Dataset



# Correction clues
## Tableau Public
* Create a field: HeureParsed = DATEPART('hour', [Heure])
* The data provider should give the hour in a more explicit, more precise format