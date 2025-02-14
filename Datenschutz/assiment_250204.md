## Aufgabe 1 ##

  Die 7 Grundprinzipien der DSGVO  

  1. Rechtmäßigkeit, Verarbeitung nach Treu und Glauben, Transparenz
Die Verarbeitung personenbezogener Daten muss rechtmäßig erfolgen. Betroffene müssen klar und verständlich darüber informiert werden, wie ihre Daten verarbeitet werden. 

  2. Zweckbindung
Daten dürfen nur für vorher festgelegte, eindeutige und legitime Zwecke erhoben und verarbeitet werden. Eine Weiterverarbeitung für andere Zwecke ist nur unter bestimmten Bedingungen erlaubt.

  3. Datenminimierung
Es sollen nur so viele Daten erhoben und verarbeitet werden, wie für den jeweiligen Zweck unbedingt erforderlich sind. Unnötige Datensammlungen sind zu vermeiden.

  4. Richtigkeit
Personenbezogene Daten müssen korrekt und aktuell sein. Falsche oder veraltete Daten müssen schnellstmöglich korrigiert oder gelöscht werden.

  5. Speicherbegrenzung
Daten dürfen nur so lange gespeichert werden, wie es für den jeweiligen Zweck notwendig ist. Danach müssen sie gelöscht oder anonymisiert werden.

  6. Integrität und Vertraulichkeit
Personenbezogene Daten müssen durch geeignete Sicherheitsmaßnahmen geschützt werden, um unbefugten Zugriff, Verlust oder Missbrauch zu verhindern.

  7. Rechenschaftspflicht
Verantwortliche Stellen müssen nachweisen können, dass sie die DSGVO einhalten. Dies erfordert dokumentierte Maßnahmen und Prozesse zur Datenschutz-Compliance.

## Augabe 2 ##


### Erkläre in 1-2 Sätzen, warum diese Methode unsicherer ist als eine Verschlüsselung mit einem zufälligen SSL-Key.
 Die Methode der Passwort-basierten Verschlüsselung ist unsicherer als die Verwendung eines zufälligen SSL-Keys, da Passwörter oft vorhersehbar oder durch Brute-Force-Angriffe geknackt werden können. Ein zufällig generierter Schlüssel ist hingegen deutlich komplexer und bietet eine höhere Sicherheit gegen solche Angriffe.


## Aufgabe 3 ##

### Warum wird für die Verschlüsselung ein „Salt“ hinzugefügt?
Ein **Salt** wird hinzugefügt, um sicherzustellen, dass selbst bei identischen Passwörtern unterschiedliche Schlüssel generiert werden. Dies verhindert Angriffe wie das Verwenden von vorerstellten Tabellen (Rainbow Tables) zur Entschlüsselung und erhöht die Sicherheit der Schlüsselableitung.  

### Was passiert, wenn der symmetrische Schlüssel verloren geht?
Wenn der symmetrische Schlüssel verloren geht, sind die verschlüsselten Daten praktisch **unwiederbringlich verloren**, da es ohne den Schlüssel keine Möglichkeit gibt, die Daten wieder zu entschlüsseln. 
