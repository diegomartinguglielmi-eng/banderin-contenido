# Guía para alimentar @banderin.app

Esta guía la sigue Claude cada viernes para preparar la tanda de la semana siguiente.

## Qué es Banderín
- Banderín hace la app de cada club de fútbol infantil y futsal: una app propia, con el nombre, el escudo y los colores del club.
- No es una app genérica con selector de clubes. Cada app lleva la firma "hecha con Banderín".
- Funciones principales:
  - Inicio con lo del hijo primero.
  - Convocatorias que arma y envía el profe desde su plantel; las familias responden Va o No puede.
  - Alerta al profe si confirmó menos del 75%, con un botón para recordar a las familias.
  - La previa del partido: cómo salió en el Apertura, la posición del rival y sus últimos 3 resultados.
  - Tabla y fixture. Integración multiliga: con FEFI, AFA Futsal, LaAmba y Argenliga, entre otras, se actualizan solos; si la liga todavía no está integrada, el club los carga desde su panel.
  - Mensajes y comunicados del club; avisos de entrenamiento suspendido o modificado.
  - Tablero para la comisión: qué categorías convocaron y cuántas familias usan la app.
  - Se instala en el celular sin pasar por las tiendas de apps (PWA).
- Demos: dos clubes inventados, Mi Ombú (verde, solo FEFI) y Mi Jacarandá (violeta, FEFI y futsal AFA). Están en apps-clubes-demo.netlify.app.
- Público: comisiones directivas, coordinadores y profes de clubes de barrio. También padres que colaboran con el club.
- Objetivo de la cuenta: que un club escriba por mensaje directo para pedir una demo con su escudo.

## Perfil
- Bio vigente:
  La app de tu club de fútbol infantil y futsal ⚽
  Convocatorias, fixture y avisos, con tu escudo
  👇 Probá la demo o pedí la de tu club
- Enlace: apps-clubes-demo.netlify.app (web de Banderín con las demos).
- Historias destacadas: Qué es · Familias · Profes · Comisión · Tus datos (tapas en destacadas/).
- Hablar de "integración multiliga" y nombrar FEFI, AFA Futsal, LaAmba y Argenliga "entre otras". No prometer que todas las ligas ya están integradas.

## Reglas
- Castellano rioplatense (vos, "escribinos", "probá"). Nunca inglés.
- Tono cercano, de club de barrio. Frases cortas. Algún emoji al principio de una línea, sin abusar.
- No mostrar chicos reales, ni nombres reales de jugadores o de clubes. Solo los clubes de ejemplo.
- No inventar clientes, cifras ni testimonios. No prometer precios ni plazos.
- Las ligas se pueden nombrar en publicaciones orgánicas, siempre las cuatro juntas y con "entre otras", para no dar a entender que la app es para una sola liga.
- Cada publicación cierra con una acción: "Probá la demo: link en la bio" o "Escribinos por mensaje directo".
- Hashtags al final, siempre los mismos: #babyfutbol #futbolinfantil #futsal #clubesdebarrio #clubdebarrio #FEFI #futsalAFA #LaAmba #Argenliga

## Formato de cada tanda
- 3 publicaciones por semana: lunes, miércoles y viernes a las 19:00 (hora de Buenos Aires).
- Variar los formatos en la semana: un carrusel de 3 a 5 láminas, un post de una lámina y un post de frase o pregunta.
  - Los reels requieren video, así que no se hacen en las tandas automáticas.
- Imágenes de 1080x1350, hechas con `herramientas/plantillas.py` (feature, portada, frase y render) y las capturas de `herramientas/capturas/`.
- Carpeta por semana: `tanda-NN/`, con archivos `1-...png`, `2-...png` y `3-...png`, más `textos.md` con el texto de cada publicación.
- Rotar los temas: dolor (WhatsApp, planillas, lluvia), función de la app, para profes, para la comisión, la previa, el escudo propio, preguntas a la comunidad, fechas especiales (fin de temporada, inscripciones, Día del Niño, vacaciones).
- Antes de elegir los temas, leer `calendario.md` y no repetir un tema de las últimas 4 semanas.

## Carga en Metricool
- Marca 7428296, red instagram, zona horaria America/Buenos_Aires.
- Siempre `draft: true` (borrador) y `autoPublish: true`. Diego aprueba cada borrador y recién ahí sale.
- `isAiGenerated: false` (son diseños con capturas reales de la demo).
- Imágenes desde https://raw.githubusercontent.com/diegomartinguglielmi-eng/banderin-contenido/main/tanda-NN/<archivo>
