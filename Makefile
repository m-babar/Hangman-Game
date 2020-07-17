freeze_dependencies:
	pip freeze | grep -v "pkg-resources" > requirements.txt

dependencies:requirements.txt
	@echo "Installing dependencies..."
	@pip install -r requirements.txt 1>/dev/null

clean:
	find . -name '*.pyc' -exec sudo rm -f {} +
	find . -name '*.pyo' -exec sudo rm -f {} +
	find . -name '*~' -exec sudo rm -f {} +
	find . -name '__pycache__' -exec sudo rm -rf {} +

lint:check-flake8 
	flake8

check-flake8:
	@type flake8 >/dev/null 2>&1 || echo "Flake8 is not installed. You can install it with 'pip install flake8'."

start-game: 
	@python Hangman.py