This is a repository of the projects I worked on or am currently working on. It is updated regularly. Click on the projects to see full analysis and code.

Please contact me on LinkedIn if you are looking to hire a data scientist linkedin.com/in/dooley-kim-809525313

[Model Predicting Pitcher Fatigue in the MLB in Snowflake](https://github.com/my-name-arch/BaseballPipeline)

As an independent project, I engineered an end-to-end project in Snowflake, using dbt and scikit-learn to predict pitcher fatigue in Major League Baseball.

Using 2024 and 2025 MLB pitch data from pybaseball, I used dbt to clean raw metrics and transform them into rolling features before ingesting them into Snowflake with medallion architecture. This dataset was fed into a hyperparameter-tuned scikit-learn LightGBM model that ranked feature importances and outputs real-time fatigue probability scores for coaches and analysts through interactive visualizations in a Streamlit application. To capture physical exhaustion and mechanical breakdown before performance noticeably degrades, the architecture constructs a dual-layer feature set: the first layer tracks trajectory mechanics via continuous rolling deviations from first-inning baselines across velocity, spin efficiency, and release coordinates, while the second models physical stress using pitch counts and pitch-type friction scores. The findings were then presented in a Streamlit application dashboard to allow for interactivity and containerized in Docker. 

The model suggests that most pitchers are being pulled before their break point; however, the results were inconclusive. Working within the parameters of pybaseball, the model achieved a 0.45 precision score for fatigue pitches, encountering several pitch-by-pitch anomalies that public metrics couldn't fully account for. This demonstrates the practical limits of modeling human performance purely through numerical analysis. The data may have been insufficient, but it is more likely that other factors such as human psychology, situational awareness, and unquantifiable components also have a large role in player performance. 

[March Madness: Modeling and Analysis of Postseason Success in R Studio](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/Final%20Paper.pdf)

For my introduction to statistical modeling class, I developed a model to define the key metrics that best forecast a team’s success in March Madness.

Implemented in R Studio using dplyr and ggplot, this project analyzed a decade of NCAA Division I basketball data to evaluate the core variables driving team performance. To objectively compare metrics across different playing styles and conferences, I applied Z-score standardization and executed precise feature engineering, notably creating a custom "Postseason Score" (PST) to weight tournament progress. By leveraging advanced statistical and predictive modeling—including extensive linear regression analysis and conference segmentation—I successfully isolated critical data trends to comprehensively evaluate team success.

The project successfully moved beyond anecdotal coaching cliches to provide a quantifiable basis and data-driven framework for evaluating team potential in high-stakes, single-elimination environments. The analysis demonstrated a causal link between defensive performance—specifically Effective Field Goal Percentage Allowed—and championship-level success, proving that defensive consistency is a superior predictor of March Madness success.

[Real Estate Model](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/AutoMl.pdf)

This is an auto machine learning model I created in my free time, using Microsoft Azure that predicts housing prices across the UK.

The technical workflow was engineered entirely within Microsoft Azure Machine Learning Studio, utilizing 30 years of historical macroeconomic and housing data. I then warehoused data using the Databricks medallion structure.  The process required robust multi-dataset integration to unify disparate economic indicators before conducting advanced regression analysis to generate the final property valuations. I then feature-engineered localized geographic variables alongside temporal economic indicators like inflation, interest rates, and housing supply before training and hyperparameter-tuning an optimized regression model. By engineering this workflow, I directly implemented cloud-based machine learning pipeline structures and automated machine learning (AutoMl) to scale the model's training efficiency. The model achieved an R^2 score exceeding 0.80, demonstrating that the pipeline reliably accounts for over 80% of the variance in historic UK housing prices.

The project successfully built a macro-micro framework for real estate forecasting and investment risk assessment by isolating how geographic factors and broader economic indicators simultaneously drive the UK housing market.  

[Telefonica Seguros: BI Intelligence Dashboard in Power BI](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/RealDATA%20(4).pdf)

To access, click View Raw.

During my internship with a consulting firm in Spain, I engineered an end-to-end Power BI executive dashboard for an insurance client, Telefonica Seguros, transforming half a million raw data points into actionable insights that exposed critical operational inefficiencies.

The project utilizes a database containing five distinct datasets of approximately 100,000 data points each. Because the raw data had significant gaps and formatting inconsistencies, I applied the Microsoft Power BI Data Analyst framework to execute high-volume data wrangling and systematic imputation. With a clean foundation, I conducted Exploratory Data Analysis (EDA) to uncover the underlying trends affecting claim performance and developed targeted KPIs, including a custom "Settled Claims with Indemnization" metric.

The dashboard provided an accessible way to extract actionable insights and expose critical operational inefficiencies. Notably, the final analysis revealed that the Claim Settlement Rate was significantly lower than Telefonica’s target benchmarks, giving leadership a clear roadmap for improvements.


[Audio-to-knowledge-based engine using PyTorch](https://github.com/my-name-arch/PytorchProject)

As an independent project, I developed a Streamlit application that transforms raw audio into an intelligent, fully searchable knowledge base. Built on a PyTorch deep-learning pipeline, the application ingests audio, transcribes it with precise timestamping, and utilizes a dual-stage neural retrieval engine to deliver exact conceptual answers synced directly to media playback. The final application was containerized using Docker.


This Streamlit app turns long-form audio into a searchable transcript using PyTorch, OpenAI Whisper, and hybrid semantic search. The ingestion pipeline converts raw audio into a 16 kHz mono wave array and generates timestamped text via OpenAI Whisper-Small. To handle conversational stumbles, phonetic errors, and the limits of simple keyword search, retrieval relies on a dual-stage ranking pipeline: a sparse lexical retriever with custom phonetic regex, dense BGE-Base-en-v1.5 embeddings combined through Reciprocal Rank Fusion (RRF), and a BGE cross-encoder reranker. The Streamlit interface includes a Search Desk—offering 25-word match summaries synced directly to audio playback—and a Transcript Inspector for reading full chronological scripts. Optimized with Streamlit caching wrappers (st.cache_resource / st.cache_data) and GPU acceleration, the pipeline transcribes and indexes a 63-minute podcast in under 4 minutes. 


