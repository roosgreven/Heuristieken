# Heuristieken: Amstelhaege
Jitse Schol, Nathalie van Sterkenburg en Roos Greven

De casus: Er wordt een nieuwe wijk gebouwd: Amstelhaege, van 160 bij 180 meter groot. Hier wil de gemeente huizen plaatsen die samen zoveel mogelijk waarde hebben. Er zijn drie soorten huizen: eengezinswoningen, bungalows en maisons. Elk huis heeft een standaardgrootte, een minimale vrijstand voor om het huis heen en een standaard waarde. Huizen kunnen echter meer waard worden: door de vrijstand rondom een huis te vergroten, wordt een huis meer waard. De gemeente wil nu weten met welke indeling de wijk het meest waard wordt. Ze twijfelen nog tussen het plaatsen van 20, 40 of 60 huizen. In deze casus zoeken we dus voor elke situatie uit hoeveel de wijk maximaal waard kan zijn. Een extra moeilijkheid is dat de gemeente water in deze wijk wil hebben. Minstens 20% van de oppervlakte moet uit water bestaan. Deze watertjes mogen geen sloten worden: de verhouding moet minstens 1 op 4 zijn. Daarnaast mogen er slechts maximaal 4 wateren zijn. 

Onze aanpak: De datastructuur is erg belangrijk bij deze casus. Ga je de huizen indelen in een grid, of juist met coördinaten? Wij kiezen voor het laatste. Het is niet wenselijk om de huizen op de centimeter precies in te delen - hier wordt het probleem eindeloos groot van -, maar door het werken met coördinaten is het wel mogelijk om preciezer dan met halve meters te werken, wat bij het gebruik van een grid toch lastig zou worden. Daarnaast is het zo makkelijker de afstand tussen de hoeken van huizen uit te rekenen. 
De huizen staan in een class gedefinieerd. Deze class 'erft', inherit de eigenschappen van een algemenere class. Hierin staan alle move-functies beschreven, welke natuurlijk hetzelfde werken voor alle huizen. 

# Gebruik
Aanroepen van de functie gaat via het format:
python Heuristieken\code\main.py TYPEOFALGORITHM NUMBEROFHOUSES 

Als NUMBEROFHOUSES worden de getallen 20, 40 en 60 geaccepteerd. Dit is het aantal huizen dat in de wijk zal worden geplaatst.
Voor TYPEOFALGORITHM bestaan de volgende mogelijkheden:
- random            
Voert het random algoritme eenmalig uit, slaat de uitkomst op en print deze.
- greedy            
Voert het greedy algoritme eenmalig uit, slaat de uitkomst op en print deze.
- hillclimber       
Voert het hill climber algoritme eenmalig uit, slaat de uitkomst op en print deze. (Werkt nog niet.)
- lotsOfRandom      
Voert het random algoritme honder keer uit, print de gemiddelde waarde, onthoudt de beste en de slechtste en print beide.
