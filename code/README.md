# Code
In deze folder staat alle code die is gebruikt om de casus Amstelhaege op te lossen. Zie voor meer informatie http://heuristieken.nl/wiki/index.php?title=Amstelhaege. Dit is gedaan met python 3.6.6. Zie het bestand requirements.txt voor de benodigde modules. 
Deze folder: main.py, kan worden aangeroepen om het gewenste algoritme uit te voeren. 
Folder algorithms: code om ieder algoritme uit te voeren. 
Folder classes: code voor de datastructuur. 
Folder helpers: functies die helpen bij het uitvoeren van de algoritmes. 
Folder resultaten: csv files met de best behaalde resultaten voor ieder algoritme. 
Folder experiments: resultaten van de experimenten die zijn uitgevoerd met een toelichting erbij.

# Gebruik
Aanroepen van de functie gaat vanuit de map code, via het format:
python main.py TYPEOFALGORITHM NUMBEROFHOUSES [ITERATIONS]

ITERATIONS wordt alleen geaccepteerd bij het aanroepen van hillclimber, simulated annealing en particle swarm. 
Als NUMBEROFHOUSES worden de getallen 20, 40 en 60 geaccepteerd. Dit is het aantal huizen dat in de wijk zal worden geplaatst.
Voor TYPEOFALGORITHM bestaan de volgende mogelijkheden:
- 	random            
	Voert het random algoritme eenmalig uit, print de uitkomst en slaat hem op als hij het beste is.
- 	greedy            
	Voert het greedy algoritme eenmalig uit, sprint de uitkomst en slaat hem op als hij het beste is.
- 	hillclimber       
	Voert het hill climber algoritme eenmalig uit, print de uitkomst en slaat hem op als hij het beste is.
- 	simulatedannealing       
	Voert het simulated annealing algoritme eenmalig uit, print de uitkomst en slaat hem op als hij het beste is.
- 	particleswarm       
	Voert het particle swarm algoritme. (MORE DETAILS)
- 	randomExperiment      
	Voert het random algoritme vijfhonderd keer uit en slaat alle waardes op. 
- 	greedyExperiment      
	Voert het greedy algoritme vijfhonderd keer uit en slaat alle waardes op. 
- 	hillclimberExperiment      
	Voert het hillclimber algoritme vijfhonderd keer uit en slaat alle waardes op. 
- 	simulatedannealingExperiment      
	Voert het simulated annealing algoritme vijfhonderd keer uit en slaat alle waardes op. 

Via het bestand barchart.html kun je visualisaties van experimenten zien. Hier staan momenteel aleen de experimenten van random in. 