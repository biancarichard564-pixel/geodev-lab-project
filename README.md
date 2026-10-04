# < My GeoDev lab Africa project>

<Flood Risk, Inundation, and Settlement Vulnerability>

<Built over twelve months with GeoDev Lab African, Cohort one.>

**GeoDev Lab Africa, Cohort One. ** 

< Richard Bianca Ihuoma> 
  
## The question

< What is the spatio-temporal extent of River Niger flood inundation in Patani LGA Delta State, and how does terrain elevation influence the vulnerability of surrounding settlements, infrastructure, farmlands, and swamp forest ecosystems? >

## What's in here

```

<project-name>
├── docs/
│   ├── 01-project-brief.md       # Week 1 project overview & objectives
│   ├── 02-data-notes.md          # Week 2 dataset sources & documentation
│   └── 03-data-note.md           # Week 3 data cleaning & preprocessing steps
│   └── 04-month-1-summary.md     # Week 4 spatial relation and analysis
├── data/
│   ├── raw/                      # Raw datasets (GRID3 boundaries,Settlement,FABDEM (Forest and Buildings removed DEM),sentinel - 1 GRD Flood Imagery,Land Cover / Farmland & Forest for Patani LGA,Water Bodies ,Roads,Buildings)
│   └── processed/                # Derived spatial layers & raster outputs
├── scripts/                      # GIS & python processing scripts
└── README.md                     # Project summary & vulnerability framework

```

## How to run it

```bash 
git clone https://github.com/biancarichard564-pixel/geodev-lab-project.git
   cd geodev-lab-project
1. ** Software Required**
   - Download and install [QGIS](https://qgis.org/) (version 3.x or higher).

2. ** Data Setup **
   - Download the raw spatial datasets:
     - **GRID3 Boundaries** (State, LGA, Ward)
     - **Water Bodies** (OpenStreetMap)
   - Place these downloaded files inside your local `data/raw/` folder.

3. ** Open Project in QGIS **
   - Launch QGIS.
   - Open the `.qgz` project file from this repository.
   - Ensure the layers from `data/raw/` are loaded properly to view the Burutu LGA land cover analysis.

the data is not this repository. Every source is linked in [the project brief](docs/01-Project.brief.md), so anyone can fetch it.

```

## Progress

## Progress & Deliverables

* **Week 1:** [Project Brief with Dataset Sources](Project.brief.md)
* **Week 2:** [Data Notes & Descriptions](data_note.md.md)
* **Week 3:** [Data Cleaning & Quality Checks](data_note.md.md)
* **Week 4:** [Month 1 Summary & Spatial Analysis](month-1-summary.md) | [Final Flood Inundation Map](week%204%20project.png)

## Key Findings (Patani LGA Flood Risk)
* **Flood Inundation Extent:** Peak Sentinel-1 radar imagery shows floodwaters heavily concentrated along the main River Niger corridor and lower riverfront wards (such as Patani town).
* **Elevation & Settlement Vulnerability:** Proximity to the river alone does not determine flood risk. Bare-earth terrain data (FABDEM) reveals that several inland settlements over 500m away from the river bank were inundated due to low ground elevation (<5m) and backwater pooling in low-lying land depressions.


## Month 2:preparation development environment and early python 
week 5: setup python, VS code and the terminal. hello.py runs



Richard Bianca Ihuoma

08100667081 

GeoDev Lab Africa Learn. Build. Collaborate. Transform.   








