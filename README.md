Multi-Source Web Scraping & Market Analysis Hub

This repository showcases a collection of end-to-end data projects where raw web data is transformed into structured datasets and actionable analysis.

The goal is simple:
👉 Convert messy, real-world web data into meaningful insights using data engineering and analysis.

📂 Project Overview
📱 Smartprix — Smartphone Market Analysis (2025–26)
Source: Smartprix
Data Size: 1000+ devices

Highlights:

Scraped latest and upcoming flagships (e.g., Samsung Galaxy S25 Ultra, Snapdragon 8s Gen 4)
Developed a Value-for-Money (VFM) Index using Z-score normalization
Cleaned complex fields (camera specs, battery, charging)
Performed EDA on price vs performance and charging trends

My Dataset Link: 🔗 https://www.kaggle.com/datasets/showmik121/smartphones-dataset-2026-1000-devices


👟 Cartup — Sneaker Trends & Pricing
Source: Cartup
Highlights:

Extracted product names, brands, and discounted prices
Analyzed price distribution and brand-wise inventory
Handled inconsistent naming and missing price data

🎒 AJIO — Backpacks & Accessories Analysis
Source: AJIO
Highlights:

Scraped dynamic product listings (brand, description, discounts)
Analyzed pricing strategies and popular price segments
Automated pagination for large-scale data extraction
🛠️ Technologies Used
Web Scraping: Python, Selenium, BeautifulSoup
Data Processing: Pandas, NumPy
Visualization: Plotly, Seaborn, Matplotlib
Automation: Request handling, rate limiting, user-agent rotation

📈 Workflow

1. Data Extraction

Built custom scrapers for static & dynamic websites
Handled pagination and dynamic content loading

2. Data Cleaning

Removed duplicates and handled missing values
Standardized units (e.g., “8 GB RAM” → 8.0)
Detected and handled outliers

3. Analysis (EDA)

Identified trends and correlations
Compared brand performance and pricing strategies

🚀 How to Run
# Clone the repository
git clone https://github.com/showmik121/web-scraping.git

# Install dependencies
pip install -r requirements.txt

📊 Explore the Work

Navigate to the notebooks/ folder to view detailed EDA and analysis for each dataset.

🎯 Key Takeaway

Data cleaning is essential, but feature engineering is what creates real value from data.

⭐ If you find this useful

Feel free to star the repo and share your feedback!

📬 Connect with Me
If you find this data useful, feel free to give the repository a ⭐ and check out my work on other platforms:
LinkedIn: https://www.linkedin.com/in/ahanaf-adil-showmik-244146252?utm_source=share_via&utm_content=profile&utm_medium=member_android
