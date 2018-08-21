include("modele");
include("global");


//TODO:

function alphabeta(@racine, alpha, beta) {
	return alphabetaV2(racine, alpha, beta);
}


function alphabetaV1(@racine, alpha, beta) {
	//version amélioré de Minmax (coupe les branche qui sont "mauvaise" => gain de performance)
	if(racine["fils"] == []) {
		return getUtilite(racine["partie"]);
	} else {
		var v;
		if(racine["type"] == "min") {
			v = _MAX_INT;
			for (var fils in racine["fils"]) {
				v = min(v, alphabeta(fils, alpha, beta));
				if(alpha >= v)  return v; /*coupure alpha*/
				beta = min(beta, v);
			}
		} else {
			v = _MIN_INT;
			for (var fils in racine["fils"]) {
				v = min(v, alphabeta(fils, alpha, beta));
				if(v >= beta)  return v; /*coupure beta*/
				alpha = max(alpha, v);
				
			}
		}
		return v;
	}
}



function alphabetaV2(@racine, alpha, beta) {
	//version amélioré de Minmax (coupe les branche qui sont "mauvaise" => gain de performance)
	// V2 => retient le meilleur chemin (et donc le meilleur fils)
	if(racine["fils"] == []) {
		return getUtilite(racine["partie"]);
	} else {
		var filsVal;
		if(racine["type"] == "min") {
			for (var fils in racine["fils"]) {
				filsVal = alphabeta(fils, alpha, beta);
                if (beta > filsVal) {
                    beta = filsVal;
                    racine["bestFils"] = @fils;
                }
                if (beta <= alpha) break;
            }
            return beta;
		} else {
			for (var fils in racine["fils"]) {
				filsVal = alphabeta(fils, alpha, beta);
                if(alpha < filsVal) {
                    alpha = filsVal;
                     racine["bestFils"] = @fils;
                }
                if (beta <= alpha) break;
			}
			return alpha;
		}
	}
}



function getUtilite(@partie) {
	//retourne une estimation de la situation de la partie
	var statut = getStatut(partie);
	if(statut == "VICTORY") return _MAX_INT;
	if(statut == "DEFEAT") return _MIN_INT;
	if(statut == "DRAW") return 0;
	if(statut == "PENDING") {
		//TODO: retouner une valeur en prennant en compte les variables de partie
		var val = 0;
		return  val;
	}
	
	
	return 0;
}

