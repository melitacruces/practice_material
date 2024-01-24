# 01 PRESENTACIÓN

Buenas tardes a todos los presentes, mi nombre es Luis Melita.
Hoy les compartiré el progreso de mi trabajo y las próximas etapas.

---
# 02 LLM

En primer lugar, para poner en contexto.

En términos simples, los LLM son un tipo de modelo entrenado con gran cantidad de datos, capaz de comprender y generar texto en lenguaje natural mediante redes neuronales. 
---
# 03 SEGURIDAD EN LOS LLM

El trabajo que está realizando el profesor (Pedro Pinacho) se basa principalmente en la seguridad de los LLM.

El trabajo general del equipo tiene cercania con los 10 desafios que plantea OWASP y su ensayo con respecto a la seguridad de los LLM.

En resumen, tienen relación con:

- Generación de contenido malicioso.
- Sesgos en los datos de entrenamiento.
- Privacidad del ususario.
- Generación de texto engañoso.

Mi trabajo debe tomar en cuenta todos estos desafios, pero más en específico evaluar la calidad de las respuestas que los LLM entregan a sus usuarios.
---
# 04 RAG

Una aplicación de los LLM y que el equipo está trabajando es RAG.

RAG o generación aumentada por recuperación, es una técnica que mejorar la calidad de la generación de texto al permitir que los LLM accedan a datos adicionales, aumentando su ventana de contexto.

Esquema simple que explica el funcionamiento de RAG.

**Las distintas etapas para realizarlo es, primero tener una fuente de datos, fragmentarlo en partes más pequeñas y hacer embeddings, esto queire decir respresentar palabras oraciones o parrafos en forma númerica, en un vectores de múltiples dimensiones, los cuales se almacenan, para luego ser recuperados por el por el LLM al hacer una pregunta.**
---
# 05 PROBLEMÁTICA

Parte del equipo se centra en evaluar distintos LLM y la calidad de las respuestas.

El gran problema encontrado es que al hacer RAG con modelos no tan grandes. Recurren en respuestas con no muy buena calidad, información no relevante con respescto al texto y la pregunta, o encuentra información relacionada con la pregunta, pero en otro contexto.
---
# 06 POSIBLES SOLUCIONES

Luego de investigar e informarme de todo lo anterior, mi trabajo es encnontrar una forma de como mejorar la calidad de las respuestas. Respuestas simples al problema son:

- Seleccionar cuidadosamente las fuentes de datos.
- Que la base de datos esté bien organizada y etiquetada.
- Realizar preguntas tan específicas como el LLM lo requiera.

Todo esto suena muy simple, pero puede variar completamente para cada LLM existente. Otras soluciones más prometedoras son:

- Trabajar más a fondo con los embeddings.
- Realizar un fine-tuning al modelo.
---
# 07 EMBEDDINGS

En este apartado se propone manipular ciertos parámetros del programa al momento de hacer embeddings, teniendo presente la cercania de los distintos vectores en la red neuronal, para que al momento de hacer la pregunta y cuando el modelo explore el vectorstore encontraría pocos vectores cercanos, entregandonos una respuesta más específica. Pero quizas con menos contenido, eso se debe evaluar.

---
# 08 FINE-TUNING

Hacer un fine-tuning al modelo, a diferencia de RAG el fine-tuning no le entrega más información al modelo, lo que hace es enseñarle o ajustarlo a responder de cierta manera.

Ahora, para el contexto que se está trabajando, el fine-tuning se podría utilizar para entrenar al modelo en un conjunto de datos de preguntas y respuestas fieles al contenido. Esto podría garantizar que las respuesta se ajusten a lo que realmente le preguntamos.

Ajustar el modelo puede mejorar la capacidad del chatbot/modelo para comprender el contexto de la pregunta, ayudándole a reconocer las diferentes formas en que se pueden formular las preguntas y que nos entregue las respuestas que queremos.