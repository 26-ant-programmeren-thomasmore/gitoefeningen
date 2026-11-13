## Clone met 2 remotes 

### Waarom: startcode 
* Voor sommige programmeer projecten zullen we je vragen om 
  * een repository uit Github te clonen  
  * en connecteren met je eigen Github repo
  * de connectie met de repo van de docent blijft, de docent zal oplossingen pushen die je dan kan pullen 
* Dit zal bvb gebeuren als:
  * docent zet start code voor een oefening op Github
  * je werkt zelf de oefening uit en commit regelmatig 
  * je pusht je oplossing naar je eigen Github repo 
  * dit doen we vooral voor kleinere oefeningen, waar de oplossingen in een aparte folder worden gezet  

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
  * **Stap 4: Connecteer met je eigen remote Repo**
    * Koppel je local repo nu aan je eigen project: klik op de +
    * URL: de url van je eigen repo op github 
    * NAAM: je moet hier een andere naaam kiezen voor de 2e remote, bvb "my_solutions"
    * Push op de 2e remote alvast de branch die je net binnenhaalde:  
      * push 
      * in de push-dialog **klik je op origin** (de default remote) en **kies je de 2e remote "my_solutions"**
      * Check dit in github (in de nieuwe repo die je gemaakt hebt)

### Oplossingen 
* als de docent later de oplossingen van de oefeningen pusht
  * dan kan je die in dit geval **gewoon pullen** uit origin
  * Dit geeft geen conflicten, als de docent deze manier van werken kiest dan zal hij steeds de oplossingen publiceren 
in een andere folder dan degene waarin je zelf gewerkt hebt.  


---
[prev](08_clone_and_disconnect.md)
[next](../04_collaboration_tool/01_simpele_workflow.md)
