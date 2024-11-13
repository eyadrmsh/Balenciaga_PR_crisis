
# Balenciaga PR Scandal Analysis: Sentiment and Brand Perception

## Overview
This repository contains the code and analysis conducted as part of a university project on the impact of PR activities on brand perception, using the Balenciaga PR scandal as a case study. The project combines exploratory data analysis (EDA), sentiment analysis, and advanced statistical modeling to understand how public sentiment evolves in response to PR strategies.

The study analyzes over **3 million tweets** collected during the scandal, providing insights into the effectiveness of different PR actions and offering recommendations for better crisis management.

---

## Key Features
- **Data Collection and Preprocessing**:
  - Collected tweets using the **Twitter API**.
  - Preprocessed data by cleaning text, translating non-English tweets, and removing irrelevant content.

- **Sentiment Analysis**:
  - Used tools like **VADER** and **Text2Emotion** to classify tweets into emotions such as anger, sadness, surprise, and happiness.
  - Identified sentiment shifts corresponding to key PR events.

- **Quantitative Analysis**:
  - Applied statistical techniques like **t-tests** and **Regression Discontinuity Design (RDD)** to quantify the impact of specific PR actions.
  - Conducted a cross-country analysis to explore cultural nuances in public perception.

---

## Key Findings
- Apologies tend to increase negative emotions like sadness and anger temporarily.
- Discount campaigns improve positive sentiment and surprise in the long term.
- Cultural differences significantly impact public reactions:
  - Audiences in Portugal and France react more emotionally than those in Japan and Thailand.

These findings underscore the importance of tailoring PR strategies to specific cultural contexts and combining apologies with proactive measures like financial incentives.

---

## Skills Demonstrated
- **Python**: For data cleaning, analysis, and visualization.
- **Sentiment Analysis**: Leveraging VADER and Text2Emotion for emotion classification.
- **Statistical Modeling**: Applying RDD and other statistical techniques to quantify event impacts.
- **Data Visualization**: Creating insightful visualizations to support data-driven recommendations.

---

## Repository Structure
- `RDD_data_analysis.ipynb`: Notebook for analyzing sentiment shifts and performing Regression Discontinuity Design (RDD).
- `scarping_tweets.ipynb`: Code for collecting tweets using the Twitter API.
- `translation.py`: Script for translating non-English tweets.
- `process_sentiment.py`: Script for cleaning tweets, analyzing sentiment, and extracting emotions.
- `merging_translated_parts.py`: Script for merging translated tweet files into a single dataset.

---

## Getting Started
### Prerequisites
- Python 3.7+
- Required Python libraries: `pandas`, `numpy`, `tweepy`, `nltk`, `text2emotion`, `statsmodels`, `tqdm`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/balenciaga-pr-analysis.git
   cd balenciaga-pr-analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
1. **Data Collection**:
   - Use `scarping_tweets.ipynb` to collect tweets using the Twitter API.

2. **Translation**:
   - Run `translation.py` to translate non-English tweets.

3. **Sentiment Analysis**:
   - Process and analyze sentiment with `process_sentiment.py`.

4. **Data Analysis**:
   - Use `RDD_data_analysis.ipynb` for statistical modeling and visualization.

5. **Merge Translations**:
   - Combine translated datasets using `merging_translated_parts.py`.

---

## Results
The findings were compiled into a comprehensive report providing practical recommendations for managing PR crises and improving public perception. This analysis highlights the power of data-driven decision-making in addressing real business challenges.

---

## Contact
For questions or feedback, please reach out via [Your Email](mailto:your-email@example.com).
