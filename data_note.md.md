# Data notes

** Week 2 deliverable. ** Geodev Lab Africa, Cohort One.
Author: <Richard Bianca Ihuoma>

What i downloaded, where it came from, what is in it and what is wrong with it.


## Summary

| # | Dataset | Type | Retrieved | Status |
|---|---|---|---|---|
| 1 | GRID3 LGA Boundaries | Vector (Polygon) | 16/09/2026 | Complete |
| 2 | OSM Roads | Vector (LineString) | 16/09/2026 | Incomplete |
| 3 | OSM Waterways | Vector (LineString) | 16/09/2026 | Partial |
 

## GRID3 NGA - Operational LGA Boundaries
- **Source:** [https://data.grid3.org/](https://data.grid3.org/)
- **Downloaded:** 16/09/2026
- **Geometry type:** Polygon (MultiPolygon) — 774 features
- **Columns:** `lga_name` (Ihitte/Uboma), `state` (Imo), `Lgacode` (17007), `Statecode` (IM)
- **Nulls:** No nulls in boundary fields
- **Quality note:** Used boundary covers my target LGA fully.

## OSM Roads (extracted via QuickOSM)
- **Query:** `highway=*` in Ihitte/Uboma
- **Extracted:** 16/09/2026
- **Geometry type:** Line (LineString) — 26 features
- **Nulls:** Yes — 25 features have no surface tag, 1 has an unpaved surface tag.
- **Quality note:** Shows dense coverage in the urban core, while the outskirts have limited representation with only major roads mapped.

 
## OSM Waterways (extracted via QuickOSM)
- **Query:** `waterway=*` within Ihitte/Uboma
- **Extracted:** 16/09/2026
- **Geometry type:** Line (LineString) — 13 features
- **Nulls:** Yes
- **Quality note:** The extracted OSM river data shows clear representation of major rivers, while rural streams and smaller tributaries are not mapped, indicating sparse coverage in the outskirts.. 

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
**COMPLETENESS:** Coverage is strong in the built‑up areas like Owerri and other major towns.

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

c. Imo State and Delta State sit comfortably in Zone 32N, so EPSG:32632 minimizes distortion for your study area.

-Area check: Imo State East 5,101 km²,matches published figure 

-Working files in data/process, raw files untouched 
```
Status: Week 3 Complete. First Spatial relation and analysis in week 4
