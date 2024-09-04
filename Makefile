install:
	poetry install --with dev
lint:
	pylint st_undp/
format:
	isort . --profile black --multi-line 3 && black .
test:
	python -m pytest tests/
run:
	python -m streamlit run app.py
