# Simple Dice Game Strategy
## <u>Règles du jeu</u>
Il s’agit d’un jeu de dé à un seul joueur. On fixe un nombre de coups maximum, disons N=5 coups.
A chaque coup, le joueur lance un dé et décide :
<ul>
    <li>s’il empoche le montant indiqué par le dé</li>
    <li>s'il relance le dé (pour espérer gagner plus)</li>
</ul>

Si le nombre de lancers atteint 0, alors le joueur empoche le montant indiqué par le dé.

## <u>Première approche, formule trouvée</u> 
Premièrement nous avons cherché quelle était la probabilité lorsqu'on a un certain nombre sur le dé, d’obtenir un nombre 
inférieur ou égal au prochain lancer. Nous avons trouvé : 

<p align="center">
    <img width="44" height="164" src="readme_data/images/frac_d_f.png#gh-light-mode-only">
    <img width="44" height="164" src="readme_data/images/frac_d_f_darkmode.png#gh-dark-mode-only">
</p>

<em>avec d : nombre indiqué par le dé
et f : nombre de faces du dé</em>

---

Cette formule ne marche que pour le prochain lancer. Si on a un nombre n de lancers restants, du fait qu'ils soient tous indépendants, la probabilité 
d’obtenir un nombre inférieur ou égal au nombre actuel sur tous les prochains lancers :


<p align="center">
    <img width="124" height="118,66" src="readme_data/images/left(_frac_d_f_r.png#gh-light-mode-only">
    <img width="124" height="118,66" src="readme_data/images/left(_frac_d_f_r_darmode.png#gh-dark-mode-only">
</p>

---

Donc la probabilité qu’au moins un futur lancer sur les n prochains lancers soit supérieur au lancer actuel est l’événement contraire. Cela correspond à la probabilité d’augmenter les gains en continuant:

<p align="center">
    <img width="212" height="118,66" src="readme_data/images/1_-_left(_frac_d.png#gh-light-mode-only">
    <img width="212" height="118,66" src="readme_data/images/1_-_left(_frac_d_darmode.png#gh-dark-mode-only">
</p>