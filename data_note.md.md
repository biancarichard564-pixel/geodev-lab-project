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

1 features
**COMPLETENESS:** Coverage is strong in the built‑up areas like patani and other major towns.

**CURRENCY**: most edits 2025. 

**POSITIONAL:** align well with satellite imagery.

**ATTRIBUTE:** no surface tag and no Null.

**FITNESS:** Adequate for statewide accessibility analysis .


## OSM roads, Imo State East 
Extracted [date] via QuickOSM, highway=*

13 features

**COMPLETENESS:** good in built-up area. Compared my own office area: all the roads present. 

**CURRENCY:** Most edits cluster around 2019–2023. Newly developed estates or peri‑urban expansions may not yet be mapped.

**POSITIONAL:** roads align well with satellite imagery, no systematic offset visible.

**ATTRIBUTE:** non has a surface tag but has Null. 

**FITNESS:** adequate for access analysis in the built-up area. Not adequate for a paved-road question.


## Hospital, Imo State East 
Extracted [date] via QuickOSM, amenity=*

21 features

**COMPLETENESS:** Major hospitals in urban centers (e.g., Federal Medical Centre Owerri, Imo State University Teaching Hospital) are mapped. Smaller rural health centers are missing

**CURRENCY:** Updates vary; new private hospitals or clinics may not yet appear in OSM.

**POSITIONAL:** Large hospitals align well with satellite imagery; rural clinics sometimes mis‑located and i saw non.

**ATTRIBUTE:** Many hospital features lack detailed tags 

**FITNESS:** Adequate for identifying major healthcare facilities. Not adequate for detailed health service capacity analysis.



```
## CRS and preparation
-All source layers arrived in EPSG:4326

-Study area:Imo state East, extracted from GRID3 state boundary

-All Layer clipped to study area, then reprojected to EPSG:32632(UTM 32N) Note : i choose it because 

a.  EPSG:32632 is a Universal Transverse Mercator projection. 

b.When you calculate area in QGIS, using EPSG:4326 (degrees) will give distorted results. Reprojecting to EPSG:32632 ensures your area is measured in square meters, which you can then convert to km². 

c. Delta State sit comfortably in Zone 32N, so EPSG:32632 minimizes distortion for your study area.

-Area check: Imo State East 5,101 km²,matches published figure 

-Working files in data/process, raw files untouched 
```
Status: Week 3 Complete. First Spatial relation and analysis in week 4
