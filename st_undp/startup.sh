# This file is used to launch a Streamlit app on Azure App Service

# 1. Add "startup.sh" as a "Startup Command" under "Stack settings"
# in "Settings" -> "Configuration" for your Web App on Azure

# 2. (Optional) Add commands to set up resources or download artefacts for
# your app, e.g., a large data or model file
# curl -o example.txt https://www.undp.org/robots.txt

# 3. (Optional) Modify the name of the entry script below if needed
python -m st_undp configure --settings style

python -m streamlit run app.py \
  --server.address 0.0.0.0 \
  --server.port 8000  \
  --server.enableStaticServing true \
  --browser.gatherUsageStats false
