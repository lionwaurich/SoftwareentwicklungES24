## Zustandsmaschinen sind ...
[[ ]] Oberbegriff für die Robotik im Haushalt
[[x]] endliche Automaten
[[x]] mit Eingaben an ihren Zuständen manipulierbar
[[ ]] Analysegeräte mit künstlicher Intelligenz
[[x]] Modelle mit Eingabe, Ausgabe, Zuständen und Verbindungen 


## Welche Komponente gehört nicht zum elementaren Aufbau einer Zustandsmaschine?

[[x]] Datenbanksystem
[[ ]] Übergangsfunktion (Transition Function)
[[x]] Clock-Signal (Taktgeber)
[[ ]] Ausgabefunktion (Output Function)
[[ ]] Speicherzustand (Memory State)
[[x]] Aktivierungsfunktion
[[x]] ALU (Arithmetic Logic Unit)
[[ ]] Eingabealphabet (Input Alphabet)
[[x]] DBMS (Datenbankenmanagementsystem)


## Welche Automaten finden in der Informatik Anwendung?

[[x]] Mealy Automat
[[ ]] Karnaugh-Veitch-Diagramm
[[ ]] Zuse Automat
[[x]] Moore Automat
[[ ]] Quine-McCluskey-Automat


## Mit welchen Logik-Gattern kann man jede beliebige Zustandsmaschine bauen?

[[ ]] Mit AND-Gattern oder OR-Gattern
[[x]] Mit NAND-Gattern und NOR-Gattern
[[ ]] Mit AND-Gattern und OR-Gattern 
[[x]] Mit AND-Gattern, OR-Gattern und NOT-Gattern


## Was ist die disjunktive Normalform (DNF) ?

[[ ]] XOR-Verknüpfungen
[[X]] Eine Disjunktion von Mintermen
[[ ]] Eine Disjunktion von Maxtermen
[[ ]] Und-Verknüpfunen

Kleine Erinnerung: disjunktiv = getrennt, konjunktiv = zusammen, Minterm = AND, Maxterm = OR


## Was ist die konjunktive Normalform (KNF) ?

[[ ]] Oder-Verknüpfungen
[[ ]] Eine Konjunktion von Mintermen
[[x]] Maxterme in Konjunktionen
[[x]] Und-Verknüpfunen

Kleine Erinnerung: disjunktiv = getrennt, konjunktiv = zusammen, Minterm = AND, Maxterm = OR


## Ordne richtig DNF oder KNF zu.

[[DNF] [KNF]]
[   [x]        [ ]  ] $ A\overline {B} \lor AB\overline {C} \lor C$
[   [ ]        [x]  ] $ \overline a \land b \land c $
[   [x]        [ ]  ] $ \lnot A \lor B \lor \lnot C $
[   [ ]        [x]  ] $ (\overline {a} + b + \overline {c}) \cdot (\overline {a} + \overline {b} + c) \cdot (\overline {b} + c)$
[   [x]        [ ]  ] $ \overline {ab} c + bc + \overline {a} b \overline {c}$
[   [x]        [ ]  ] $ A \land \overline {B} \land \overline {C} \lor \overline {A} \land B \land \overline {C} \lor \overline {B} \land C $
[   [ ]        [x]  ] $ (\overline {A} \lor B \lor \overline {C}) \land (A \lor \overline {B} \lor \overline {C}) \land (\overline {A} \lor \overline {B} \lor C)$


## Was ist die kanonische Normalform (KNF) ?

[[x]] Standartnormalform einer Wahrheitsfunktion.
[[ ]] die KNF besteht nur aus Maxtermen
[[x]] die KNF besteht aus Maxtermen in Mintermen oder Mintermen in Maxtermen
[[ ]] die KNF ist eine minimierte Wahrheitsfunktion


## Was ist das Karnaugh-Veitch-Diagramm ?

[[ ]] Eine spezielle Zustandsmaschine
[[x]] Methode zur Minimalisierung von Wahrheitsfunktionen
[[x]] Wahrheitstabelle für bestimmte Max- und Minterme 
[[ ]] Ein Diagramm für das stochastische Eintreten der jeweiligen Zustände


## Ablauf zur Wahreitsfunktionermittlung.

Schritt [[ 4]] : Minimieren<br/>
Schritt [[ 3]] : Karnaugh-Veitch-Diagramm erstellen<br/>
Schritt [[ 1]] : Wahrheitstabelle erstellen <br/>
Schritt [[ 5]] : minimierte Wahrheitsfunktion aufstellen<br/>
Schritt [[ 2]] : Max- und Minterme finden<br/>


## Vervollständige das Karnaugh-Veitch-Diagramm.

Wahrheitstabelle

<!-- data-type="none" -->
| $a$ | $b$ | $c$ | $y$ |
| --- | --- | --- | --- |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 1   |
| 0   | 1   | 0   | 1   |
| 0   | 1   | 1   | 1   |
| 1   | 0   | 0   | 0   |
| 1   | 0   | 1   | 1   |
| 1   | 1   | 0   | 0   |
| 1   | 1   | 1   | 0   |


Karnaugh-Veitch-Diagramm

|                | $b\overline{c}$ | $bc$   | $\overline{b}c$ | $\overline{bc}$ |
| -------------- | --------------- | ------ | --------------- | -------------------------- |
| $a$            | [[ 0]]          | [[ 0]] | [[ 1]]          | [[ 0]]                     |
| $\overline{a}$ | [[ 1]]          | [[ 1]] | [[ 1]]          | [[ 0]]                     |

