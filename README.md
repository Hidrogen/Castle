Castle
======

Castle 2D top-down game project

Idea principal:
======

Mecanicas de hide and seek con 2 tipos de usuarios en 2D top-down:
	Humanos: 
		Poseen una antorcha inagotable que alumbra un radio a su alrededor.
		Todos lucen igual.
		Mecanismo que les permite detectar enemigos:
			Si es relacionado a distancia entonces seria muy facil, pienso en algo como un item que analize a todo usuario en cierto rango, pero tendria un cooldown.
			Quizas no un item y mas bien una habilidad.
		Mecanismo que les permite escapar:
			"Sprint". Los Humanos son mas velozes lo que les permite quedar fuera de la vision del enemigo rapidamente, pero si se agotan deben descansar un tiempo.
			Cuando estan agotados pueden caminar.
		Mecanismo que les permite esconderse:
			En el mapa generado idealmente aleatorio existen tambien objetos tales como candelabros, cortinas, mesas, sillas, comodas, etc.
			El humano puede acercarse a 1 bloque de estos y presionar una tecla, idealmente "e", por su cercania a las teclas "w,a,s,d" que serian su movimiento.
			"e" esconderia al humano en tal objeto. Al estar escondido el humano desaparece del mapa reemplazando el objeto.
			El humano no puede moverse mientras esta escondido, si lo hace equivale a salir del escondite.
			El humano no puede permanecer escondido para siempre, pero si por un largo tiempo.
			Si el humano agota el tiempo que tiene para permanecer escondido no puede volver a esconderse por un tiempo.
		Misiones y objetivos:
			Estos tienen por objeto incentivar al usuario a explorar el mapa y no buscar un escondite y permanecer en el.
			Las misiones de los humanos se traducen en la busqueda de llaves, las que ultimamente significarian la salida del castillo y la victoria.
			Misiones secundarias que podrian llevar a "boosts" tales como velocidad o vision aumentada deben ser evaluados.
	
	Monstruo:
		Poseen la misma vision sobre el mapa que los humanos.
		lucen igual que los humanos, pero para el jugador tiene un sprite distinto.
		Mecanimo que les permite detectar aliados:
			Indicacion permanente sobre el jugador aliado.
			Indicacion permanente en la pantalla indicando la direccion del jugador aliado si este no se encuentra en la vision.
		Mecanismo que les permite perseguir:
			Los monstruos son notablemente mas lentos al correr, pero su resitencia es mucho mayor.
		Mecanismo que les permite buscar escondites:
			Los monstruos pueden acercarse a objetos de los cuales sospechan hay un humano escondido y examinarlos.
			Si el humano efectivamente se encuentra en el objeto, pierde.
			Metodos para balancear la examinacion de objetos:
				#Deberia ser balanceado porque un jugador monstruo podria examinar todos los objetos de una pieza sin darle un respiro al humano para escapar.
				Dar a la examinacion un tiempo para completarse? lo que podria dar al humano tiempo para recuperar su sprint y salir de la pieza corriendo pero haria 				  virtualmente imposible escaparse, pues el monstruo lo perseguiria convirtiendose en un ciclo
				Limite de examinaciones? que se rellenan con el tiempo o algo por el estilo.
				Ideas requeridas.
		Mecanismo de infeccion?:
			Que sucede cuando un humano muere, se convierte en un monstruo o simplemente deja de jugar? Por temas de balance seria preferible que solo muriera.
		Mecanismo de movimiento por paredes?:
			Como el juego es 2d top-down no hay techo, pero la habilidad para moverse por las paredes podria ampliar la jugabilidad.
			Al presionar una tecla el monstruo se convierte en un fantasma capaz de moverse por las paredes asi acortando caminos, esto duraria 1 segundo o menos.
	Mapa:
		El mapa es un castillo sin fuente de luz propia. Solo los jugadores iluminan el mapa.
		El mapa es un laberinto de varios pasillos y conecciones entre las diferentes habitaciones, las cuales varian respecto al numero de jugadores.
		El mapa debe permitir varias vias de escape y rutas a elegir, incluso se deberia pensar en la posibilidad de plantas bajas y altas.
		El mapa debe tener siempre mas salidas que monstruos, esto evita que el jugador monstruo "campee" junto a una salida.
		Las salidas deben tener una distancia considerable entre ellas, fomentanto al jugador monstruo merodear por el mapa.
		Diferentes llaves obtenidas por los humanos podrian desbloquear pasillos o habitaciones que no son progresan hacia una salida, mas bien funcionan como
		rutas de escape o escondite.
		El diseño del mapa debe permitir que los encuentros entre jugadores no sean frecuentes, incluso cuando se dirijen al mismo lugar.
		El mapa debe tener variados objetos ya mencionados anteriormente y contar con una distribuicion razonable para estos.
		

