# Emissions report 1

## Emissions per type on 2014

``` SQL
    SELECT type_of_air_emissions_event AS emission_type, count(id)
    FROM emissions_emissionevent where began_date > '2014-01-01'
    GROUP BY type_of_air_emissions_event;
```

       emission_type     | count 
-------------------------|-------
 AIR SHUTDOWN            |     3
 EXCESS OPACITY          |    10
 EMISSIONS EVENT         |   204
 EMERGENCY RESPONSE      |    36
 WASTEWATER BYPASS       |    13
                         |    39
 AIR STARTUP             |    10
 BOIL WATER NOTICE (BWN) |    39
 MAINTENANCE             |    37
 FISH KILL               |     1


## Emissions per type on 2013

``` SQL
    SELECT type_of_air_emissions_event AS emission_type, count(id)
    FROM emissions_emissionevent where began_date > '2013-01-01'
    AND began_date < '2014-01-01'
    GROUP BY type_of_air_emissions_event;
```

             emission_type             | count 
---------------------------------------|-------
 , EMERGENCY RESPONSE                  |     6
 EXCESS OPACITY                        |   402
 SPECIAL PROJECT                       |     9
 WASTEWATER BYPASS                     |   359
 , TSSWCB REFERRAL                     |     1
 AIR STARTUP                           |   160
 BOIL WATER NOTICE (BWN)               |  1109
 FISH KILL                             |    24
 EMERGENCY RESPONSE, WASTEWATER BYPASS |     4
 EMERGENCY RESPONSE                    |   872
                                       |   784
 AIR SHUTDOWN                          |    43
 TSSWCB REFERRAL                       |    38
 EMERGENCY RESPONSE, FISH KILL         |     4
 , FISH KILL                           |     1
 MAINTENANCE                           |   465
 FISH KILL, WASTEWATER BYPASS          |     1
 EMISSIONS EVENT                       |  3743
 EMISSIONS EVENT, EMERGENCY RESPONSE   |     2

## Contaminants per maintenance (2014)

``` SQL
SELECT emissions_contaminantreleased.contaminant AS contaminant,
COUNT(emissions_contaminantreleased.id)
FROM emissions_contaminantreleased
JOIN emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number)
WHERE
  emissions_emissionevent.type_of_air_emissions_event = 'MAINTENANCE'
  AND emissions_emissionevent.began_date > '2014-01-01'
GROUP BY emissions_contaminantreleased.contaminant;
```

            contaminant             | count 
------------------------------------|-------
 Isobutylene                        |     1
 VOC                                |     3
 N-Hexane                           |     4
 Cyclohexane                        |     1
 Ethylene (gaseous)                 |     3
 2-Butene-cis                       |     1
 Xylenes                            |     4
 Nitrogen Oxides                    |     4
 Hydrogen Sulfide                   |    13
 Smoke                              |     1
 NATURAL GAS                        |     4
 Ethane                             |     1
 Methane                            |     1
 Propylene                          |     1
 C5+ (not including benzene)        |     1
 Sulfur dioxide (anhydrous)         |     1
 Nitrogen Oxides (NOx)              |     1
 NOX                                |     6
 Carbon Monoxide                    |    19
 Nitrogen monoxide                  |     2
 Benzene                            |     7
 VOC GAS MIXTURE                    |     3
 Pentane                            |     4
 2-Butene-trans                     |     1
 Isobutane                          |     3
 Sulfur dioxide                     |    12
 VOCs                               |     4
 Visible Emissions                  |     1
 1,3-BUTADIENE                      |     1
 Pentane, N-                        |     1
 Acetylene                          |     1
 Butane, i                          |     1
 Opacity                            |    32
 Non-Methane Non-Ethane Natural Gas |     2
 Propane, N-                        |     5
 pentane, iso-                      |     1
 CO                                 |     3
 1-Butene                           |     1
 Oxides of Nitrogen (NOx)           |     2
 Styrene                            |     1
 Butane                             |     6
 Methanol                           |     1
 Butane, N-                         |     2
 Nitrogen dioxide                   |     3
 Toluene                            |     5
 Nitrogen oxide                     |     6
 hexanes +                          |     1
 Propane                            |     9
 Methyl Acetate                     |     1

## No emission estimation method (2014)

``` SQL
SELECT COUNT(id)
FROM emissions_emissionevent
WHERE emissions_estimation_method = ''
  AND began_date > '2014-01-01';
```

 count 
-------
    29

## No emission estimation method (2013)

``` SQL
SELECT COUNT(id)
FROM emissions_emissionevent
WHERE emissions_estimation_method = ''
  AND began_date > '2013-01-01'
  AND began_date < '2014-01-01';
```

 count 
-------
   659

## Contaminant by type of emission (2014)

``` SQL
SELECT DISTINCT emissions_contaminantreleased.contaminant,
  emissions_emissionevent.type_of_air_emissions_event AS type_of_emission
FROM emissions_contaminantreleased
JOIN emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number)
WHERE began_date > '2014-01-01'
ORDER BY emissions_emissionevent.type_of_air_emissions_event;
```

                   contaminant                   |  type_of_emission  
-------------------------------------------------|--------------------
 1,3-BUTADIENE                                   | AIR SHUTDOWN
 VOC                                             | AIR SHUTDOWN
 Cis-2-butene                                    | AIR SHUTDOWN
 Sulfur dioxide                                  | AIR SHUTDOWN
 Trans-2-butene                                  | AIR SHUTDOWN
 Ethylene (gaseous)                              | AIR SHUTDOWN
 Butane                                          | AIR SHUTDOWN
 Nitrogen Oxides                                 | AIR SHUTDOWN
 Hexene                                          | AIR SHUTDOWN
 Isobutylene                                     | AIR SHUTDOWN
 Particulate Matter                              | AIR SHUTDOWN
 Isobutane                                       | AIR SHUTDOWN
 Carbon Monoxide                                 | AIR SHUTDOWN
 C5+ (not including benzene)                     | AIR SHUTDOWN
 Propane                                         | AIR SHUTDOWN
 2-ETHYL-1-HEXENE                                | AIR SHUTDOWN
 Nitrogen oxide                                  | AIR SHUTDOWN
 Propylene (Propene)                             | AIR SHUTDOWN
 Hydrogen Sulfide                                | AIR SHUTDOWN
 Octene                                          | AIR SHUTDOWN
 2-Ethyl-1-Butene                                | AIR SHUTDOWN
 Toluene                                         | AIR STARTUP
 Nitrogen oxide                                  | AIR STARTUP
 Benzene                                         | AIR STARTUP
 Propane, N-                                     | AIR STARTUP
 Ethylbenzene                                    | AIR STARTUP
 Isobutane                                       | AIR STARTUP
 Xylene                                          | AIR STARTUP
 Particulate Matter                              | AIR STARTUP
 Butane                                          | AIR STARTUP
 Ammonia                                         | AIR STARTUP
 Oxides of Nitrogen (NOx)                        | AIR STARTUP
 Heptane,-n                                      | AIR STARTUP
 Sulfur dioxide                                  | AIR STARTUP
 VOC( unspeciated)                               | AIR STARTUP
 PM10                                            | AIR STARTUP
 Hexane, i                                       | AIR STARTUP
 NOX                                             | AIR STARTUP
 Pentane                                         | AIR STARTUP
 VOC - NONMETHANE                                | AIR STARTUP
 decane                                          | AIR STARTUP
 Opacity                                         | AIR STARTUP
 Octane                                          | AIR STARTUP
 Isopentane                                      | AIR STARTUP
 Carbon Monoxide                                 | AIR STARTUP
 Hydrogen Sulfide                                | AIR STARTUP
 Solvent Refined Heavy Naphtha                   | EMERGENCY RESPONSE
 DIESEL OIL #2/GUAR GUM                          | EMERGENCY RESPONSE
 Ferrous sulfate                                 | EMERGENCY RESPONSE
 Crude Oil                                       | EMERGENCY RESPONSE
 Naphtha (petroleum), catalytic reformed         | EMERGENCY RESPONSE
 CONDENSATE                                      | EMERGENCY RESPONSE
 Fuel oil 2                                      | EMERGENCY RESPONSE
 Sewage                                          | EMERGENCY RESPONSE
 Mercury                                         | EMERGENCY RESPONSE
 Drilling mud (oil/gas related)                  | EMERGENCY RESPONSE
 OIL                                             | EMERGENCY RESPONSE
 Fuel oil 6                                      | EMERGENCY RESPONSE
 Propylene Glycol                                | EMERGENCY RESPONSE
 Diesel fuel                                     | EMERGENCY RESPONSE
 Hydraulic fluid                                 | EMERGENCY RESPONSE
 Toluene                                         | EMISSIONS EVENT
 Isopentane                                      | EMISSIONS EVENT
 decane                                          | EMISSIONS EVENT
 Isoprene                                        | EMISSIONS EVENT
 i-butane                                        | EMISSIONS EVENT
 Propadiene                                      | EMISSIONS EVENT
 Ethylene, gaseous                               | EMISSIONS EVENT
 CO                                              | EMISSIONS EVENT
 pentane, iso-                                   | EMISSIONS EVENT
 VOCs                                            | EMISSIONS EVENT
 Butane, i                                       | EMISSIONS EVENT
 Carbon Monoxide                                 | EMISSIONS EVENT
 MTBE                                            | EMISSIONS EVENT
 Hexane Plus                                     | EMISSIONS EVENT
 Xylenes                                         | EMISSIONS EVENT
 Hydrogen Sulfide                                | EMISSIONS EVENT
 Cyclohexane                                     | EMISSIONS EVENT
 Octanes                                         | EMISSIONS EVENT
 Carbon disulfide                                | EMISSIONS EVENT
 1-Butene                                        | EMISSIONS EVENT
 Ethanol                                         | EMISSIONS EVENT
 C5                                              | EMISSIONS EVENT
 Isobutane                                       | EMISSIONS EVENT
 Hexane, n                                       | EMISSIONS EVENT
 Ethylbenzene                                    | EMISSIONS EVENT
 NATURAL GAS                                     | EMISSIONS EVENT
 Nitrogen Oxides (NOx)                           | EMISSIONS EVENT
 VOC( unspeciated)                               | EMISSIONS EVENT
 Nitrogen oxide                                  | EMISSIONS EVENT
 Nitrogen dioxide                                | EMISSIONS EVENT
 Trans-butene-2                                  | EMISSIONS EVENT
 Butadiene, 1-3                                  | EMISSIONS EVENT
 Pentane, N-                                     | EMISSIONS EVENT
 1,3-BUTADIENE                                   | EMISSIONS EVENT
 Pentenes                                        | EMISSIONS EVENT
 Sulfur dioxide                                  | EMISSIONS EVENT
 Heptanes                                        | EMISSIONS EVENT
 Trans-2-butene                                  | EMISSIONS EVENT
 Xylene                                          | EMISSIONS EVENT
 Propylene                                       | EMISSIONS EVENT
 Carbonyl sulfide                                | EMISSIONS EVENT
 VOC (light hydrocarbons)                        | EMISSIONS EVENT
 Pentene                                         | EMISSIONS EVENT
 Butenes, All Isomers                            | EMISSIONS EVENT
 n-butane                                        | EMISSIONS EVENT
 Isobutylene                                     | EMISSIONS EVENT
 Butadiene                                       | EMISSIONS EVENT
 Butane, N-                                      | EMISSIONS EVENT
 Other                                           | EMISSIONS EVENT
 Non-Methane Non-Ethane Natural Gas              | EMISSIONS EVENT
 Propane, N-                                     | EMISSIONS EVENT
 Catalyst fines                                  | EMISSIONS EVENT
 Pentanes                                        | EMISSIONS EVENT
 Pentane                                         | EMISSIONS EVENT
 Ethane                                          | EMISSIONS EVENT
 Butanes                                         | EMISSIONS EVENT
 VOC (unspeciated)                               | EMISSIONS EVENT
 Particulate Matter                              | EMISSIONS EVENT
 Ethylene (gaseous)                              | EMISSIONS EVENT
 Propylene (Propene)                             | EMISSIONS EVENT
 Volatile Organic Compounds                      | EMISSIONS EVENT
 VOC                                             | EMISSIONS EVENT
 Natural Gas VOCs                                | EMISSIONS EVENT
 Methanol                                        | EMISSIONS EVENT
 Methyl Acetylene                                | EMISSIONS EVENT
 hexanes +                                       | EMISSIONS EVENT
 Heptane (or n-)                                 | EMISSIONS EVENT
 Hexane                                          | EMISSIONS EVENT
 Acetylene                                       | EMISSIONS EVENT
 Benzene                                         | EMISSIONS EVENT
 Cis-2-butene                                    | EMISSIONS EVENT
 C6+                                             | EMISSIONS EVENT
 Calcined Alumina Dust                           | EMISSIONS EVENT
 Ethyl Benzene                                   | EMISSIONS EVENT
 Cis-butene-2                                    | EMISSIONS EVENT
 Oxides of Nitrogen (NOx)                        | EMISSIONS EVENT
 Butane                                          | EMISSIONS EVENT
 Anhydrous ammonia                               | EMISSIONS EVENT
 Octane                                          | EMISSIONS EVENT
 Nonanes                                         | EMISSIONS EVENT
 C5+ (not including benzene)                     | EMISSIONS EVENT
 VOC MIXTURE                                     | EMISSIONS EVENT
 Propane                                         | EMISSIONS EVENT
 VOC - NONMETHANE                                | EMISSIONS EVENT
 Hexanes                                         | EMISSIONS EVENT
 Butene                                          | EMISSIONS EVENT
 Unspeciated VOCs                                | EMISSIONS EVENT
 Opacity                                         | EMISSIONS EVENT
 Nitrogen monoxide                               | EMISSIONS EVENT
 Butylene Isomers                                | EMISSIONS EVENT
 Acrylonitrile                                   | EMISSIONS EVENT
 Nonane                                          | EMISSIONS EVENT
 NOX                                             | EMISSIONS EVENT
 Ethylene oxide                                  | EMISSIONS EVENT
 Nitrogen Oxides                                 | EMISSIONS EVENT
 Petroleum Naphtha; Light Steam-Cracked Aromatic | EMISSIONS EVENT
 Vinyl Chloride                                  | EMISSIONS EVENT
 Opacity                                         | EXCESS OPACITY
 NATURAL GAS                                     | MAINTENANCE
 Nitrogen Oxides (NOx)                           | MAINTENANCE
 Butane, N-                                      | MAINTENANCE
 Toluene                                         | MAINTENANCE
 Non-Methane Non-Ethane Natural Gas              | MAINTENANCE
 1-Butene                                        | MAINTENANCE
 hexanes +                                       | MAINTENANCE
 Styrene                                         | MAINTENANCE
 Ethane                                          | MAINTENANCE
 Methyl Acetate                                  | MAINTENANCE
 VOC                                             | MAINTENANCE
 Propane                                         | MAINTENANCE
 Opacity                                         | MAINTENANCE
 Xylenes                                         | MAINTENANCE
 2-Butene-cis                                    | MAINTENANCE
 Hydrogen Sulfide                                | MAINTENANCE
 NOX                                             | MAINTENANCE
 Cyclohexane                                     | MAINTENANCE
 Nitrogen monoxide                               | MAINTENANCE
 N-Hexane                                        | MAINTENANCE
 Methanol                                        | MAINTENANCE
 Carbon Monoxide                                 | MAINTENANCE
 Acetylene                                       | MAINTENANCE
 Butane, i                                       | MAINTENANCE
 Smoke                                           | MAINTENANCE
 Methane                                         | MAINTENANCE
 CO                                              | MAINTENANCE
 pentane, iso-                                   | MAINTENANCE
 Isobutylene                                     | MAINTENANCE
 Nitrogen Oxides                                 | MAINTENANCE
 VOCs                                            | MAINTENANCE
 Sulfur dioxide                                  | MAINTENANCE
 Propylene                                       | MAINTENANCE
 Sulfur dioxide (anhydrous)                      | MAINTENANCE
 Butane                                          | MAINTENANCE
 Ethylene (gaseous)                              | MAINTENANCE
 Benzene                                         | MAINTENANCE
 Pentane                                         | MAINTENANCE
 Oxides of Nitrogen (NOx)                        | MAINTENANCE
 Nitrogen oxide                                  | MAINTENANCE
 Nitrogen dioxide                                | MAINTENANCE
 Isobutane                                       | MAINTENANCE
 Visible Emissions                               | MAINTENANCE
 Propane, N-                                     | MAINTENANCE
 Pentane, N-                                     | MAINTENANCE
 2-Butene-trans                                  | MAINTENANCE
 VOC GAS MIXTURE                                 | MAINTENANCE
 C5+ (not including benzene)                     | MAINTENANCE
 1,3-BUTADIENE                                   | MAINTENANCE
 Wastewater discharge, municipal                 | WASTEWATER BYPASS
 Sewage                                          | WASTEWATER BYPASS


## Notas

    psql -d emission_events -c 'SELECT id FROM emissions_emissionevent;
