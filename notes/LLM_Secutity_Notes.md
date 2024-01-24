# LLMs

En el ámbito de la inteligencia artificial y el procesamiento del lenguaje natural, los "LLMs" se refieren a modelos de lenguaje de gran tamaño.

Los modelos de lenguaje son sistemas de inteligencia artificial diseñados para comprender y generar lenguaje humano.

## Vulnerabilidades más críticas que se ven a menudo en aplicaciones LLM

Destacando su Impacto potencial, factibilidad de explotación y revalencia en aplicaciones del mundo real.

### Ejemplos de vulnerabilidades:

* Inyecciones rápidas.
* Fuga de datos.
* Zona de pruebas inadecuadas-
* Ejecución de código no autorizado.

El objetivo es crear conciencia sobre estas vulnerabilidades, sugerir estrategias de solución y, en última instancia, mejorar la postura de seguridad de las aplicaciones LLM.

## Ataques Spear Phishing Utilizando LLMs

El spear phishing es una forma de ataque cibernético que utiliza correos electrónicos personalizados y engañosos para robar información confidencial. El spear phishing se enfoca en objetivos específicos, como empleados de una organización, clientes de un banco o figuras públicas.

Actualmente los grandes modelos de lenguaje (LLMs) pueden asistir en tareas como el reconocimiento y la generación de texto, gracias a esto se pueden automatizar procesos del desarrollo del ataque antes mencionado, donde ya teniendo el material a usar se le puede dar contexto al modelo y que este genere los correos de ataque, siendo **completamente personalizados para el objetivo**.

## Jailbreaks a LLMs

La vulnerabilidad se basa en la capacidad de los modelos de lenguaje generativos para aprender de los datos en los que se han entrenado. Esto significa que si un atacante puede proporcionar al modelo un conjunto de datos específico, el modelo puede aprender a generar texto que contiene información de ese conjunto de datos.

**En el artículo, los investigadores de seguridad demuestran cómo se puede utilizar esta vulnerabilidad para:**

* **Robar datos de entrenamiento:** Los atacantes pueden proporcionar al modelo un conjunto de datos que contenga información confidencial, como números de tarjetas de crédito o datos de salud. El modelo luego puede aprender a generar texto que contiene esta información.
* **Ejecutar código remoto:** Los atacantes pueden proporcionar al modelo un conjunto de datos que contenga código malicioso. El modelo luego puede aprender a generar texto que ejecuta este código malicioso en el sistema del usuario.
* **Manipular la información del usuario:** Los atacantes pueden proporcionar al modelo un conjunto de datos que contenga información falsa o engañosa. El modelo luego puede aprender a generar texto que contenga esta información, lo que podría usarse para engañar a los usuarios.

**Para mitigar esta vulnerabilidad, los investigadores recomiendan que los desarrolladores de modelos de lenguaje generativos tomen las siguientes medidas:**

* **Utilizar conjuntos de datos de entrenamiento seguros:** Los desarrolladores deben asegurarse de que los conjuntos de datos de entrenamiento no contengan información confidencial.
* **Implementar mecanismos de detección de ataques:** Los desarrolladores deben implementar mecanismos para detectar y bloquear ataques que utilicen esta vulnerabilidad.

# Counterfit

[Counterfit](https://www.microsoft.com/en-us/security/blog/2021/05/03/ai-security-risk-assessment-using-counterfit/)