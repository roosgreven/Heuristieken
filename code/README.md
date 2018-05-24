# Code
In deze folder staat alle code die is gebruikt om de casus Amstelhaege op te lossen. Direct in deze folder staat main.py die kan worden aangeroepen om het gewenste algoritme uit te voeren. In de folder algorithms staat de code om ieder algoritme uit te voeren. In de folder classes staat de code voor de datastructuur. In de folder helpers staan de functies die helpen bij het uitvoeren van de algoritmes. In de folder resultaten staan csv files met de best behaalde resultaten voor ieder algoritme en in de folder experiments staan de resultaten van de experimenten die zijn uitgevoerd met een toelichting erbij.

# Gebruik
Aanroepen van de functie gaat via het format:
python Heuristieken\code\main.py TYPEOFALGORITHM NUMBEROFHOUSES 

Als NUMBEROFHOUSES worden de getallen 20, 40 en 60 geaccepteerd. Dit is het aantal huizen dat in de wijk zal worden geplaatst.
Voor TYPEOFALGORITHM bestaan de volgende mogelijkheden:
- random            
Voert het random algoritme eenmalig uit, print de uitkomst en slaat hem op als hij het beste is.
- greedy            
Voert het greedy algoritme eenmalig uit, sprint de uitkomst en slaat hem op als hij het beste is.
- hillclimber       
Voert het hill climber algoritme eenmalig uit, print de uitkomst en slaat hem op als hij het beste is.
- simulatedannealing       
Voert het simulated annealing algoritme eenmalig uit, print de uitkomst en slaat hem op als hij het beste is.
- particleswarm       
Voert het particle swarm algoritme. (MORE DETAILS)
- randomExperiment      
Voert het random algoritme vijfhonderd keer uit en slaat alle waardes op. 
- greedyExperiment      
Voert het greedy algoritme vijfhonderd keer uit en slaat alle waardes op. 
- hillclimberExperiment      
Voert het hillclimber algoritme vijfhonderd keer uit en slaat alle waardes op. 
- simulatedannealingExperiment      
Voert het simulated annealing algoritme vijfhonderd keer uit en slaat alle waardes op. 

