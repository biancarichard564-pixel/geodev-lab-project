< My GeoDev lab Africa project>
<Burutu LGA Wetland & Land Cover Analysis>

<Built over twelve months with GeoDev Lab African, Cohort one.>

** GeoDev Lab Africa, Cohort One. **

< Richard Bianca Ihuoma>

The question
< What is the proportion of dry land relative to open water bodies and wetlands across Burutu Local Government Area, Delta state? >

What's in here

<project-name>
├── docs/
│   ├── 01-project-brief.md       # Week 1 project overview & objectives
│   ├── 02-data-notes.md          # Week 2 dataset sources & documentation
│   └── 03-data-preparation.md    # Week 3 data cleaning & preprocessing steps
├── data/
│   ├── raw/                      # Raw datasets (GRID3 boundaries, OSM water bodies)
│   └── processed/                # Derived spatial layers & raster outputs
├── scripts/                      # GIS & python processing scripts
└── README.md                     # Project summary & vulnerability framework


How to run it
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


Progress
-[x] Week 1, project brief with a source link for every dataset
-[x] Week 2, data downloaded, opened and described
-[x] Week 3, reprojected, clipped and quality checked
-[x] Week 4, first spatial analysis, checked four ways

GeoDev Lab Africa Learn. Build. Collaborate. Transform.
