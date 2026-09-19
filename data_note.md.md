# Data notes
##GRID3 NGA - Operational LGA Boundaries
- Source: https://data.grid3.org/
- Downloaded: \[16/9/2026]
- 774 features -Polygon (MultiPolygon)
- Columns:lga\_name (Ihitte/Uboma), state (Imo),Lgacode (17007),Statecode(IM) 
- No nulls in ward name
Quality note:- Used boundary so it Covers my LGA fully.



##OSM Road,extracted via QuickOSM
- Query: highway=\* in Ihitte/Uboma
- Extracted: \[16/09/2026]
- 26 features, Line (LineString)
Nulls:- yes and 25 have no surface tag,1 has unpaved surface tag
Note:-The extracted OSM road data shows dense coverage in the urban core, while the outskirts have limited representation, with only major roads mapped.


##OSM water way,extracted via QuickOSM
- Query: river=\* within Ihitte/Uboma
- Extracted: \[16/09/2026]
- 13 features, lines (LineString)
Null: - yes
Note: -The extracted OSM river data shows clear representation of major rivers, while rural streams and smaller tributaries are not mapped, indicating sparse coverage in the outskirts..


That last line about coverage is the kind of note that saves you in month six
commit it with the message Add data notes.
keep adding to the file all year



##Grid3, state boundary 
GRID3-https://data.grid3.org/datasets/c41532b720504f4799fe20438b7e3b7f_0/explore?location=9.077959%2C8.685290%2C5#:~:text=GRID3%20NGA%20%2D%20Operational%20State%20Boundaries -
Extracted [2025] via Grid3, Boundary=*

1 features

COMPLETENESS: Coverage is strong in the built‑up areas like Owerri and other major towns.

CURRENCY: most edits 2025. 

POSITIONAL: align well with satellite imagery.

ATTRIBUTE: no surface tag and no Null.

FITNESS: Adequate for statewide accessibility analysis .




##OSM roads, Imo State East 
Extracted [date] via QuickOSM, highway=*

13 features

COMPLETENESS: good in built-up area. Compared my own office area: all the roads present. 

CURRENCY: Most edits cluster around 2019–2023. Newly developed estates or peri‑urban expansions may not yet be mapped.

POSITIONAL: roads align well with satellite imagery, no systematic offset visible.

ATTRIBUTE: non has a surface tag but has Null. 

FITNESS: adequate for access analysis in the built-up area. Not adequate for a paved-road question.




##Hospital, Imo State East 
Extracted [date] via QuickOSM, amenity=*

21 features

COMPLETENESS: Major hospitals in urban centers (e.g., Federal Medical Centre Owerri, Imo State University Teaching Hospital) are mapped. Smaller rural health centers are missing

CURRENCY: Updates vary; new private hospitals or clinics may not yet appear in OSM.

POSITIONAL: Large hospitals align well with satellite imagery; rural clinics sometimes mis‑located and i saw non.

ATTRIBUTE: Many hospital features lack detailed tags 

FITNESS: Adequate for identifying major healthcare facilities. Not adequate for detailed health service capacity analysis.




## CRS and preparation
-All source layers arrived in EPSG:4326
-Study area:Imo state East, extracted from GRID3 state boundary
-All Layer clipped to study area, then reprojected to EPSH:32632(UTM 32N)
-Area check: Imo State East 5,101 km²,matches published figure 
-Working files in data/process,raw files untouched 
