# Beste Percentages

Bij het hill climber algoritme worden er verschillende typen veranderingen aan een plattegrond aangebracht, waarbij de mogelijkheden als volgt zijn:  
- MOVE - Een huis wordt tussen de 0m en 1m verplaatst in x-richting en in de y-richting.
- SWAP - Twee verschillende soorten huizen worden van plek verwisseld. Hierbij is het coördinaat van de hoek linksonder het coördinaat dat wordt uitgewisseld.
- ROTATE - De oriëntatie van een huis wordt veranderd. Dus de lengte wordt de breedte en de breedte wordt de lengte.
Welke verandering er steeds plaatsvindt, hangt af van hoe groot de kans is dat die verandering wordt uitgekozen. In dit experiment wordt er naar een aantal verschillende kansen voor iedere verandering gekeken. Op volgorde move/swap/rotate zijn de percentages 100/0/0, 60/20/20, 50/25/25, 33.3/33.3/33.3. Move heeft steeds de grootste kans om gekozen te worden omdat er binnen die verandering de meeste variatie zit. Er wordt steeds met 3000 iteraties, 3000 potentiële veranderingen, gewerkt.

Het resultaat is hier te vinden: https://roosgreven.github.io/Heuristieken/code/experiments/html/hillclimberPercentages.html

## Resultaat
Zoals in de barcharts te zien is, liggen voor alle drie de varianten de uitkomsten van ieder percentage dicht bij elkaar. Daarom kan er niet worden gesproken over een beste verdeling, de verschillen zijn daarvoor te klein om na dit experiment iets met zekerheid te kunnen zeggen. Wel lijkt het erop dat het percentage 60/20/20 bij de variant van 20 en 40 huizen het iets beter doet dan de rest, terwijl deze voorsprong bij de 60-huizen variant is weggezakt. Hier lijkt het of het percentage 100/0/0 net het beste is. Wat ook opvalt is dat het percentage 50/25/25 iets lijkt weg te zakken bij hogere aantallen huizen. Deze observaties zouden er op kunnen wijzen dat percentages waarin de kansen eerlijk verdeeld zijn, het beter doen bij lagere aantallen huizen, terwijl het voor hogere aantallen huizen voordeliger is om de kans voor move te verhogen. Dit is echter niet te bevestigen of te ontkennen met dit experiment.
