# My Project brief

## The question 
What is the spatio-temporal extent of River Niger flood inundation in Patani LGA, Delta State, and how does bare-earth terrain elevation influence the spatial vulnerability of surrounding settlements, infrastructure, farmlands, and freshwater swamp forest ecosystems?

## Why it matters 

### Urgent Disaster Risk Reduction (DRR) & Early Warning
- Predictable Safety Zones: Mapping flood inundation extent and terrain elevation pinpoints exactly which communities are at risk during seasonal swells of the River Niger, allowing local emergency management agencies to establish targeted evacuation routes and safe shelters before peak flooding hits.

### Protecting Local Food Security & Agricultural Planning
- Crop Loss Mitigation: Patani relies heavily on farming (such as cassava, yam, and plantain). Identifying when and where floodwaters overflow onto agricultural lands allows farmers to adjust planting cycles and harvest before peak inundation periods.

### Infrastructure Resiliency & Urban Planning
- Climate-Proof Construction: Knowing which elevation zones are most vulnerable guides future engineering decisions, ensuring roads (like the East-West Highway corridor), bridges, health centers, and schools are built at safe elevations or reinforced against flood damage.

### Freshwater Swamp Conservation & Ecosystem Health
- Tracking Wetland Loss: Patani’s inland freshwater swamp forests provide critical biodiversity habitats and natural buffer zones. Spatial analysis reveals how recurring floods, combined with human encroachment, alter forest cover, soil erosion, and natural drainage channels.

### Data-Driven Policy & Resource Allocation
- Justifying Financial & Humanitarian Aid: Government bodies, international NGOs, and relief agencies require spatial evidence to allocate funds, emergency supplies, and climate-resilience grants to the most vulnerable communities.


## The data I need
- Nigeria state Bounaries 
- Nigeria Lga Boundaries
- Nigeria Ward Boundaries
- Settlement
- FABDEM (Forest and Buildings removed DEM)
- sentinel - 1 GRD Flood Imagery
- Land Cover / Farmland & Forest for Patani LGA
- Water Bodies 
- Roads
- Buildings

- Spatio-temporal extent of River Niger flood inundation"

Dataset: Sentinel-1 SAR Radar Imagery (Raster)

Role: Tracks water boundaries across wet and dry seasons over time to map where and when floodwaters spread.


- Bare-Earth terrain elevation (derived via FABDEM)"

Dataset: FABDEM V1-2 Tile N05E006 (Raster)

Role: Strips away tree canopy heights and building tops to give true ground elevation, ensuring accurate water flow and inundation modeling.


- Surrounding settlements [and] infrastructure"

Datasets: Buildings, Roads, & Waterways via OpenStreetMap / QuickOSM (Vector Layers)

Role: Identifies which homes, communities, and transport corridors (like the East-West Road) overlap with low-elevation flood zones


- Farmlands, and freshwater swamp forest ecosystems"

Dataset: Esri 10m Land Cover 

Role: Measures the total land surface area (in $\text{km}^2$ or hectares) of crops and native swamp forests submerged during peak flooding



## Where each dataset comes from
| Sn | Dataset | Source | Location | Size |
|---|---|---|---|---|
| 1 | Nigeria State Boundaries | [GRID3 NGA Operational State Boundaries](https://data.grid3.org/datasets/c41532b720504f4799fe20438b7e3b7f_0/explore?location=9.077959%2C8.685290%2C5#:~:text=GRID3%20NGA%20%2D%20Operational%20State%20Boundaries) | Shapefile | 645 KB |
| 2 | Nigeria LGA Boundaries | [GRID3 NGA Operational LGA Boundaries](https://data.grid3.org/datasets/2bb616a49ee84f409427cc2143787113_0/explore?location=9.077959%2C8.685290%2C5#:~:text=GRID3%20NGA%20%2D%20Operational%20LGA%20Boundaries) | Shapefile | 2.6 MB |
| 3 | Nigeria Ward Boundaries | [GRID3 NGA Operational Wards v3.0](https://data.grid3.org/datasets/45cd2ef592094d12aca43113a90a6054_0/explore?location=9.077872%2C8.670771%2C5#:~:text=GRID3%20NGA%20%2D%20Operational%20Wards%20v3.0,-Private%20Member) | Shapefile | 128 MB |
| 4 | Nigeria settlement| [GRID3 NGA - Settlement Extents v4.1] (https://data.grid3.org/datasets/f705d65c012c46748e6e5f44a33728b1_0/explore?location=9.079999%2C8.679167%2C5#:~:text=GRID3%20NGA%20%2D%20Settlement%20Extents%20v4.1 | Shapefile | 2.6 MB |   
| 5 | FABDEM (Forest and Buildings removed DEM) | [University of Bristol / FABDEM V1-2](https://data.bris.ac.uk/data/dataset/s5hqmjcdj8yo2ibzi9b4ew3sn) | Raster Layer (GeoTIFF) | ~1.1 GB (Tile N05E006) | 
| 6 | Sentinel -1 flood imagery for Patani LGA |https://browser.dataspace.copernicus.eu/?Sentinel-1 flood imagery for Patani LGA | [Copernicus Data Space Browser](https://browser.dataspace.copernicus.eu/) | Raster Layer (GeoTIFF)  |1323 MB | 
| 7 |Land Cover / Farmland & Forest for Patani LGA | [Esri 10m Land Cover ]([https://livingatlas.arcgis.com/landcover/](https://livingatlas.arcgis.com/landcoverexplorer/#mapCenter=6.13951%2C5.24847%2C10.64&mode=step&timeExtent=2017%2C2025&year=2025&downloadMode=true) | Raster Layer (GeoTIFF) | ~139MB AND  –85.9 MB |
| 8 | Water Bodies for Patani LGA | OpenStreetMap via QuickOSM (QGIS Plugin) | Vector Layer | — | 
| 9| Road for Patani LGA | OpenStreetMap via QuickOSM (QGIS Plugin) | Vector Layer | — | 
| 10 | Building for Patani LGA | OpenStreetMap via QuickOSM (QGIS Plugin) | Vector Layer | — |



## what i will build 
### Core Spatial Maps (Your Maps & Visual Outputs)
- Flood Inundation & Footprint Maps: Visualizations comparing normal dry-season water levels against peak flood extents (extracting data from historic flood events like 2012 and 2022 using Sentinel-1 SAR imagery).

- Digital Elevation & Slope Models: Terrain elevation maps generated from SRTM/ALOS DEMs showing low-lying, flood-prone basin contours.

- Topographic Wetness Index (TWI) Map: A hydrological spatial layer highlighting natural drainage paths, depressions, and water-accumulation zones.

- Land Use / Land Cover (LULC) Map: Classified spatial map depicting Freshwater Swamp Forest, Farmland, Built-up/Settlement, Open Water, and Sandbars.

- Composite Flood Hazard & Risk Map: A final overlay map dividing Patani LGA into Very Low, Low, Moderate, High, and Very High flood risk zones.

### Analytical Data & Statistical Outputs
- Vulnerability & Exposure Matrix: A structured table listing specific settlements, roads (e.g., the East-West Highway corridor), and public infrastructure (schools, health centers) categorized by their flood hazard level.

- LULC Transition Matrix: Statistical tables calculating exact acreage and percentage changes of swamp forest lost or converted into farmland and settlement footprints.

- Zonal Statistics: Data summarizing flood depth/extent aggregated by local Ward boundaries across Patani LGA.

### Decision-Support Deliverables (Final Practical Products)
- Safe Evacuation & Emergency Route Map: Identification of high-ground refuge sites and clear, flood-safe access corridors for emergency response agencies.

- Post-Flood Agricultural Calendar/Suitability Guide: A spatial outline identifying floodplains best suited for seasonal recession farming after floodwaters recede.

 status: week 1 complete. Data acquisition in week 2, see data_note.md



