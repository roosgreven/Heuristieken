# Heuristieken: Amstelhaege
Jitse Schol, Nathalie van Sterkenburg en Roos Greven

## Casus
Er wordt een nieuwe wijk gebouwd: Amstelhaege, van 160 bij 180 meter groot. Hier wil de gemeente huizen plaatsen die samen zoveel mogelijk waarde hebben. Er zijn drie soorten huizen: eengezinswoningen, bungalows en maisons. Elk huis heeft een standaardgrootte, een minimale vrijstand voor om het huis heen en een standaardwaarde. Huizen kunnen echter meer waard worden: door de vrijstand rondom een huis te vergroten, wordt een huis meer waard. De gemeente wil nu weten met welke indeling de wijk het meest waard wordt. Ze twijfelen nog tussen het plaatsen van 20, 40 of 60 huizen. In deze casus zoeken we dus voor elke situatie uit hoeveel de wijk maximaal waard kan zijn. Een extra moeilijkheid is dat de gemeente water in deze wijk wil hebben. Minstens 20% van de oppervlakte moet uit water bestaan. Deze watertjes mogen geen sloten worden: de verhouding moet minstens 1 op 4 zijn. Daarnaast mogen er slechts maximaal 4 wateren zijn. 

## Aanpak
De datastructuur is erg belangrijk bij deze casus. Ga je de huizen indelen in een grid, of juist met coördinaten? Wij kiezen voor het laatste. Het is niet wenselijk om de huizen op de centimeter precies in te delen - hier wordt het probleem eindeloos groot van -, maar door het werken met coördinaten is het wel mogelijk om preciezer dan met halve meters te werken, wat bij het gebruik van een grid toch lastig zou worden. Daarnaast is het zo makkelijker de afstand tussen de hoeken van huizen uit te rekenen. 
De huizen staan in een class gedefinieerd. Deze class 'erft', inherit de eigenschappen van een algemenere class. Hierin staan alle move-functies beschreven, welke natuurlijk hetzelfde werken voor alle huizen. 

## Algoritmen
Om deze casus op te lossen hebben we een aantal algoritmen geïmplementeerd die oplossingen voor het probleem kunnen vinden. Hieronder een lijst met een korte beschrijving van ieder algoritme.   
- Random    
Genereert een oplossing door random huizen op een plattegrond te plaatsen, totdat aan alle eisen en restricties wordt voldaan.    
- Greedy    
Gaat voor ieder huis alle mogelijke coördinaten af en plaatst het huis op de plek waar het op dat moment het meeste oplevert.   
- Hill Climber / Simulated Annealing    
Begint met een random oplossing en brengt willekeurige veranderingen aan. Veranderingen bestaan uit het verplaatsen van een huis, het roteren van een huis en het omwisselen van twee huizen. Als de verandering een verbetering is, wordt deze geaccepteerd. In het geval van een Hill Climber, wordt een verslechtering altijd teruggedraaid, maar in het geval van Simulated Annealing is er een kans dat de verslechtering wordt geaccepteerd.    
- Particle Swarm Optimization    
Begint met een lijst van oplossingen en probeert de waarde voor iedere oplossing te verhogen. Ieder huis in iedere oplossingen wordt langzaam verplaatst, dit gebeurt met een snelheid die afhangt van het best behaalde resultaat door de hele lijst, en het best behaalde resultaat door de oplossing waar het huis zelf toe behoord. Doordat de snelheid wordt bepaald door de best gevonden waarden, valt het te verwachten dat de verplaatsing naar een betere oplossing leidt.

## Visualisaties
https://roosgreven.github.io/Heuristieken/code/experiments/html/index.html

# Vereisten
De code is geschreven in Python 3.6. Alle packages die nodig zijn om de code te runnen, staat in het bestand requirements.txt

# Structuur
Alle code staat in de folder code. In deze folder bevindt zich ook een folder met resultaten en een folder met de experimenten die zijn gedaan met de code. In de folder files staan een aantal bestanden waarin aantekeningen en presentaties worden bijgehouden. In de folder doc staan plaatjes van plattegronden en grafieken.

# Gebruik
In de folder code staat een README met daarin uitgebreidere informatie over het uitvoeren van de code.

# Auteurs
- Roos Greven
- Jitse Schol
- Nathalie van Sterkenburg
