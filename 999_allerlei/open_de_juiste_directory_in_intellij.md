## Open de juiste directory in IntelliJ

Wanneer je een project opent in IntelliJ, moet je altijd de **juiste basismap (Project Root)** kiezen.

Open je per ongeluk een bovenliggende map (parent folder) of een submap (child folder)? Dan ontstaan er problemen met zowel IntelliJ als Git.

---

### Het probleem in IntelliJ

Studenten openen dikwijls de verkeerde map:
* **Een parent folder openen:** Je opent bijvoorbeeld de map `c:/Projects` of een verzamelmap waarin meerdere verschillende oefeningen zitten.
* **Een child folder openen:** Je opent rechtstreeks de submap `src` van een oefening.

### Wat loopt er dan mis?
* IntelliJ herkent je code niet als een uitvoerbaar project of module.
* Er verschijnt **geen groen start-icoon (Play-knop)** naast je `main`-methode.
* Je kunt geen **Run Configuration** aanmaken.
* IntelliJ weet niet welke SDK of Java-versie bij het project hoort.
* IntelliJ maakt een `.idea`-map aan in die verkeerde map, waardoor je mappenstructuur vervuild raakt.

### Fout geopend? Zo los je het op

Heb je toch per ongeluk een verkeerde map (zoals een parent folder) geopend in IntelliJ? 
Dan heeft IntelliJ daarin automatisch een `.idea`-map aangemaakt. Ruim dit meteen op om verwarring en vervuiling te vermijden:

* Klik in IntelliJ op `File > Close Project`.
* Open je bestandsverkenner en zorg dat **verborgen bestanden** zichtbaar zijn.
* Blader naar de verkeerde map die je per ongeluk had geopend.
* **Kuis de map op:**
  * Verwijder de verborgen map `.idea`.
  * Verwijder eventuele bestanden die eindigen op `.iml`.
  * Heb je er per ongeluk ook Git gestart? Verwijder dan ook de verborgen map `.git`.
* Ga terug naar het startscherm van IntelliJ (Welcome to IntelliJ IDEA).
* Klik op `Open`.
* Selecteer nu de **juiste project root** (gebruik de herkenningsgids hierboven).
* Klik op `OK` om het project correct te laden.

### Gevaar voor Git: initialiseer nooit de verkeerde directory!

Als je in IntelliJ via `VCS > Create Git repository` (of via `git init`) Git inschakelt op de verkeerde map, veroorzaak je grote problemen:

* **Git initialiseren op een parent folder:**
  * Git behandelt al je verschillende oefeningen en mappen als één gigantische repository.
  * Wijzigingen in oefening A komen per ongeluk in de commits van oefening B terecht.
  * Je commit history wordt onoverzichtelijk en vervuild.
  * Op GitHub upload je onbedoeld al je persoonlijke bestanden of al je andere cursusoefeningen tegelijk in één repository.
* **Git initialiseren op een child folder (zoals `src`):**
  * Belangrijke configuratiebestanden die buiten `src` staan (zoals `.gitignore`, `pom.xml` of `package.json`) worden niet opgenomen in Git.
  * Als iemand anders (of jijzelf op een andere computer) deze repository clonet, ontbreken de instellingen en start het project niet op.

### Hoe herstel je een foute Git-initialisatie?
* Sluit IntelliJ af (`File > Close Project`).
* Open je bestandsverkenner en zorg dat **verborgen bestanden** zichtbaar zijn (hidden files).
* Ga naar de verkeerde map waar je per ongeluk Git hebt gestart.
* Verwijder daar de verborgen map `.git`.  **Let op**: je bent je git history dan kwijt 
* Open daarna pas de juiste projectmap in IntelliJ en initialiseer Git opnieuw.

---

## Hoe herken je de juiste directory?

Kijk naar de bestanden en mappen die direct in de map staan. Dit verschilt per technologie en type project:

| Technologie | Voorbeelden van vakken | Belangrijkste herkenningspunt | Wat open je in IntelliJ? |
|---|---|---|---|
| **Basis Java** (geen build tool) | Programming Fundamentals, Object Oriented Programming | Bevat direct de map `src` | De map net boven `src` |
| **Java met Maven** | Object Oriented 2 | Bevat het bestand `pom.xml` | De map met `pom.xml` |
| **Spring Boot met Maven** | Advanced Programming Techniques, Projecten Voor het Werkveld | Bevat het bestand `pom.xml` | De map met `pom.xml` |
| **JavaScript met npm** | Interactive Webapps | Bevat het bestand `package.json` | De map met `package.json` |
| **React met Vite en npm** | Frontend single-page apps (o.a. kwartaal 5) | Bevat `package.json` en `vite.config.js` | De map met `package.json` |

---
[prev](linux_en_dos_commandos.md)
[next](tips.md)
