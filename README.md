# E-Commerce Revenue Collapse and AI-Driven Strategic Analysis

## Executive Summary
This project presents a strategic analysis of a global e-commerce business that experienced a severe 85% revenue decline in early 2025. The objective was to diagnose the root cause of the collapse and identify actionable recovery opportunities. 

The analysis demonstrates that the decline was not driven by pricing, as Average Order Value (AOV) remained stable across markets. Instead, the core issue was a sharp drop in purchase frequency among high-value customers, signaling a critical retention failure. By combining traditional RFM analysis with AI-driven clustering, the project identifies high-value customer groups transitioning into inactivity, with Germany emerging as the most critical risk market.

---

## Data Context
The analysis is conducted on a simulated e-commerce dataset intentionally structured to replicate real-world customer behavior, revenue volatility, and retention dynamics commonly observed in global retail businesses.

---

## Business Problem
Stakeholders observed extreme sales volatility without clear visibility into its cause. The analysis was designed to answer three core business questions:
1. **Is the revenue decline driven by pricing or volume?**
2. **Which markets show the highest retention risk?**
3. **Can advanced analytics uncover hidden churn patterns beyond standard segmentation?**

---

## Key Business Findings

### Revenue Collapse
Revenue dropped simultaneously across all regions starting January 2025, resulting in an overall decline of approximately 85%. The synchronized nature of the drop strongly suggests a systemic operational or technical failure, rather than a localized marketing issue.

### Retention Crisis in Germany
Germany, previously a top-performing market, currently contains the highest number of **At Risk** customers. While acquisition performance was strong historically, repeat purchase behavior deteriorated significantly, indicating a broken retention funnel.

### AI-Driven Insight
Unsupervised machine learning (K-Means clustering) revealed a high-value customer cluster with strong historical spend but increasing inactivity. This behavioral group was not clearly distinguishable through traditional RFM scoring alone, highlighting significant revenue leakage risk.

### Market Stability in the USA
The United States remains the most resilient market, demonstrating stronger customer loyalty and more stable lifetime value dynamics compared to other regions.

---

## Visual Evidence

### 1. Revenue Trend Analysis
Monthly time-series analysis reveals a volatile sawtooth pattern ending in a sharp revenue collapse in Q1 2025, reinforcing the hypothesis of a systemic disruption.
![Revenue Trend](https://github.com/tamari-javakhishvili/ecommerce-revenue-collapse-analysis/blob/main/Total%20Revenue%20By%20Months.png)

### 2. Customer Value Matrix
RFM-based scatter analysis confirms a strong relationship between frequency and monetary value, while also exposing a large concentration of previously high-spending customers now classified as **At Risk**.
![Customer Value Matrix](https://github.com/tamari-javakhishvili/ecommerce-revenue-collapse-analysis/blob/main/Frequency%20vs%20Monetary.png)

### 3. AI-Based Clustering
K-Means clustering segmented customers into four behavioral groups based on Recency, Frequency, and Monetary value. One cluster represents high historical value combined with declining engagement, posing the highest retention risk.
![AI Clusters](https://github.com/tamari-javakhishvili/ecommerce-revenue-collapse-analysis/blob/main/ai_clusters.png)

### 4. Market-Specific Risk Distribution
This visualization highlights why Germany requires immediate attention, showing a disproportionate number of high-value customers transitioning into the "At Risk" category compared to other regions.
![Customer Segmentation By Country](https://github.com/tamari-javakhishvili/ecommerce-revenue-collapse-analysis/blob/main/Customer%20Segmentation%20By%20Country.png)

---

## Strategic Recommendations

* **Germany Reactivation Campaign (Immediate):** Launch targeted win-back campaigns for high-value inactive customers identified through AI clustering. Reactivating these users is significantly more cost-effective than new customer acquisition.
* **Operational Audit (Urgent):** Conduct a detailed investigation into the January 2025 period to identify potential technical, logistical, or data integrity failures responsible for the synchronized revenue drop.
* **Proactive Retention Monitoring (Mid-term):** Transition from static RFM reporting to continuous AI-based churn monitoring to detect early warning signals and prevent future revenue collapse.

---

## Technical Approach

### Data Extraction and Analysis
* **SQL (SQLite):** Used for data extraction, transformation, and complex aggregations.
* **Window Functions:** Applied `NTILE`, `LAG`, and `LEAD` for customer scoring and trend detection.

### Analytics and Machine Learning
* **Python (Pandas, NumPy):** Used for data preparation and feature engineering.
* **Scikit-learn:** Applied for data standardization and **K-Means Clustering** implementation.
* **Matplotlib & Seaborn:** Used for generating business-focused visualizations and the Elbow Method analysis.

---

## About the Author
**Tamar Javakhishvili**
*Commercial Data Strategist | Former Commercial Director (Extra.ge)*

I help businesses identify revenue leakage, retention risks, and operational failures by translating complex data into clear strategic decisions. I combine over 15 years of P&L and commercial leadership experience with advanced data analytics to drive measurable business impact.
