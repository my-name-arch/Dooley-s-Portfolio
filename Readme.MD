This is a repository of the projects I worked on or currently working on. It is updated regularly. The projects are mostly done in R Studio, with a few in Python and Power BI. Click on the projects to see full analysis and code.

Please contact me on [LinkedIn](https://linkedin.com/in/dooley-kim-809525313)

[Telefonica Seguros: BI Intelligence Dashboard](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/RealDATA%20(4).pdf)

To Access Click View Raw.

The Telefonica Seguros BI dashboard transformed raw data into a strategic executive dashboard. The goal was to provide an accessible way to extract actionable insights and find operational inefficiencies. By developing KPIs such as the "Settled Claims with Indemnization" metric and designing custom visualizations, I identified several key areas for improvement. Notably, the Claim Settlement Rate was significantly lower than Telefonica’s target benchmarks.

The analysis was based on a database provided by Telefonica containing five datasets, each with approximately 100,000 data points. The raw data contained significant gaps and formatting inconsistencies; hence, I performed extensive data cleaning and imputation to ensure accuracy. Once the data was cleaned, I conducted Exploratory Data Analysis (EDA) to uncover the underlying trends affecting claim performance. This allowed me to demonstrate strong skills in data cleansing, imputation, dashboard optimization, and Power BI development.

[March Madness: Determinants of Postseason Success](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/Final%20Paper.pdf)

The Determinants of March Madness Success project investigates whether offense or defense is more important when it comes to March Madness success. By analyzing a decade of NCAA Division I basketball data, the project aimed to move beyond anecdotal coaching cliches and provide a quantifiable basis for tournament success. The primary objective was to identify which performance metrics most closely correlate with deep tournament runs, offering stakeholders and analysts a data-driven framework for evaluating team potential in high-stakes, single-elimination environments.

The technical workflow, implemented in R Studio, involved advanced data wrangling with dplyr and the engineering of a "Postseason Score" (PST) to weight tournament progress. The methodology focused on standardizing statistics through Z-score normalization, allowing for objective comparisons across different team styles and eras. Using linear regression modeling and conference segmentation, the analysis successfully demonstrated a causal link between defensive performance—specifically Effective Field Goal Percentage Allowed—and championship-level success, proving that defensive consistency is a superior predictor of March Madness Success. Through this project, I strengthened my expertise in linear regression modeling, Z-score normalization, feature engineering, and advanced data manipulation.

[Music Suggestion Application](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/MusicRecs-Pipeline-Final.Rmd)
View the demo video: [Demo Video](https://drive.google.com/file/d/1-XFW0a-M3kWb344YoHAHhmhxqID5gpMD/view?usp=sharing)

This Music Suggestion algorithm is an interactive application that recommends songs based on a specific input. The project’s primary objective is to identify the most similar tracks, allowing users to discover new music effortlessly. By utilizing a Shiny app, I’ve transformed these recommendations into a dynamic and interactive user experience.

Developed in RStudio, the technical workflow began with comprehensive data wrangling to eliminate duplicates and perform one-hot encoding on genre categories. I implemented a k-Nearest Neighbors (KNN) machine learning algorithm to generate recommendations. This approach was chosen because KNN effectively identifies clusters of similar items within the dataset based on feature proximity. This pipeline successfully demonstrates my skills in machine learning clustering algorithms, application pipeline architecture, and front-end R Shiny design.

[Real Estate Model](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/AutoMl.pdf)

4 Parts in Workflows: Building Dataset, Cleaning, AutoMl, Testing.

The UK Real Estate Modeling project leverages cloud-based machine learning to forecast property valuation trends using 30 years of historical macroeconomic and housing data. The primary objective was to isolate how geographic factors and broader economic indicators—such as inflation, interest rates, and housing supply—simultaneously drive the UK housing market. By integrating disparate datasets, the project provides a macro-micro framework for real estate forecasting and investment risk assessment.

The technical workflow was engineered entirely within Microsoft Azure Machine Learning Studio. I ingested and blended longitudinal datasets from the Office for National Statistics (ONS), the Bank of England, and the UK Government, managing significant structural variance across the data sources. After feature engineering localized geographic variables and temporal economic indicators, I trained and hyperparameter-tuned an optimized regression model. The final model achieved an $R^2$ score exceeding 0.80, demonstrating that the pipeline successfully accounts for over 80% of the variance in historic English housing prices. This process built heavy skills in cloud-based automated machine learning (AutoML), complex multi-dataset integration, and model hyperparameter optimization.

sources

[UK Housing](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads)

[GDP Growth](https://www.ons.gov.uk/economy/grossdomesticproductgdp/timeseries/ihyq/pn2)

[Bank Rate](https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp)

[CPI](https://www.ons.gov.uk/economy/inflationandpriceindices/datasets/consumerpriceinflation)

[Housing Supply](https://www.gov.uk/government/statistical-data-sets/live-tables-on-house-building) Table 251 A



[Python Minesweeper: GUI & Logic Engine](https://github.com/my-name-arch/Dooley-s-Portfolio/blob/main/.github/workflows/FinalProject.py)

The Python Minesweeper project is an interactive application that translates classic logic-puzzle mechanics into a functional desktop game. The primary objective was to create the fun and very common computer game, Minesweeper. By implementing automated mine generation and a neighbor-check algorithm, the project successfully provides a seamless and engaging user experience.

The technical architecture utilizes multiple python files, leveraging Tkinter for the graphical interface and Canvas for grid rendering. I developed a event-handling system to manage mouse clicks, using coordinate mapping to link visual squares to an underlying logic array. The game features a randomized mine generator and logic that calculates nearby threats in real-time. This project directly developed and demonstrated my skills in Object-Oriented Programming (OOP), coordinate mapping logic, event-driven architecture, and Python GUI development.
