AgriSure
 
 1. 💢Problema

¿Te imaginas ver cómo tu trabajo de los últimos meses se pierde en un abrir y cerrar de ojos debido a las inclemencias del clima? Esta es la realidad que enfrentan muchos agricultores en Ecuador, Panamá y República Dominicana. Según el último informe de la FAO sobre  “Repercusiones de las catástrofes en la agricultura y la seguridad alimentaria” (2024), en los últimos 30 años, se han perdido alrededor de 3.8 billones de USD en producción agrícola y ganadera debido a catástrofes, lo que representa el 5% del PIB agrícola mundial anual.

Ante este panorama, muchos gobiernos han impulsado leyes para fomentar los seguros agrícolas. Un seguro agrícola es un acuerdo financiero entre un agricultor y una compañía aseguradora que protege contra pérdidas inesperadas relacionadas con la agricultura. Este seguro funciona de manera similar a un seguro de auto o de vida, pero está diseñado específicamente para cultivos, ganadería e incluso piscicultura. En muchos países, los gobiernos asumen parte del costo del seguro, facilitando su acceso.
A pesar de los beneficios que ofrece esta práctica, países como Panamá, Ecuador y República Dominicana, tienen menos del 1% de las tierras cultivables aseguradas (CITA?). Pero, ¿por qué sucede esto si los seguros agrícolas son tan beneficiosos? Existen tres barreras principales:
Desconocimiento: Muchos productores no están al tanto de la existencia de estos seguros.
Procesos complicados: Aquellos que conocen sobre los seguros agrícolas señalan que los procesos son presenciales y difíciles de acceder, especialmente para los agricultores que viven en áreas remotas.
Costos elevados: Algunos productores han encontrado que los seguros disponibles son costosos y ofrecen poco respaldo para sus cultivos.
 
![Imagen1](https://github.com/user-attachments/assets/38b79971-01e5-410f-8bdb-5d19a6768eab)


2. 💡Idea 

A partir de esta problemática, nuestro equipo se hizo la siguiente pregunta: ¿Cómo podemos aprovechar los datos espaciales y la IA para aumentar la resiliencia agrícola en Ecuador, Panamá y República Dominicana? Nuestra solución debe permitir a los productores acceder a seguros de forma rápida y sencilla, desde la comodidad de sus hogares, y encontrar una opción que realmente valga la pena. 

Imagina que un productor, usando su celular, pueda ver un mapa, marcar la ubicación de su cultivo y seleccionar el tipo de cultivo que tiene. Después de subir esta información básica, recibiría recomendaciones de seguros personalizados según distintos niveles de riesgo. Proponemos AgriSure como una solución insurtech para el sector agrícola, con el objetivo de ayudar a los agricultores a adaptarse y ser más resilientes ante desastres naturales. Para lograrlo, ofrecemos recomendaciones de seguros agrícolas basadas en diferentes escenarios  de riesgo que enfrentan. Además, realizamos un análisis de costos y beneficios fácil de entender, lo que permite a los agricultores determinar cuánto invertir en su seguro agrícola según sus posibles pérdidas, acelerando así el crecimiento del número de tierras aseguradas y brindando un respaldo esencial en caso de pérdidas.

3. 🛰️Solución Utilizando Tecnologías Espaciales de la UE
   
![Imagen2](https://github.com/user-attachments/assets/33aa4951-9ea1-4665-a9ab-1c1f693207b7)


Para obtener el informe simplificado con una recomendación de cual seguro adquirir, el agricultor deberá crear un polígono en el mapa indicando donde está su parcela indicada, indicar el tipo de cultivo. Se extrae la data de COPERNICUS en este espacio delimitado. Específicamente usaremos data de Sentinel-2 para calcular distintos indicadores ambientales:  
Humedad de suelo (NDMI): ayuda a evaluar el estrés hídrico en los cultivos. 
Índice de Vegetación Optimizado (EVI): mayor sensibilidad de la salud de la vegetación en zonas con alta densidad de biomasa. 

Para asegurar tener data satelital siempre disponible, a pesar de la nubosidad durante el día, pretendemos usar CropSAR para completar con Sentinel-1 los huecos de las nubes y asegurar disponibilidad de data diariamente. 

Aparte de esta data, también se utilizará el Modelo de Elevación Digital (DEM) que representa en 3D el terreno del área de estudio, necesaria para analizar riesgos como inundación. También, se utilizarán datos climáticos como temperatura y precipitación diaria, así como vectores de ríos y datos socioeconómicos necesarios para el análisis final.

Esta información alimentará a CLIMADA, una herramienta de código abierto diseñada para evaluar riesgos climáticos. CLIMADA integra datos sobre peligros, exposición y vulnerabilidad para calcular impactos y analizar la eficacia de las medidas de adaptación, generando resultados sobre posibles pérdidas económicas y escenarios de adaptación (CLIMADA, n.d.). 

La herramienta ya proporciona informes globales sobre los principales riesgos climáticos, como huracanes tropicales, inundaciones, sequías y tormentas de invierno, con una resolución espacial de 4 km². Sin embargo, gracias a los datos de Sentinel-2, podremos acceder a imágenes satelitales con una alta resolución espacial de 10 m². Esto nos permitirá ofrecer este servicio a agricultores que posean parcelas de 1 hectárea o más, asegurando que el análisis sea significativo y representativo de la zona.

Además todos los datos extraídos del lugar cultivo serán almacenados en una base de datos que contendrá tanto distintas imágenes satelitales y datos estadísticos del área, que permitirá tener información más concisa de los distintos lugares de cultivo. 

Una vez que CLIMADA genere el informe inicial, este será procesado por un sistema de Recuperación Aumentada Generativa (RAG) que utiliza un modelo de lenguaje (LLM) implementado con HuggingFace y una base de datos vectorial. Esta base de datos contendrá información sobre las coberturas disponibles en las principales aseguradoras de Ecuador, Panamá y República Dominicana. El sistema entregará un informe final claro y fácil de entender, que incluirá los niveles de riesgo, estimaciones de pérdidas económicas potenciales y recomendaciones de seguros ajustadas a cada nivel de riesgo. 



4. 🌠Desafío e Impacto del proyecto

Desafío 1: Asegurar la producción y distribución de alimentos

¿Qué hace a AgriSure diferente? La clave está en los productores. Tan solo en Panamá, Ecuador y República Dominicana, existen más de 3 millones de productores agrícolas. En países como Ecuador, estos representan el 8% del PIB, y en los tres países combinados, la agricultura genera 18.9 mil millones de dólares. Para los pequeños y grandes agricultores, la pérdida de cultivos no solo es un golpe económico devastador, sino que afecta a miles de familias que dependen de esta actividad.

![Imagen3](https://github.com/user-attachments/assets/5d53db69-8c0c-4f88-ae2d-79395ce4e11b)


La FAO destaca que los seguros agrícolas son un instrumento crucial para la gestión de riesgos, asegurando la producción agrícola a niveles que permitan generar ingresos sostenibles para los productores, y mantener flujos de alimentos que garanticen la seguridad alimentaria y contribuyan a la eliminación de la pobreza rural.
Por ello, creemos que AgriSure puede acelerar el acceso a seguros agrícolas, protegiendo no solo los medios de subsistencia de los agricultores, sino también toda una cadena alimentaria que beneficia a millones de personas.

5. 💵Oportunidad de negocios

Pero ¿será un negocio rentable asegurar un sector tan vulnerable como la agricultura? Para AgriSure, el mercado total (TAM) es el de la región de Latinoamérica. En 2023, el mercado de seguros agrícolas en la región alcanzó los 3.27 mil millones de dólares y se prevé que crezca a una tasa compuesta anual de 4.7% (CAGR) en el período 2023-2032.
Antes de hablar del mercado disponible (SAM) y objetivo (SOM) de AgriSure, es importante entender cómo funciona un seguro agrícola. Los agricultores pagan por cada hectárea asegurada, y el valor del seguro depende de varios factores, como el tipo de cultivo y el riesgo asociado al área. Nuestro mercado objetivo incluye los países de donde proviene nuestro equipo: Panamá, Ecuador y República Dominicana. En estos países, el costo del seguro por hectárea varía entre $20 y más de $220, dependiendo de la región y el tipo de cultivo.
En conjunto, estos tres países cuentan con 2,466,000 hectáreas dedicadas a la agricultura. Basándonos en este número, podemos calcular nuestro mercado disponible y objetivo, asumiendo lo siguiente:
  - El costo promedio para asegurar una hectárea es de $60.
  - El mercado objetivo representa el 10% del mercado disponible.

![Imagen4](https://github.com/user-attachments/assets/6f62cc0f-60b2-4d39-b864-9199bb0ad454)


Esto nos lleva a un mercado disponible de 147.96 millones de dólares y un mercado objetivo de 14.79 millones de dólares. Este es un buen punto de partida, ya que en 2023, las primas pagadas en Panamá, Ecuador y República Dominicana sumaron 21.4 millones de dólares. Entre los competidores más grandes de la región, destacamos a MAPFRE, que domina el 60% del mercado de seguros agrícolas en Brasil y tiene presencia en Argentina, Colombia, México y otros países.

![Imagen5](https://github.com/user-attachments/assets/e507102b-7f2d-4e28-820b-6a65d17fad7d)


5.1  💵Modelo de negocios y ventaja competitiva 


Modelo de negocio

Siendo realistas, para ser una aseguradora del tamaño de MAPFRE se necesita un capital considerable. Sin embargo, nuestro objetivo no es convertirnos en una compañía como MAPFRE. El modelo de negocio de AgriSure se basará en actuar como intermediario entre los productores y las grandes aseguradoras. Por cada venta de seguro realizada a través de nuestra plataforma, recibiremos una comisión de la aseguradora correspondiente.

Para explicar con mayor claridad el modelo de negocio de AgriSure, a continuación presentamos un lean canvas:

![Modelo de Negocio](https://github.com/user-attachments/assets/e16f64e6-0d28-44b8-a2bb-b2a417993a26)


Ventaja competitiva 

La ventaja competitiva de AgriSure es la combinación de tecnologías avanzadas (IA y datos satelitales) con la simplificación del acceso a seguros agrícolas personalizados, dirigida a un mercado desatendido en América Latina. Esto permite ofrecer un servicio único y altamente diferenciado frente a los competidores tradicionales, al tiempo que contribuye a mejorar la resiliencia agrícola y la seguridad alimentaria en la región.

Escalabilidad y Expansión 

Otro aspecto clave es la escalabilidad de este proyecto. Al ser un InsurTech, AgriSure puede crecer rápidamente gracias a su base tecnológica, dependiendo del éxito en las ventas. En países como Panamá, donde no existen empresas InsurTech especializadas en seguros agrícolas, tenemos la ventaja de ser los primeros en el mercado. Esto nos posiciona para expandirnos a otros países centroamericanos, donde la agricultura es un motor económico clave. Por ejemplo, entre 2021 y junio de 2022, países como Honduras y Costa Rica experimentaron un crecimiento en primas de seguros agrícolas del 87% y 26%, respectivamente, según Latino Insurance.




6. 🔭AgriSure más allá de esta página

Más allá de esta fase inicial, vemos varias áreas en las que AgriSure puede generar un mayor impacto tanto en la tecnología como en la agricultura y la protección del medio ambiente. 

En la tecnología 
La base de datos que se construya a partir de los datos obtenidos de cada área de cultivo, mediante el programa Copernicus, junto con una adecuada documentación sobre los efectos del clima en cultivos o áreas forestales, puede ofrecerse gratuitamente para fines científicos o gubernamentales, para  facilitar lla creación de soluciones con un mayor alcance social.

 Además, es posible entrenar un modelo multimodal que permita analizar estos datos de manera más eficiente, sin necesidad de escribir tanto código  y utilizando sistemas RAG, como el propuesto en el PMV de este proyecto, este modelo puede impulsar la generación de ideas innovadoras que ayuden a resolver otros problemas.

En los productores y el medio ambiente
A través de este proyecto, que busca ofrecer un acceso fácil a los seguros agrícolas, hemos identificado dos escenarios en los que AgriSure puede marcar la diferencia:

Préstamos para la adaptación al cambio climático: Además de los seguros, creemos que podemos ayudar a los productores a adaptarse a los cambios climáticos que los afectan. A través de consultorías en línea, ofrecemos una guía personalizada sobre cómo afrontar estos cambios, conectándolos con préstamos que se ajusten a sus necesidades y lograr esta adaptación.
Aumento del mercado de carbono mediante la planificación agrícola: Aunque los seguros y préstamos son valiosos para los productores, hay zonas que enfrentan desastres recurrentes o condiciones extremas donde la ayuda es limitada. Sin embargo, proponemos poder convertirlos en reservas privadas e integrarlos al mercado de bonos de carbono. Esto no solo generaría ingresos para los productores, sino que también contribuiría a la recuperación de áreas forestales. Además, es una solución económicamente viable. Según el Banco Mundial, en el informe "State and Trends of Carbon Pricing 2024", los ingresos del mercado de carbono superarán los 100 mil millones de dólares para 2023.

Estas ideas ilustran cómo AgriSure puede ampliar su impacto en problemas que, como ciudadanos, tenemos la capacidad de resolver. No solo queremos que el lector perciba las grandes oportunidades de negocio, sino también los muchos desafíos que aún necesitan soluciones o mayor inversión para llevar a cabo iniciativas como AgriSure.. 

7. 👨‍🚀Equipo👩‍🚀

🤖 Miguel Pineda: ingeniero de machine learning con experiencia en Python, PyTorch, y AutoML. Ha trabajado en análisis de datos, creación de aplicaciones en plataformas low-code, y sistemas de detección en tiempo real con Yolov8.

🌿 Isabela Pichardo Velázquez: especialista en teledetección aplicada al medio ambiente, agricultura y planificación urbana.


🌌 Lizbeth Lara: desarrolladora especializada en Python y simulaciones de nubes de gas y dinámica neuronal. Ha creado interfaces para visualizar datos satelitales usando Arduino y Unity, además de manejar lenguajes como Octave, Matlab y Mathematica.

🌿 Mary Galán: Ecóloga y especialista en Sostenibilidad Ambiental con experiencia en cambio climático, MRV y cálculo de emisiones de GEI.

🌌 Andrés Vinces: especializado en Data Science con enfoque en storytelling y visualización de datos. Desde hace un año, estudia el protocolo ICP en Web3 y tiene experiencia en Python, C++ y Move.
