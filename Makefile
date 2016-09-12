APP=emissions_events

local/db-fetch:
	aws --profile newsapps s3 cp s3://emissions-postgres-exports/pg.dump pg.dump

local/db-restore:
	dropdb ${APP} --if-exists
	createdb ${APP}
	pg_restore --dbname ${APP} --no-privileges --no-owner pg.dump

setup:
	createdb emission_events
	python emission_events/manage.py syncdb --noinput
	python emission_events/manage.py makemigrations
	python emission_events/manage.py migrate

resetdb:
	dropdb emission_events
	createdb emission_events
	python emission_events/manage.py syncdb --noinput
	python emission_events/manage.py makemigrations
	python emission_events/manage.py migrate
