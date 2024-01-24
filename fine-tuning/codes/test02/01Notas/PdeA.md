01 PRESENTACIÓN

Buenas tardes a todos los presentes, mi nombre es Luis Melita.
Hoy les expondré lo que ha sido el avance de mi trabajo y también lo será las próximas semanas.
---
02 LLM

En primer lugar, para poner en contexto.

En palabras simples los LLM son un tipo de modelo de lenguaje que ha sido entrenado con gran cantidad de datos en forma de texto y código, que tiene el objetivo de comprender y generar texto en lenguaje natural.

Los LLM están basado en redes neuronales, estos modelos son capaces de aprender patrones complejos y representaciones semánticas del lenguaje a partir de la información que se les proporciona.
---
03 SEGURIDAD EN LOS LLM

El trabajo que está realizando el profesor (Pedro Pinacho) se basa principalmente en la seguridad de los LLM. Sin duda los LLM son herramientas poderosas, pero también pueden plantear preocupaciones en términos de seguridad y vulnerabilidad.

El trabajo general del equipo tiene cercania con los 10 desafios que plantea OWASP y su ensayo con respecto a la seguridad de los LLM.

En resumen, tienen relación con:

- Generación de contenido malicioso.
- Sesgos en los datos de entrenamiento.
- Privacidad del ususario.
- Generación de texto engañoso.

Mi trabajo debe tomar en cuenta todos estos desafios, pero más en específico la calidad de las respuestas que los LLM entregan a sus usuarios.
---
04 RAG

Una aplicación de los LLM y que el equipo está trabajando es RAG.

RAG o generación aumentada por recuperación, es una técnica que puede mejorar la calidad de la generación de texto al permitir que los LLM accedan a datos adicionales sin necesidad de un nuevo entrenamiento, aumentando su ventana de contexto.

Esquema simple que explica el funcionamiento de RAG.

Lo que se destaca de este método, es cargar documentos de distinto tipo, fragmentarlo en partes más pequeñas y hacer embeddings, esto queire decir respresentar palabras oraciones o parrafos en forma númerica, en un vectores de múltiples dimensiones, los cuales se almacenan, para luego ser recuperados por el por el LLM al hacer una pregunta dado un prompt en específico.
---
05 PROBLEMÁTICA

Parte del equipo se centra en evaluar distintos LLM y la calidad de las respuestas con respecto a distintas preguntas.

El problema encontrado es que al hacer RAG con modelos no tan grandes. Recurren en respuestas con no muy buena calidad, información no relevante con respescto al texto y la pregunta, información de otras fuentes, o encuentra información relacionada con la pregunta, pero en otro contexto.
---
06 POSIBLES SOLUCIONES

Luego de investigar e informarme de todo lo anterior, mi trabajo es encnontrar una forma de como mejorar la calidad de las respuestas. Respuestas simples al problema son:

- Seleccionar cuidadosamente las fuentes de datos.
- Que la base de datos esté bien organizada y etiquetada.
- Y realizar preguntas tan específicas como el LLM lo requiera.

Todo esto suena muy simple, pero puede variar completamente para cada LLM existente. Soluciones propuestas:

- Trabajar más a fondo con los embeddings:
- Realizar un fine-tuning al modelo:
---
07 EMBEDDINGS

En este apartado se propone manipular ciertos parámetros al momento de hacer embeddings, teniendo presente la cercania de los distintos vectores en la red neuronal, al momento de hacer la pregunta cuando el modelo explore el vectorstore encontraría pocos vectores cercanos, entregandonos una respuesta más específica. Pero quizas con menos contenido, eso se debe evaluar.

---
08 FINE-TUNING

Hacer un fine-tuning al modelo, a diferencia de RAG el fine-tuning no le entrega más información al modelo, lo que hace es enseñarle o ajustarlo a responder de cierta manera.
Esto mejora la capacidad del modelo para entender lo que se le pregunta y entrgue respuestas de calidad.