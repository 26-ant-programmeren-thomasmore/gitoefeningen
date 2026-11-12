# Markdown Conventies en Kwaliteitsregels

Dit document definieert de bindende standaarden voor alle Markdown-bestanden binnen het `gitoefeningen`-project. Een AI-agent of ontwikkelaar moet elk `.md`-bestand aan onderstaande checklist toetsen.

---

## 1. Encoding en Byte Order Mark (BOM)
* **Formaat:** Sla elk bestand uitsluitend op in **pure UTF-8 (zonder BOM)**.
* **Geen BOM:** De bytes `\xef\xbb\xbf` mogen nooit aan het begin van een bestand staan (dit breekt H1-herkenning en veroorzaakt `[ZWNBSP]` bij samenvoegen).
* **Geen Windows-1252:** Gebruik geen legacy Windows-1252/ANSI tekens (zoals smart quotes `0x93` / `0x94` of en-dashes `0x96`). Gebruik altijd standaard ASCII of valide UTF-8 tekens.

---

## 2. Koppenstructuur (H1)
* **Start op regel 1:** Elk document moet verplicht direct op regel 1 beginnen met precies één H1-kop:
  ```markdown
  # <Titel>
  ```
* **Geen witregels vóór H1:** Er mogen geen lege regels of spaties voorafgaan aan het `#`-teken op regel 1.
* **Subkoppen:** Gebruik voor tussenkoppen uitsluitend `##` (H2) en `###` (H3).

---

## 3. Interne Links en Uitlijning met H1
* **Linkformaat:** Elke interne link naar een ander markdown-document moet een relatief pad bevatten inclusief `.md`-extensie:
  ```markdown
  [Titel](relatief/pad/bestand.md)
  ```
* **Exacte 1-op-1 match met H1:** De linktekst `[Titel]` moet **exact** overeenkomen met de `# <Titel>` van het doelbestand (hoofdletters, leestekens en spaties).
  * *Voorbeeld:* Als het doelbestand begint met `# Installeer Git`, dan moet de link `[Installeer Git](01_getting_started/02_installeer_git.md)` zijn.
  * *Reden:* Hierdoor kan het samenvoegscript `combine_files.sh` de interne anker-slug (`#installeer-git`) direct afleiden uit de linktekst zelf, zonder externe bestandslookups.

---

## 4. Afbeeldingen en Paden
* **Centrale map:** Alle afbeeldingen staan centraal in de hoofdmap `images/<mapnaam>/` in de projectroot (geen lokale `images/`-mappen binnen de submappen).
* **Relatieve paden:** Vanuit cursusdocumenten in submappen wordt altijd verwezen via:
  ```markdown
  ![Omschrijving](../images/<mapnaam>/<afbeelding>.png)
  ```
* **Bestandsnamen:** Gebruik voor afbeeldingsbestandsnamen uitsluitend kleine letters, cijfers en underscores (geen spaties).

---

## 5. Paginanavigatie en Afsluitende Scheiders
* **Einde van hoofdstukdocumenten:** Elk inhoudelijk document moet verplicht eindigen met een scheidingslijn `---` en navigatielinks:
  ```markdown
  ---
  [prev](pad/naar/vorig_bestand.md)
  [next](pad/naar/volgend_bestand.md)
  ```
* **Start- en eindhoofdstuk:**
  * In het eerste hoofdstuk verwijst `[prev]` naar `../README.md`.
  * In het laatste hoofdstuk ontbreekt de `[next]`-regel of is deze leeg.
* **Naslagbestanden zonder navigatie:** Documenten zonder `[prev]` / `[next]` (zoals in `999_allerlei/`) moeten altijd afsluiten met een `---` op een eigen regel.

---

## 6. Mappen- en Bestandsnaamstructuur
* **Cursusmappen:** Gebruik een tweecijferige nummering met underscore in de root:
  `01_getting_started/`, `02_time_travel/`, `03_github/`, `04_collaboration_tool/`, `05_branches/`, `999_allerlei/`.
* **Cursusbestanden:** Bestanden binnen cursusmappen starten met een tweecijferige nummering:
  `01_wat_is_git.md`, `02_installeer_git.md`, enz.
* **Projectroot:** In de root van het project bevindt zich als cursusdocument uitsluitend `README.md` (de inhoudsopgave). Bestanden zoals `CONVENTIONS.md` worden uitgesloten van compilatie naar `all_pages.md`.

---

## 7. Regeleinden (Line Endings)
* **Unix LF:** Alle bestanden moeten worden opgeslagen met Unix LF (`\n`) regeleinden, nooit met Windows CRLF (`\r\n`).
