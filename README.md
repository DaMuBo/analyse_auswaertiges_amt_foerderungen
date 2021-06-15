# Projektarbeit - Analyse von Förderungstätigkeiten des Auswärtigen Amtes
- Student: D. Müller
- Matrikelnummer: ******
- Vorlesung: Angewandte Programmierung
- Dozent:  D**** G*******

# Gliederung

* Definition der Fragestellung [[1]](#1)
* Packages einlesen [[2]](#2)
* Datei einlesen und in Dataframe konvertieren [[3]](#3)
* Übersicht Datenstrukturen [[4]](#4)
* Erste Visualisierungen [[5]](#5)
    * Partizipierende Organisationen [[6]](#6)
    * Budget Vs Kosten [[7]](#7)
    * Die Größten Geldempfänger und die Verteilung [[8]](#8)
* Text Mining Ansatz zur Clusterung [[9]](#9)
    * Preprocessing [[10]](#10)
    * Clusteranzahl definieren [[11]](#11)
    * Training ML [[12]](#12)
* Visualisierung der ML Ergebnisse [[13]](#13)
    * Dimensionsreduktion [[14]](#14)
    * Scatterplot [[15]](#15)
* Fazit / Ausblick  [[16]](#16)
* Quellenverzeichnis [[17]](#quellenverzeichnis)

## Definition der Fragestellung:  <a class="anchor" id="1"></a> 

ZUr Untersuchung des Datensatzes sind sich die folgenden Fragen gestellt worden. Diese sollen mithilfe der Daten beantwortet werden:

1. Mit welchen Organisationen hat das Auswärtige Amt hauptsächlich zusammengearbeitet?
2. Wie viel Budget und Kosten sind in den Jahren dokumentiert? 
3. Gibt es Jahre in denen die Ausgaben das Budget überstiegen haben?
4. Welche Organisationen haben besonders viel Geld vom Auswärten Amt erhalten?
5. Ist es möglich Themen Felder mithilfe von Machine Learning zu identifizieren?
