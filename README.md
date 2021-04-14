# Visualise deforestation-driven temperature change on a web map 

## Setup

```
pip install titiler 
```

### 1. Create COG

Create COG file to render on basemap.

```
gdal_translate -scale 0 1 0 255 -a_nodata 0 -ot Byte MC_1000.tif mc_1000_byte.tif

rio cogeo create --web-optimized mc_1000_byte.tif mc_1000_byte_cog.tif
```

### 2. Setup TiTiler 

Titiler is a dynamic tiler server that can read data from a COG file and generate web map tiles.

`cd` into app directory. Launch TiTiler application:

```
uvicorn main:app --reload
```

### 3. Visualise web map tiles

Open a new terminal. Launch *cog-demo.ipynb*. 
