// modele : Il faut refaire toute le modele de LW pour pouvoir le simuler

function createPartie() {
	var partie = [];
	partie["currentLeek"]  = null;
	partie["OrdreJeu"] = []; //liste des joueurs dans le bon ordre, en première position : le joueur courant
	partie["TeamAllie"] = []; //leek allie
	partie["TeamEnnemis"] = []; //leek ennemis
	partie["Turn"] = 0; //Le tour de la partie
	partie["leeks"] = []; //tableau d'objet "leek" <= contient les infos importante sur un leek
	return @partie;
}

/*	Fonction elementaire	*/

function clone(something) {
	//devrait marcher : copie lors du passage par valeur, retour l'adresse de la copie 
	return @something;
}

function initPartie(@partie) {
	//initialise les variables de partie pour le début du tour
	// peut-être le faire dans create Partie !?!?!?
}

function nextTour(@partie) {
	// simule un nouveau tour sur "l'objet" partie 
	/* TODO:
			- turn ++
			- changer l'ordre de jeu, le joueur courrant
			- appliquer/retirer les "effets" sur le joueur courrant 
			- retirer les leeks mort (à cause du poison)
			- .... (je vois pas d'autres chose pour l'instant)
	*/
}

function getStatut(@partie) {
	// retourn le statut de la partie : EN_COURS, EGALITE, VICTOIRE, DEFAITE (par rapport au joueur courrant)
}

function setDamage(@partie, leek, value) {
	// appliquer des dégat sur leek
	// TODO: ne pas oublier l'érosion 
	// si il doit mourir, le retirer de la liste d'ordre de jeu + retirer tout les effects qu'il a lancé
}

function upMaxlife(@partie, leek, value) {
	// monte la vie total (et la vie)
}

function setHeal(@partie, leek, value) {
	// monte la vie de leek (ne pas dépasser max_life)
}

function addEffect(@partie, leek, @effect) {
	// ajoute un effect sur le leek (et dans la liste des effets du lanceur avec le même pointeur <= vérifier que c'est bien le même)
	// applique les effets qui sont immédiats (libé, antidote, debuff sur soi même (ché pas si c'est possible))
}

function moveLeek(@partie, newCell, dist) {
	// met à jour la position/MP du joueur courrant 
	// pas de vérif ! 
}

function setCurrentWeapon(@partie, weapon) {
	// change l'arme principale du joueur courrant, lui retire 1PT
}

function useTool(@partie, tool) {
	// change PT/CD sur un tool
	// pas de vérif !
}

function canUseTool(@partie, tool) {
	// verifie PT/CD pour un tool
	// hyp : je joueur courrant à forcement l'item tool
	return false;
}


/*	Fonction un peu plus haut niveau	*/

function getAccessibleCell(@parti, leek) {
	var cells = [];
	return @cells;
}


