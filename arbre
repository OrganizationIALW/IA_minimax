include("modele");
include("action");
/*
var noeud = [];
noeud["partie"] = null;
noeud["type"] = null; // "min" ou "max" ou "racine" ? 
noeud["fils"] = [];
noeud["action"] = null;*/


/**
 * créer la racine de l'arbre pour le tour, la partie est "l'image" la vrai partie 
 */
function createRacine(@partie) {
	var noeud = [];
	noeud["partie"] = partie;
	noeud["type"] = "racine"; 
	noeud["fils"] = [];
	noeud["action"] = null;
	return @noeud;
}

/**
 * addFeuille: créer un nouveau fils à partir d'une partie et d'une action et l'ajoute à la liste des fils de la racine
 */
function addFeuille(@racine, @partie, @action) {
	var noeud = [];
	noeud["partie"] = partie;
	noeud["type"] = (racine["type"] == "max") ? "min" : "max"; //Hypothèse : on alterne les noeud min et max
	noeud["fils"] = [];
	noeud["action"] = action;
	push(racine["fils"], @noeud);
}

/**
 * generateFils : génère une liste de fils à partir d'une liste d'action et l'ajoute à la racine d'un arbre
 * actions : liste d'action, une action est un combo
 */
function generateFils(@racine, @actions) {
	for(var action in actions) {
		var partie = clone(racine["partie"]);
		simulateCombo(partie, action);
		addFeuille(racine, partie, action);
	}
}

/**
 * generateDeapthTree => génère une profondeur de plus à l'arbre
 */
function generateDeapthTree(@racine, etage) {
	if(etage > 0) {
		if(racine["fils"] = []) {
			var actions = getCombos(racine["partie"]);
			generateFils(racine, actions); //génénère les premiers noeuds max
		} else {
			for (var fils in racine["fils"]) {
				generateDeapthTree(fils, etage-1);
			}
		}
	}	
}
