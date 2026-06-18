# Automated Cloud-Penetrating Flood Boundary Detection

Rapid and accurate mapping of inundated areas is critical for effective emergency response. Traditional disaster monitoring relies on multi-spectral optical satellite imagery, which is severely limited by the heavy cloud cover that typically accompanies severe flooding events.

This repository provides an automated software pipeline for real-time flood boundary extraction using Synthetic Aperture Radar (SAR) data. Operating in the microwave spectrum, SAR emits active pulses that pass unhindered through clouds and darkness, making it an ideal zero-visibility situational awareness tool.

## Repository Contents

- `Indus_flood.ipynb`: The main Jupyter Notebook containing the data acquisition, preprocessing, model training, and evaluation code.
- `models/sar_flood_resnet34_best.pth`: The pre-trained model weights.

## Pipeline Architecture

The end-to-end system consists of the following sequential stages:

- **Data Acquisition:** Sentinel-1 dual-polarization (VV and VH) SAR data is retrieved via the Google Earth Engine (GEE) API.
- **Preprocessing & Engineering:** A temporal and spatial speckle filtering process mitigates multiplicative noise. A "pseudo-color" composite is mathematically engineered by averaging the VV and VH bands to create a third tensor channel for the neural network.
- **Deep Learning Inference:** Semantic segmentation is performed using an advanced U-Net architecture featuring a pre-trained ResNet-34 encoder.
- **Geospatial Alignment:** Predictions are extracted using Rasterio metadata and anchored to physical EPSG:4326 coordinates.

## Model Optimization and Performance

- The network is optimized using the Adam optimizer and a hybrid Binary Cross-Entropy (BCE) and Dice Loss function to combat severe class imbalance (water vs. non-water).
- Heavy geometric data augmentation, including grid distortions and random rotations, is applied via the `Albumentations` library to simulate highly irregular flood boundaries.
- The ResNet-34 U-Net achieves an Intersection over Union (IoU) of **66.24%**, vastly outperforming traditional thresholding techniques.

## Prerequisites and Usage

Ensure you have Python 3 installed. You can install the required dependencies using pip:

```bash
pip install segmentation-models-pytorch albumentations earthengine-api geemap rasterio
```
