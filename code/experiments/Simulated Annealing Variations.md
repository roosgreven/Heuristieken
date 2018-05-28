# Beste Temperatuur 
Bij het simulated annealing algoritme, worden er veranderingen aan een plattegrond aangebracht waarbij er een kans bestaat dat een verslechtering wordt geaccepteerd. De kans dat dit gebeurt is afhankelijk van hoe erg de verslechtering is, en een zogeheten temperatuur; een functie afhankelijk van het aantal veranderingen dat al is geprobeerd. Er zijn veel mogelijkheden voor zo'n temperatuur, en in dit experiment zijn er drie recursieve functies uitgekozen waarmee is getest welke de beste resultaten oplevert. De functies waren:   
- functie 1: temp<sub>i</sub> = 0.95 * temp<sub>i-1</sub> 
- functie 2: temp<sub>i</sub> = temp<sub>i-1</sub> - 6  
- functie 3: temp<sub>i</sub> = temp<sub>i-1</sub><sup>0.995</sup>  

De experimenten zijn uitgevoerd met 3000 iteraties, een begintemperatuur van 50000 en met een kans op veranderingen move/swap/rotate van 0.6/0.2/0.2. De constanten in de functies zijn zo gekozen dat de temperatuur ongeveer de volle 3000 iteraties nodig had om in de buurt te komen van 0.

## Resultaat  
In de barcharts voor alle drie de varianten (20, 40 en 60) is duidelijk te zien dat in ons experiment functie 1 het beste resultaat geeft. Functie 2 komt op de tweede plek en functie 3 gaf het slechtste resultaat. Naarmate het aantal huizen toeneemt, lijkt functie 1 zich ook steeds verder te onderscheiden van functie 2 en 3. Uit dit experiment trekken wij de conclusie dat een temperatuur van de vorm y<sub>x</sub> = a * y<sub>x-1</sub> beter werkt dan een temperatuur van de vorm y<sub>x</sub> = y<sub>x-1</sub> - a of y<sub>x</sub> = y<sub>x-1</sub><sup>a</sup>. Het moet echter nog door vervolgonderzoek worden vastgesteld of dit echt zo is, omdat het kan zijn dat de constanten die zijn gekozen voor functie 2 en 3 niet optimaal zijn.
