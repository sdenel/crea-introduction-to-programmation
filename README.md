# Using Tableau Public
## Warm up (10 minutes)
* Download and install Tableau public
## Presentation of Tableau by Alexandre
## First step with Tableau (30 minutes)
* Working in pairs
    * Get traffic accidents data for the Geneva Canton (in csv format). You can grasp a first idea of the data online: https://www.etat.ge.ch/geoportail/pro/?mapresources=CATALOGUE&visiblelayerindexes={%22CATALOGUE%22:[8139]}
    * Take a look at the data in a text editor
    * Import the data in Tableau
    * (30 minutes) Explore the dataset. For example:
        * Can you display the data on a map?
        * Can you display the number of accidents for each hour?
    * (30 minutes) prepare a quick presentation (3 minutes by group) about these data using Tableau Public
    * You are now in charge of the firefighter unit of Geneva, and you would like to learn from data to handle injuries more quickly while being more cost efficient.
      * Define a first strategy based on this data
      * Do you have all the data you need? What can the data provider do to help you become more data driven?


## Tips
* Location coordonates are provided in the CH1903+ / LV95 system. You can transform them to WGS 84 by taking two points for which you know coordinates in both systems and by taking the approximation that the transformation is linear. For example, given two points in Geneva:
 https://map.geo.admin.ch/?lang=fr&topic=ech&bgLayer=ch.swisstopo.pixelkarte-farbe&layers=ch.swisstopo.zeitreihen,ch.bfs.gebaeude_wohnungs_register,ch.bav.haltestellen-oev,ch.swisstopo.swisstlm3d-wanderwege&layers_visibility=false,false,false,false&layers_timestamp=18641231,,,&E=2501012.71&N=1118072.85&zoom=11.843333333333332
https://map.geo.admin.ch/?lang=fr&topic=ech&bgLayer=ch.swisstopo.pixelkarte-farbe&layers=ch.swisstopo.zeitreihen,ch.bfs.gebaeude_wohnungs_register,ch.bav.haltestellen-oev,ch.swisstopo.swisstlm3d-wanderwege&layers_visibility=false,false,false,false&layers_timestamp=18641231,,,&E=2497281.51&N=1121171.99&zoom=9.709999999999994
We can create columns:
  * lon = 6.09203 + ([E]-2496000)/(2501000-2496000)*(6.15485-6.09203)
  * lat = 46.16941 +([N]-1114000)/(1123000-1114000)*(46.25111-46.16941)
* You can create new fields. For example, you can compute the number of physical injuries in a new column, naming it "Nb Physical Injuries":
 [Nb Blesses Legers]+[Nb Blesses Graves]+[Nb Tues]

# Introduction to programmation
## Kick start
Brainstorming: Which langages do you know? Can you classify them on a dashboard with two axes:
* Easiness
* Ability to build real products
* By you and the instructor: one word on each language

## Hands on!
TP0 : Introduction to programmation. Basic principles: printing / conditions / loops...
TP1 : With the dataset from Titanic, can you find the number of lines, the number of columns? Can you extract some statistics?
TP2 : Titanic competition: can you predict who died?
TP3 : Demonstration by Alex: Random Forest example

# Introduction to Data Science

## To go further
### Demonstration by the teacher
* Answer the question: how many injuries will I have during the coming permanence?
    * How precise if this model?
* We could take data from other cantons to have stronger statistics
* We could even go a bit further and wonder if we should change the time for the duty shift to have a better ratio figherfighter / injuries

## Hands on with the Titanic Dataset

# Correction clues
## Tableau Public
* Create a field: HeureParsed = DATEPART('hour', [Heure])
* The data provider should give the hour in a more explicit, more precise format