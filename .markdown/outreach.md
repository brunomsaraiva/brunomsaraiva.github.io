# Scientific Talks

## 2024
### AI/Smart microscopy workshop (AISMW2024)
- **Title**: Accelerating bioimage analysis throught an adaptive Python framework
- **Location**: Lund, Sweden
- **Dates**: 17-21 June 2024

## 2023

### NEUBIAS 2023
- **Title**: NanoPyx: a high-performance Python Library for microscopy image analysis
- **Location**: Porto, Portugal
- **Dates**:11-12 May 2023
- **Abstract**: Super-resolution microscopy is a powerful technique for investigating biological samples at the nanoscale. However, users wanting to take advantage of this technique face several challenges: access to super-resolution microscopy is limited by available microscopes, and the resulting data can be large and complex, making it difficult to analyse. To address these challenges, we present NanoPyx, a high-performance Python library that enables users to generate super-resolution microscopy images without the need for specialised hardware through the implementation of SRRF-based approaches (SRRF standing for Super-Resolution Radial Fluctuations)1. In addition to super-resolution image generation, NanoPyx provides a range of tools for super-resolution microscopy image processing and analysis, through implementations of timelapse drift correction and alignment of different colour channels based on inter-timepoint cross-correlations2. NanoPyx also allows users to detect artefacts introduced by the super-resolution image producing methods using SQUIRREL (super-resolution quantitative image rating and reporting of error locations)3 and to estimate image resolution through implementations of FRC (Fourier Ring Correlation)4 and Decorrelation analysis. Nanopyx library methods will also be implemented as plugins for the open-source Python-based image viewer, Napari6, allowing users to easily view, analyse, and process microscopy image datasets in real-time, and produce super-resolution images of biological samples.

## 2022

### EMBO Course: Computational Optical Biology
- **Title**: Biological discovery through image analysis
- **Location**: Oeiras, Portugal
- **Dates**: 2-7 October 2022

## 2021

### Microbiotec 21
- **Title**: eHooke: a framework for automated image analysis of <i>Staphylococcus aureus</i> based on cell cycle progression
- **Location**: Online
- **Dates**: 23-26 November 2021
- **Abstract**: Imaging of bacterial cells by fluorescence microscopy is an essential approach for cell biology studies on bacteria, especially for studies on cell division and morphogenesis. Due to the amount of time and work required to perform manual analyses on microscopy images, several image analysis tools were developed(1,2), capable of performing automatic cell detection and measurement of single cell features. However, when the goal is to uncover the cellular processes involved in bacterial growth and division, it is of utter importance to perform these analyses in the context of cell cycle progression. Manual assignment of cell cycle stages is a very laborious, time-consuming task and is prone to user bias. In rod-shaped or ovoid bacteria, elongation can be used as a proxy for cell cycle progression. However, that is not the case for cocci, such as Staphylococcus aureus. For this reason, we developed eHooke(3), an image analysis framework developed specifically for automated analysis of microscopy images of round-shaped bacterial cells. Furthermonre, we trained an artificial neural network to automatically classify the cell cycle phase of individual S. aureus cells and implemented it in eHooke. This allows users to use eHooke to obtain biologically relevant data on fluorescence signals, morphological features and cellular localization of proteins in individual cells, in the context of the cell cycle stage.

# Poster Sessions
## 2023

### Seeing is believing: imaging the molecular processes of life 2023
- **Title**: NanoPyx: Accelerating bioimage analysis with adaptive machine learning
- **Location**: Heidelberg, Germany
- **Dates**: 4-7 October 2023
- **Abstract**: In the realm of bioimaging, the analysis of large and intricate datasets has become a bottleneck for researchers, impeding the efficiency and scalability of experiments. To surmount this challenge, we introduce NanoPyx, a Python framework designed to facilitate rapid and adaptive bioimage analysis. At the heart of NanoPyx lies the Liquid Engine, an intelligent machine learning-based agent that significantly expedites image analysis tasks. Central to its functionality is a meta-programming tool that empowers users to effortlessly develop multiple CPU and GPU code implementations for the same task. Leveraging the Liquid Engine's dynamic decision-making capabilities, the fastest implementation for a given device is automatically selected, optimizing runtime performance. Notably, NanoPyx integrates a comprehensive suite of super-resolution methods, including previously exclusive NanoJ ImageJ plugins, encompassing drift correction, channel registration, SRRF/eSRRF, Fourier Ring Correlation, Image Decorrelation Analysis, NanoJ-SQUIRREL's error map for artifact detection, and more to come. Through its adaptive nature and self-optimization capabilities, NanoPyx offers substantially reduced runtimes compared to its predecessor, NanoJ. Moreover, NanoPyx caters to researchers of varying coding expertise, providing accessible access through Python libraries, interactive Codeless Jupyter Notebooks, and a seamless napari plugin. Importantly, the self-optimization principles underlying the Liquid Engine hold considerable promise for advancing high-performance computing in diverse research domains. NanoPyx emerges as a valuable tool empowering researchers to unleash the full potential of bioimaging data analysis.

### Focus On Microscopy 2023
- **Title**: 
- **Location**: Porto, Portugal
- **Dates**: 2-5 April 2023
- **Abstract**: Super-resolution microscopy is a powerful technique for investigating biological samples at the nanoscale. However, users wanting to take advantage of this technique face several challenges: access to super-resolution microscopy is limited by available microscopes, and the resulting data can be large and complex, making it difficult to analyse. To address these challenges, we present NanoPyx, a high-performance Python library that enables users to generate super-resolution microscopy images without the need for specialised hardware through the implementation of SRRF-based approaches (SRRF standing for  Super-Resolution Radial Fluctuations)1. In addition to super-resolution image generation, NanoPyx provides a range of tools for super-resolution microscopy image processing and analysis, through implementations of timelapse drift correction and alignment of different colour channels based on inter-timepoint cross-correlations2. NanoPyx also allows users to detect artefacts introduced by the super-resolution image producing methods using SQUIRREL (super-resolution quantitative image rating and reporting of error locations)3 and to estimate image resolution through implementations of FRC (Fourier Ring Correlation)4 and Decorrelation analysis. Nanopyx library methods will also be implemented as plugins for the open-source Python-based image viewer, Napari6, allowing users to easily view, analyse, and process microscopy image datasets in real-time, and produce super-resolution images of biological samples.