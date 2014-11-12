# Contaminants

## Ranking of facilities emitting hydrogen-cyanide

```sql
select emissions_regulatedentity.name as regulated_entity,
emissions_emissionevent.regulated_entity_rn_number as regulated_entity,
CAST(sum(emissions_contaminantreleased.amount_released_lbs) as int) as amount
from emissions_contaminantreleased
join emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number
  )
join emissions_regulatedentity on (
  emissions_regulatedentity.regulated_entity_rn_number = emissions_emissionevent.regulated_entity_rn_number
  )
where emissions_contaminantreleased.contaminant_parameterized='hydrogen-cyanide'
and emissions_contaminantreleased.amount_released_lbs is not null
and emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
group by emissions_emissionevent.regulated_entity_rn_number, emissions_regulatedentity.name
order by amount desc
limit 20;
```

| Name | RN | hydrogen-cyanide [lbs]|
|----------------------------------------------------|-------------|-----------|
| ASCEND PERFORMANCE MATERIALS CHOCOLATE BAYOU PLANT | RN100238682 | 11196.81 |
| INVISTA SARL | RN102663671 | 7012.855 |
| INVISTA SARL SABINE RIVER SITE | RN104392626 | 3007.12 |
| EXXON MOBIL BAYTOWN FACILITY | RN102579307 | 1048.6911 |
| LUCITE BEAUMONT SITE | RN102736089 | 1021.12 |
| FLINT HILLS RESOURCES EAST REFINERY | RN102534138 | 216 |
| SID RICHARDSON CARBON BIG SPRING FACILITY | RN100226026 | 150.489 |
| ROHM AND HAAS TEXAS DEER PARK PLANT | RN100223205 | 105.9 |
| DOW TEXAS OPERATIONS FREEPORT | RN100225945 | 33 |
| ZOLTEK | RN100543867 | 28.03442 |
| EXXONMOBIL CHEMICAL BAYTOWN CHEMICAL PLANT | RN102574803 | 5.0621 |
| GB BIOSCIENCES GREENS BAYOU PLANT | RN100238492 | 0.56 |
| GEO SPECIALTY CHEMICALS | RN100219070 | 0.00024 |

## Ranking of facilities emitting hydrogen-sulfide

```sql
select emissions_regulatedentity.name as regulated_entity,
emissions_emissionevent.regulated_entity_rn_number as regulated_entity,
sum(emissions_contaminantreleased.amount_released_lbs) as amount
from emissions_contaminantreleased
join emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number
  )
join emissions_regulatedentity on (
  emissions_regulatedentity.regulated_entity_rn_number = emissions_emissionevent.regulated_entity_rn_number
  )
where emissions_contaminantreleased.contaminant_parameterized='hydrogen-sulfide'
and emissions_contaminantreleased.amount_released_lbs is not null
and emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
group by emissions_emissionevent.regulated_entity_rn_number, emissions_regulatedentity.name
order by amount desc
limit 20;
```

| Name | RN | hydrogen-sulfide [lbs]|
|-----------------------------------------------------|-------------|------------------|
| MEANS CO2 DISCHARGE-INJECTION LINES | RN106188451 | 810006.5 |
| KEYSTONE GAS PLANT | RN100238633 | 464748.206 |
| GSAU 2 2 BATTERY | RN104149430 | 241144 |
| MALLET CO2 RECOVERY PLANT | RN102205119 | 151681.69135 |
| GOLDSMITH GAS PLANT | RN100222330 | 130320.49939 |
| WA COONS BATTERY | RN102547759 | 94468.08 |
| DOLLARHIDE SWD STATION | RN101989747 | 85453.17 |
| JT MCELROY 202 TB | RN102303336 | 82459.54 |
| VALERO PORT ARTHUR REFINERY | RN102584026 | 70915.3682 |
| TEXSTAR FIELD SERVICES PIPELINE ATASCOSA COUNTY | RN104858808 | 68621 |
| RUSSELL COMPRESSOR STATION | RN102554243 | 67424.00101 |
| GOLDSMITH LANDRETH DEEP UNIT CTB AND SATELLITE 11 | RN102996071 | 51432.5 |
| EXXONMOBIL BEAUMONT REFINERY | RN102450756 | 51330.421 |
| COMPRESSOR STATION 120 | RN102607975 | 48938.205 |
| TILDEN GAS PLANT | RN100216621 | 48408.9119999999 |
| REINECKE CTB AND CO2 RECYCLE FACILITY | RN102792637 | 47884.464 |
| SLAUGHTER GASOLINE PLANT | RN100212786 | 44763.81201 |
| MCELROY SECTION 199 EMERGENCY FLARE | RN102297827 | 43778.75 |
| NORTH MALLET TEST 8 OIL AND GAS PRODUCTION FACILITY | RN105742423 | 43152.93 |
| WAHA GAS PLANT | RN100211408 | 42410.3081000001 |

## Ranking of facilities emitting benzene

```sql
select emissions_regulatedentity.name as regulated_entity,
emissions_emissionevent.regulated_entity_rn_number as regulated_entity,
sum(emissions_contaminantreleased.amount_released_lbs) as amount
from emissions_contaminantreleased
join emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number
  )
join emissions_regulatedentity on (
  emissions_regulatedentity.regulated_entity_rn_number = emissions_emissionevent.regulated_entity_rn_number
  )
where emissions_contaminantreleased.contaminant_parameterized='benzene'
and emissions_contaminantreleased.amount_released_lbs is not null
and emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
group by emissions_emissionevent.regulated_entity_rn_number, emissions_regulatedentity.name
order by amount desc
limit 20;
```

| Name | RN | Benzene [lbs]|
|-------------------------------------------------|-------------|-------------|
| FORMOSA POINT COMFORT PLANT                     | RN100218973 | 80276.21221 |
| DOW TEXAS OPERATIONS FREEPORT                   | RN100225945 | 53850.1734  |
| SHELL OIL DEER PARK                             | RN100211879 | 44032.79567 |
| BLANCHARD REFINING GALVESTON BAY REFINERY       | RN102535077 | 40446.8762  |
| FLINT HILLS RESOURCES PORT ARTHUR FACILITY      | RN100217389 | 23437.045   |
| GOLDSMITH GAS PLANT                             | RN100222330 | 22851.51001 |
| CHEVRON PHILLIPS CHEMICAL CEDAR BAYOU PLANT     | RN103919817 | 21436       |
| EXXONMOBIL OIL BEAUMONT CHEMICAL PLANT          | RN100542844 | 18535.271   |
| FLINT HILLS RESOURCES CORPUS CHRISTI WEST PLANT | RN100235266 | 11509.1804  |
| EASTMAN CHEMICAL TEXAS OPERATIONS               | RN100219815 | 9559.34723  |
| TEXAS CITY CHEMICAL PLANT                       | RN104579487 | 8886.65     |
| BOYD COMPRESSOR STATION                         | RN100213701 | 6503.18     |
| CHEVRON PHILLIPS CHEMICAL PORT ARTHUR FACILITY  | RN100209857 | 6094.5001   |
| REGENCY FIELD SERVICES PIPELINE WEBB COUNTY     | RN107119547 | 6020        |
| CHEVRON PHILLIPS CHEMICAL SWEENY COMPLEX        | RN100825249 | 5994.276    |
| EXXON MOBIL CHEMICAL BAYTOWN OLEFINS PLANT      | RN102212925 | 5819.08002  |
| AFP TANK BATTERY                                | RN105966550 | 4507        |
| SWEENY REFINERY                                 | RN101619179 | 3938.43     |
| BASF TOTAL FINA NAFTA REGION OLEFINS COMPLEX    | RN100216977 | 3759.51029  |
| EXXONMOBIL BEAUMONT REFINERY                    | RN102450756 | 3703.361    |

## Ranking of facilities emitting CO

```sql
select emissions_regulatedentity.name as regulated_entity,
emissions_emissionevent.regulated_entity_rn_number as regulated_entity,
sum(emissions_contaminantreleased.amount_released_lbs) as amount
from emissions_contaminantreleased
join emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number
  )
join emissions_regulatedentity on (
  emissions_regulatedentity.regulated_entity_rn_number = emissions_emissionevent.regulated_entity_rn_number
  )
where emissions_contaminantreleased.contaminant_parameterized in 
('carbon-monoxide', 'co')
and emissions_contaminantreleased.amount_released_lbs is not null
and emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
group by emissions_emissionevent.regulated_entity_rn_number, emissions_regulatedentity.name
order by amount desc
limit 20;
```

| Name | RN | CO [lbs]|
|--------------------------------------------|-------------|------------------|
| BEAUMONT PLANT                             | RN102559291 | 8574775.65       |
| EXXONMOBIL BEAUMONT REFINERY               | RN102450756 | 2595781.461      |
| MIDKIFF GAS PLANT                          | RN100215714 | 2124099.44       |
| MIDMAR WEST GAS PLANT                      | RN105730485 | 1774072          |
| MALLET CO2 RECOVERY PLANT                  | RN102205119 | 1668259.04135    |
| SALT CREEK GAS PLANT                       | RN101222602 | 1404058.00002    |
| ALON USA BIG SPRING REFINERY               | RN100250869 | 1355838.6579     |
| GOLDSMITH GAS PLANT                        | RN100222330 | 1294147.39858    |
| DELEK TYLER REFINERY                       | RN100222512 | 1146239.14       |
| DOW TEXAS OPERATIONS FREEPORT              | RN100225945 | 1145664.3316     |
| EXXON MOBIL BAYTOWN FACILITY               | RN102579307 | 1091177.85946    |
| WASSON CO2 REMOVAL PLANT                   | RN100226687 | 978104.61        |
| SID RICHARDSON CARBON BORGER PLANT         | RN100222413 | 928436.19242     |
| BLANCHARD REFINING GALVESTON BAY REFINERY  | RN102535077 | 902518.044099999 |
| KEYSTONE GAS PLANT                         | RN100238633 | 608110.789       |
| EXXONMOBIL OIL BEAUMONT CHEMICAL PLANT     | RN100542844 | 607081.01        |
| FLINT HILLS RESOURCES PORT ARTHUR FACILITY | RN100217389 | 583943.26        |
| DENVER UNIT 2 RECOVERY PLANT               | RN102413861 | 555750           |
| RUSSELL COMPRESSOR STATION                 | RN102554243 | 543276.32701     |
| PORT ARTHUR REFINERY                       | RN100209451 | 507377.6698      |

## Ranking of facilities emitting Sulfur Dioxide

```sql
select emissions_regulatedentity.name as regulated_entity,
emissions_emissionevent.regulated_entity_rn_number as regulated_entity,
sum(emissions_contaminantreleased.amount_released_lbs) as amount
from emissions_contaminantreleased
join emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number
  )
join emissions_regulatedentity on (
  emissions_regulatedentity.regulated_entity_rn_number = emissions_emissionevent.regulated_entity_rn_number
  )
where emissions_contaminantreleased.contaminant_parameterized in 
('sulfur-dioxide', 'sulfur-dioxide-anhydrous')
and emissions_contaminantreleased.amount_released_lbs is not null
and emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
group by emissions_emissionevent.regulated_entity_rn_number, emissions_regulatedentity.name
order by amount desc
limit 20;
```

| Name | RN | Sulfur Dioxide [lbs]|
|----------------------------------------------------|-------------|----------------|
| KEYSTONE GAS PLANT                                 | RN100238633 | 43357744       |
| GOLDSMITH GAS PLANT                                | RN100222330 | 11555000.33794 |
| MALLET CO2 RECOVERY PLANT                          | RN102205119 | 8296544.40135  |
| RUSSELL COMPRESSOR STATION                         | RN102554243 | 6227389.00101  |
| VALERO PORT ARTHUR REFINERY                        | RN102584026 | 5701643.3067   |
| JT MCELROY 202 TB                                  | RN102303336 | 4360419.08     |
| TILDEN GAS PLANT                                   | RN100216621 | 4283403.391    |
| SAND HILLS GAS PLANT                               | RN102552031 | 4269454.94     |
| MCELROY SECTION 199 EMERGENCY FLARE                | RN102297827 | 3984158.85     |
| SLAUGHTER GASOLINE PLANT                           | RN100212786 | 3952524.70801  |
| WAHA GAS PLANT                                     | RN100211408 | 3939081.30598  |
| SID RICHARDSON CARBON BORGER PLANT                 | RN100222413 | 3584821.91389  |
| EXXONMOBIL BEAUMONT REFINERY                       | RN102450756 | 3543608.541    |
| MIDLAND FARMS CENTRAL TANK BATTERY                 | RN102570884 | 2850165        |
| CAG CENTRAL BATTERY NO 448                         | RN103914461 | 2722335.1      |
| AMERADA HESS SEMINOLE GAS PROCESSING PLANT         | RN103758470 | 2683067.5      |
| WEST SEMINOLE SAN ANDRES UNIT CENTRAL TANK BATTERY | RN102941358 | 2287015        |
| CAG 437 SATELLITE BATTERY                          | RN103914354 | 1858531.1      |
| NORTH RILEY CENTRAL BATTERY                        | RN100219831 | 1742771.04     |
| WASSON CO2 REMOVAL PLANT                           | RN100226687 | 1542193.42     |

## Ranking of facilities emitting Sulfur Dioxide

```sql
select emissions_regulatedentity.name as regulated_entity,
emissions_emissionevent.regulated_entity_rn_number as regulated_entity,
sum(emissions_contaminantreleased.amount_released_lbs) as amount
from emissions_contaminantreleased
join emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number
  )
join emissions_regulatedentity on (
  emissions_regulatedentity.regulated_entity_rn_number = emissions_emissionevent.regulated_entity_rn_number
  )
where emissions_contaminantreleased.contaminant_parameterized in (
'nox',
'nitrogen-oxide',
'nitrogen-oxides-nox',
'nitrogen-oxides',
'oxides-of-nitrogen-nox',
'nitrogen-dioxide',
'nitric-oxide',
'nox-startup-shutdown'
)
and emissions_contaminantreleased.amount_released_lbs is not null
and emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
group by emissions_emissionevent.regulated_entity_rn_number, emissions_regulatedentity.name
order by amount desc
limit 20;
```

| Name | RN | Nitrogen Dioxide/Nitric Oxide [lbs]|
|------------------------------------------------|-------------|---------------|
| GOLDSMITH GAS PLANT                            | RN100222330 | 1679195.27307 |
| MIDMAR WEST GAS PLANT                          | RN105730485 | 894102        |
| BIG LAKE GAS PLANT                             | RN100217686 | 767289.6001   |
| KEYSTONE GAS PLANT                             | RN100238633 | 552881.21     |
| MIDKIFF GAS PLANT                              | RN100215714 | 394352.98     |
| RUSSELL COMPRESSOR STATION                     | RN102554243 | 271966.41101  |
| UNIVERSITY 2 AND 3                             | RN105013478 | 237341.02     |
| MALLET CO2 RECOVERY PLANT                      | RN102205119 | 192138.73135  |
| DOW TEXAS OPERATIONS FREEPORT                  | RN100225945 | 170601.8216   |
| SALT CREEK GAS PLANT                           | RN101222602 | 163725.30002  |
| SAND HILLS GAS PLANT                           | RN102552031 | 162307.5      |
| MIDMAR EAST GAS PLANT                          | RN106570609 | 161857        |
| BLANCHARD REFINING GALVESTON BAY REFINERY      | RN102535077 | 154410.8087   |
| CAG CENTRAL BATTERY NO 448                     | RN103914461 | 121204.1      |
| CHEVRON PHILLIPS CHEMICAL PORT ARTHUR FACILITY | RN100209857 | 117156.6401   |
| EXXONMOBIL OIL BEAUMONT CHEMICAL PLANT         | RN100542844 | 116676.242    |
| WASSON CO2 REMOVAL PLANT                       | RN100226687 | 114086.86     |
| SOUTHEAST LEVELLAND UNIT PGG                   | RN106908007 | 102023.5      |
| EXXONMOBIL BEAUMONT REFINERY                   | RN102450756 | 101215.655    |
| ENTERPRISE PRODUCTS MONT BELVIEU WEST FACILITY | RN100543107 | 96748.1054    |

```sql

```
