# Data notes

** Week 2 deliverable. ** Geodev Lab Africa, Cohort One.
Author: <Richard Bianca Ihuoma>

What i downloaded, where it came from, what is in it and what is wrong with it.


## Summary

| # | Dataset | Type | Retrieved | Status |
|---|---|---|---|---|
| 1 | GRID3 State Boundaries | Vector (Polygon) | 8/09/2026 | Complete |
| 2 | GRID3 LGA Boundaries | Vector (Polygon) | 8/09/2026 | Complete |
| 3 | GRID3 Ward Boundaries | Vector (Polygon) | 8/09/2026 | Complete |
| 4 | Settlement | Vector (point) | 26/02/2026 | Complete |
| 5 | OSM Waterways | Vector (LineString) | 16/09/2026 | Partial |
| 6 | Roads | Vector (LineString) | 16/09/2026 | Incomplete |
| 7| Building | Vector (LineString) | 16/09/2026 | Incomplete |


 ## GRID3 NGA - Operational State Boundaries
- **Source:** [GRID3 NGA Operational State Boundaries])
- **Downloaded:** 8/09/2026
- **Geometry type:** Polygon (MultiPolygon) — 37 features
- **Columns:** `globalid`, `uniq_id`,`timestamp`,`editor`,`state name`,`capacity `,`source`, `geozone`
- **Nulls:** No nulls in boundary fields
- **Quality note:** Used for state boundary covers my target LGA fully.

## GRID3 NGA - Operational LGA Boundaries
- **Source:** [https://data.grid3.org/](https://data.grid3.org/)
- **Downloaded:** 8/09/2026
- **Geometry type:** Polygon (MultiPolygon) — 774 features
- **Columns:** `globalid`, `uniq_id`,`timestamp`,`editor`,`lganame`(patani),`state name`(delta),`statecode `,`source`, `amapcode`  
- **Nulls:** No nulls in boundary fields
- **Quality note:** Used boundary covers my target LGA fully.

## GRID3 NGA - Operational Ward Boundaries
- **Source:** [[GRID3 NGA Operational Wards v3.0])
- **Downloaded:** 16/09/2026
- **Geometry type:** Polygon (MultiPolygon) — 5872 features
- **Columns:** `Country`, `iso3`,`state`,`statecode`,`lga`(patani),`lga_alt_na`,`ward `,`ward_alt_n`, `ward-v1_gr`, `ward_in_gr`,`multipart`,`source`, `date`
- **Nulls:** yes columns like lga_alt_na and ward-v1_gr
- **Quality note:** Ward boundary covers my target LGA fully.

## GRID3 NGA - Settlement
- **Source:** [[GRID3 NGA - Settlement Extents v4.1])
- **Downloaded:** 26/02/2026
- **Geometry type:**is_primary — 292,438 features
- **Columns:** `globalid`, `uniq_id`,`timestamp`,`editor`,`scdy_edtor,`wardname`,`wardcode `,`lganame`, `lgacode`, `statename`,`statecode`,`set_altnam`, `set_id`,`set_name`,`is_primary`,`source`
- **Nulls:** yes columns like scdy_edtor,set_altnam and is_primary
- **Quality note:** Settlement covers my target LGA fully.

## OSM Waterways (extracted via QuickOSM)
- **Query:** `waterway=*` in and within Patani
- **Extracted:** 27/09/2026
- **Geometry type:** Line (LineString) — 25 features
- **Columns:** `fid`, `full_id`,`osm_id`,`osm_type`,`Waterway(stream),`tunnel`,`layer `
- **Nulls:** Yes column like tunnel and layer has 23 null    
- **Quality note:** The extracted OSM river data shows clear representation of major rivers, while rural streams and smaller tributaries are not mapped, indicating sparse coverage in the outskirts.. 

## OSM Roads (extracted via QuickOSM)
- **Query:** `highway=*` in Patani
- **Extracted:** 16/09/2026
- **Geometry type:** Line (LineString) — 8 features
- **Columns:** `fid`, `full_id`,`osm_id`,`osm_type`,`highway(tertiary),`layer`,`bridge `,`surface`,
- **Nulls:** Yes columns like layer has 7 null out of 8 and bridge has 7 null and one yes
- 8 features have no surface tag, 1 has an unpaved surface tag.
- **Quality note:** Shows dense coverage in the urban core, while the outskirts have limited representation with only major roads mapped.

 ## OSM Building (extracted via QuickOSM)
- **Query:** `Building =*` in Patani
- **Extracted:** 27/09/2026
- **Columns:** `fid`, `full_id`,`osm_id`,`osm_type`,`building,
- **Geometry type:** Polygon (MultiPolygon) — 420 features
- **Nulls:** nil
- **Quality note:** The extracted OSM building data shows a bit of settlement in patani .

## Problem 
The extracted OSM river data shows clear representation of major rivers, while rural streams and smaller tributaries are not mapped, indicating sparse coverage in the outskirts..


Status: week 2 complete. reprojection and quality check in week 3. 




  






# Data notes
**Week 3 deliverable. ** Geodev Lab Africa, Cohort One.
Author: < Richard Bianca Ihuoma >

This document outlines the data cleaning, clipping, reprojection, and preprocessing steps performed on raw datasets to prepare them for spatial analysis.


## Grid3, state boundary 
GRID3-https://data.grid3.org/datasets/c41532b720504f4799fe20438b7e3b7f_0/explore?location=9.077959%2C8.685290%2C5#:~:text=GRID3%20NGA%20%2D%20Operational%20State%20Boundaries -
Extracted [2025] via Grid3, Boundary=*

37 features
**COMPLETENESS:** Coverage is strong in the built‑up areas like patani and other major towns.

**CURRENCY**: most edits 2025. 

**POSITIONAL:** align well with satellite imagery.

**ATTRIBUTE:** no surface tag and no Null.

**FITNESS:** Adequate for statewide accessibility analysis .


## Grid3, Lga boundary 
(https://data.grid3.org/datasets/2bb616a49ee84f409427cc2143787113_0/explore?location=9.077959%2C8.685290%2C5#:~:text=GRID3%20NGA%20%2D%20Operational%20LGA%20Boundaries)
Extracted [2026] via Grid3, Boundary=*

774 features
**COMPLETENESS:** Coverage is strong in the built‑up areas like patani and other major towns.

**CURRENCY**: most edits 2026. 

**POSITIONAL:** align well with satellite imagery.

**ATTRIBUTE:** yes columns like lga_alt_na and ward-v1_gr.

**FITNESS:** Adequate for statewide accessibility analysis .


## Grid3, Ward boundary 
(https://data.grid3.org/datasets/45cd2ef592094d12aca43113a90a6054_0/explore?location=9.077872%2C8.670771%2C5#:~:text=GRID3%20NGA%20%2D%20Operational%20Wards%20v3.0,-Private%20Member)
Extracted [2026] via Grid3, Boundary=*
5872 features

**COMPLETENESS:** 100% complete for Patani LGA. Covers all constituent electoral/administrative wards without gaps or overlapping boundary polygons.

**CURRENCY**: most edits 2026. 

**POSITIONAL:** Adequate macro-scale positional accuracy. Boundaries follow recognized geographic features, rivers, and local government lines

**ATTRIBUTE:** no surface tag and no Null.

**FITNESS:** Ideal for sub-LGA zonal statistics and spatial aggregation. .


## Grid3, settlement 
(https://data.grid3.org/datasets/f705d65c012c46748e6e5f44a33728b1_0/explore?location=9.079999%2C8.679167%2C5#:~:text=GRID3%20NGA%20%2D%20Settlement%20Extents%20v4.1
Extracted [2025] via Grid3, Boundary=*
292,438 features

**COMPLETENESS:** High coverage across Patani LGA. Most built-up areas, rural villages, and linear settlements along the River Niger and major roads are captured as polygons. However, very small isolated farmsteads or newly built structures are missed.

**CURRENCY**: most edits 2025. 

**POSITIONAL:** Settlement boundaries align closely with high-resolution satellite basemaps (

**ATTRIBUTE:** yes columns like scdy_edtor,set_altnam and is_primary.

**FITNESS:** Highly fit for spatial exposure and population vulnerability analysis. Directly enables counting or intersecting flooded settlement footprint areas against Sentinel-1 inundation layers.


## OSM roads, Patani Delta 
Extracted [date] via QuickOSM, water body=*

25 features

**COMPLETENESS:** High completeness for primary river channels (such as the main course of the River Niger and major distributaries like the Forcados River). Lower completeness for minor inland streams, seasonal flood channels, or dense swamp forest creeks, which was not be mapped in OpenStreetMap

**CURRENCY:** Moderate to High currency (2026)

**POSITIONAL:** Good positional accuracy for major permanent watercourses, aligning well with high-resolution satellite basemaps. However, seasonal riverbank shifts and dynamic floodplains mean boundaries may differ slightly from real-time flood extents.

**ATTRIBUTE:** Yes column like tunnel and layer has 23 null    

**FITNESS:** Highly fit as a baseline reference for permanent/dry-season open water.


## OSM roads, Patani Delta state
Extracted [date] via QuickOSM, highway=*

8 features

**COMPLETENESS:** Good coverage in built-up areas and primary transportation corridors (such as the East-West Road and main arterial town roads). Minor rural farm tracks, unpaved village paths, or newly built residential access roads may be incomplete or unmapped.

**CURRENCY:** Moderate currency (most edits cluster between 2019 and 2026)

**POSITIONAL:** Good positional accuracy.

**ATTRIBUTE:** non has a surface tag but has Null. 

**FITNESS:** adequate for access analysis in the built-up area. Not adequate for a paved-road question.


## OSM roads, Patani Delta 
Extracted [date] via QuickOSM, Building=*

420 features

**COMPLETENESS:** Moderate to High completeness across Patani LGA. Built-up hubs, formal administrative structures, and dense residential clusters along the River Niger and major transit corridors are mapped as distinct polygons. However, small informal structures, temporary rural farmsteads, and newly erected buildings post-dating the last satellite imagery scan are omitted.

**CURRENCY:** Up to date (derived from 2024–2026 satellite imagery extractions).

**POSITIONAL:** Good positional accuracy. Polygon boundaries align closely

**ATTRIBUTE:** Yes columns like layer has 7 null out of 8 and bridge has 7 null and one yes
- 8 features have no surface tag, 1 has an unpaved surface tag.
- 
**FITNESS:** Highly fit for network connectivity, emergency route accessibility, and spatial exposure analysis



```
## CRS and preparation
-All source layers arrived in EPSG:4326

-Study area: Patani delta state (south-south), extracted from GRID3 state boundary

-All Layer clipped to study area, then reprojected to EPSG:32632(UTM 32N) Note : i choose it because 

a.  EPSG:32632 is a Universal Transverse Mercator projection. 

b.When you calculate area in QGIS, using EPSG:4326 (degrees) will give distorted results. Reprojecting to EPSG:32632 ensures your area is measured in square meters, which you can then convert to km². 

c. Delta State sit comfortably in Zone 32N, so EPSG:32632 minimizes distortion for your study area.

-Area check: Delta State Total Area: Approximately $17,698km.Patani LGA Total Area: Approximately 217km to 220km.

-Working files in data/process, raw files untouched 
```
Status: Week 3 Complete. First Spatial relation and analysis in week 4
