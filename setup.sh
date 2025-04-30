# setup for backend api
cd word2vec-api
python -m venv venv
pip install -r requirements.txt

# setup for nuxt app
cd ..
cd word2vec-api
npm install .
