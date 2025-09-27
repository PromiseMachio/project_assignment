# 📊 CORD-19 Data Explorer

A simple **Streamlit web app** to explore the **CORD-19 research papers metadata**.
It allows you to filter papers by year, view publication trends, check top journals, and generate a word cloud from paper titles.

---

## 🚀 Features

* Load and cache the CORD-19 dataset (`metadata.csv`).
* Convert `publish_time` to proper datetime and extract publication years.
* Sidebar slider to filter papers by year range.
* Display sample data after filtering.
* Interactive bar charts:

  * Publications by year
  * Top 10 journals
* Word cloud visualization of paper titles.

---

## 📂 Project Structure

```
CORD19-Explorer/
│── app.py          # Streamlit app
│── metadata.csv    # Dataset (not included in repo, download separately)
│── README.md       # Project documentation
```

---

## 🛠️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/CORD19-Explorer.git
   cd CORD19-Explorer
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   **requirements.txt** should include:

   ```
   streamlit
   pandas
   matplotlib
   wordcloud
   ```

4. Place `metadata.csv` in the project root directory.

---

## ▶️ Usage

Run the app locally:

```bash
streamlit run app.py
```

Then open your browser at [http://localhost:8501](http://localhost:8501).

---

## 📸 Screenshots

* **Sidebar filter (Year range)**
* **Bar chart of publications by year**
* **Top 10 journals bar chart**
* **Word cloud of titles**

---

## 📜 License

This project is open-source under the MIT License.
Feel free to use, modify, and share.

---
