# My Project brief

## The question 
What is the spatio-temporal extent of River Niger flood inundation in Patani LGA Delta State, and how does terrain elevation influence the vulnerability of surrounding settlements, infrastructure, farmlands, and swamp forest ecosystems?

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
- Water Bodies 
- Roads
- Buildings
- settlement 
- Elevation and topographic data data covering patani lga 
- Remote Sensing & Imagery Data


## Where each dataset comes from
| Sn | Dataset | Source | Location | Size |
|---|---|---|---|---|
| 1 | Nigeria State Boundaries | [GRID3 NGA Operational State Boundaries](https://data.grid3.org/datasets/c41532b720504f4799fe20438b7e3b7f_0/explore?location=9.077959%2C8.685290%2C5#:~:text=GRID3%20NGA%20%2D%20Operational%20State%20Boundaries) | Shapefile | 645 KB |
| 2 | Nigeria LGA Boundaries | [GRID3 NGA Operational LGA Boundaries](https://data.grid3.org/datasets/2bb616a49ee84f409427cc2143787113_0/explore?location=9.077959%2C8.685290%2C5#:~:text=GRID3%20NGA%20%2D%20Operational%20LGA%20Boundaries) | Shapefile | 2.6 MB |
| 3 | Nigeria Ward Boundaries | [GRID3 NGA Operational Wards v3.0](https://data.grid3.org/datasets/45cd2ef592094d12aca43113a90a6054_0/explore?location=9.077872%2C8.670771%2C5#:~:text=GRID3%20NGA%20%2D%20Operational%20Wards%20v3.0,-Private%20Member) | Shapefile | 128 MB |
| 4 | Nigeria settlement| [GRID3 NGA - Settlement Extents v4.1] (https://data.grid3.org/datasets/f705d65c012c46748e6e5f44a33728b1_0/explore?location=9.079999%2C8.679167%2C5#:~:text=GRID3%20NGA%20%2D%20Settlement%20Extents%20v4.1 | Shapefile | 2.6 MB |   
| 5 | Water Bodies for Patani LGA | OpenStreetMap via QuickOSM (QGIS Plugin) | Vector Layer | — | 
| 6 | Road for Patani LGA | OpenStreetMap via QuickOSM (QGIS Plugin) | Vector Layer | — | 
| 7 | Building for Patani LGA | OpenStreetMap via QuickOSM (QGIS Plugin) | Vector Layer | — |
| 9 | Elevation for Patani LGA |  | raster Layer | — | 



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



