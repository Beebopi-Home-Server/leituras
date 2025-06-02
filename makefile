run:
	gunicorn "app:create_app('production')"

debug:
	python leituras.py --debug
