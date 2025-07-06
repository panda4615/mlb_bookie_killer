
# ⚾ MLB Bookie Killer - Clean Modular Pipeline

A **modular, scalable, and frustration-free workflow** for daily MLB props and totals betting using your prediction pipeline on Deepnote.

---

## 📂 Project Structure

- `bot/` - Contains your modular pipeline scripts (feature_engineering, schedule, bankroll, telegram, etc.).
- `data/` - Stores cached parquet feature files and picks JSON.
- `models/` - Stores trained ML models.
- `notebooks/` - Modular pipeline:
  - `01_data_ingestion.ipynb` - Fetches and caches daily MLB schedule & odds.
  - `02_feature_engineering.ipynb` - Engineers features and caches them.
  - `03_model_training.ipynb` - Trains model, saves to `models/`.
  - `04_pipeline_execution.ipynb` - Generates picks, bankroll sizing, saves JSON, shows mock Telegram alerts.
  - `05_recap_and_healthcheck.ipynb` - Recaps bankroll, health checks pipeline outputs.
  - `06_data_app_dashboard.ipynb` - Visualizes daily picks and bankroll chart.

---

## 🛠️ Usage Workflow (Daily)

1️⃣ Run `01_data_ingestion.ipynb` before games (once daily).  
2️⃣ Run `02_feature_engineering.ipynb` to process features.  
3️⃣ Run `03_model_training.ipynb` only when updating your model.  
4️⃣ Run `04_pipeline_execution.ipynb` to generate daily picks.  
5️⃣ Run `05_recap_and_healthcheck.ipynb` after games to update bankroll state.  
6️⃣ Open `06_data_app_dashboard.ipynb` anytime for fast insights.

---

## ⚙️ Customization & Next Steps

✅ Replace mock ingestion with live scraping (StatsAPI, OddsAPI).  
✅ Swap in your advanced `feature_engineering.py`.  
✅ Replace mock Telegram alerts with `bot/alerts/telegram.py` live alerts.  
✅ Integrate with your bankroll management logic.  
✅ Automate notebooks using Deepnote schedules.

---

## 🩺 Why Modular?

✅ Prevents slow, heavy reruns.  
✅ Keeps memory usage low.  
✅ Enables clear debugging, upgrades, and strategy expansion without system breakage.

---

## Need Help?

Reach out anytime to continue systematically improving your **world-class bookie killer pipeline.**

---
