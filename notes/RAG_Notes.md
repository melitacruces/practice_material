# LLMs

En el ámbito de la inteligencia artificial y el procesamiento del lenguaje natural, los "LLMs" se refieren a modelos de lenguaje de gran tamaño.

Los modelos de lenguaje son sistemas de inteligencia artificial diseñados para comprender y generar lenguaje humano.

# ChatBots

Los ChatBots utilizan Retrieval-Augmented Generation (RAG), generación de recuperación aumentada

# RAG

[Q&A with RAG](https://python.langchain.com/docs/use_cases/question_answering/)

Es una técnica para mejorar la precisión y confiabilidad de los modelos generativos de inteligencia artificial (LLMs) con datos obtenidos de fuentes externas.

Sirve para darle información al modelo, aumentar su ventana de contexto y que pueda responder preguntas especificas acerca de esos datos o información adicional.

## Secuencia común de los datos sin procesar

### Indexing (indexación):

* **Load:** Cargar los datos con [Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
* **Split:** Utilizar [Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/) para fragmentar los grande documentos, para indexar datos y pasarlos a la ventana finita de un modelo.
* **Store:** Donde se almacenan e indexan las divisiones. Se hacen usando un [VectorStores](https://python.langchain.com/docs/modules/data_connection/vectorstores/) y un modelo de [Embeddings](https://python.langchain.com/docs/modules/data_connection/text_embedding/).

![Indexing](https://python.langchain.com/assets/images/rag_indexing-8160f90a90a33253d0154659cf7d453f.png "Indexing")

### Retrieval and Generation (recuperación  y generación):

* **Retrieve:** Se recuperan las divisiones del almacenamiento gracias a [Retrievers](https://python.langchain.com/docs/modules/data_connection/retrievers/).

* **Generate:** Generación de respuestas gracias a un [ChatModel](https://python.langchain.com/docs/modules/model_io/chat) ([LLM](https://python.langchain.com/docs/modules/model_io/llms/)).

![R&G](https://python.langchain.com/assets/images/rag_retrieval_generation-1046a4668d6bb08786ef73c56d4f228a.png "R&G")

## ¿Cómo se le da contexto al modelo?

Se utilizan Embeddings y VectorStores.

### Embeddings

Representaciones numéricas de datos, especialmente diseñadas para capturar ciertas características o propiedades semánticas de esos datos. Estos son ampliamente utilizados en el procesamiento del lenguaje natural (NLP) y en otras áreas de la inteligencia artificial.

Facilitan el aprendizaje automático (Machine Learning) en entradas grandes, como vectores dispersos que representan palabras.

### VectorStores

En el contexto de la inteligencia artificial, los VectorStores juegan un papel fundamental en el área de la **búsqueda por similitud** y, más específicamente, en el ámbito del procesamiento de **lenguaje natural** (PLN) y el **aprendizaje profundo**. Son, básicamente, **bases de datos especializadas en el almacenamiento y la recuperación de vectores**.

![VectorStores](https://python.langchain.com/assets/images/vector_stores-125d1675d58cfb46ce9054c9019fea72.jpg "VectorStores")