## Undo changes 

### Undo unstaged change: git checkout 

* Dus: je hebt een aanpassing gedaan die je niet meer wil. 
* Deze aanpassing is nog niet gecommit
* Je wil terug naar de situatie van de laatste commit.


#### In Git Bash
* doe een checkout van de laatste commit:
```bash
    cd gittest
    git status
    <pas de file aan>
    git status
    <we willen nu de aanpassingen rollbacken:> 
    git checkout <aangepaste file>
    git status
```

#### In IntelliJ 
* open het commit-window (klik op Commit in de linker marge)
* rechts-klik op "default change list"
* kies "Rollback" 
* als je Unversioned File hebt moet je deze manueel deleten 

### Undo staged change: git reset HEAD 

* Dus: je hebt een aanpassing gedaan en deze gestaged (git add .)
* Je wil terug naar de situatie van de laatste commit.

#### In Git Bash
* gebruik het commando "**git reset HEAD**"
```bash
    cd gittest
    git status
    <pas de file aan>
    git add . 
    git status
    <we willen nu de aanpassingen rollbacken:> 
    git reset HEAD
    git status
```

#### In IntelliJ
* in IntelliJ zie je niet echt het verschil tussen staged en niet-staged (dat gebeurt achter de schermen door in het commit window de files te selecteren)
* open het commit-window (klik op Commit in de linker marge)
* rechts-klik op "default change list"
* kies "Rollback"
* als je Unversioned File hebt moet je deze manueel deleten

### Undo last commit

* Dus: je hebt een aanpassing gedaan en deze gecommit
* Je wil terug naar de situatie van de **vorige commit**.

#### In Git Bash
* gebruik het commando "**git reset HEAD~**"
```bash
    cd gittest
    git status
    <pas file aan>
    git status
    git add <file>
    git commit -m "<zet hier de commit message>"
    git status
    git log
    <we willen nu de gecommitte aanpassingen rollbacken:> 
    git reset HEAD~
    git log
    git status
```

#### In IntelliJ
* Ga naar de history (de "Log" tab in het Git Tool window onderaan)
* selecteer de vorige commit 
* rechts-klik en kies "Reset Current Branch to here..."
* Kies in de dialog de eerste optie "Soft". De situatie is dan terug exact zoals die was voor je commit. Je kan nu verder de files aanpassen (of rollbacken) 

### Oefening
* doe een aanpassing en rollback 
* doe een aanpassing, commit en undo  

---
[prev](02_go_back_in_time.md)
[next](../03_github/01_wat_is_github.md)
