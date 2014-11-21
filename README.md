# News Apps Django Template

## Emission events type

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

https://www.tceq.texas.gov/assets/public/comm_exec/agendas/comm/backup/Agendas/2014/9-24-2014/1447PST.pdf

http://www11.tceq.texas.gov/oce/ch/index.cfm?fuseaction=main.search&RequestTimeout=90&principalname=&rename=DOW%20TEXAS%20OPERATIONS%20FREEPORT&rern=&aid=&progid=&county=&region=&startdate=09/01/2006&endate=&principalid=&reid=203518192001135

http://www2.tceq.texas.gov/oce/penenfac/index.cfm?fuseaction=home.details&rn=346523962013242

http://www11.tceq.texas.gov/oce/ch/index.cfm?fuseaction=main.search&RequestTimeout=90&principalname=&rename=DOW%20TEXAS%20OPERATIONS%20FREEPORT&rern=&aid=&progid=&county=&region=&startdate=09/01/2006&endate=&principalid=&reid=203518192001135

http://www.tceq.state.tx.us/assets/public/comm_exec/agendas/comm/marked/2014/140115.Mrk.pdf

from 
http://www2.tceq.texas.gov/oce/penenfac/index.cfm?fuseaction=home.details&rn=904547452014029

to 
http://www7.tceq.state.tx.us/uploads/eagendas/Agendas/2014/9-24-2014/0158PWS.pdf

https://www.tceq.texas.gov/assets/public/compliance/enforcement/enf_reports/AER/FY13/enfrptfy13.pdf

http://www11.tceq.state.tx.us/oce/eer/index.cfm?fuseaction=main.getDetails&target=205264
