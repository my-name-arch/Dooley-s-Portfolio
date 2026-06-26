This is a repository of the projects I worked on or currently working on. It is updated regularly. The projects are mostly done in R Studio, with a few in Python and Power BI. Click on the projects to see full analysis and code.

Please contact me on [LinkedIn](https://linkedin.com/in/dooley-kim-809525313)



[Telefonica Seguros: BI Intelligence Dashboard](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/RealDATA%20(4).pdf)

To access, click View Raw.

The dashboard was based on a database provided by Telefonica containing five datasets, each with approximately 100,000 data points. The raw data contained significant gaps and formatting inconsistencies; hence, I performed extensive data cleaning and imputation to ensure accuracy. Once the data was cleaned, I conducted Exploratory Data Analysis (EDA) to uncover the underlying trends affecting claim performance, developed KPIs such as the "Settled Claims with Indemnization" metric, and designed custom visualizations.

The Telefonica Seguros BI dashboard successfully transformed this raw data into a strategic executive dashboard. The implementation provided an accessible way to extract actionable insights and expose critical operational inefficiencies. Notably, the final analysis revealed that the Claim Settlement Rate was significantly lower than Telefonica’s target benchmarks, giving leadership a clear roadmap for improvements. 

To build this dashboard, I applied core data competencies by executing high-volume data wrangling and systematic data transformation to synthesize the messy raw metrics. Through extensive exploratory data analysis (EDA), I uncovered the critical operational variables needed to drive effective KPI development and strategic dashboard creation. This entire lifecycle allowed me to directly leverage my formal training within the Microsoft Power BI Data Analyst framework to deliver professional-grade dashboard optimization.

[March Madness: Determinants of Postseason Success](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/Final%20Paper.pdf)

The project, implemented in R Studio, involved advanced data wrangling with ggplot and dplyr, and the engineering of a "Postseason Score" (PST) to weight tournament progress. The methodology focused on analyzing a decade of NCAA Division I basketball data and standardizing statistics through Z-score normalization. This approach allowed for objective comparisons across different team styles and eras before building linear regression models and conducting conference segmentation.

The project successfully moved beyond anecdotal coaching cliches to provide a quantifiable basis and data-driven framework for evaluating team potential in high-stakes, single-elimination environments. The analysis demonstrated a causal link between defensive performance—specifically Effective Field Goal Percentage Allowed—and championship-level success, proving that defensive consistency is a superior predictor of March Madness Success.

To execute this research, I applied advanced statistical modeling and predictive modeling techniques to evaluate the core variables driving team performance. By leveraging R and ggplot, I performed extensive regression analysis alongside precise feature engineering, which allowed me to isolate critical data trends. Additionally, implementing Z-score standardization proved essential for normalizing the data, ensuring that all metrics could be objectively scaled and compared across different eras and playing styles.

[Music Suggestion Application](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/MusicRecs-Pipeline-Final.Rmd)
View the demo video: [Demo Video](https://drive.google.com/file/d/1-XFW0a-M3kWb344YoHAHhmhxqID5gpMD/view?usp=sharing)

Developed in RStudio, the technical workflow began with comprehensive data wrangling to eliminate duplicates and perform one-hot encoding on categorical genre variables. I then implemented a k-Nearest Neighbors (KNN) machine learning algorithm to generate recommendations. This approach was specifically chosen because KNN effectively identifies clusters of similar items within the dataset based on feature proximity.

By utilizing a Shiny app, I transformed these algorithmic recommendations into a dynamic and interactive user experience. The resulting music suggestion application successfully identifies the most similar tracks based on a specific user input, allowing music fans to discover new content effortlessly through a responsive web interface.

This project allowed me to deploy an end-to-end machine learning data pipeline that integrated categorical data encoding with clustering algorithms to generate real-time user recommendations. By constructing an interactive data visualization interface, I translated complex algorithmic outputs into a highly intuitive user experience. Ultimately, this application serves as a strong reflection of my technical development in R, uniquely merging my academic background in music with practical data science application.


[Real Estate Model](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/AutoMl.pdf)

4 Parts in Workflows: Building Dataset, Cleaning, AutoMl, Testing.

The technical workflow was engineered entirely within Microsoft Azure Machine Learning Studio, utilizing 30 years of historical macroeconomic and housing data. I ingested and blended longitudinal datasets from the Office for National Statistics (ONS), the Bank of England, and the UK Government, managing significant structural variance across the data sources. I then feature-engineered localized geographic variables alongside temporal economic indicators like inflation, interest rates, and housing supply before training and hyperparameter-tuning an optimized regression model.

The project successfully built a powerful macro-micro framework for real estate forecasting and investment risk assessment by isolating how geographic factors and broader economic indicators simultaneously drive the UK housing market. The final model achieved an $R^2$ score exceeding 0.80, demonstrating that the pipeline reliably accounts for over 80% of the variance in historic English housing prices.

By engineering this workflow, I directly implemented cloud-based machine learning pipeline structures and automated machine learning (AutoML) to scale the model's training efficiency. The process required robust multi-dataset integration to unify disparate economic indicators before conducting advanced regression analysis to generate the final property valuations. Developing this architecture allowed me to put my professional training into practice, directly aligning with the core competencies tested in the Microsoft DP-100 certification for Azure ML Studio.
sources

[UK Housing](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads)

[GDP Growth](https://www.ons.gov.uk/economy/grossdomesticproductgdp/timeseries/ihyq/pn2)

[Bank Rate](https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp)

[CPI](https://www.ons.gov.uk/economy/inflationandpriceindices/datasets/consumerpriceinflation)

[Housing Supply](https://www.gov.uk/government/statistical-data-sets/live-tables-on-house-building) Table 251 A



[Python Minesweeper: GUI & Logic Engine](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/FinalProject.py)

The technical architecture utilizes multiple Python files, leveraging Tkinter for the graphical interface and Canvas for grid rendering. I developed a custom event-handling system to manage mouse clicks, using coordinate mapping to link visual squares directly to an underlying multi-dimensional logic array. Additionally, I programmed a randomized mine generator and a mathematical neighbor-check algorithm to calculate nearby threats in real time.

The project successfully translated classical logic puzzle mechanics into a functional, lightweight desktop game. By seamlessly connecting the visual front-end grid to the back-end computation engine, the application provides an engaging and responsive user experience that handles complex cascading game logic with zero operational lag.

Building this desktop game required applying strict Object-Oriented Programming (OOP) principles to cleanly separate the visual frontend interface from the backend engine. I engineered an event-driven architecture to handle real-time user input seamlessly, mapping those interactions directly to multi-dimensional array logic that computed state changes on the fly. This project allowed me to gain strong, practical experience with desktop interface rendering using Python, Tkinter, and Canvas.

