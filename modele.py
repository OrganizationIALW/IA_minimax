// modele : Il faut refaire toute le modele de LW pour pouvoir le simuler

/*
Un effet :  [type, value, lanceur_id, turns_left, critical, item_id, target_id]
*/


global EFFECTS_TO_STRING = [
EFFECT_ABSOLUTE_SHIELD: ["absolute_schield", "positive", "non cumulable"], EFFECT_BUFF_AGILITY: ["agility", "positive", "non cumulable"], EFFECT_BUFF_FORCE: ["force", "positive", "non cumulable"], EFFECT_BUFF_MP: ["PM", "positive", "non cumulable"], EFFECT_BUFF_RESISTANCE: ["resistance", "positive", "non cumulable"], EFFECT_BUFF_STRENGTH: ["force", "positive", "non cumulable"], EFFECT_BUFF_TP: ["PT", "positive", "non cumulable"], EFFECT_BUFF_WISDOM: ["sagesse", "positive", "non cumulable"], EFFECT_DAMAGE_RETURN: ["damage_return", "positive", "non cumulable"], EFFECT_POISON: ["poisonOn", "positive", "cumulable"], EFFECT_RELATIVE_SHIELD: ["relative_schield", "positive", "non cumulable"], EFFECT_SHACKLE_MAGIC: ["magie", "negative", "cumulable"], EFFECT_SHACKLE_MP: ["PM", "negative", "cumulable"], EFFECT_SHACKLE_STRENGTH: ["force", "negative", "cumulable"], EFFECT_SHACKLE_TP: ["PT", "negative", "cumulable"], EFFECT_VULNERABILITY: ["relative_schield", "negative", "non cumulable"], EFFECT_HEAL: ["vaccinOn", "positive", "non cumulable"]];

global BULBES = [
"puny_bulb" : ["vie" : 300, "force" : 100, "sagesse" : 100, "resistance" : 100, "agilité" : 100, "science" : 0, "magie" : 0, "PT" : 7, "PM" : 5, "vieTotale" : 300],
"rocky_bulb" : ["vie" : 600, "force" : 200, "sagesse" : 0, "resistance" : 100, "agilité" : 100, "science" : 0, "magie" : 0, "PT" : 8, "PM" : 3, "vieTotale" : 600],
"iced_bulb" : ["vie" : 500, "force" : 300, "sagesse" : 0, "resistance" : 0, "agilité" : 100, "science" : 100, "magie" : 0, "PT" : 8, "PM" : 4, "vieTotale" : 500],
"healer_bulb" : ["vie" : 400, "force" : 0, "sagesse" : 300, "resistance" : 0, "agilité" : 100, "science" : 0, "magie" : 0, "PT" : 8, "PM" : 6, "vieTotale" : 400],
"metallic_bulb" : ["vie" : 1100, "force" : 0, "sagesse" : 0, "resistance" : 300, "agilité" : 100, "science" : 200, "magie" : 0, "PT" : 9, "PM" : 3, "vieTotale" : 1100],
"fire_bulb" : ["vie" : 500, "force" : 300, "sagesse" : 200, "resistance" : 0, "agilité" : 100, "science" : 0, "magie" : 0, "PT" : 10, "PM" : 5, "vieTotale" : 500],
"lightning_bulb" : ["vie" : 600, "force" : 400, "sagesse" : 0, "resistance" : 0, "agilité" : 100, "science" : 200, "magie" : 0, "PT" : 10, "PM" : 6, "vieTotale" : 600]];


function createPartie() {
	var partie = [];
	partie["currentLeek"] = null;
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
	var leeks = getAllies()+getEnemies();
	partie["currentLeek"] = getLeek();
	partie["OrdreJeu"] = leeks;
	fill(partie["OrdreJeu"], 0);
	partie["TeamAllie"] = getAliveAllies();
	partie["TeamEnnemis"] = getAliveEnemies();
	partie["Turn"] = getTurn();
	partie["leeks"] = []; 
	
	for(var leek in leeks){
		partie["OrdreJeu"][getEntityTurnOrder(leek)-1] = leek;
		partie["leeks"] [leek] = [];
		partie["leeks"] [leek]["vie"] = getLife(leek);
		partie["leeks"] [leek]["force"] = getStrength(leek);
		partie["leeks"] [leek]["sagesse"] = getWisdom(leek);
		partie["leeks"] [leek]["resistance"] = getResistance(leek);
		partie["leeks"] [leek]["agilité"] = getAgility(leek);
		partie["leeks"] [leek]["science"] = getScience(leek);
		partie["leeks"] [leek]["magie"] = getMagic(leek);
		partie["leeks"] [leek]["PT"] = getTP(leek);
		partie["leeks"] [leek]["PM"] = getMP(leek);
		partie["leeks"] [leek]["vieTotale"] = getTotalLife(leek);
		partie["leeks"] [leek]["currentCell"] = getCell(leek);
		partie["leeks"] [leek]["ArmeEquipee"] = getWeapon(leek);
		partie["leeks"] [leek]["effects"] = [];
	}
}



function nextTour(@partie) {
	// simule un nouveau tour sur "l'objet" partie 
	/* TODO:
			- turn ++
			- changer l'ordre de jeu, le joueur courrant
			- appliquer/retirer les "effets" sur le joueur courrant 
			- retirer les leeks mort (à cause du poison)
	*/
	var nb_leeks = count(partie["OrdreJeu"]);
	//partie["OrdreJeu"][nb_leeks - 1] = partie["OrdreJeu"][0];
	//remove(partie["OrdreJeu"], 0);
	push(partie["OrdreJeu"], shift(partie["OrdreJeu"]));
	partie["currentLeek"] = partie["OrdreJeu"][0];

	if(getEntityTurnOrder(partie["currentLeek"]) == 1){
		partie["Turn"]++;
	}
	debug("ok");
	if(partie["leeks"][partie["currentLeek"]]["vie"] <= 0){
		nextTour(partie);
	}
	
	// EFFETS //
	var leek = partie["currentLeek"];
	for (var effet in partie["leeks"][leek]["effects"]) {
		
		effet[3] -= 1;
		if(effet[3] <= -1) {
			removeElement(partie["leeks"][leek]["effects"], effet);
		} else {
			if(effet[0] == EFFECT_POISON){
				partie["leeks"][leek]["vie"] -= effet[1];
				partie["leeks"][leek]["vieTotale"] -= effet[1]/10;
				if(partie["leeks"][leek]["vie"] <= 0){
					kill(partie, leek);
					nextTour(partie);
				}
			}
			if(effet[0] == EFFECT_HEAL){
				partie["leeks"][leek]["vie"] += min(partie["leeks"][leek]["vie"]+effet[1], partie["leeks"][leek]["vieTotale"]);
			}
		}
	}
}


function summon(@partie, entity_type, cell) {
	var id_leeks = [];
	for(var key : var value in partie["leeks"]){
		push(id_leeks, key);
	}
	var Max = 0;
	for(var id_leek in id_leeks){
		if(id_leek > Max){
			Max = id_leek;
		}
	}
	var id = Max + 1;
	partie["leeks"][id] = BULBES[entity_type];
	partie["leeks"][id]["currentCell"] = cell;
	insert(partie["OrdreJeu"], id, 1);
}



function kill(@partie, leek){
	// On retire les effets lancés par leek
	for(var entity in partie["OrdreJeu"]){
		for(var effect in partie["leeks"][leek]["effects"]){
			if(effect[2] == leek){
				removeElement(partie["leeks"][leek]["effects"], effect);
			}
		}
	}
}


function getStatut(@partie) {/*
	// retourn le statut de la partie : EN_COURS, EGALITE, VICTOIRE, DEFAITE (par rapport au joueur courrant)
	if(partie["Turn"] >= 64){
		return "EGALITE";
	}
	var AliveEnnemis = false;
	var AliveAllies = false;
	for(var leek in partie["TeamAllie"]){
		if(partie["leeks"][leek]["vie"] > 0 and AliveAllies == false){
			AliveAllies = true;
			break; // C'est moche...
		}
	}
	for(var leek in partie["TeamEnnemis"]){
		if(partie["leeks"][leek]["vie"] > 0 and AliveEnnemis == false){
			AliveEnnemis = true;
			break; // C'est moche...
		}
	}
	if(AliveAllies and not AliveEnnemis){
		if(leek in partie["TeamAllie"]){
			return "VICTOIRE";
		} else {
			return "DEFAITE";
		}		
	}
	if(AliveEnnemis and not AliveAllies){
		if(leek in partie["TeamAllie"]){
			return DEFAITE;
		} else {
			return "VICTOIRE";
		}
	}
	return "EN_COURS";
*/
}






function setDamage(@partie, leek, value) {
	// appliquer des dégat sur leek
	var lanceur = partie["currentLeek"];
	var renvoisDegats = 0;
	for (var effet in partie["leeks"][leek]["effects"]) {
		if(effet[0] == EFFECT_DAMAGE_RETURN){
				renvoisDegats += effet[1];
		}
	}
	partie["leeks"][leek]["vie"] -= value;
	partie["leeks"][leek]["vieTotale"] -= value/20;
	var valueVolDeVie = value * (partie["leeks"][lanceur]["sagesse"]/1000);
	partie["leeks"][lanceur]["vie"] += min(partie["leeks"][lanceur]["vie"] + valueVolDeVie, partie["leeks"][lanceur]["vieTotale"]);
	partie["leeks"][lanceur]["vie"] -= value * (renvoisDegats/100);
}



function ItemInEffects(effects, item){	// pour la cumulabilité
	for(var e in effects){
		if(e[5] == item){
			return true;
		}
	}
	return false;
}


function removeEffectWithItem(@partie, item, leek){	
	for(var e in partie["leeks"][leek]["effects"]){
		if(e[5] == item){
			removeElement(partie["leeks"][leek]["effects"], e);
			return;
		}
	}
	return;
}


function addEffect(@partie, leek, @effect) {
	// ajoute un effect sur le leek (et dans la liste des effets du lanceur avec le même pointeur <= vérifier que c'est bien le même)
	// applique les effets qui sont immédiats (libé, antidote, debuff sur soi même (ché pas si c'est possible))
	var type = effect[0];
	var value = effect[1];
	var lanceur = partie["currentLeek"];

	if (EFFECTS_TO_STRING[type] != null) {
		var item_to_give = effect[5];
		// Cumulabilité
		if(EFFECTS_TO_STRING[type][2] == "non cumulable"){
			if(ItemInEffects(partie["leeks"][leek]["effects"], item_to_give)){
				removeEffectWithItem(partie, item_to_give, leek);
			}
		}
		push(partie["leeks"][leek]["effects"], effect);
		if (EFFECTS_TO_STRING[type][1] == "positive") {
			partie["leeks"][leek][EFFECTS_TO_STRING[type][0]] += value;
		} else {
			partie["leeks"][leek][EFFECTS_TO_STRING[type][0]] -= value;
		}
	} else { // effets particuliers
		if (type == EFFECT_ANTIDOTE) {
			for (var effet in partie["leeks"][leek]["effects"]) {
				if (effet[0] == EFFECT_POISON) {
					removeElement(partie["leeks"][leek]["effects"], effet);
				}
			}
		}
		if (type == EFFECT_DEBUFF) {
			for (var effet in partie["leeks"][leek]["effects"]) {
				if (EFFECTS_TO_STRING[effet[0]] != null) {
					var v = effet[1] / 2;
					if (EFFECTS_TO_STRING[effet[0]][1] == "positive") {
						partie["leeks"][leek][EFFECTS_TO_STRING[type][0]] -= v;
					} else {
						partie["leeks"][leek][EFFECTS_TO_STRING[type][0]] += v;
					}
				}
			}
		}
	}
}


function moveLeek(@partie, newCell, dist) {
	// met à jour la position/MP du joueur courrant 
	// pas de vérif ! 
	var leek = partie["currentLeek"];
	partie["leeks"][leek]["currentCell"] = newCell;
	partie["leeks"][leek]["PM"] -= dist;
}


function setCurrentWeapon(@partie, weapon) {
	// change l'arme principale du joueur courrant, lui retire 1PT
	var leek = partie["currentLeek"];
	partie["leeks"][leek]["ArmeEquipee"] = weapon;
	partie["leeks"][leek]["PT"] -= 1;
}


function useTool(@partie, tool) {
	// change PT/CD sur un tool
	// pas de vérif !
	var leek = partie["currentLeek"];
	isChip(tool) ? partie["leeks"][leek]["PT"] -= getChipCost(tool) : partie["leeks"][leek]["PT"] -= getWeaponCost(tool);
	if (isChip(tool)) {
		partie["leeks"][leek][tool]["cooldown"] = getChipCooldown(tool);
	} else {
		partie["leeks"][leek][tool]["cooldown"] = 0;
	}
}


function canUseTool(@partie, tool) { // LANCEUR ?
	// verifie PT/CD pour un tool
	// hyp : je joueur courrant à forcement l'item tool
	var cost = isChip(tool) ? getChipCost(tool) : getWeaponCost(tool);
	var leek = partie["currentLeek"];
	if (partie["leeks"][leek][tool]["cooldown"] == 0 and partie["leeks"][leek]["PT"] >= cost) {
		return true;
	}
	return false;
}



function upMaxlife(@partie, leek, value) {
	// monte la vie total (et la vie)
	partie["leeks"][leek]["vie"] += value;
	partie["leeks"][leek]["vieTotale"] += value;
}



function setHeal(@partie, leek, value) {
	// monte la vie de leek (ne pas dépasser max_life)
	partie["leeks"][leek]["vie"] += min(partie["leeks"][leek]["vieTotale"], partie["leeks"][leek]["vie"] + value);
}



/*	Fonction un peu plus haut niveau	*/
function isEmptyCell_(@partie, cell){
	if(cell == null){
		return false;
	}
	if(isObstacle(cell)){
		return false;
	}
	for(var leek in partie["OrdreJeu"]){
		if(partie["leeks"][leek]["currentCell"] == cell){
			return false;
		}
	}
	return true;
}


function getAccessibleCell(@partie, leek) {
	var cellule = partie["leeks"][leek]["currentCell"];
	var mp = partie["leeks"][leek]["PM"];
	var deplacement = [cellule: 0];
	var caseTest = [cellule: true];

	for (var a = 1; a <= mp; a++) {
		var CaseEnTest = caseTest;
		caseTest = [];
		
		for (var case :var i in CaseEnTest) {
			var cx = getCellX(case);
			var cy = getCellY(case);

			for (var x = -1; x <= 1; x += 2) {
				var o = getCellFromXY(cx + x, cy);
				if (o != null && isEmptyCell_(partie,o) == CELL_EMPTY) {
					if (deplacement[o] === null){
						caseTest[o] = true;
						deplacement[o] = a;
					}
				}
			}

			for (var y = -1; y <= 1; y += 2) {
				var p = getCellFromXY(cx, cy + y);
				if (p != null && isEmptyCell_(partie, p) == CELL_EMPTY) {
					if (deplacement[p] === null) {
						caseTest[p] = true;
						deplacement[p] = a;
					}
				}
			}
		}
	}
	return @deplacement;
}
	
