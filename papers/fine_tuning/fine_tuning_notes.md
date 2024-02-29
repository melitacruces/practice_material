# Fine-tuning

En el ámbito del **aprendizaje profundo**, el fine-tuning (ajuste fino) es una técnica de transferencia de aprendizaje que implica tomar un modelo pre-entrenado y adaptarlo a una tarea específica.

El fine-tuning es un paso crucial para mejorar los modelos de lenguajes grandes (LLMs) a través del aprendizaje por transferencia. Implica ajustar los parámetros de un LLM con datos específicos para una tarea, manteniendo su conocimiento de formación original.

![](media\01.png)

## Pasos para hacer fine-tuning:

* **Definir el objetivo del fine-tuning.**

* **Seleccionar un modelo pre-entrenado.** 

* **Preparar los datos:** 
    
    Preparar los datos que se utilizarán para el entrenamiento. Los datos deben estar formateados de acuerdo con las especificaciones del LLM en cuestión. En el caso de los modelos de lenguaje, los datos deben estar **tokenizados** (divididos en unidades más pequeñas, como palabras o frases) y **etiquetados** (asociados con una clase o categoría).

* **Configurar el entrenamiento.**

* **Entrenar el modelo:**
    
    El entrenamiento puede realizarse en una computadora personal o en un servidor. El tiempo de entrenamiento depende del tamaño del modelo, la cantidad de datos y la potencia computacional disponible.

* **Evaluar el modelo.**

## Ecenarios en los que es necesario:

* Transferencia de aprendizaje.

* Disponibilidad limitada de datos.

* Eficiencia de tiempo y recursos.

* Adaptación para tareas específicas.

* Aprendizaje continuo.

* Mitigación de sesgos.

* Seguridad y cumplimiento de datos.

---

>[The Ultimate Guide to LLM Fine Tuning: Best Practices & Tools](https://www.lakera.ai/blog/llm-fine-tuning-guide)

>[Fine-tuning - OpenAI API](https://platform.openai.com/docs/guides/fine-tuning)

>[A guide on how to Finetune Large Language Models (LLMs)](https://blog.monsterapi.ai/fine-tune-a-large-language-model-llm-guide-2023/)