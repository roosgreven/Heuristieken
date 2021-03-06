# General Comparison
In dit project hebben wij vijf algoritmes uitgevoerd om een zo hoog mogelijke waarde voor de wijk Amstelhaege te vinden. Dan is het belangrijk om te weten welk algoritme het beste werkt. Daarom hebben we alle algoritmes meermalig laten runnen en de gevonden waarde voor ieder algoritmen in een bar chart gezet. We hebben dit voor alle drie de varianten gedaan. Details over de algoritmes:
- Hill Climber heeft gerund met 3000 iteraties en kansen op het type verandering van move/swap/rotate van 0.6/0.2/0.2.
- Simulated Annealing heeft gerund met 3000 iteraties en kansen op het type verandering van move/swap/rotate van 0.6/0.2/0.2. De temperatuur begon op temp = 50000 en de formule temp<sub>i</sub> = 0.95 * temp<sub>i-1</sub>.
- Particle Swarm heeft gerund met een populatie van 100 floorplans en 500 iteraties.

Het resultaat is hier te zien: https://roosgreven.github.io/Heuristieken/code/experiments/html/index.html

## Resultaat
Wat meteen opvalt aan de grafiek is dat de waarden van alle algoritmes uit elkaar liggen, behalve simulated annealing en hill climber, die samen de hoogste waarden hebben. Er is dus duidelijk kwaliteitsverschil tussen de algoritmen. Als er goed naar de chart wordt gekeken, blijkt dat hill climber het beste uit dit experiment naar voren komt, maar het verschil met simulated annealing is zo minimaal dat er meer experimenten gedaan zouden moeten worden om hier een uitspraak over te kunnen doen. Misschien dat er ook nog betere temperaturen voor simulated annealing te vinden zijn.  
Nog iets wat opvalt aan de grafiek is dat de waarden van particle swarm boven de waarden van random liggen. Hierdoor lijkt het alsof onze particle swarm een beter algoritme is dan onze random. Maar het blijkt dat onze particle swarm zelden verbeteringen vindt omdat huizen te erg beperkt zijn in hun bewegingsvrijheid. Wat particle swarm wel heeft, is een populatie van 100 floorplans waaruit de beste wordt gekozen. Dat is de reden dat particle swarm toch beter lijkt dan random, omdat zelfs als er geen verbeteringen worden gevonden, dan nog selecteert particle swarm de beste random plattegrond uit honderd.
