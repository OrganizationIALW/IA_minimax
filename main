include("modele");
include("arbre");
include("action");
include("global");
include("alphabeta");

var partie = createPartie();
initPartie(partie);
var racine = createRacine(partie);


var etage = 0; //Profondeur de l'arbre
var condition = function() {
	//todo: faire la condition
	return getOperations() < 0.6 * OPERATIONS_LIMIT; 
};


while (condition()) {
	etage++;
	generateDeapthTree(racine, etage);
	alphabeta(racine, _MIN_INT, _MAX_INT);
}


executeCombo(racine["bestFils"]);
// Fini ! =)




