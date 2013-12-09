Castle
======

Castle 2D top-down game project

### Idea principal: ###


<b>Mecanicas de hide and seek con 2 tipos de usuarios en 2D top-down:</b>

<b>Humanos: </b>
<ul>
	<li>Poseen una antorcha inagotable que alumbra un radio a su alrededor.</li>
	<li>Todos lucen igual.</li>
	
	<li>Mecanismo que les permite detectar enemigos:</li>
	<ul>
		<li>Si es relacionado a distancia entonces seria muy facil, pienso en algo como un item que analize a todo usuario en cierto rango, pero tendria un cooldown.</li>
		<li>Quizas no un item y mas bien una habilidad.</li>
	</ul>
	
	<li>Mecanismo que les permite escapar:</li>
	<ul>
		<li>"Sprint". Los Humanos son mas velozes lo que les permite quedar fuera de la vision del enemigo rapidamente, pero si se agotan deben descansar un tiempo.</li>
		<li>Cuando estan agotados pueden caminar.</li>
	</ul>
	
	<li>Mecanismo que les permite esconderse:</li>
	<ul>
		<li>En el mapa generado idealmente aleatorio existen tambien objetos tales como candelabros, cortinas, mesas, sillas, comodas, etc.</li>
		<li>El humano puede acercarse a 1 bloque de estos y presionar una tecla, idealmente "e", por su cercania a las teclas "w,a,s,d" que serian su movimiento.</li>
				"e" esconderia al humano en tal objeto. Al estar escondido el humano desaparece del mapa reemplazando el objeto.</li>
		<li>El humano no puede moverse mientras esta escondido, si lo hace equivale a salir del escondite.</li>
		<li>El humano no puede permanecer escondido para siempre, pero si por un largo tiempo.</li>
		<li>Si el humano agota el tiempo que tiene para permanecer escondido no puede volver a esconderse por un tiempo.</li>
	</ul>
	<li>Misiones y objetivos:</li>
	<ul>
		<li>Estos tienen por objeto incentivar al usuario a explorar el mapa y no buscar un escondite y permanecer en el.</li>
		<li>Las misiones de los humanos se traducen en la busqueda de llaves, las que ultimamente significarian la salida del castillo y la victoria.</li>
		<li>Misiones secundarias que podrian llevar a "boosts" tales como velocidad o vision aumentada deben ser evaluados.</li>
	</ul>
</ul>
<b>Monstruo: </b>
<ul>
	<li>Poseen la misma vision sobre el mapa que los humanos.</li>
	<li>lucen igual que los humanos, pero para el jugador tiene un sprite distinto.</li>
	
	<li>Mecanimo que les permite detectar aliados:
	<ul>
		<li>Indicacion permanente sobre el jugador aliado.</li>
		<li>Indicacion permanente en la pantalla indicando la direccion del jugador aliado si este no se encuentra en la vision.</li>
	</ul>
	
	<li>Mecanismo que les permite perseguir:</li>
	<ul>
		<li>Los monstruos son notablemente mas lentos al correr, pero su resitencia es mucho mayor.</li>
	</ul>
	
	<li>Mecanismo que les permite buscar escondites:</li>
	<ul>	
		<li>Los monstruos pueden acercarse a objetos de los cuales sospechan hay un humano escondido y examinarlos.</li>
		<li>Si el humano efectivamente se encuentra en el objeto, pierde.</li>
	</ul>
	<li>Metodos para balancear la examinacion de objetos:</li>
	<ul>
			<li>#Deberia ser balanceado porque un jugador monstruo podria examinar todos los objetos de una pieza sin darle un respiro al humano para escapar.</li>
			<li>Dar a la examinacion un tiempo para completarse? lo que podria dar al humano tiempo para recuperar su sprint y salir de la pieza corriendo pero haria virtualmente imposible escaparse, pues el monstruo lo perseguiria convirtiendose en un ciclo</li>
			<li>Limite de examinaciones? que se rellenan con el tiempo o algo por el estilo.</li>
			<li>Ideas requeridas.</li>
	</ul>
	
	<li>Mecanismo de infeccion?:</li>
	<ul>
		<li>Que sucede cuando un humano muere, se convierte en un monstruo o simplemente deja de jugar? Por temas de balance seria preferible que solo muriera.</li>
	</ul>
	
	<li>Mecanismo de movimiento por paredes?:</li>
	<ul>
		<li>Como el juego es 2d top-down no hay techo, pero la habilidad para moverse por las paredes podria ampliar la jugabilidad.</li>
		<li>Al presionar una tecla el monstruo se convierte en un fantasma capaz de moverse por las paredes asi acortando caminos, esto duraria 1 segundo o menos.</li>
	</ul>
</ul>
<b>Mapa: </b>
<ul>
	<li>El mapa es un castillo sin fuente de luz propia. Solo los jugadores iluminan el mapa.</li>
	<li>El mapa es un laberinto de varios pasillos y conecciones entre las diferentes habitaciones, las cuales varian respecto al numero de jugadores.</li>
	<li>El mapa debe permitir varias vias de escape y rutas a elegir, incluso se deberia pensar en la posibilidad de plantas bajas y altas.</li>
	<li>El mapa debe tener siempre mas salidas que monstruos, esto evita que el jugador monstruo "campee" junto a una salida.</li>
	<li>Las salidas deben tener una distancia considerable entre ellas, fomentanto al jugador monstruo merodear por el mapa.</li>
	<li>Diferentes llaves obtenidas por los humanos podrian desbloquear pasillos o habitaciones que no son progresan hacia una salida, mas bien funcionan como</li>
	<li>rutas de escape o escondite.</li>
	<li>El diseño del mapa debe permitir que los encuentros entre jugadores no sean frecuentes, incluso cuando se dirijen al mismo lugar.</li>
	<li>El mapa debe tener variados objetos ya mencionados anteriormente y contar con una distribuicion razonable para estos.</li>
</ul>
