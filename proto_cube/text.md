# proto_cube

Industrie 4.0 Retrofit zur integrativen Erfassung von Betriebs und Maschinendaten



## Ziel 

Wir wollen mehr Informationen über Prozesse in der Produktion



Viel möglichkeiten diese zu verwenden:

- Predictive Maintainance
- Optimierung
- Verbesserte Kostenzuweiseung
- Unterstützung der Mitarbeiter
- ...



## Was wird gemacht?

1. Sensordaten erfassen
2. Kommunikation ermöglichen
3. IoT-/Datenplatform einrichten
4. Erfassung von zusätlichen Daten über Web-App



Das ganze soll als Box an der Maschine nachgerüstet werden. Es soll also ein Box an die Maschine gescharubt werden an welcher Sensoren angschlossen sind und vorne das Tablet für die Bedienung befestigt werden kann. 



## Wie wirds gemacht?

## Technologische Strucktur

- Maschine mit Sensoren ausgerüstet
- RevPi sendet empfängt und verarbeite diese Daten
- stellt sie via OPC UA und MQTT zur verfügung 
- Speichert sie in einer InfluxDB Datenbank



- Die App befindet sich Ebenfalls auf dem RevPi
- Über das Device können Daten von der Maschine als auch von der Auftragdatenbank abgerufen werden
- Es können zusätzliche Informationen eingegeben werden. Was wo passiert ist. 