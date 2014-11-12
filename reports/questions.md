# Questions

## Type of emissions reported since 2010:

```sql
select distinct type_of_emission
from emissions_emissionevent
order by type_of_emission
```

| type_of_emission               |
|--------------------------------|
| air-shutdown                   |
| air-startup                    |
| boil-water-notice-bwn          |
| boil-water-notice-bwn-wastewat |
| cercla-superfund               |
| emergency-response             |
| emergency-response-fish-kill   |
| emergency-response-fish-kill-w |
| emergency-response-pesticides- |
| emergency-response-wastewater- |
| emissions-event                |
| emissions-event-emergency-resp |
| excess-opacity                 |
| fish-kill                      |
| fish-kill-wastewater-bypass    |
| maintenance                    |
| none                           |
| ol-criminal-conviction-review  |
| pesticides-adverse-incident-wa |
| special-project                |
| tsswcb-referral                |
| tsswcb-referral-wastewater-byp |
| wastewater-bypass              |
| water-security                 |

## Contaminants released since 2010

```sql
select distinct contaminant_parameterized
from emissions_contaminantreleased
JOIN emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number)
WHERE emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
order by contaminant_parameterized
```

## Emissions per year

```sql
select count(*)
from emissions_emissionevent
where type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
and began_date > '2009-01-01'
and began_date < '2010-01-01'
```

| Year | Emissions |
|------|-----------|
| 2014 | 3805 |
| 2013 | 4846 |
| 2012 | 4465 |
| 2011 | 4515 |
| 2010 | 4369 |

## Aggregation of emission in 2013

```sql
select type_of_emission, count(*)
from emissions_emissionevent
where type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
and began_date > '2013-01-01'
and began_date < '2014-01-01'
GROUP BY type_of_emission;
```

| type of emission               | count|
|--------------------------------|------|
| air-startup                    | 162  |
| air-shutdown                   | 46   |
| emissions-event                | 3765 |
| excess-opacity                 | 405  |
| emissions-event-emergency-resp | 3    |
| maintenance                    | 465  |

## Top 5 busiest counties per year

```sql
select county, count(*) as emissions_per_county
from emissions_emissionevent
where type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
and began_date > '2014-01-01'
and began_date < '2015-01-01'
GROUP BY county
order by emissions_per_county desc
limit 5;
```

| County (2014) | emissions|
|---------|-----|
| ECTOR   | 493 |
| CRANE   | 424 |
| ANDREWS | 328 |
| HARRIS  | 217 |
| GAINES  | 162 |

| County (2013) | emissions|
|---------|-----|
| ECTOR   | 619 |
| CRANE   | 412 |
| ANDREWS | 357 |
| HARRIS  | 255 |
| GAINES  | 252 |

| County (2012) | emissions|
|-----------|-----|
| ECTOR     | 562 |
| CRANE     | 281 |
| HARRIS    | 267 |
| ANDREWS   | 255 |
| JEFFERSON | 217 |

| County (2011) | emissions|
|-----------|-----|
| ECTOR     | 427 |
| HARRIS    | 338 |
| ANDREWS   | 239 |
| JEFFERSON | 231 |
| GAINES    | 216 |

| County (2010) | emissions|
|-----------|-----|
| HARRIS    | 403 |
| ECTOR     | 342 |
| JEFFERSON | 254 |
| ANDREWS   | 176 |
| CALHOUN   | 161 |

# Frequent contaminants per year

```sql
SELECT DISTINCT emissions_contaminantreleased.contaminant,
count(*) as contaminant_count
FROM emissions_contaminantreleased
JOIN emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number)
WHERE emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
AND emissions_emissionevent.began_date > '2014-01-01'
AND emissions_emissionevent.began_date < '2015-01-01'
GROUP BY emissions_contaminantreleased.contaminant
ORDER BY contaminant_count DESC
LIMIT 5;
```

| Contaminants (2014) | Freq|
|------------------|------|
| Carbon Monoxide  | 2724 |
| Sulfur dioxide   | 2501 |
| Hydrogen Sulfide | 2427 |
| NATURAL GAS      | 1092 |
| NOX              | 941  |

| Contaminants (2013) | Freq|
|------------------|------|
| Carbon Monoxide  | 3458 |
| Hydrogen Sulfide | 3298 |
| Sulfur dioxide   | 3232 |
| NOX              | 1320 |
| Opacity          | 1317 |

| Contaminants (2012) | Freq|
|------------------|------|
| Carbon Monoxide  | 2597 |
| Sulfur dioxide   | 2571 |
| Hydrogen Sulfide | 2542 |
| Opacity          | 1218 |
| Propane          | 931  |

| Contaminants (2011) | Freq|
|------------------|------|
| Carbon Monoxide  | 2689 |
| Sulfur dioxide   | 2576 |
| Hydrogen Sulfide | 2497 |
| Opacity          | 1558 |
| Propane          | 1001 |

| Contaminants (2010) | Freq|
|------------------|------|
| Carbon Monoxide  | 2105 |
| Hydrogen Sulfide | 1846 |
| Sulfur dioxide   | 1823 |
| Opacity          | 1648 |
| Propane          | 761  |

## Busiest Facilities

```sql
select emissions_regulatedentity.name,
emissions_regulatedentity.county,
emissions_regulatedentity.regulated_entity_rn_number,
count(*) as freq
from emissions_emissionevent join emissions_regulatedentity
ON (emissions_regulatedentity.regulated_entity_rn_number = emissions_emissionevent.regulated_entity_rn_number)
WHERE emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
AND began_date > '2014-01-01'
and began_date < '2015-01-01'
group by emissions_regulatedentity.name,
emissions_regulatedentity.regulated_entity_rn_number,
emissions_regulatedentity.county
order by freq DESC
limit 10
```

| Facility | County | RN | Freq (2014)|
|-------------------------------|-------------|-------------|-----|
| MALLET CO2 RECOVERY PLANT     | HOCKLEY     | RN102205119 | 119 |
| KEYSTONE GAS PLANT            | WINKLER     | RN100238633 | 116 |
| GOLDSMITH GAS PLANT           | ECTOR       | RN100222330 | 91  |
| WAHA GAS PLANT                | PECOS       | RN100211408 | 70  |
| ANDREWS BOOSTER STATION       | ANDREWS     | RN100219047 | 67  |
| INVISTA SARL                  | VICTORIA    | RN102663671 | 62  |
| NORBORD TEXAS NACOGDOCHES     | NACOGDOCHES | RN100543040 | 53  |
| DOW TEXAS OPERATIONS FREEPORT | BRAZORIA    | RN100225945 | 52  |
| TILDEN GAS PLANT              | MCMULLEN    | RN100216621 | 47  |
| SAND HILLS GAS PLANT          | CRANE       | RN102552031 | 45  |

| Facility | County | RN | Freq (2013)|
|-------------------------------|-------------|-------------|-----|
| TILDEN GAS PLANT                | MCMULLEN | RN100216621 | 165 |
| KEYSTONE GAS PLANT              | WINKLER  | RN100238633 | 129 |
| MALLET CO2 RECOVERY PLANT       | HOCKLEY  | RN102205119 | 74  |
| RUSSELL COMPRESSOR STATION      | GAINES   | RN102554243 | 72  |
| MABEE RANCH C02 PLANT           | ANDREWS  | RN102535796 | 63  |
| GOLDSMITH GAS PLANT             | ECTOR    | RN100222330 | 61  |
| RED RIVER ARMY DEPOT            | BOWIE    | RN100224104 | 52  |
| WAHA GAS PLANT                  | PECOS    | RN100211408 | 52  |
| ENTERPRISE MONT BELVIEU COMPLEX | CHAMBERS | RN102323268 | 51  |
| INVISTA SARL                    | VICTORIA | RN102663671 | 50  |

| Facility | County | RN | Freq (2012)|
|---------------------------------------|--------------|-------------|-----|
| WAHA GAS PLANT                        | PECOS        | RN100211408 | 113 |
| REINECKE CTB AND CO2 RECYCLE FACILITY | BORDEN       | RN102792637 | 103 |
| FORMOSA POINT COMFORT PLANT           | CALHOUN      | RN100218973 | 99  |
| KEYSTONE GAS PLANT                    | WINKLER      | RN100238633 | 98  |
| TILDEN GAS PLANT                      | MCMULLEN     | RN100216621 | 95  |
| ALCOA POINT COMFORT OPERATIONS        | CALHOUN      | RN100242577 | 88  |
| SHERWIN ALUMINA PLANT                 | SAN PATRICIO | RN102318847 | 76  |
| GOLDSMITH GAS PLANT                   | ECTOR        | RN100222330 | 67  |
| TEXAS INDUSTRIES                      | COMAL        | RN100212067 | 60  |
| RUSSELL COMPRESSOR STATION            | GAINES       | RN102554243 | 59  |

| Facility | County | RN | Freq (2011)|
|-------------------------------------------|-----------|-------------|----|
| FORMOSA POINT COMFORT PLANT               | CALHOUN   | RN100218973 | 87 |
| KEYSTONE GAS PLANT                        | WINKLER   | RN100238633 | 86 |
| TILDEN GAS PLANT                          | MCMULLEN  | RN100216621 | 86 |
| REINECKE CTB AND CO2 RECYCLE FACILITY     | BORDEN    | RN102792637 | 84 |
| GOLDSMITH GAS PLANT                       | ECTOR     | RN100222330 | 74 |
| AEP - WELSH POWER PLANT                   | TITUS     | RN100213370 | 70 |
| INVISTA SARL                              | VICTORIA  | RN102663671 | 66 |
| ALCOA POINT COMFORT OPERATIONS            | CALHOUN   | RN100242577 | 65 |
| PITTSBURG GAS PLANT                       | CAMP      | RN100223783 | 63 |
| BLANCHARD REFINING GALVESTON BAY REFINERY | GALVESTON | RN102535077 | 62 |

| Facility | County | RN | Freq (2010)|
|------------------------------------|-----------|-------------|-----|
| MARTIN LAKE STEAM ELECTRIC STATION | RUSK      | RN102583093 | 122 |
| WAHA GAS PLANT                     | PECOS     | RN100211408 | 101 |
| BIG BROWN STEAM ELECTRIC STATION   | FREESTONE | RN101198059 | 91  |
| ALCOA POINT COMFORT OPERATIONS     | CALHOUN   | RN100242577 | 88  |
| AEP - WELSH POWER PLANT            | TITUS     | RN100213370 | 82  |
| SANDOW STEAM ELECTRIC STATION      | MILAM     | RN102147881 | 76  |
| FORMOSA POINT COMFORT PLANT        | CALHOUN   | RN100218973 | 71  |
| ZOLTEK                             | TAYLOR    | RN100543867 | 70  |
| TILDEN GAS PLANT                   | MCMULLEN  | RN100216621 | 66  |
| MONTICELLO STEAM ELECTRIC STATION  | TITUS     | RN102285921 | 66  |
