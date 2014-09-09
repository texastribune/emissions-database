resetdb:
	dropdb emission_events
	createdb emission_events
	python emission_events/manage.py syncdb --noinput
	python emission_events/manage.py makemigrations
	python emission_events/manage.py migrate

