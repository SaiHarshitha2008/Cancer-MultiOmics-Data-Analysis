# EGFR Survival Analysis in Lung Adenocarcinoma

This repository contains the code used for the EGFR survival analysis part of the lung adenocarcinoma project.

## What this analysis does

The analysis compares overall survival between:

- EGFR-altered patients
- EGFR-unaltered patients

The analysis uses Kaplan-Meier survival curves and the log-rank test.

The patient-level data should be exported from the TCGA Lung Adenocarcinoma PanCancer Atlas study in cBioPortal and saved as:

`data/egfr_survival.csv`

The file should contain these columns:

```text
PATIENT_ID
OS_MONTHS
OS_STATUS
EGFR_STATUS
```

For `EGFR_STATUS`, use only:

```text
Altered
Unaltered
```

## Run the analysis

Install the required packages:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python analysis.py
```

The script will create:

- `results/kaplan_meier_egfr.png`
- `results/summary.txt`

## Data source

The data source is the TCGA Lung Adenocarcinoma PanCancer Atlas study available through cBioPortal:

https://www.cbioportal.org/study?id=luad_tcga_pan_can_atlas_2018

cBioPortal provides programmatic access to its datasets through its REST API and also provides downloadable study files.

## Note

The repository focuses on the computational survival-analysis part of the project. The numerical results should be generated again from the exported patient-level data before the repository is submitted.
