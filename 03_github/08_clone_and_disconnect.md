## Clone en disconnect 

### Waarom: startcode 
* Voor sommige programmeer projecten zullen we je vragen om 
  * een repository uit Github te clonen 
  * disconnecteren van de remote repo (dit zal de docent expliciet vragen indien nodig)
  * en connecteren met je eigen Github repo 
* Dit zal bvb gebeuren als:
  * docent zet start code voor een oefening op Github
  * je werkt zelf de oefening uit en commit regelmatig 
  * je pusht je oplossing naar je eigen Github repo 
  * dit doen we vooral voor grotere stap-voor-stap oefeningen, waar de oplossingen ook stap voor stap gecommit worden 
* let op: dit doe je normaal gezien niet in een bedrijfssituatie, daar heb je gewoonlijk 1 remote repo die door verschillende mensen lokaal gecloned wordt 

### Hoe
* Wat moet je doen: 
  * **Stap 1: Clone** 
    * Open IntelliJ en voer het volgende uit: 
    * File > New > Project from Version Control...,
    * kopieer de github repository die hierboven staat
    * kies een map waarin je dat project wenst te plaatsen, en kies Clone.
    * Check welke branch je nodig hebt en maak deze  branch actief in je project.
  * **Stap 2: Maak je eigen lege remote Repo**
    * Ga naar github 
    * maak een nieuwe lege **private** repository, bvb advanced_toets1 of
      advanced_toets2. Deze moet **geen** files bevatten.
    * nodig je docent uit als collaborator voor je repository (Settings > Collaborators > Add people)
  * **Stap 3: Disconnecteer de local repo**  
    * Koppel jouw local repo los van github: 
    * Git > Manage Remotes..., selecteer de github-repository en klik op het min-icoon (-)
  * **Stap 4: Connecteer met je eigen remote Repo**
    * Koppel je local repo nu aan je eigen project: klik op de +
    * URL: de url van je eigen repo op github 
    * Push op die nieuwe repository alvast de branch die je net binnenhaalde. Check dit in
      github.

### Oplossingen 
* als de docent later de oplossingen van de oefeningen pusht
  * dan kan je die in dit geval **niet pullen**, want je repo is losgekoppeld van de repo van de docent
  * Dit zou ook conflicten geven, want jouw oplossingen staan in dezelfde files als de oplossingen van de docent 
  * Je maakt dan een 2e clone van de repo van de docent waar je de oplossingen kan binnenhalen
  * Je kan de 2 projecten openenen in IntelliJ en de code vergelijken

### Oefening
* Maak een test-repository aan op GitHub.
* Clone deze via IntelliJ naar een nieuwe lokale map (Stap 1).
* Koppel de remote los via **Manage Remotes** (Stap 3).
* Maak een tweede lege repository aan op GitHub en koppel je lokale repo hieraan (Stap 4).
* Push je code naar de nieuwe repository en verifieer het resultaat op GitHub.

---
[prev](07_github_pages.md)
[next](09_clone_met_2_remotes.md)
