<<<<<<< HEAD
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
=======
# Integrated Computational Bioengineering for EGFR-Driven Lung Adenocarcinoma: Multi-Omics, Molecular Docking, and Synthetic Biosensor Design

## 1. Introduction

Lung adenocarcinoma is the leading histological type of non-small cell lung cancer (NSCLC) that takes the largest share of all cases of lung cancer[cite: 2]. It originates from the glandular tissue in the outer part of the lungs responsible for secreting mucus[cite: 2]. Tobacco smoking is considered the leading environmental cause of lung adenocarcinoma; nevertheless, it is the most common form of lung cancer among non-smokers and females[cite: 2]. At the same time, lung adenocarcinoma is primarily guided by genetic mutations and rearrangements of the Epidermal Growth Factor Receptor (EGFR)[cite: 2]. EGFR encodes a tyrosine kinase receptor that plays an essential role in cell proliferation, differentiation, and survival[cite: 2]. Mutations of this receptor lead to the development of cancerous tumors[cite: 2]. Therefore, the identification of driver mutations allows for the creation of targeted molecular kinase inhibitors and the development of biosensors for diagnostics[cite: 2].

### 1.1 Background and Clinical Context
Genomic and clinical profiling of tumor tissue provides an in-depth understanding of the underlying genetic mechanisms of malignancy[cite: 2]. Lung cancer is divided into multiple histological subtypes according to the World Health Organization, among which lung adenocarcinoma is the most common and extremely aggressive[cite: 2]. Therefore, there is a critical need to identify genes that mutate during disease progression to prioritize them as therapeutic targets[cite: 2].

The Epidermal Growth Factor Receptor (EGFR) is a receptor tyrosine kinase controlling cellular proliferation, differentiation, and survival[cite: 2]. Aberrant activation of EGFR and its driver mutations are key features of lung adenocarcinoma, making it an oncogenic driver and a primary target for therapeutic intervention[cite: 2].

### 1.2 Paradigm of Computational Bio-Engineering
Conventional cancer research aims to understand disease from multiple angles independently[cite: 2]. Modern computational biotechnology enables the integration of these domains into a single workflow[cite: 2]:

* Cancer Genomics & Multi-Omics: Large-scale patient databases are analyzed to identify genetic prevalence and survival trends[cite: 2].
* Structure-Based Molecular Docking: *In silico* experiments predict the thermodynamic binding affinity of small-molecule therapeutics to target receptors, prioritizing compounds for preclinical development[cite: 2].
* Synthetic Biology Circuitry: Cellular machinery is repurposed to construct designer reporter cells capable of detecting oncogenic markers and emitting fluorescent signals[cite: 2].

### 1.3 Objectives of this Integrated Study
1. Determine the incidence of EGFR aberrations and their impact on clinical outcomes using patient data[cite: 2].
2. Compute the binding and energetic properties of Erlotinib to elucidate its molecular mechanism of action[cite: 2].
3. Design a synthetic plasmid circuit that outputs an optical fluorescent signal in response to EGFR overexpression[cite: 2].

---

## 2. Phase I: Multi-Omics Data Analysis & Survival Profiling

### 2.1 Methodology
Clinical and genomic sequencing data were extracted from the Lung Adenocarcinoma dataset (TCGA, PanCancer Atlas) via the cBioPortal platform ($n = 503$ clinical patients)[cite: 2].

* OncoPrint Profile: Generated to depict the frequency distribution of mutations, amplifications, and structural variations in the EGFR gene[cite: 2].
* Cohort Stratification: Patients were stratified into two subgroups[cite: 2]:
  * *EGFR-altered:* Patients with EGFR mutations or structural variations[cite: 2].
  * *EGFR-unaltered:* Patients with no variations in the EGFR gene[cite: 2].
* Survival Analysis: A Kaplan-Meier survival curve was plotted (Overall Survival Probability vs. Time in months)[cite: 2]. The Logrank Test was evaluated for statistical significance[cite: 2].

### 2.2 Results
Analysis of the OncoPrint profile indicated that EGFR was structurally altered or mutated in 122 of the 503 surveyed patients (24%)[cite: 2]. 

> 🔗 Interactive Data: [View Live OncoPrint Profile on cBioPortal](https://www.cbioportal.org/results/oncoprint?cancer_study_list=luad_tcga_pan_can_atlas_2018&Z_SCORE_THRESHOLD=2.0&RPPA_SCORE_THRESHOLD=2.0&profileFilter=mutations%2Cstructural_variants%2Cgistic%2Crna_seq_v2_mrna_median_Zscores&case_set_id=luad_tcga_pan_can_atlas_2018_3way_complete&gene_list=EGFR&geneset_list=%20&tab_index=tab_visualize&Action=Submit) | [View Live Kaplan-Meier Survival Dataset](https://www.cbioportal.org/results/comparison/survival?cancer_study_list=luad_tcga_pan_can_atlas_2018&Z_SCORE_THRESHOLD=2.0&RPPA_SCORE_THRESHOLD=2.0&profileFilter=mutations%2Cstructural_variants%2Cgistic%2Crna_seq_v2_mrna_median_Zscores&case_set_id=luad_tcga_pan_can_atlas_2018_3way_complete&gene_list=EGFR&geneset_list=%20&tab_index=tab_visualize&Action=Submit)

* Survival Trends: The Overall Survival Probability for the altered group quickly drops below that of the unaltered group[cite: 2].
* Long-Term Survival: At 50 months post-study, overall survival for the altered group dropped below 30%[cite: 2].
* Statistical Evaluation: The Logrank test yielded a P-value of 0.324[cite: 2]. While the Kaplan-Meier plot visually suggests an initial survival deficit for the EGFR-altered group, this P-value indicates that the overall survival difference between the two subpopulations is not statistically significant ($p > 0.05$)[cite: 2]. This highlights the need for larger cohort sizes and controlling for confounding clinical factors[cite: 2].

### 2.3 Phase I Discussion & Transition
The 24% alteration frequency demonstrates that EGFR is an overrepresented oncogene in lung adenocarcinoma[cite: 2]. While population trends indicate an adverse outcome associated with EGFR genetic abnormalities, molecular targeting of EGFR kinase activity remains a high-priority therapeutic pathway[cite: 2].

---

## 3. Phase II: Structure-Based Molecular Docking & Drug Validation

### 3.1 Methodology
*In silico* molecular docking was performed targeting the active site of the human EGFR tyrosine kinase domain[cite: 2].

1. Receptor Preparation: The crystallographic structure of human EGFR kinase was obtained from the RCSB Protein Data Bank (PDB ID: 1M17)[cite: 2]. Water molecules were removed, hydrogens were added at physiological pH 7.4, and a 3D receptor grid was generated around the active tyrosine kinase domain[cite: 2].
2. Ligand Benchmark: Erlotinib was selected as a positive control small-molecule inhibitor[cite: 2].
3. Docking Simulation: Performed using AutoDock Vina via Webina[cite: 2]. Exhaustiveness was set to 8 to ensure accurate pose prediction[cite: 2].

### 3.2 Results
The docking simulation predicted the binding modes and Gibbs Free Energy ($\Delta G$) of the EGFR-Erlotinib interaction[cite: 2]. Large negative free energy values indicate favorable binding[cite: 2].

| Mode | Affinity Score (kcal/mol) | Distance from RMSD L.B. | Distance from RMSD U.B. |
| :--- | :--- | :--- | :--- |
| 1 | -10.598 | 0.000 | 0.000 |
| 2 | -9.614 | 1.314 | 3.276 |
| 3 | -9.386 | 1.969 | 3.043 |
| 4 | -9.122 | 1.809 | 3.743 |
| 5 | -8.979 | 2.336 | 3.485 |
| 6 | -8.661 | 5.768 | 7.966 |
| 7 | -8.306 | 3.340 | 4.601 |
| 8 | -8.225 | 2.280 | 3.524 |
| 9 | -8.206 | 1.170 | 3.451 |

* Top Pose (Mode 1): Achieved an affinity score of -10.598 kcal/mol[cite: 2].
* Interactions: Strong binding is stabilized by hydrogen bonding and hydrophobic interactions within the active tyrosine kinase pocket[cite: 2].

### 3.3 Phase II Discussion & Transition
The binding score of -10.598 kcal/mol confirms high structural affinity, supporting Erlotinib's therapeutic efficacy[cite: 2]. However, targeted therapies require early detection[cite: 2]. Phase III explores a synthetic biosensor designed to optically signal the presence of EGFR-overexpressing cancer cells[cite: 2].

---

## 4. Phase III: Synthetic Biology Circuit Design for Biosensing

### 4.1 Methodology
A synthetic gene circuit was designed using the Benchling Molecular Biology Workspace[cite: 2].

1. Plasmid Backbone: Derived from pBR322 vector backbone, designated pBR322_EGFR[cite: 2].
2. Circuit Assembly: Assembled a linear transcriptional unit comprising:
   * Synthetic promoter responsive to EGFR activation[cite: 2].
   * Green Fluorescent Protein (GFP) reporter gene (derived from *Aequorea victoria*)[cite: 2].
   * Transcriptional termination sequence[cite: 2].
3. *In Silico* Verification: Sequence alignment and frame verification were performed to confirm restriction sites, reading frames, and orientation[cite: 2].

### 4.2 Results
The resulting biosensor construct is the 720 bp plasmid pBR322_EGFR[cite: 2].

> 🔗 Interactive Design: [View Interactive Plasmid Map & Sequence on Benchling](https://benchling.com/s/seq-KOxkuU88pFXySalHKMzH?item_id=seq_l7gBrD9i5J&m=slm-sHTkF117jHqHEd7DYU7n)

* Mechanism: Reporter cells are engineered to express a Synthetic Notch (SynNotch) receptor featuring an anti-EGFR extracellular binding domain[cite: 2]. Upon contacting EGFR-overexpressing lung cancer cells, the SynNotch receptor undergoes cleavage, releasing a customized intracellular transcription factor[cite: 2]. This factor translocates to the nucleus and binds specifically to the synthetic promoter on pBR322_EGFR, driving GFP transcription to produce a green fluorescent signal[cite: 2].
* Sequence Alignment: Confirmed correct reading frame alignment of the GFP gene downstream of the promoter with zero frameshift mutations[cite: 2].

### 4.3 Phase III Discussion
Cellular diagnostic processing provides a rapid alternative to labor-intensive lab assays[cite: 2]. The pBR322_EGFR circuit converts extracellular target binding into a clear optical readout[cite: 2].

---

## 5. Synthesis, Limitations, & Future Directions

### 5.1 Integrated Translational Synthesis
This study couples clinical genomics, *in silico* pharmacology, and synthetic diagnostics into a single translational continuum[cite: 2].

### 5.2 Critical Methodological Limitations
* Phase I Transcriptomic Origins: Utilizes retrospective clinical data, which fails to account for post-transcriptional, translational, and environmental factors influencing overall survival[cite: 2].
* Phase II Receptor Docking Assumptions: Molecular docking assumes rigid receptor models, whereas actual protein chains undergo dynamic conformational changes upon ligand binding[cite: 2].
* Phase III Plasmid Circuitry Concerns: Synthetic promoters may exhibit "leaky" constitutive expression independent of target engagement, and plasmid integration can introduce metabolic burden on host cells[cite: 2].

### 5.3 Future Research Directions
1. Proteomic Profiling: Conduct Mass Spectrometry and Western blot assays across lung cancer cell lines to confirm transcript-level alterations correlate with oncoprotein expression[cite: 2].
2. Molecular Dynamics (MD) Simulations: Run long-timescale MD simulations in explicit solvent to test the dynamic stability of the EGFR-Erlotinib complex under physiological conditions[cite: 2].
3. In-Vitro Wet-Lab Validation: Perform enzyme inhibition assays to determine IC50 values for Erlotinib and evaluate biosensor signal-to-noise ratios in cell culture[cite: 2].

---

## 6. Conclusion
1. Multi-omics analysis revealed EGFR mutations in 24% of lung adenocarcinoma patients (122/503) associated with an initial survival deficit[cite: 2].
2. Structure-based docking validated Erlotinib as a potent kinase inhibitor with a thermodynamic binding affinity of -10.598 kcal/mol against PDB ID: 1M17[cite: 2].
3. Synthetic biology modeling generated the pBR322_EGFR plasmid circuit connecting an EGFR-sensitive promoter to a GFP optical readout[cite: 2].

---

## 7. Tools & Data Sources
* Genomic Data: The Cancer Genome Atlas (TCGA) PanCancer Atlas via cBioPortal[cite: 2].
* Molecular Docking: AutoDock Vina (Webina); RCSB PDB (ID: 1M17); PubChem (Erlotinib)[cite: 2].
* Synthetic Biology: Benchling Molecular Biology Workspace[cite: 2].
>>>>>>> e36ec5ecf867950f83686ed90c2f6503ee9aec4c
