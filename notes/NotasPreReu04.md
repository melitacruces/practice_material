https://blog.monsterapi.ai/fine-tune-a-large-language-model-llm-guide-2023/

Cuando se crea inicialmente un LLM, se somete a una capacitación previa, donde aprende de conjuntos de datos vastos y diversos para captar los matices del lenguaje y construir una base sólida para la comprensión general. Sin embargo, esta fase de preentrenamiento no convierte al modelo en un experto en ninguna tarea específica; simplemente lo dota de una amplia comprensión de los patrones del lenguaje.

La necesidad de realizar ajustes surge porque cada aplicación o tarea tiene sus características y requisitos únicos. El amplio conocimiento adquirido durante la formación previa puede no ser suficiente para manejar las complejidades y matices de tareas específicas.

He aquí por qué es tan importante realizar ajustes finos:

Conocimiento de dominio específico: el campo médico tiene su propia terminología y convenciones de lenguaje únicas. Para comprender plenamente la intrincada jerga médica necesaria para un diagnóstico preciso, es imprescindible realizar ajustes.

Comprensión contextual: perfeccionar el LLM con registros de pacientes y literatura médica relevante lo ayuda a contextualizar los síntomas y hacer predicciones más informadas.

Seguridad y ética: el ajuste permite que el chatbot sea más cauteloso al proporcionar diagnósticos y recomendaciones.

Reducción de sesgos: ajustar el LLM en un conjunto de datos médicos diversos y representativos ayuda a mitigar los sesgos y promueve recomendaciones de atención médica justas y equitativas.

En primer lugar, puede ayudar al modelo a aprender a generar respuestas más relevantes para el contexto de la pregunta. Esto se debe a que el fine-tuning permite al modelo ajustar sus parámetros en función de los datos de entrenamiento, que incluyen tanto la pregunta como la respuesta correcta. En segundo lugar, el fine-tuning puede ayudar al modelo a aprender a generar respuestas más completas y coherentes. Esto se debe a que el fine-tuning permite al modelo aprender a identificar las relaciones entre las diferentes partes de la respuesta.

---

- Para modelos no tan grandes la formación previa puede que no sea suficiente para manejar lo complejo de algunas preguntas con respecto a un contenido entregado al moemento de hacer RAG.

- Puede ayudar al modelo a aprender a generar respuestas más relevantes para el contexto de la pregunta.

- Se entrana con una base de datos preguntas y respuestas correctas.

- Esto tmabien puede ayudar al modelo a aprender a generar respuestas más completas y coherentes.

- Esto, debido a que permite al modelo aprender a identificar las relaciones entre las diferentes partes de la pregunta y el contexto.

- Hacking face.


TRABAJO:
- rag vs rag+fine-tuning