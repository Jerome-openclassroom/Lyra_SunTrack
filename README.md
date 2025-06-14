
# Lyra SunTrack — Solar Projection and Measurement Protocol

## 📑 Purpose

Lyra SunTrack demonstrates a complete, safe, and low-cost workflow for observing, identifying, and measuring sunspots using a simple projection device — the **Solarscope**.

The **Solarscope** is an affordable, foldable cardboard tool that projects a ~10 cm solar image onto a white screen, allowing group observation without any risk to eyesight. It is highly recommended for schools, astronomy clubs, and public outreach.

This project combines:
- The Solarscope for projection.
- A **Stonyhurst grid** (transparent PNG) adjusted for June (B0 correction).
- **ImageJ** for distance measurement and light profiles.
- **Mesurim2** for counting sunspots and groups (Wolf Number).
- A **custom Python script**, designed with GPT-4o and Grok, to convert angular distances into real kilometers at given solar latitudes.
- Use of AI (GPT-4o and Grok) for optical corrections and scripting.

## 📂 Folder: `Tools_results`

Contains:
- **AR_June_14th_2025.JPG** — Sunspots labeled with NOAA numbers.
- **Center_side_darkening.JPG** — Limb darkening brightness profile.
- **Local_observation.JPG** — Raw Solarscope projection.
- **Local_Observation_Stonyhurst.JPG** — Projection with overlaid Stonyhurst grid PNG.
- **Nb_Wolf_Mesurim.JPG** — Sunspot and group count (Mesurim2).
- **SDO_HMIIF_june_14th_2025.JPG** — Official SDO/HMI reference image.
- **Solarscope.JPG** — Photo of the instrument.
- **stonyhurst_June.PNG** — Stonyhurst grid (transparent PNG, B0 adjusted).
- **suntrack_converter.py** — Python script for angular to km conversion.

## 🗺️ Stonyhurst Grid

The Stonyhurst disk is a **transparent PNG file** created based on the [Stanford Solar Center](https://solar-center.stanford.edu/solar-images/latlong.html) model, adjusted for the June B0 angle (+7° to +8°). The raw solar projection is flipped vertically and horizontally to correct the optical inversion caused by the Solarscope. The grid layer was also carefully adjusted to match the slight optical deformation of the Sun's image inherent to the Solarscope's projection system. The grid is manually aligned using [Photopea](https://www.photopea.com/).

## 📐 Scale Conversion

The `suntrack_converter.py` script calculates the real physical length (in km) of a 15° arc in longitude and latitude at any given solar latitude. This allows converting pixel measurements in ImageJ to real dimensions.

## 📈 Limb Darkening Measurement

A light intensity profile was extracted across the solar disk using ImageJ. This demonstrates the gradual decrease in brightness from the center to the limb — clear evidence of the photosphere's radiative structure.

## 🧮 Wolf Number

Counted with **Mesurim2** ([Mesurim2](https://www.pedagogie.ac-nice.fr/svt/productions/mesurim2/)):
- 14 individual sunspots
- 2 distinct groups

Wolf Number:
> **W = 10 × 2 + 14 = 34**  
A typical value for an active solar cycle period.

## ⚡ Sunspot Measurements (within ARs)

Measurements of individual sunspots inside Active Regions (ARs):
- **AR 4115:** 16,571 km
- **AR 4114:** 11,503 km
- **AR 4111:** 22,107 km
- **AR 4116:** 11,280 km

## ✅ Final Result

- Local observation successful and reproducible.
- Stonyhurst grid correctly overlaid (B0 adjusted).
- Grid adjusted for optical deformation.
- Limb darkening profile measured and verified.
- Dimensions consistent with official SDO data ([Space Weather Live](https://www.spaceweatherlive.com/en/solar-activity/sunspot-regions.html)).
- Python script and optical checks supported by GPT-4o and Grok.

## 🔗 Resources and Tools

- **Stonyhurst Grid:** [Stanford Solar Center](https://solar-center.stanford.edu/solar-images/latlong.html)
- **SDO Data:** [Space Weather Live](https://www.spaceweatherlive.com/en/solar-activity/sunspot-regions.html)
- **Photopea:** [Photopea.com](https://www.photopea.com/)
- **ImageJ:** [ImageJ.net](https://imagej.net/)
- **Mesurim2:** [Mesurim2](https://www.pedagogie.ac-nice.fr/svt/productions/mesurim2/)

## 📄 Additional Information

**Author:** Jérôme / Lyra Project 2025  
**License:** Open Science — free for educational and scientific use

## 🔗 Related Repositories

- [Main GitHub profile](https://github.com/Jerome-openclassroom)  
  *→ Overview of all published repositories and Lyra projects.*
- [Related project: AI applied to Astrophysics](https://github.com/Jerome-openclassroom/AI_Astrophysics)  
  *→ AstresDB — A Stellar Journey in SQL and Linux with a handcrafted MySQL database.*
- [Related project: VLTI Mirror Curvature Modeling (VBA, 2005)](https://github.com/Jerome-openclassroom/VLTI_Mirror_Curvature_Model_C_VBA_2005)  
  *→ Historical VBA and C project for modeling VLTI mirror curvature.*
- [Related project: Artisan Spectroscopy & Plasma Physics](https://github.com/Jerome-openclassroom/Artisan_Spectroscopy_Plasma_Physics)  
  *→ Low-cost experimental spectroscopy and homemade plasma physics studies.*
