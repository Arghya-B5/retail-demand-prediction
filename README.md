# retail-demand-prediction
Retail Sales Promotions and Demand Prediction using EDA, data preprocessing, and Machine Learning. Analyzes promotional impact and sales trends to predict future demand and support data-driven retail decisions.

## Exploratory Data Analysis (EDA)

The dataset was analyzed to understand the factors affecting retail demand (`units_sold`).

### EDA Performed
- Checked dataset shape, data types, and statistical summary.
- Handled missing values and duplicate records.
- Converted date-related information into useful features.
- Removed `product_id` as it was not required for the current analysis.
- Analyzed the relationship between price and units sold.
- Analyzed the impact of promotions and discount percentages on demand.
- Studied inventory levels and their relationship with units sold.
- Analyzed demand across different categories, stores, and days of the week.
- Checked correlations between numerical features and `units_sold`.
- Used visualizations to identify trends, distributions, relationships, and potential outliers.

### Target Variable

`units_sold` is used as the target variable because it represents the demand that the ML model will predict.

### Key Features

The main features considered for demand prediction are:

- `store_id`
- `category`
- `price`
- `promotion_active`
- `discount_percent`
- `inventory_level`
- `day_of_week`
- `month`
- `day`
- `week_of_year`

The cleaned dataset was saved for the next stage of preprocessing and machine learning model development.