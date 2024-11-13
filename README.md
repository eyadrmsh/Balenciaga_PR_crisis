
# Balenciaga PR Scandal Analysis: Sentiment and Brand Perception

## Overview
This repository analyzes over 2 million tweets from the Balenciaga PR scandal to explore public sentiment shifts and inform crisis management strategies.

## Key Features  
- **Data Collection**: Tweets collected using the **Twitter API** and preprocessed by cleaning, translation, and filtering.  
- **Sentiment Analysis**: Leveraged **VADER** and **Text2Emotion** to classify emotions like anger, sadness, and happiness.  
- **Quantitative Analysis**: Applied **t-tests** and **Regression Discontinuity Design (RDD)** to evaluate PR impact and explore cultural differences.

---

## Repository Structure
- `scarping_tweets.ipynb`: Code for collecting tweets using the Twitter API.
- `translation.py`: Script for translating non-English tweets.
- `merging_translated_parts.py`: Script for merging translated tweet files into a single dataset.
- `process_sentiment.py`: Script for cleaning tweets, analyzing sentiment, and extracting emotions.
- `RDD_data_analysis.ipynb`: Notebook for analyzing sentiment shifts and performing Regression Discontinuity Design (RDD).

---

## Key Findings
- Apologies tend to increase negative emotions like sadness and anger temporarily.
- Discount campaigns improve positive sentiment and surprise in the long term.

---

## Contact
For questions and data, please reach out via [deryadurmush@gmail.com](mailto:deryadurmush@gmail.com).
