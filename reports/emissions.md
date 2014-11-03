# Deeper report

* air-shutdown
* air-startup
* emissions-event
* emissions-event-emergency-resp
* excess-opacity
* maintenance

## Tables

 Schema |                 Name                 | Type   
 -------|--------------------------------------|------
 public | emissions_contaminantreleased        | table
 public | emissions_emissionevent              | table
 public | emissions_pagehtml                   | table
 public | emissions_requestattempt             | table

## emissions_emissionevent

 Column                      | Type                     
 ----------------------------|--------------------------
 id                          | integer                  
 tracking_number             | integer                  
 dc_date_meta                | character varying(20)    
 regulated_entity_name       | character varying(30)    
 physical_location           | text                     
 regulated_entity_rn_number  | character varying(50)    
 city_county                 | character varying(50)    
 type_of_air_emissions_event | character varying(200)   
 based_on_the                | character varying(50)    
 event_began                 | character varying(30)    
 event_ended                 | character varying(30)    
 cause                       | text                     
 action_taken                | text                     
 emissions_estimation_method | text                     
 dc_date                     | date                     
 city                        | character varying(200)   
 county                      | character varying(200)   
 began_date                  | timestamp with time zone 
 ended_date                  | timestamp with time zone 
 duration                    | double precision         
 type_of_emission            | character varying(30)    
 page_html_id                | integer                  

## emissions_contaminantreleased

Column                     |          Type
---------------------------|----------------------
 id                        | integer               
 tracking_number           | integer               
 contaminant               | character varying(100)
 authorization             | character varying(200)
 limit                     | character varying(100)
 amount_released           | character varying(200)
 contaminant_parameterized | character varying(100)
 limit_lbs                 | double precision      
 amount_released_lbs       | double precision      
 limit_op                  | double precision      
 amount_released_op        | double precision      
 emission_event_id         | integer               

### Longest duration events

```sql
select tracking_number, regulated_entity_name, county, CAST(duration/24 as int)
from emissions_emissionevent
where type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
order by duration desc
limit 200;
```

| ID     | Regulated Entity               | County     | Days   |
|--------|--------------------------------|------------|--------|
| 180117 | CORNELL-MAHONEY GAS PLANT      | YOAKUM     | 360795 |
| 185367 | PARKS BOOSTER COMPRESSOR STATI | MIDLAND    | 365    |
| 186750 | SID RICHARDSON CARBON BORGER P | HUTCHINSON | 308    |
| 189292 | MIDMAR WEST GAS PLANT          | ANDREWS    | 266    |
| 184935 | GALENA PARK TERMINAL           | HARRIS     | 243    |
| 189507 | MIDMAR EAST GAS PLANT          | ANDREWS    | 226    |
| 190319 | HOUSTON PLANT                  | HARRIS     | 193    |
| 187234 | COWDEN CENTRAL TB              | ANDREWS    | 158    |
| 180336 | CHALK G BATTERY                | HOWARD     | 148    |
| 191208 | FLINT HILLS RESOURCES HOUSTON  | HARRIS     | 123    |
| 189865 | FLINT HILLS RESOURCES LONGVIEW | HARRISON   | 116    |
| 186698 | WE CONNELL COMINGLING          | ECTOR      | 111    |
| 191628 | WE CONNELL COMINGLING          | ECTOR      | 111    |
| 192412 | CHALK NORTH BATTERY            | HOWARD     | 103    |
| 187727 | TANK SITE A-MASTEN INJECT      | COCHRAN    | 91     |
| 179762 | E ARMSTRONG C TB NO 1          | ANDREWS    | 85     |
| 181130 | DOW TEXAS OPERATIONS FREEPORT  | BRAZORIA   | 84     |
| 177552 | LCRA SAM SEYMOUR FAYETTE POWER | FAYETTE    | 81     |
| 186737 | NORTH COWDEN TEST STATION 8    | ECTOR      | 78     |
| 183952 | DOW TEXAS OPERATIONS FREEPORT  | BRAZORIA   | 75     |
| 203862 | INVISTA SARL SABINE RIVER SITE | ORANGE     | 70     |
| 191392 | JOHNSON DEEP UNIT              | ECTOR      | 68     |
| 185185 | CAG 480 SATELLITE BATTERY      | ECTOR      | 62     |
| 185194 | CAG 120 SATELLITE BATTERY      | ECTOR      | 62     |
| 177937 | CINDY TANK BATTERY             | ANDREWS    | 61     |
| 181002 | CHEVRON PHILLIPS CHEMICAL PORT | JEFFERSON  | 60     |
| 182756 | CLYDE COWDEN BATTERY 1         | ECTOR      | 53     |
| 181674 | LE WIGHT B TANK BATTERY        | ECTOR      | 52     |
| 181505 | SID RICHARDSON CARBON BORGER P | HUTCHINSON | 51     |
| 191179 | ELIZABETH ARMSTRONG D TB1      | ANDREWS    | 50     |
| 178424 | CHALK NORTH BATTERY            | HOWARD     | 48     |
| 182420 | KEYSTONE GAS PLANT             | WINKLER    | 48     |
| 180300 | CENTRAL TB AND SAT STA 11      | ECTOR      | 46     |
| 177550 | NORTH WESTBROOK WEST UNIT      | MITCHELL   | 45     |
| 189629 | CORNELL-MAHONEY GAS PLANT      | YOAKUM     | 44     |
| 185375 | NOLTEX                         | HARRIS     | 44     |
| 190108 | WAHA GAS PLANT                 | PECOS      | 44     |
| 190318 | HOUSTON PLANT                  | HARRIS     | 40     |
| 189933 | SOUTH FOSTER CENTRAL TANK BATT | ECTOR      | 40     |
| 181580 | RHODES COWDEN UNIT CENTRAL BAT | ECTOR      | 39     |
| 181581 | JOHNSON DEEP UNIT              | ECTOR      | 39     |
| 179426 | WE CONNELL COMINGLING          | ECTOR      | 39     |
| 186254 | FULLERTON CLEARFORK UNIT SUBBA | ANDREWS    | 37     |
| 181698 | FULLERTON CLEARFORK UNIT SUBBA | ANDREWS    | 37     |
| 180415 | NPU 1 & MILLARD C TANK BATTERY | ECTOR      | 37     |
| 180417 | MILLARD A & D TANK BATTERY     | ECTOR      | 37     |
| 181730 | JOHNSON GBSA UNIT CB           | ECTOR      | 36     |
| 178563 | CLYDE COWDEN BATTERY 5         | ECTOR      | 34     |
| 187706 | CHEVRON PHILLIPS CHEMICAL CEDA | HARRIS     | 33     |
| 188063 | CAG 437 SATELLITE BATTERY      | ECTOR      | 32     |
| 185669 | MAVERICK GAS PLANT             | LA SALLE   | 30     |
| 183159 | CAG 437 SATELLITE BATTERY      | ECTOR      | 30     |
| 183461 | MRS BAIRDS BAKERIES HOUSTON TX | HARRIS     | 30     |
| 203651 | FLINT HILLS RESOURCES PORT ART | JEFFERSON  | 30     |
| 183153 | CAG 446 D SATELLITE BATTERY    | ECTOR      | 30     |
| 203869 | BORGER REFINERY                | HUTCHINSON | 30     |
| 187478 | KDB CENTRAL TREATING FACILITY  | KARNES     | 29     |
| 185012 | UNIVERSITY BLOCK9 CE TANK BATT | ANDREWS    | 29     |
| 181697 | FULLERTON CLEARFORK 200 5      | ANDREWS    | 29     |
| 185082 | STATE UNIVERSITY ATAUBA BATTER | ANDREWS    | 28     |
| 185085 | XTO ENERGY UNIV N TANK BATTERY | ANDREWS    | 28     |
| 183187 | DEADWOOD CRYO PLANT            | GLASSCOCK  | 28     |
| 181724 | JED CLAMPETT PRODUCTION FACILI | GAINES     | 28     |
| 178102 | REGENCY FIELD SERVICES PIPELIN | WARD       | 27     |
| 182054 | MIDLAND FARMS UNIT NORTH FLARE | ECTOR      | 27     |
| 179900 | LE WIGHT B TANK BATTERY        | ECTOR      | 27     |
| 189927 | LAGUNA A STORAGE SYSTEM        | ECTOR      | 27     |
| 203578 | DOLLARHIDE GAS PLANT           | ANDREWS    | 27     |
| 178260 | CAG 480 SATELLITE BATTERY      | ECTOR      | 26     |
| 185701 | RED BLUFF GAS PROCESSING PLANT | REEVES     | 26     |
| 182479 | NORTH RILEY CENTRAL BATTERY    | GAINES     | 25     |
| 190250 | MIDLAND MESA BLENDING STATION  | MIDLAND    | 25     |
| 188566 | TOTAL PETRO CHEMICALS & REFINI | JEFFERSON  | 25     |
| 185101 | MIDLAND FARMS UNIT NORTH FLARE | ECTOR      | 23     |
| 187829 | NORTH COWDEN CO2 INJECTION FAC | ECTOR      | 23     |
| 192502 | ALON USA BIG SPRING REFINERY   | HOWARD     | 22     |
| 204197 | BRASKEM AMERICA                | BRAZORIA   | 22     |
| 185041 | RUSSELL COMPRESSOR STATION     | GAINES     | 22     |
| 183421 | CAG 511 SATELLITE BATTERY      | ECTOR      | 22     |
| 185052 | LANCASTER RANCH COMPRESSOR STA | FRIO       | 21     |
| 185943 | UNIVERSITY ANDREWS 7T BATTERY  | ANDREWS    | 21     |
| 189091 | VALERO CORPUS CHRISTI REFINERY | NUECES     | 21     |
| 203004 | DOW TEXAS OPERATIONS FREEPORT  | BRAZORIA   | 21     |
| 184266 | HOUSTON PLANT                  | HARRIS     | 21     |
| 192212 | WHARTON UNIT TANK BATTERY      | GAINES     | 21     |
| 180221 | CHEVRON PHILLIPS CHEMICAL SWEE | BRAZORIA   | 20     |
| 188739 | WAHA GAS PLANT                 | PECOS      | 20     |
| 192206 | NORTH RILEY CENTRAL BATTERY    | GAINES     | 20     |
| 185066 | NORTH COWDEN TEST STATION 8    | ECTOR      | 20     |
| 185067 | N COWDEN UNIT TEST STA 9       | ECTOR      | 20     |
| 185064 | N COWDEN UNIT TEST STN 3       | ECTOR      | 20     |
| 189212 | DOLLARHIDE TANK BATT 1         | ANDREWS    | 20     |
| 192185 | STATE UNIVERSITY ATAUBA BATTER | ANDREWS    | 20     |
| 186893 | MFDU SOUTH TEST STATION        | ANDREWS    | 20     |
| 191477 | MONT BELVIEU NGL FRACTIONATION | CHAMBERS   | 20     |
| 181027 | N COWDEN UNIT TEST STN 3       | ECTOR      | 19     |
| 181039 | N COWDEN UNIT TEST STA 23      | ECTOR      | 19     |
| 187801 | JAVELINA GAS PROCESSING FACILI | NUECES     | 19     |
| 187760 | HALEY CTB                      | WINKLER    | 19     |
| 189423 | WHARTON UNIT TANK BATTERY      | GAINES     | 19     |
| 192213 | ROBERTSON CLEARFORK INIT SAT 1 | GAINES     | 19     |
| 180770 | RUSSELL COMPRESSOR STATION     | GAINES     | 19     |
| 189917 | SONORA GAS PLANT               | UPTON      | 18     |
| 181076 | GANDU 36 BATTERY               | ECTOR      | 18     |
| 184143 | BORGER REFINERY                | HUTCHINSON | 18     |
| 179092 | N COWDEN UNIT TS 19            | ECTOR      | 18     |
| 184888 | FULLERTON CLEARFORK UNIT SUBBA | ANDREWS    | 18     |
| 188130 | STEWART SECTION 1 TANK BATTERY | PECOS      | 18     |
| 188132 | LIZZY SECTION 4 TANK BATTERY   | PECOS      | 18     |
| 188144 | BONEBRAKE SECTION 1 TANK BATTE | PECOS      | 18     |
| 188126 | WOLFPUP SECTION 78 96 BATTERY  | PECOS      | 18     |
| 188138 | CHILTON SECTION 56 TANK BATTER | PECOS      | 18     |
| 188141 | BIG TEX NORTH SECTION 15 BATTE | PECOS      | 18     |
| 188140 | BIG TEX NORTH SECTION 13 TANK  | PECOS      | 18     |
| 188127 | TRAINER TRUST SECTION 16 TANK  | PECOS      | 18     |
| 188142 | BONEBRAKE SECTION 98 TANK BATT | PECOS      | 18     |
| 188149 | BISSETT SECTION 97 TANK BATTER | PECOS      | 18     |
| 188135 | LEGEAR SECTION 11 BATTERY      | REEVES     | 18     |
| 188383 | SSU SATELLITE 1-12             | HOCKLEY    | 18     |
| 188394 | SSU SATELLITE 1 18             | HOCKLEY    | 18     |
| 188400 | SUNDOWN SLAUGHTER UNIT SAT 3-4 | HOCKLEY    | 18     |
| 188397 | SSU SATELLITE 1 19             | HOCKLEY    | 18     |
| 188402 | SSU SATT 6-01                  | HOCKLEY    | 18     |
| 188384 | SSU SATELLITE 1 13             | HOCKLEY    | 18     |
| 188357 | SSU SATELLITE 1 11             | HOCKLEY    | 18     |
| 183500 | WILLARD CO2 SEPARATION PLANT   | YOAKUM     | 17     |
| 192480 | JENKINS UNIT SATELLITE 2 AND C | GAINES     | 17     |
| 186204 | KEYSTONE CATTLE 404 BATTERY    | WINKLER    | 17     |
| 189837 | SOLVAY SPECIALTY POLYMERS USA  | ORANGE     | 16     |
| 185032 | PENN UNIT ABCD BATTERY ANDRES  | ANDREWS    | 16     |
| 191948 | TOTAL PETRO CHEMICALS & REFINI | JEFFERSON  | 16     |
| 191051 | WHARTON UNIT TANK BATTERY      | GAINES     | 16     |
| 179049 | N COWDEN UNIT TS 26            | ECTOR      | 16     |
| 182985 | RUSSELL COMPRESSOR STATION     | GAINES     | 16     |
| 179199 | CAG 437 SATELLITE BATTERY      | ECTOR      | 16     |
| 188386 | SSU SATELLITE 1 14             | HOCKLEY    | 16     |
| 188372 | SSU SATELLITE 1 10             | HOCKLEY    | 16     |
| 188390 | SSU SATELLITE 1 16             | HOCKLEY    | 16     |
| 192270 | INVISTA SARL                   | VICTORIA   | 16     |
| 188388 | SATELLITE NO 15                | HOCKLEY    | 16     |
| 183431 | ENTERPRISE MONT BELVIEU COMPLE | CHAMBERS   | 16     |
| 188611 | MALLET CO2 RECOVERY PLANT      | HOCKLEY    | 16     |
| 188613 | LEVELLAND BOOSTER              | HOCKLEY    | 16     |
| 188612 | MALLET CO2 RECOVERY PLANT      | HOCKLEY    | 16     |
| 181586 | TOTAL PETRO CHEMICALS & REFINI | JEFFERSON  | 15     |
| 178612 | SHELL OIL DEER PARK            | HARRIS     | 15     |
| 177703 | GOLDSMITH GAS PLANT            | ECTOR      | 15     |
| 187758 | GOLDSMITH LANDRETH DEEP UNIT S | ECTOR      | 15     |
| 203580 | ROBERTSON CLEARFORK INIT SAT 1 | GAINES     | 15     |
| 186581 | BORGER REFINERY                | HUTCHINSON | 14     |
| 180292 | FULLERTON CLEARFORK 200 5      | ANDREWS    | 14     |
| 180293 | FULLERTON CLEARFORK UNIT SUBBA | ANDREWS    | 14     |
| 189038 | WA COONS BATTERY               | HOCKLEY    | 14     |
| 189039 | NORTH MALLET TEST 8 OIL AND GA | HOCKLEY    | 14     |
| 189036 | EAST MALLET CENTRAL TANK BATTE | HOCKLEY    | 14     |
| 188798 | SOUTHEAST LEVELLAND UNIT PGG   | HOCKLEY    | 14     |
| 188640 | WEST RKM UNIT BATTERY 2        | HOCKLEY    | 14     |
| 203892 | CLYDE COWDEN BATTERY 2         | ECTOR      | 14     |
| 188644 | SOUTH WATER INJECTION          | HOCKLEY    | 14     |
| 190148 | WAGNER COMPRESSOR SITE         | JOHNSON    | 14     |
| 187665 | STANLEY CPF A                  | WEBB       | 14     |
| 190407 | BORGER REFINERY                | HUTCHINSON | 14     |
| 180331 | GARDENDALE SOUTH PGS GARDENDAL | LA SALLE   | 14     |
| 183167 | FULLERTON CLEARFORK 200 5      | ANDREWS    | 14     |
| 189074 | TILDEN GAS PLANT               | MCMULLEN   | 14     |
| 203570 | JENKINS UNIT SATELLITE 2 AND C | GAINES     | 14     |
| 182693 | SWEENY REFINERY                | BRAZORIA   | 14     |
| 180527 | CLYDE COWDEN BATTERY 1         | ECTOR      | 14     |
| 203575 | SYCO NO 1 TANK BATTERY         | GAINES     | 14     |
| 191018 | BORGER REFINERY                | HUTCHINSON | 14     |
| 203577 | ROBERTSON UNIT TANK BATTERY    | GAINES     | 14     |
| 184532 | GOLDSMITH LANDRETH DEEP UNIT S | ECTOR      | 14     |
| 180235 | LCRA SAM SEYMOUR FAYETTE POWER | FAYETTE    | 14     |
| 190041 | DENVER UNIT 2 RECOVERY PLANT   | YOAKUM     | 13     |
| 189806 | MALLET CO2 RECOVERY PLANT      | HOCKLEY    | 13     |
| 189938 | MALLET CO2 RECOVERY PLANT      | HOCKLEY    | 13     |
| 192187 | UNIVERSITY BLOCK9 CE TANK BATT | ANDREWS    | 13     |
| 192188 | PENN UNIT ABCD BATTERY ANDRES  | ANDREWS    | 13     |
| 204987 | AMERADA HESS SEMINOLE GAS PROC | GAINES     | 13     |
| 189675 | OWENS CORNING ROOFING AND ASPH | DALLAS     | 13     |
| 180525 | GSAU 2 2 BATTERY               | ECTOR      | 13     |
| 180524 | GSAU 1 147 PUMP OUT            | ECTOR      | 13     |
| 189151 | PRENTICE NE LACT 2 TANK BATTER | TERRY      | 13     |
| 189152 | PRENTICE NE 2 TANK BATTERY     | TERRY      | 13     |
| 191930 | OWENS CORNING ROOFING AND ASPH | DALLAS     | 13     |
| 182039 | DUCRP COMPRESSION STATION 2    | YOAKUM     | 13     |
| 178443 | GOLDSMITH GAS PLANT            | ECTOR      | 13     |
| 182682 | STEPHENSON LAS A PAD           | LA SALLE   | 13     |
| 203229 | LONE STAR PROCESSING FACILITY  | BEE        | 13     |
| 185108 | EASTMAN CHEMICAL TEXAS OPERATI | HARRISON   | 13     |
| 182424 | E WADDELL RANCH SAT 38         | CRANE      | 13     |
| 191635 | GSAU 2 2 BATTERY               | ECTOR      | 13     |
| 191526 | BORGER REFINERY                | HUTCHINSON | 13     |
| 177947 | DOW TEXAS OPERATIONS FREEPORT  | BRAZORIA   | 13     |
| 184501 | MIDLAND FARMS UNIT NORTH FLARE | ECTOR      | 13     |
| 184577 | CLYDE COWDEN BATTERY 5         | ECTOR      | 13     |
| 180312 | GOLDSMITH LANDRETH DEEP UNIT S | ECTOR      | 13     |
| 180311 | GOLDSMITH LANDRETH DEEP UNIT S | ECTOR      | 13     |
| 180313 | GLDU STATION 8                 | ECTOR      | 13     |
| 184575 | CLYDE COWDEN BATTERY 2         | ECTOR      | 13     |

### Popular counties

```sql
select county as County, count(id) as Freq
from emissions_emissionevent
where emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
GROUP BY county
ORDER BY Freq DESC;
```

| County        | frq |
|---------------|-----|
| ECTOR         | 757 |
| CRANE         | 463 |
| ANDREWS       | 415 |
| HARRIS        | 303 |
| GAINES        | 271 |
| WINKLER       | 234 |
| JEFFERSON     | 196 |
| MCMULLEN      | 187 |
| HOCKLEY       | 153 |
| DIMMIT        | 149 |
| BRAZORIA      | 117 |
| CHAMBERS      | 117 |
| PECOS         | 111 |
| WARD          | 107 |
| HOWARD        | 95  |
| NUECES        | 78  |
| MIDLAND       | 77  |
| REAGAN        | 66  |
| VICTORIA      | 64  |
| HUTCHINSON    | 61  |
| BOWIE         | 59  |
| DALLAS        | 59  |
| YOAKUM        | 53  |
| ELLIS         | 45  |
| GALVESTON     | 45  |
| MARTIN        | 44  |
| UPTON         | 44  |
| ORANGE        | 42  |
| MOORE         | 41  |
| FREESTONE     | 41  |
| HARRISON      | 39  |
| SAN PATRICIO  | 34  |
| PANOLA        | 34  |
| LA SALLE      | 34  |
| JASPER        | 32  |
| ZAVALA        | 31  |
| RUSK          | 30  |
| FAYETTE       | 29  |
| BORDEN        | 28  |
| MONTAGUE      | 26  |
| KENT          | 24  |
| JACKSON       | 24  |
| REEVES        | 23  |
| MCLENNAN      | 23  |
| CROCKETT      | 22  |
| IRION         | 22  |
| TITUS         | 22  |
| HALE          | 21  |
| WISE          | 21  |
| CALHOUN       | 20  |
| FRIO          | 20  |
| CAMP          | 19  |
| DAWSON        | 19  |
| ATASCOSA      | 18  |
| SMITH         | 17  |
| SCURRY        | 17  |
| GLASSCOCK     | 17  |
| BEE           | 16  |
| STERLING      | 16  |
| COCHRAN       | 15  |
| BEXAR         | 15  |
| HENDERSON     | 15  |
| VAN ZANDT     | 15  |
| TRAVIS        | 14  |
| NACOGDOCHES   | 13  |
| GRIMES        | 12  |
| GARZA         | 11  |
| LOVING        | 11  |
| KARNES        | 10  |
| CASS          | 9   |
| LIMESTONE     | 9   |
| TERRY         | 8   |
| UPSHUR        | 8   |
| WHEELER       | 7   |
| LIVE OAK      | 7   |
| MATAGORDA     | 7   |
| POTTER        | 7   |
| CAMERON       | 7   |
| COMAL         | 7   |
| WEBB          | 6   |
| FORT BEND     | 6   |
| HAYS          | 6   |
| MILAM         | 6   |
| WICHITA       | 5   |
| TARRANT       | 5   |
| HANSFORD      | 4   |
| EL PASO       | 4   |
| MARION        | 4   |
| JOHNSON       | 4   |
| KLEBERG       | 4   |
| COKE          | 4   |
| KAUFMAN       | 4   |
| GRAY          | 4   |
| DUVAL         | 4   |
| WILBARGER     | 3   |
| DEWITT        | 3   |
| ROBERTSON     | 3   |
| WHARTON       | 3   |
| DENTON        | 3   |
| CALDWELL      | 3   |
| JIM HOGG      | 3   |
| RANDALL       | 2   |
| CARSON        | 2   |
| MONTGOMERY    | 2   |
| PARKER        | 2   |
| TYLER         | 2   |
| NAVARRO       | 2   |
| HEMPHILL      | 2   |
| LAMB          | 2   |
| ANGELINA      | 2   |
| GUADALUPE     | 2   |
| DEAF SMITH    | 2   |
| NEWTON        | 2   |
| COLLIN        | 2   |
| JACK          | 2   |
| WILLIAMSON    | 2   |
| LEE           | 2   |
| POLK          | 2   |
| OCHILTREE     | 2   |
| GRAYSON       | 1   |
| WOOD          | 1   |
| SAN JACINTO   | 1   |
| HIDALGO       | 1   |
| MITCHELL      | 1   |
| RAINS         | 1   |
| STEPHENS      | 1   |
| SAN AUGUSTINE | 1   |
| JIM WELLS     | 1   |
| TAYLOR        | 1   |
| AUSTIN        | 1   |
| ZAPATA        | 1   |
| HARDIN        | 1   |
| HUNT          | 1   |
| MADISON       | 1   |
| VAL VERDE     | 1   |
| CLAY          | 1   |
| BRAZOS        | 1   |
| HOOD          | 1   |
| SUTTON        | 1   |
| COLORADO      | 1   |
| SHERMAN       | 1   |
| KENEDY        | 1   |
| LIPSCOMB      | 1   |

### Popular regulated entities

```sql
select regulated_entity_name as regulated_entity,
county,
count(id) as freq
from emissions_emissionevent
where emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
GROUP BY regulated_entity_name
ORDER BY freq DESC;
```

| Regulated Entity               | County       | frq |
|--------------------------------|--------------|-----|
| TILDEN GAS PLANT               | MCMULLEN     | 171 |
| KEYSTONE GAS PLANT             | WINKLER      | 147 |
| MALLET CO2 RECOVERY PLANT      | HOCKLEY      | 94  |
| GOLDSMITH GAS PLANT            | ECTOR        | 81  |
| RUSSELL COMPRESSOR STATION     | GAINES       | 73  |
| WAHA GAS PLANT                 | PECOS        | 69  |
| MABEE RANCH C02 PLANT          | ANDREWS      | 69  |
| INVISTA SARL                   | VICTORIA     | 66  |
| RED RIVER ARMY DEPOT           | BOWIE        | 59  |
| LBR CS & CTB 1                 | DIMMIT       | 56  |
| ENTERPRISE MONT BELVIEU COMPLE | CHAMBERS     | 56  |
| OWENS CORNING ROOFING AND ASPH | DALLAS       | 52  |
| GOLDSMITH LANDRETH DEEP UNIT S | ECTOR        | 50  |
| FLINT HILLS RESOURCES PORT ART | JEFFERSON    | 47  |
| HAMILTON CS & CTB 1            | DIMMIT       | 46  |
| MIDKIFF GAS PLANT              | REAGAN       | 44  |
| NORTH RILEY CENTRAL BATTERY    | GAINES       | 41  |
| DOW TEXAS OPERATIONS FREEPORT  | BRAZORIA     | 40  |
| ANDREWS BOOSTER STATION        | ANDREWS      | 38  |
| ALON USA BIG SPRING REFINERY   | HOWARD       | 34  |
| SHERWIN ALUMINA PLANT          | SAN PATRICIO | 32  |
| CHITTIM F1H PRODUCTION FACILIT | ZAVALA       | 31  |
| CARTHAGE ORIENTED STRANDBOARD  | PANOLA       | 30  |
| TOTAL PETRO CHEMICALS & REFINI | JEFFERSON    | 29  |
| SNEED BOOSTER STATION          | MOORE        | 29  |
| BORGER REFINERY                | HUTCHINSON   | 29  |
| ASH GROVE CEMENT               | ELLIS        | 29  |
| FULLERTON GAS PLANT            | ANDREWS      | 28  |
| NASA JOHNSON SPACE CENTER      | HARRIS       | 28  |
| JT MCELROY 202 TB              | CRANE        | 28  |
| SAND HILLS GAS PLANT           | CRANE        | 28  |
| BEAUMONT PLANT                 | JEFFERSON    | 27  |
| FULLERTON CLEARFORK 200 5      | ANDREWS      | 27  |
| REINECKE CTB AND CO2 RECYCLE F | BORDEN       | 27  |
| MCELROY SECTION 199 EMERGENCY  | CRANE        | 27  |
| LCRA SAM SEYMOUR FAYETTE POWER | FAYETTE      | 27  |
| JASPER ORIENTED STRANDBOARD OS | JASPER       | 27  |
| EXXON MOBIL BAYTOWN FACILITY   | HARRIS       | 26  |
| DOLLARHIDE GAS PLANT           | ANDREWS      | 26  |
| SOUTH FULLERTON BOOSTER STATIO | ANDREWS      | 26  |
| FLINT HILLS RESOURCES CORPUS C | NUECES       | 25  |
| BLANCHARD REFINING GALVESTON B | GALVESTON    | 25  |
| JACKSON COUNTY GAS PLANT       | JACKSON      | 24  |
| MARTIN LAKE STEAM ELECTRIC STA | RUSK         | 24  |
| WEST SEMINOLE SAN ANDRES UNIT  | GAINES       | 23  |
| SWEENY REFINERY                | BRAZORIA     | 23  |
| MIDLAND FARMS CENTRAL TANK BAT | ANDREWS      | 23  |
| MARSHALL PLANT                 | HARRISON     | 22  |
| WEST WADDELL RANCH SAT217      | CRANE        | 22  |
| RILEY BOOSTER STATION          | GAINES       | 22  |
| WEST WADDELL RANCH SAT220      | CRANE        | 21  |
| PENN UNIT ABCD BATTERY ANDRES  | ANDREWS      | 20  |
| DUPONT SABINE RIVER WORKS      | ORANGE       | 20  |
| VALERO PORT ARTHUR REFINERY    | JEFFERSON    | 20  |
| BELVAN MIDWAY LANE GAS PLANT   | CROCKETT     | 20  |
| SID RICHARDSON CARBON BORGER P | HUTCHINSON   | 20  |
| PARKS BOOSTER COMPRESSOR STATI | MIDLAND      | 20  |
| LDH ENERGY MONT BELVIEU FRACTI | CHAMBERS     | 20  |
| CHEVRON PHILLIPS CHEMICAL SWEE | BRAZORIA     | 20  |
| WEST WADDELL RANCH SAT221      | CRANE        | 19  |
| SHELL OIL DEER PARK            | HARRIS       | 19  |
| SALT CREEK GAS PLANT           | KENT         | 19  |
| LUTHER BOOSTER STATION         | HOWARD       | 19  |
| WELCH CO2 GAS PROCESSING FACIL | DAWSON       | 19  |
| WEST WADDELL RANCH SAT244      | CRANE        | 19  |
| PITTSBURG GAS PLANT            | CAMP         | 19  |
| BIG BROWN STEAM ELECTRIC STATI | FREESTONE    | 18  |
| CHAP BOOSTER STATION           | MIDLAND      | 18  |
| ANTON CO2 RE-INJECTION FACILIT | HALE         | 18  |
| CEDAR LAKE BOOSTER STATION     | GAINES       | 18  |
| FULLERTON CLEARFORK UNIT SUBBA | ANDREWS      | 18  |
| PORT ARTHUR REFINERY           | JEFFERSON    | 18  |
| WEST WADDELL RANCH BAT316      | CRANE        | 17  |
| ENTERPRISE EAST                | CHAMBERS     | 17  |
| MONTICELLO STEAM ELECTRIC STAT | TITUS        | 16  |
| CAG 437 SATELLITE BATTERY      | ECTOR        | 16  |
| AMERADA HESS SEMINOLE GAS PROC | GAINES       | 16  |
| SAN MIGUEL ELECTRIC PLANT      | ATASCOSA     | 16  |
| OWENS-BROCKWAY GLASS CONTAINER | MCLENNAN     | 16  |
| DELEK TYLER REFINERY           | SMITH        | 16  |
| VALERO CORPUS CHRISTI REFINERY | NUECES       | 16  |
| CREDO BOOSTER STATION          | STERLING     | 16  |
| SLAUGHTER GASOLINE PLANT       | HOCKLEY      | 15  |
| EUSTACE GAS PLANT              | HENDERSON    | 15  |
| CAG 480 SATELLITE BATTERY      | ECTOR        | 15  |
| UNIVERSITY BLOCK9 CE TANK BATT | ANDREWS      | 15  |
| CHEVRON PHILLIPS CHEMICAL CEDA | HARRIS       | 15  |
| LANCASTER RANCH COMPRESSOR STA | FRIO         | 15  |
| TEAGUE PLANT                   | FREESTONE    | 15  |
| GANDU 36 BATTERY               | ECTOR        | 15  |
| BIG LAKE GAS PLANT             | REAGAN       | 14  |
| WEST WADDELL RANCH BAT353      | CRANE        | 14  |
| HUNTSMAN PORT NECHES           | JEFFERSON    | 14  |
| WEST WADDELL RANCH SAT191      | CRANE        | 14  |
| KEYSTONE CATTLE 404 BATTERY    | WINKLER      | 14  |
| SAN PEDRO RANCH CTB 9          | DIMMIT       | 14  |
| OWENS CORNING INSULATING SYSTE | ELLIS        | 14  |
| WAHA GAS PLANT                 | REEVES       | 14  |
| E WADEL RCH BAT140 SAT633      | CRANE        | 14  |
| ANDECTOR BOOSTER STATION       | ECTOR        | 14  |
| BENEDUM GAS PLANT              | UPTON        | 14  |
| TARZAN BOOSTER STATION MARTIN  | MARTIN       | 13  |
| HOUSTON PLANT                  | HARRIS       | 13  |
| MYRTLE SPRINGS COMPRESSOR STAT | VAN ZANDT    | 13  |
| FULLERTON FIELD SAT 2004       | ANDREWS      | 12  |
| GIBBONS CREEK STEAM ELECTRIC S | GRIMES       | 12  |
| GSMITH LANDRETH DEEP ST12      | ECTOR        | 12  |
| WN WADDELL TB 11               | CRANE        | 12  |
| FULLERTON SATELLITE TANK BATTE | ANDREWS      | 12  |
| CLYDE COWDEN BATTERY 5         | ECTOR        | 12  |
| WEST WADDELL RANCH SAT137      | CRANE        | 12  |
| EASTMAN CHEMICAL TEXAS OPERATI | HARRISON     | 12  |
| WEST WADDELL RANCH SAT 14      | CRANE        | 12  |
| MIDLAND FARMS UNIT NORTH FLARE | ECTOR        | 12  |
| ST JO PROCESSING PLANT         | MONTAGUE     | 12  |
| WEIR BOOSTER STATION           | UPTON        | 12  |
| E WADDELL RANCH BAT 265        | CRANE        | 12  |
| CEDAR HILL GAS PLANT           | GARZA        | 11  |
| CAG 120 SATELLITE BATTERY      | ECTOR        | 11  |
| BLALOCK BOOSTER STATION        | GLASSCOCK    | 11  |
| NORBORD TEXAS NACOGDOCHES      | NACOGDOCHES  | 11  |
| JAVELINA GAS PROCESSING FACILI | NUECES       | 11  |
| DRIVER GAS PLANT               | MIDLAND      | 11  |
| EAST WADDEL RANCH BATT 52      | CRANE        | 11  |
| INVISTA SARL SABINE RIVER SITE | ORANGE       | 11  |
| ALCOA POINT COMFORT OPERATIONS | CALHOUN      | 11  |
| CAG 511 SATELLITE BATTERY      | ECTOR        | 11  |
| WEST WADDELL COMPRESSOR STATIO | CRANE        | 10  |
| CAG 446 D SATELLITE BATTERY    | ECTOR        | 10  |
| N COWDEN UNIT TS 22            | ECTOR        | 10  |
| HUTTO BOOSTER STATION          | HOWARD       | 10  |
| CLYDE COWDEN BATTERY 1         | ECTOR        | 10  |
| GREENWOOD COMPRESSOR STATION   | WISE         | 10  |
| N COWDEN UNIT TS 20            | ECTOR        | 10  |
| CAG CENTRAL BATTERY NO 448     | ECTOR        | 10  |
| GOLDSMITH C02 PILOT PHASE II F | ECTOR        | 10  |
| SAN PEDRO RANCH CTB 10         | DIMMIT       | 10  |
| CLYDE COWDEN BATTERY 7         | ECTOR        | 10  |
| GANDU 26 FRANK B BATTERY       | ECTOR        | 10  |
| VALERO MCKEE REFINERY          | MOORE        | 10  |
| EAST WADDELL RANCH BAT 11      | CRANE        | 10  |
| LEHMAN COMPRESSOR STATION      | COCHRAN      | 10  |
| EAST WADDELL RANCH BATTERY 72  | CRANE        | 10  |
| ROBERTSON CLEARFORK SATELLITE  | GAINES       | 9   |
| WN WADDELL NO 290 TB           | CRANE        | 9   |
| TEXARKANA MILL                 | CASS         | 9   |
| EXXONMOBIL BEAUMONT REFINERY   | JEFFERSON    | 9   |
| KEYSTONE CATTLE 301 BATTERY    | WINKLER      | 9   |
| GARDENDALE SOUTH PGS GARDENDAL | LA SALLE     | 9   |
| SEALY SMITH COMPRESSOR STATION | WARD         | 9   |
| GSAU 1 147 PUMP OUT            | ECTOR        | 9   |
| HEADLEE GAS PLANT              | ECTOR        | 9   |
| STOLTHAVEN HOUSTON TERMINAL    | HARRIS       | 9   |
| A 1O HUTT COMPRESSOR STATION   | MIDLAND      | 9   |
| WEST WADDELL RANCH SAT521      | CRANE        | 9   |
| SACROC CARBON DIOXIDE TREATMEN | SCURRY       | 9   |
| N COWDEN UNIT TEST STA 9       | ECTOR        | 9   |
| CITGO CORPUS CHRISTI REFINERY  | NUECES       | 9   |
| SALE RANCH GAS PLANT           | MARTIN       | 9   |
| ASCEND PERFORMANCE MATERIALS C | BRAZORIA     | 9   |
| LIMESTONE ELECTRIC GENERATING  | LIMESTONE    | 9   |
| N COWDEN UNIT TEST SATELLITE 1 | ECTOR        | 9   |
| CHALK NORTH BATTERY            | HOWARD       | 8   |
| CLYDE COWDEN BATTERY 6         | ECTOR        | 8   |
| JED CLAMPETT PRODUCTION FACILI | GAINES       | 8   |
| SAMSUNG AUSTIN SEMICONDUCTOR   | TRAVIS       | 8   |
| JE PARKER TANK BATTERY         | ANDREWS      | 8   |
| WEST WADDELL RANCH BAT 67      | CRANE        | 8   |
| E WADDELL RANCH SAT 38         | CRANE        | 8   |
| EAST WADDELL RANCH BAT116      | CRANE        | 8   |
| DENVER UNIT 2 RECOVERY PLANT   | YOAKUM       | 8   |
| N COWDEN UNIT TEST STA 10      | ECTOR        | 8   |
| EQUISTAR CHEMICALS LA PORTE CO | HARRIS       | 8   |
| AGRIUM US BORGER NITROGEN OPER | HUTCHINSON   | 8   |
| CLYDE COWDEN SATELLITE 4       | ECTOR        | 8   |
| BRIDGEPORT GAS PLANT           | WISE         | 8   |
| N COWDEN UNIT TEST STN 3       | ECTOR        | 8   |
| N COWDEN UNIT TS 15            | ECTOR        | 8   |
| WEST WADDELL RANCH SAT311      | CRANE        | 8   |
| WEST WADDELL RANCH SAT 1       | CRANE        | 8   |
| CENTRAL ROBERTSON CLEARFORK UN | GAINES       | 8   |
| N COWDEN UNIT TS 26            | ECTOR        | 8   |
| CLYDE COWDEN BATTERY 2         | ECTOR        | 8   |
| GLDU STATION 4                 | ECTOR        | 8   |
| CHANNELVIEW COMPLEX            | HARRIS       | 8   |
| STATE UNIVERSITY ATAUBA BATTER | ANDREWS      | 8   |
| WEST ANDREWS BOOSTER STATION   | ANDREWS      | 8   |
| RHODES COWDEN UNIT CENTRAL BAT | ECTOR        | 8   |
| WEST WADDELL RANCH SAT 59      | CRANE        | 8   |
| EW ESTES 133 AUXILIARY         | WARD         | 7   |
| N COWDEN UNIT TEST STA 23      | ECTOR        | 7   |
| NPU 1 & MILLARD C TANK BATTERY | ECTOR        | 7   |
| LONE STAR PROCESSING FACILITY  | BEE          | 7   |
| CAPITOL CEMENT PLANT           | BEXAR        | 7   |
| H O MAHONEY TANK BATTERY       | YOAKUM       | 7   |
| LEVELLAND BOOSTER              | HOCKLEY      | 7   |
| FLINT HILLS RESOURCES EAST REF | NUECES       | 7   |
| PAWNEE TREATING PLANT          | BEE          | 7   |
| N COWDEN UNIT TS 18            | ECTOR        | 7   |
| SAN PEDRO RANCH CTB 7 CS 4     | DIMMIT       | 7   |
| GW OBRIEN 231 AUXILIARY        | WARD         | 7   |

### Contaminants in selected emission types

```sql
SELECT emissions_contaminantreleased.contaminant_parameterized AS contaminant,
COUNT(emissions_contaminantreleased.id) as frequency
FROM emissions_contaminantreleased
JOIN emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number)
WHERE
  emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
GROUP BY emissions_contaminantreleased.contaminant_parameterized
ORDER BY frequency DESC;
```

| Contaminant                               | freq |
|-------------------------------------------|------|
| carbon-monoxide                           | 3873 |
| hydrogen-sulfide                          | 3670 |
| sulfur-dioxide                            | 3617 |
| nox                                       | 1475 |
| opacity                                   | 1446 |
| propane                                   | 1143 |
| natural-gas                               | 1112 |
| non-methane-non-ethane-natural-gas        | 732  |
| nitrogen-oxide                            | 668  |
| butane-n                                  | 632  |
| nitrogen-oxides-nox                       | 617  |
| nitrogen-oxides                           | 610  |
| isobutane                                 | 530  |
| pentane-n                                 | 523  |
| benzene                                   | 483  |
| hexanes                                   | 467  |
| ethylene-gaseous                          | 461  |
| oxides-of-nitrogen-nox                    | 412  |
| nitrogen-dioxide                          | 384  |
| pentane-iso                               | 355  |
| butane-i                                  | 349  |
| voc-light-hydrocarbons                    | 342  |
| butane                                    | 334  |
| isopentane                                | 317  |
| voc                                       | 308  |
| nitrogen-monoxide                         | 300  |
| pentane                                   | 270  |
| toluene                                   | 261  |
| propylene-propene                         | 253  |
| particulate-matter                        | 250  |
| hexane                                    | 216  |
| propylene                                 | 201  |
| vocs                                      | 196  |
| co                                        | 184  |
| ethylbenzene                              | 176  |
| 1-3-butadiene                             | 174  |
| voc-unspeciated                           | 169  |
| trans-2-butene                            | 119  |
| cis-2-butene                              | 114  |
| propane-n                                 | 113  |
| butanes                                   | 104  |
| ethane                                    | 101  |
| butenes-all-isomers                       | 100  |
| voc-nonmethane                            | 99   |
| isobutylene                               | 92   |
| octane                                    | 91   |
| xylene                                    | 87   |
| 1-butene                                  | 87   |
| methane                                   | 85   |
| butadiene-1-3                             | 84   |
| pentanes                                  | 84   |
| natural-gas-vocs                          | 83   |
| heptane-or-n                              | 82   |
| acetylene                                 | 79   |
| butene                                    | 77   |
| xylenes                                   | 68   |
| c5-not-including-benzene                  | 64   |
| decane                                    | 64   |
| voc-gas-mixture                           | 59   |
| ammonia                                   | 56   |
| other                                     | 51   |
| n-butane                                  | 50   |
| cyclohexane                               | 47   |
| smoke                                     | 43   |
| pm10                                      | 43   |
| pentenes                                  | 42   |
| heptanes                                  | 39   |
| n-pentane                                 | 38   |
| hexane-plus                               | 38   |
| carbon-disulfide                          | 37   |
| octanes                                   | 37   |
| hydrogen                                  | 34   |
| hydrogen-cyanide                          | 34   |
| styrene                                   | 33   |
| isobutene                                 | 32   |
| hexane-n                                  | 32   |
| pm-unspeciated                            | 32   |
| i-pentane                                 | 31   |
| i-butane                                  | 29   |
| heptane-n                                 | 29   |
| carbon-dioxide                            | 27   |
| calcined-alumina-dust                     | 27   |
| ethylene-oxide                            | 27   |
| xylene-mixed-isomers                      | 26   |
| nonane                                    | 25   |
| acrylonitrile                             | 24   |
| voc-unclassified                          | 24   |
| carbonal-sulfite                          | 22   |
| other-vocs                                | 22   |
| sulfur-dioxide-anhydrous                  | 20   |
| hexene                                    | 20   |
| methanol                                  | 20   |
| nitric-oxide                              | 19   |
| voc-unspecified                           | 16   |
| nitrous-oxide                             | 16   |
| naphthalene                               | 16   |
| butylene                                  | 16   |
| alumina-hydrate-dust                      | 16   |
| carbonyl-sulfide                          | 16   |
| acetonitrile                              | 16   |
| pentene                                   | 15   |
| volatile-organic-compounds                | 15   |
| n-hexane-110543                           | 15   |
| cumene                                    | 14   |
| ammonia-anhydrous                         | 14   |
| nonanes                                   | 14   |
| n-hexane                                  | 14   |
| acetone                                   | 14   |
| butenes                                   | 14   |
| unspeciated-vocs                          | 13   |
| c6                                        | 13   |
| c5-plus                                   | 13   |
| propadiene                                | 12   |
| methyl-acetylene                          | 12   |
| vinyl-chloride                            | 11   |
| acrolein                                  | 11   |
| cyclopentadiene                           | 11   |
| pentenenitrile                            | 11   |
| nitrogen                                  | 11   |
| catalyst-fines                            | 11   |
| cyclopentane                              | 10   |
| hcn                                       | 10   |
| 1-pentene                                 | 10   |
| ethyl-benzene                             | 10   |
| vinyl-acetate                             | 10   |
| propene                                   | 10   |
| 2-2-4-trimethylpentane                    | 9    |
| methacrylic-acid                          | 9    |
| trans-butene-2                            | 9    |
| voc-mixture                               | 9    |
| 1-2-4-trimethylbenzene                    | 9    |
| methylacetylene                           | 9    |
| methylcyclohexane                         | 9    |
| isoprene                                  | 9    |
| octene                                    | 8    |
| 2-methyl-2-butene                         | 8    |
| nox-startup-shutdown                      | 8    |
| vinyl-acetylene                           | 8    |
| sulfuric-acid                             | 8    |
| anhydrous-ammonia                         | 8    |
| ethylene-liquid                           | 7    |
| formaldehyde                              | 7    |
| cyclopentene                              | 7    |
| ethanol                                   | 7    |
| dimethylethanolamine                      | 7    |
| t-butyl-alcohol                           | 7    |
| methylcyclopentane                        | 7    |
| lead                                      | 7    |
| biphenyl                                  | 7    |
| cis-butene-2                              | 7    |
| hexene-1                                  | 7    |
| other-organics                            | 7    |
| methyl-mercaptan                          | 6    |
| pm10-calcium-carbonate-caco3              | 6    |
| trimethylbenzene                          | 6    |
| propylene-glycol-monomethyl-ether-acetate | 6    |
| undecane                                  | 6    |
| chlorine                                  | 6    |
| nmne-natural-gas                          | 6    |
| methylcyclopentadiene                     | 6    |
| propylene-oxide                           | 6    |
| indene                                    | 6    |
| butanol                                   | 6    |
| hydrogen-chloride                         | 6    |
| diethylene-glycol-monohexyl-ether         | 6    |
| xylene-o                                  | 5    |
| butene-1                                  | 5    |
| xylene-p                                  | 5    |
| hydrocarbons                              | 5    |
| cyclohexanone                             | 5    |
| isohexane                                 | 5    |
| isobutyl-alcohol                          | 5    |
| soda-ash                                  | 5    |
| dimethyl-ether                            | 5    |
| n-heptane                                 | 5    |
| cyclohexanol                              | 5    |
| 1-butene-isobutylene                      | 5    |
| n-butyl-acrylate                          | 5    |
| 1-2-butadiene                             | 5    |
| iso-octane                                | 5    |
| methyl-acetate                            | 5    |
| nickel                                    | 5    |
| 2-butoxyethanol                           | 5    |
| ethyltoluene                              | 5    |
| decanes                                   | 5    |
| dicyclopentadiene                         | 5    |
| 2-butene-cis                              | 5    |
| 2-butene-trans                            | 4    |
| t-2-butene                                | 4    |
| p-xylene                                  | 4    |
| 2-ethyl-1-hexene                          | 4    |
| c15                                       | 4    |
| 2-methylbutene-2                          | 4    |
| crude-oil                                 | 4    |
| dodecane                                  | 4    |
| pentane-3-methyl                          | 4    |
| visible-emissions                         | 4    |
| m-xylene                                  | 4    |
| 3-methyl-hexane                           | 4    |
| ethyl-chloride                            | 4    |
| pentadiene                                | 4    |

## Authorization number freq

```sql
select distinct left(emissions_contaminantreleased.authorization, 30),
COUNT(emissions_contaminantreleased.id) as frequency
FROM emissions_contaminantreleased
JOIN emissions_emissionevent ON (
  emissions_contaminantreleased.tracking_number = emissions_emissionevent.tracking_number)
WHERE
  emissions_emissionevent.type_of_emission in (
  'air-shutdown',
  'air-startup',
  'emissions-event',
  'emissions-event-emergency-resp',
  'excess-opacity',
  'maintenance'
)
GROUP BY emissions_contaminantreleased.authorization
ORDER BY frequency DESC
LIMIT 200;
```

| Authorization   | freq |
|-----------------|------|
| Emergency Flari | 2234 |
| N/A             | 1535 |
| §101.201        | 1064 |
| AIR PERMIT ID # | 730  |
| 'No specific em | 566  |
| PBR             | 531  |
| 90277           | 494  |
| No specific Aut | 453  |
| Permit # 16842  | 450  |
| None            | 448  |
| permit #74857   | 360  |
| Allowable entry | 305  |
| TCEQ Air Permit | 300  |
| 8404            | 298  |
| Permit 46396    | 282  |
| §111.111        | 268  |
| No specific emi | 267  |
| 2724            | 255  |
| 116.715(a)      | 247  |
| RN102983533     | 240  |
| NA              | 224  |
| 106.492         | 222  |
| AIR PERMIT ID#5 | 210  |
| Air Permit # 53 | 210  |
| No specific emi | 200  |
| 5920A           | 195  |
| Permit 47256    | 195  |
| 30 TAC 111      | 182  |
| RN106416738     | 171  |
| No specific aut | 168  |
| No specific emi | 163  |
| Not specificall | 162  |
| SE 96 (01/08/19 | 159  |
| AIR PERMIT ID#5 | 150  |
| Permit No. 5269 | 145  |
| X-20759         | 141  |
| Not Listed on P | 127  |
| 76070 (as VOC)  | 125  |
| 83193 and PSDTX | 125  |
| NSR 9824A       | 124  |
| REGISTRATION PE | 123  |
| Air Permit # 53 | 120  |
| Normal Emission | 120  |
| 47256           | 118  |
| 6580/PSD-TX-151 | 118  |
| SP-73563        | 117  |
| 31588           | 115  |
| 38259           | 115  |
| Permit # 18406  | 113  |
| NSR 48944       | 112  |
| SOP O-2585      | 111  |
|                 | 109  |
| Permit 22690    | 106  |
| AIR PERMIT ID # | 100  |
| No Air Permit N | 100  |
| Permit # 53135  | 100  |
| RN106424336     | 100  |
| #20432          | 99   |
| 1867A/PSD-TX-10 | 99   |
| NSR Permit 6825 | 99   |
| 76070           | 95   |
| 1867a/PSD-TX-10 | 92   |
| Emergency Flari | 90   |
| No air permit i | 90   |
| Not specificall | 90   |
| RN#106848229    | 90   |
| PERMIT 46396    | 89   |
| AIR PERMIT ID # | 88   |
| NSR Permit 3219 | 87   |
| No Specific Aut | 85   |
| Permit #20660   | 85   |
| 1302 & PSD-TX-1 | 84   |
| 6056            | 84   |
| Permit No. R-89 | 84   |
| AIR PERMIT ID # | 80   |
| Air Permit ID # | 80   |
| 5144A           | 77   |
| No specific emi | 77   |
| no specific aut | 76   |
| None Permitted  | 75   |
| SE 96 - 01/08/1 | 75   |
| Permit #20432   | 73   |
| SE 96           | 73   |
| 49683           | 72   |
| Air Permit ID # | 72   |
| NSR Permit 9395 | 72   |
| n/a             | 72   |
| permit # 20432  | 72   |
| Permit 5955     | 71   |
| Portions may be | 71   |
| 31069           | 70   |
| No specific emi | 70   |
| PBR 46762       | 68   |
| Flex Permit 224 | 66   |
| No specific emi | 65   |
| 19823           | 63   |
| 30 TAC Chapter  | 63   |
| 901             | 63   |
| PN5920A         | 62   |
| Air Permit 1929 | 61   |
| 31064           | 60   |
| 82119           | 60   |
| AIR PERMIT ID # | 60   |
| No authorizatio | 60   |
| RN 106877954    | 60   |
| 20432           | 59   |
| 2167            | 59   |
| 30 TAC 111.111  | 59   |
| AIR PERMIT ID # | 59   |
| 8315A           | 58   |
| 46307           | 57   |
| PBR 27846       | 55   |
| 19732           | 54   |
| 76810           | 52   |
| NSR Permit No.  | 52   |
| Not Specificall | 52   |
| PBR 106.492     | 52   |
| Permit 676A     | 52   |
| Permit 19823    | 51   |
| 30550           | 50   |
| 30616           | 50   |
| 36644/PSDTX903/ | 50   |
| 80052           | 50   |
| AIR NEW SOURCE  | 50   |
| AIR PERMIT ID # | 50   |
| Air Permit 2600 | 50   |
| Air Permit ID # | 50   |
| ID 105808       | 50   |
| R-8986          | 50   |
| SP-77267        | 50   |
| 18978           | 49   |
| No Authorizatio | 49   |
| No specific aut | 49   |
| 21265           | 48   |
| NSR Permit No.  | 48   |
| No specific emi | 48   |
| 73140           | 47   |
| 6051 & PSDTX55M | 46   |
| 7467A           | 46   |
| 30191           | 45   |
| NSR 81011       | 45   |
| NSR permit 6825 | 45   |
| PORTIONS MAY BE | 44   |
| NO SPECIFIC EMI | 43   |
| Permit #53135   | 43   |
| Permit No. 8165 | 43   |
| 111.111         | 42   |
| No Known Author | 42   |
| No authorizatio | 42   |
| 810             | 41   |
| No Authorized L | 41   |
| Portions of the | 41   |
| 29248           | 40   |
| 30098           | 40   |
| 30192           | 40   |
| 30448           | 40   |
| 30551           | 40   |
| 41648           | 40   |
| 44032           | 40   |
| 48976           | 40   |
| 76076           | 40   |
| AIR PERMIT #224 | 40   |
| Air Permit # 33 | 40   |
| Standard Permit | 40   |
| TCEQ Air Permit | 40   |
| Permit # 77267  | 39   |
| Permit 51310    | 39   |
| 30 TAC 111.111( | 38   |
| 7186            | 38   |
| 21262           | 37   |
| Permit #91264   | 37   |
| 53117 (02/16/20 | 36   |
| 93973           | 36   |
| No Authorized L | 36   |
| 21123           | 35   |
| 30430           | 35   |
| 30447           | 35   |
| 30549           | 35   |
| 30618           | 35   |
| 31107           | 35   |
| 31615           | 35   |
| 33012           | 35   |
| 48982           | 35   |
| 54242           | 35   |
| 86003           | 35   |
| NO SPECIFIC EMI | 35   |
| Permit # 2211A  | 35   |
| Permit # O8414  | 35   |
| Permit # 676A   | 34   |
| Permit 19823 as | 34   |
| 100085          | 33   |
| 27846           | 33   |
| 56389           | 33   |
| 93973 (as VOC)  | 33   |
| 6051 & PSD-TX-5 | 32   |
| Allowable entry | 32   |
| NSR Permit 812  | 32   |
| O-02503 (10/19/ | 32   |
| Permit #17847 C | 32   |
| 116.715         | 31   |
