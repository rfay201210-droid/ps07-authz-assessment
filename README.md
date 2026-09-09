# # PS-07 AuthZ Assessment Demo

Controlled security assessment prototype for **app.archscale.in**.  
Focus: authentication boundaries, session handling, authorization, and API parity.

## 🚀 Features
- Login flow mapping (reset/recovery paths)
- Authentication boundary tests (rate limits, invalid tokens)
- Session handling (cookies, JWTs, refresh/logout)
- Role/object/tenant access checks
- API permission parity validation
- Evidence + remediation docs

## 🛠️ Setup
```bash
git clone https://github.com/rfay201210-droid/ps07-authz-assessment
cd ps07-authz-assessment
pip install -r requirements.txt
streamlit run streamlit_app.py
