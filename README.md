# Emission events database

Scraper tools for the following databases:

* [Air Emission Event Report Database](http://www11.tceq.state.tx.us/oce/eer/index.cfm?fuseaction=main.searchForm)
* [Central Registry Query - Regulated Entity Search](http://www15.tceq.texas.gov/crpub/index.cfm?fuseaction=regent.RNSearch)
* [Commission Issued Orders](http://www14.tceq.texas.gov/epic/CIO/)

## Setup

You will need python and some dependencies, a postgres database and that's it:

    pip install -r requirements.txt
    make setup

And to start the party, you will need to populate the database. So far we have 4 different commands to start working:

    python emission_events/manage.py COMMAND

Where command can be:

* `downloadbatch` to download a batch of emission events starting with `--initial`.
* `updateemissions` will download 100 emissions from the last one stored in the database. If you run this command daily, you will always have the latest data on your system.
* `updateregulatedentities` Regulated Entities don't change too ofter. But from time to time you can check wheather you have a new kid on the block.
* `downloadissuedorders` will download the issued orders emited for every regulated entity on your database.

## Emission events type

For now, we are only focusing on the following emission events:

* air-shutdown
* air-startup
* emissions-event
* emissions-event-emergency-resp
* excess-opacity
* maintenance

## Commands

    psql -h 127.0.0.1 -U postgres -p 5433
    pg_dump -h 127.0.0.1 -U postgres -p 5433 emissions_project > database.sql
    psql emission_events < database.sql

## Backup

    export DATABASE_URL=postgis://docker:docker@localhost:5433/emission_events
    phd pg_dump > marcosdb-today.sql

## References

* https://www.tceq.texas.gov/assets/public/comm_exec/agendas/comm/backup/Agendas/2014/9-24-2014/1447PST.pdf
* http://www11.tceq.texas.gov/oce/ch/index.cfm?fuseaction=main.search&RequestTimeout=90&principalname=&rename=DOW%20TEXAS%20OPERATIONS%20FREEPORT&rern=&aid=&progid=&county=&region=&startdate=09/01/2006&endate=&principalid=&reid=203518192001135
* http://www2.tceq.texas.gov/oce/penenfac/index.cfm?fuseaction=home.details&rn=346523962013242
* http://www11.tceq.texas.gov/oce/ch/index.cfm?fuseaction=main.search&RequestTimeout=90&principalname=&rename=DOW%20TEXAS%20OPERATIONS%20FREEPORT&rern=&aid=&progid=&county=&region=&startdate=09/01/2006&endate=&principalid=&reid=203518192001135
* http://www.tceq.state.tx.us/assets/public/comm_exec/agendas/comm/marked/2014/140115.Mrk.pdf
* http://www2.tceq.texas.gov/oce/penenfac/index.cfm?fuseaction=home.details&rn=904547452014029
* http://www7.tceq.state.tx.us/uploads/eagendas/Agendas/2014/9-24-2014/0158PWS.pdf
* https://www.tceq.texas.gov/assets/public/compliance/enforcement/enf_reports/AER/FY13/enfrptfy13.pdf
* http://www11.tceq.state.tx.us/oce/eer/index.cfm?fuseaction=main.getDetails&target=205264
