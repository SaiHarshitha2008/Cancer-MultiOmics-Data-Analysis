# Data

Do not upload the full TCGA dataset into this folder just to make the repository look complete.

Export only the patient-level information needed for this analysis and save it as:

`egfr_survival.csv`

Required columns:

- `PATIENT_ID`
- `OS_MONTHS`
- `OS_STATUS`
- `EGFR_STATUS`

Example:

```csv
PATIENT_ID,OS_MONTHS,OS_STATUS,EGFR_STATUS
TCGA-XX-0001,32.4,1:DECEASED,Altered
TCGA-XX-0002,54.8,0:LIVING,Unaltered
```

The example above is only the format. It is not real patient data.
