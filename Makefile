install: # первое клонирование репозитория
	poetry install

brain-games: # запуск программы 
	poetry run brain-games

build: # сборка пакета
	poetry build

publish: # без добавления в каталог PyPI
	poetry publish --dry-run

package-install: # установка пакета из ОС
	python3 -m pip install --user dist/*.whl

make lint: # запуск линтера
	poetry run flake8 brain_games
