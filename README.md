
<div align="center">
  <h1>Awesome Datasets</h1>
</div>

We're collecting (an admittedly opinionated) list of data annotated datasets in high quality. Most of the data sets listed below are free, however, some are not. They are classified by use case.

*We're only at the beginning, and you can help by contributing to this GitHub!*

<!-- omit in toc -->
## How Can I Help?

If you're interested in this area and would like to hear more, join our [Slack community (coming soon)](#)! We'd also appreciate if you could fill out this short [form (coming soon)](#) to help us better understand what your interests might be.

<!-- omit in toc -->
### Feedback

If you have ideas on how we can make this repository better, feel free to submit an issue with suggestions.

<!-- omit in toc -->
### Contributing

We want this resource to grow with contributions from readers and data enthusiasts. If you'd like to make contributions to this Github repository, please read our contributing guidelines.

<!-- omit in toc -->
# Table of Content
- [Audio](#audio)
   - [Speech Recognition](#Speech-Recognition)
      - [English](#english)

- [Document processing](#document-processing)
  - [Document Classification](#document-classification)
    - [English](#english-1)
  - [Key Information Extraction](#key-information-extraction)
    - [English](#english-2)
    - [Multilingual](#multilingual)
  - [Optical Character Recognition](#optical-character-recognition)
    - [English](#english-3)
  - [Document Layout Analysis](#document-layout-analysis)
    - [English](#english-4)
    - [Japanese](#japanese)
  - [Document Question Answering](#document-question-answering)
    - [English](#english-5)
    - [Multilingual](#multilingual-1)
- [Image Processing](#image-processing)
  - [Instant Segmentation](#instant-segmentation)
      - [Defense](#defense) 
      - [Manufacturing](#manufacturing)
      - [Medical](#medical)
- [Natural Language Processing](#natural-language-processing)
  - [Named-Entity Recognition](#named-entity-recognition)
    - [English](#english-6)
      - [Defense](#defense-1)
      - [Finance](#finance)
      - [Medical](#medical-1)
      - [News](#news)
      - [Queries](#queries)
      - [Social media](#social-media)
      - [Technology](#technology)
      - [Twitter](#twitter)
      - [Various](#various)
      - [Wikipedia](#wikipedia)
    - [French](#french)
      - [Medical](#medical-1)
      - [News](#news-1)
      - [Twitter](#twitter-1)
      - [Wikipedia](#wikipedia-1)
  - [Relation Extraction](#relation-extraction)
# Audio
## Speech Recognition
### English
- [M-AILABS Speech Dataset](https://www.caito.de/2019/01/03/the-m-ailabs-speech-dataset/) Include 1000 hours of audio plus transcriptions. It includes multiple languages arranged by male voices, female voices, and a mix of the two. Most of the data is based on LibriVox and Project Gutenberg.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/M-AILABS Speech Dataset.png" />
  </details>
- [CREMA-D](https://dagshub.com/mert.bozkirr/CREMA-D) is a dataset of 7,442 original clips from 91 actors. These clips were from 48 male and 43 female actors between the ages of 20 and 74 coming from various ethnicities.



# Document processing

Documents are an essential part of many businesses in many fields such as law, finance and technology, among others. Automatic processing of documents such as invoices, contracts and resumes is lucrative and opens up many new business avenues. The fields of natural language processing and computer vision have seen considerable progress with the development of deep learning, so these methods have begun to be incorporated into contemporary document understanding systems.

Here is a curated list of datasets for intelligent document processing.

## Document Classification

### English

- [GHEGA](https://bit.ly/3x6z33q) contains two groups of documents: 110 data-sheets of electronic components and 136 patents. Each group is further divided in classes: data-sheets classes share the component type and producer; patents classes share the patent source.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/GHEGA.jpeg" />
  </details>

- [RVL-CDIP Dataset](https://bit.ly/3x8W4CK) The RVL-CDIP dataset consists of 400,000 grayscale images in 16 classes (letter, memo, email, file folder, form, handwritten, invoice, advertisement, budget, news article, presentation, scientific publication, questionnaire, resume, scientific report, specification), with 25,000 images per class.
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://production-media.paperswithcode.com/datasets/RVL-CDIP-0000000502-f579eaab_GQ7QoTc.jpg" />
  </details>
- [Top Streamers on Twitch](https://www.kaggle.com/datasets/aayushmishra1512/twitchdata) contains data of Top 1000 Streamers from past year. This data consists of different things like number of viewers, number of active viewers, followers gained and many other relevant columns regarding a particular streamer. It has 11 different columns with all the necessary information that is needed. 
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/Top Streamers on Twitch.png" />
  </details>

## Key Information Extraction

### English

- [CORD](https://bit.ly/3NmtdSc) The dataset consists of thousands of Indonesian receipts, which contains images and box/text annotations for OCR, and multi-level semantic labels for parsing. Labels are the bouding box position and the text of the key informations.
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://guillaumejaume.github.io/FUNSD/img/two_forms.png" />
  </details>

- [DUE: End-to-End Document Understanding Benchmark](https://duebenchmark.com/leaderboard) includes Visual Question Answering, Key Information Extraction, and Machine Reading Comprehension tasks over various document domains and layouts featuring tables, graphs, lists, and infographics. In addition, the current study reports systematic baselines and analyzes challenges in currently available datasets using recent advances in layout-aware language modeling.
  <details>
    <summary><i>Preview</i></summary>
    <img src="images/DUE.png" />
  </details>



- [FUNSD](https://bit.ly/3Q3owhV) A dataset for Text Detection, Optical Character Recognition, Spatial Layout Analysis and Form Understanding. Its consists of 199 fully annotated forms, 31485 words, 9707 semantic entities, 5304 relations.
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://github.com/clovaai/cord/raw/master/figure/sample.png" />
  </details>

- [NIST](https://bit.ly/3Q7aBaS) The NIST Structured Forms Database consists of 5,590 pages of binary, black-and-white images of synthesized documents: 900 simulated tax submissions, 5,590 images of completed structured form faces, 5,590 text files containing entry field answers.
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://www.nist.gov/sites/default/files/styles/2800_x_2800_limit/public/images/2019/04/27/sd2.jpg" />
  </details>

- [SROIE](https://bit.ly/3MnIWzl) Consists of a dataset with 1000 whole scanned receipt images and annotations for the competition on scanned receipts OCR and key information extraction (SROIE). Labels are the bouding box position and the text of the key informations.
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://production-media.paperswithcode.com/datasets/Screenshot_2021-08-09_at_14.29.44.png" />
  </details>

### Multilingual

- [GHEGA](https://bit.ly/3x6z33q) contains two groups of documents: 110 data-sheets of electronic components and 136 patents. Each group is further divided in classes: data-sheets classes share the component type and producer; patents classes share the patent source.
  <details>
    <summary><i>Preview</i></summary>
    <img src="/images/GHEGA.png" />
  </details>

- [XFUND](https://bit.ly/3zly4yW) is a multilingual form understanding benchmark dataset that includes human-labeled forms with key-value pairs in 7 languages (Chinese, Japanese, Spanish, French, Italian, German, Portuguese).


## Optical Character Recognition

### English

- [FUNSD](https://bit.ly/3Q3owhV) for Text Detection, Optical Character Recognition, Spatial Layout Analysis and Form Understanding. Its consists of 199 fully annotated forms, 31485 words, 9707 semantic entities, 5304 relations.
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://github.com/clovaai/cord/raw/master/figure/sample.png" />
  </details>

- [RDCL2019](https://bit.ly/3xcEEoz) contains scanned pages from contemporary magazines and technical articles.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/RDCL2019.png" />
  </details>

- [SROIE](https://bit.ly/3MnIWzl) consists of a dataset with 1000 whole scanned receipt images and annotations for the competition on scanned receipts OCR and key information extraction (SROIE). Labels are the bouding box position and the text of the key informations.
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://production-media.paperswithcode.com/datasets/Screenshot_2021-08-09_at_14.29.44.png" />
  </details>

- [Synth90k](https://bit.ly/3NoVLdX) consists of 9 million images covering 90k English words.
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://www.robots.ox.ac.uk/~vgg/data/text/synthflow.png" />
  </details>

- [Total Text Dataset](https://bit.ly/3QfKrmn) consists of 1555 images with more than 3 different text orientations: Horizontal, Multi-Oriented, and Curved, one of a kind.
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://github.com/cs-chan/Total-Text-Dataset/raw/master/ttstatistics.png" />
  </details>

## Document Layout Analysis

### English

- [DocBank](https://bit.ly/3xoheOF) includes 500K document pages, with 12 types of semantic units: abstract, author, caption, date, equation, figure, footer, list, paragraph, reference, section, table, title.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/DocBank.png" />
  </details>

- [Layout Analysis Dataset](https://bit.ly/3avHxZZ) contains realistic documents with a wide variety of layouts, reflecting the various challenges in layout analysis. Particular emphasis is placed on magazines and technical/scientific publications which are likely to be the focus of digitisation efforts.
  <details>
    <summary><i>Preview</i></summary>
    <img src="http://www.primaresearch.org/www/media/datasets/Layout_Analysis.png" />
  </details>

- [PubLayNet](https://bit.ly/3NScp5u) is a large dataset of document images, of which the layout is annotated with both bounding boxes and polygonal segmentations.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/PubLayNet.png" />
  </details>

- [TableBank](https://bit.ly/3NnRnMl) is a new image-based table detection and recognition dataset built with novel weak supervision from Word and Latex documents on the internet, contains 417K high-quality labeled tables.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/TableBank.png" />
  </details>

### Japanese

- <p><a href="https://bit.ly/3xdqdkt">HJDataset</a> contains over 250,000 layout element annotations of seven types. In addition to bounding boxes and masks of the content regions, it also includes the hierarchical structures and reading orders for layout elements for advanced analysis.</p>
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/HJDataset.png" />
  </details>

## Document Question Answering
### English
- [AmbigQA](https://nlp.cs.washington.edu/ambigqa//) is inherent to open-domain question answering; especially when exploring new topics, it can be difficult to ask questions that have a single, unambiguous answer. AmbigQA is a new open-domain question answering task which involves predicting a set of question-answer pairs, where every plausible answer is paired with a disambiguated rewrite of the original question.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/AmbigQA.png" />
  </details>
- [Break](https://allenai.github.io/Break/)  is a question understanding dataset, aimed at training models to reason over complex questions.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/break.png" />
  </details>
- [ConvAI2 dataset](http://convai.io/data/ ) The dataset contains more than 2000 dialogs for a PersonaChat contest, where human evaluators recruited through the Yandex.Toloka crowdsourcing platform chatted with bots submitted by teams.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/ConvAI2 dataset.png" />
  </details>
- [Customer Support on Twitter](https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter )  This Kaggle dataset includes more than 3 million tweets and responses from leading brands on Twitter.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/Customer Support on Twitter.png" />
  </details>
- <p><a href="https://bit.ly/395Qbyi">DocVQA</a> contains 50 K questions and 12K Images in the dataset. Images are collected from UCSF Industry Documents Library. Questions and answers are manually annotated.</p>
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://bit.ly/3thmxNm" />
  </details>
- [DuReader 2.0](https://allenai.github.io/Break/)  is a large-scale, open-domain Chinese data set for reading comprehension (RK) and question answering (QA). It contains over 300K questions, 1.4M obvious documents and corresponding human-generated answers.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/DuReader 2.0.jpg" />
  </details>
- [Maluuba goal-oriented dialogue](https://datasets.maluuba.com/Frames ) is a set of open dialogue data where the conversation is aimed at accomplishing a task or making a decision - in particular, finding flights and a hotel. The data set contains complex conversations and decisions covering over 250 hotels, flights and destinations.
- [NarrativeQA](https://github.com/deepmind/narrativeqa)  is a data set constructed to encourage deeper understanding of language. This dataset involves reasoning about reading whole books or movie scripts. This dataset contains approximately 45,000 pairs of free text question-and-answer pairs. 
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/NarrativeQA.png" />
  </details>
- [QASC](https://github.com/allenai/qasc) is a question-and-answer data set that focuses on sentence composition. It consists of 9,980 8-channel multiple-choice questions on elementary school science (8,134 train, 926 dev, 920 test), and is accompanied by a corpus of 17M sentences. 
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/QASC.png" />
  </details>
- [QuAC](https://quac.ai/) is a data set for answering questions in context that contains 14K information-seeking QI dialogues (100K questions in total). Question Answering in Context is a dataset for modeling, understanding, and participating in information-seeking dialogues.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/QuAC.png" />
  </details>
- [SGD (Schema-Guided Dialogue) dataset](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue)  containing over 16k of multi-domain conversations covering 16 domains. 
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/The Schema-Guided Dialogue Dataset.png" />
  </details>
- [TREC QA Collection](https://trec.nist.gov/data/qa.html)  has had a track record of answering questions since 1999. In each track, the task was defined so that systems had to retrieve small fragments of text containing an answer to open-domain and closed-domain questions.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/TREC QA Collection.png" />
  </details>
- [The WikiQA corpus](https://www.microsoft.com/en-us/download/details.aspx?id=52419&from=http%3A%2F%2Fresearch.microsoft.com%2Fapps%2Fmobile%2Fdownload.aspx%3Fp%3D4495da01-db8c-4041-a7f6-7984a4f6a905)  Is a set of publicly available pairs of questions and phrases collected and annotated for research on the answer to open-domain questions. In order to reflect the true information needs of general users, they used Bing query logs as a source of questions. Each question is linked to a Wikipedia page that potentially contains the answer.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/The WikiQA corpus.png" />
  </details>


### Multilingual  
- [EXCITEMENTS datasets](https://github.com/hltfbk/EOP-1.2.1/wiki/Data-Sets#data-sets-that-have-to-be-downloaded-separately)  is available in English and Italian and contain negative comments from customers giving reasons for their dissatisfaction with a given company.
- [OPUS](https://allenai.github.io/Break/)   was created for the standardization and translation of social media texts. It is built by randomly selecting 2,000 messages from the NUS corpus of SMS in English and then translating them into formal Chinese.
  <details>  
    <summary><i>Preview</i></summary>
    <img src="./images/OPUS .png" />
  </details>
- [TyDi QA](https://github.com/google-research-datasets/tydiqa#download-the-dataset )  is a set of question response data covering 11 typologically diverse languages with 204K question-answer pairs.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/TyDi QA.png" />
  </details>
# Image Processing
## Instant Segmentation
### Defense 
- [A DATASET FOR DETECTING FLYING AIRPLANES ON SATELLITE IMAGES](https://ieee-dataport.org/open-access/dataset-detecting-flying-airplanes-satellite-images) contains satellite images of areas of interest surrounding 30 different European airports. It also provides ground-truth annotations of flying airplanes in part of those images to support future research involving flying airplane detection. This dataset is part of the work entitled "Measuring economic activity from space: a case study using flying airplanes and COVID-19" published by the IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/A DATASET FOR DETECTING FLYING AIRPLANES ON SATELLITE IMAGES.png" />
  </details>
- [Airbus Aircraft Detection](https://www.kaggle.com/datasets/airbusgeo/airbus-aircrafts-sample-dataset/download) can be used to detect the number, size and type of aircrafts present on an airport. In turn, this can provide information about the activity of any airport.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/airbus detection.jpg" />
  </details>
- [Highway Traffic Videos Dataset](https://www.kaggle.com/datasets/aryashah2k/highway-traffic-videos-dataset) is a database of video of traffic on the highway used in [1] and [2]. The video was taken over two days from a stationary camera overlooking I-5 in
Seattle, WA. The video were labeled manually as light, medium, and heavy traffic, which correspond respectively to free-flowing traffic, traffic at reduced speed, and stopped or very slow speed traffic.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/Highway Traffic Videos Dataset.png" />
  </details>
- [iSAID](https://captain-whu.github.io/iSAID/dataset.html) contain 655 451 object instances from 15 categories across 2 806 high resolution images. iSAID uses pixel-level annotations. The object categories in iSAID include plane, ship, storage tank, baseball diamond, tennis court, basketball court, ground track field, harbor, bridge, large vehicle, small vehicle, helicopter, roundabout, soccer ball field and swimming pool. The images of ISAID are mainly collected from google earth

  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/iSAID.png" />
  </details>
- [Traffic Analysis in Original Video Data of Ayalon Road](https://github.com/ido90/AyalonRoad) Is compose of 81 (14 hours) videos recording the traffic in Ayalon Road. It can detect and track vehicle over consecutive frame.

  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/Traffic Analysis in Original Video Data of Ayalon Road.png" />
  </details>
### Manufacturing
- [Coco Car Damage Detection Dataset](https://www.kaggle.com/datasets/lplenka/coco-car-damage-detection-dataset ) contains car images with one or more damaged parts. The dataset has 150 images.
   <details>
  <summary><i>Preview</i></summary>
  <img src="./images/Coco Car Damage Detection Dataset.jpg" />
     </details>

- [DAGM 2007](https://www.kaggle.com/datasets/mhskjelvareid/dagm-2007-competition-dataset-optical-inspection ) is a synthetic dataset for defect detection on textured surfaces. It was originally created for a competition at the 2007 symposium of the DAGM
   <details>
  <summary><i>Preview</i></summary>
  <img src="./images/DAGM 2007.png" />
   </details>
     
- [MVTec AD](https://www.mvtec.com/company/research/datasets/mvtec-ad/) is a dataset for benchmarking anomaly detection methods with a focus on industrial inspection. It contains over 5000 high-resolution images divided into fifteen different object and texture categories. Each category comprises a set of defect-free training images and a test set of images with various kinds of defects as well as images without defects.
   <details>
  <summary><i>Preview</i></summary>
  <img src="./images/MV.png" />
    </details>
- [Oil Storage Tanks](https://www.kaggle.com/datasets/towardsentropy/oil-storage-tanks) contains nearly 200 satellite images taken from Google Earth of tank-containing industrial areas around the world. Images are annotated with bounding box information for floating head tanks in the image. Fixed head tanks are not annotated.
   <details>
  <summary><i>Preview</i></summary>
  <img src="./images/OIL.png" />
     </details>

- [Kolector surface](https://www.vicos.si/resources/kolektorsdd/) is a dataset to detect steel defect.
   <details>
  <summary><i>Preview</i></summary>
  <img src="./images/defect detection 2.png" />
    </details>
### Medical 
- [BRATS2016](https://www.smir.ch/BRATS/Start2016) BRATS 2016 is a brain tumor segmentation dataset. It shares the same training set as BRATS 2015, which consists of 220 HHG and 54 LGG. Its testing dataset consists of 191 cases with unknown grades.
    <details>
  <summary><i>Preview</i></summary>
  <img src="./images/BRATS2016.jpg" />
    </details>
- [CheXpert](https://stanfordmlgroup.github.io/competitions/chexpert/) dataset contains 224,316 chest radiographs of 65,240 patients with both frontal and lateral views available. The task is to do automated chest x-ray interpretation, featuring uncertainty labels and radiologist-labeled reference standard evaluation sets.
    <details>
  <summary><i>Preview</i></summary>
  <img src="./images/CheXpert.jpg" />
    </details>
- [CT Medical Images](https://www.kaggle.com/datasets/kmader/siim-medical-images) is designed to allow for different methods to be tested for examining the trends in CT image data associated with using contrast and patient age. The data are a tiny subset of images from the cancer imaging archive. They consist of the middle slice of all CT images taken where valid age, modality, and contrast tags could be found. This results in 475 series from 69 different patients.
    <details>
  <summary><i>Preview</i></summary>
  <img src="./images/CT Medical Images.jpg" />
    </details>
- [Open Access Series of Imaging Studies (OASIS)](https://www.oasis-brains.org/) is a retrospective compilation of data for >1000 participants that were collected across several ongoing projects through the WUSTL Knight ADRC over the course of 30 years. Participants include 609 cognitively normal adults and 489 individuals at various stages of cognitive decline ranging in age from 42-95yrs.
    <details>
  <summary><i>Preview</i></summary>
  <img src="./images/Open Access Series of Imaging Studies (OASIS).jpg" />
    </details>
- [TMED (Tufts Medical Echocardiogram Dataset)](https://paperswithcode.com/dataset/tmed) contains imagery from 2773 patients and supervised labels for two classification tasks from a small subset of 260 patients (because labels are difficult to acquire). All data is de-identified and approved for release by our IRB. Imagery comes from transthoracic echocardiograms acquired in the course of routine care consistent with American Society of Echocardiography (ASE) guidelines, all obtained from 2015-2020 at Tufts Medical Center.
    <details>
  <summary><i>Preview</i></summary>
  <img src="./images/TMED (Tufts Medical Echocardiogram Dataset).png" />
    </details>
# Natural Language Processing

## Named-Entity Recognition

Named-entity recognition (NER) (also known as (named) entity identification, entity chunking, and entity extraction) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.

State-of-the-art NER systems for English produce near-human performance. For example, the best system entering MUC-7 scored 93.39% of F-measure while human annotators scored 97.60% and 96.95%.

### English

#### Defense
- [CCCS-CIC-AndMal-2020](https://www.unb.ca/cic/datasets/andmal2020.html) proposes a new comprehensive and huge android malware dataset, named CCCS-CIC-AndMal-2020. The dataset includes 200K benign and 200K malware samples totalling to 400K android apps with 14 prominent malware categories and 191 eminent malware families.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/CCCS-CIC-AndMal-2020.png" />
  </details>
- [Malware](https://bit.ly/3tdIwEM) consists of texts about malware. It was developed by researchers at the Singapore University of Technology and Design and DSO National Laboratories.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/Malware.png" />
  </details>
     
- [re3d](https://bit.ly/3xcZLHq) focuses on entity and relationship extraction relevant to somebody operating in the role of a defence and security intelligence analyst.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/re3d.png" />
  </details>
  


#### Finance

- <p><a href="https://bit.ly/3x1ZTJS">SEC-filings</a> is generated using CoNll2003 data and financial documents obtained from U.S. Security and Exchange Commission (SEC) filings.</p>
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/SEC-filings.png" />
  </details>

#### Medical

- [AnEM](https://bit.ly/38RDLd0) consists of abstracts and full-text biomedical papers.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/AnEM.png" />
  </details>

- [CADEC](https://bit.ly/3xvywtj) is a corpus of adverse drug event annotations.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/CADEC.png" />
  </details>

- [i2b2-2006](https://bit.ly/3MhJxSR) is the Deidentification and Smoking Challenge dataset.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/i2b2_2006.png" />
  </details>

- [i2b2-2014](https://bit.ly/3mhcX95) is the 2014 De-identification and Heart Disease Risk Factors Challenge.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/i2b2_2014.png" />
  </details>


#### News

- [CONLL 2003](https://bit.ly/3NXfCR8) is an annotated dataset for Named Entity Recognition. The tokens are labeled under one of the 9 possible tags.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/CONLL 2003.png" />
  </details>

- [MUC-6](https://bit.ly/3GS2QkC) contains the 318 annotated Wall Street Journal articles, the scoring software and the corresponding documentation used in the MUC6 evaluation.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/MUC-6.png" />
  </details>

- [NIST-IEER](https://bit.ly/3NXfzoq)
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/NIST-IEER.png" />
  </details>
  

#### Queries

- [MITMovie](https://bit.ly/3NrwoIg) is a semantically tagged training and test corpus in BIO format.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/MITMovie.png" />
  </details>

- [MITRestaurant](https://bit.ly/3x4qAxw) is a semantically tagged training and test corpus in BIO format.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/MITRestaurant.png" />
  </details>

#### Social media	
- [Enron](https://bit.ly/3x4qAxw) Over half a million anonymized emails from over 100 users. It’s one of the few publically available collections of “real” emails available for study and training sets. 
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/Enron2.png" />
  </details>
- <p><a href="https://bit.ly/3x8Apuu">WNUT17</a> is the dataset for the WNUT 17 Emerging Entities task. It contains text from Twitter, Stack Overflow responses, YouTube comments, and Reddit comments.</p>
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/WNUT17.png" />
  </details>

#### Technology

- <p><a href="https://bit.ly/3xlUK0t">Assembly</a> is a dataset for Named Entity Recognition (NER) from assembly operations text manuals.</p>
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/Assembly.png" />
  </details>

#### Twitter

- [BTC](https://bit.ly/3aomybD) is the Broad Twitter corpus, a dataset of tweets collected over stratified times, places and social uses.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/BTC.png" />
  </details>

- [Ritter](https://bit.ly/3xkMrlC) is the same as the training portion of WNUT16 (though with sentences in a different order).
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/Ritter.png" />
  </details>

#### Various
  
  
- [BBN](https://bit.ly/3ml7dvk) contains approximately 24,000 pronoun coreferences as well as entity and numeric annotation for approximately 2,300 documents.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/BBN.png" />
  </details>

- [Groningen Meaning Bank (GMB)](https://bit.ly/3Q5Dfck) comprises thousands of texts in raw and tokenised format, tags for part of speech, named entities and lexical categories, and discourse representation structures compatible with first-order logic.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/Groningen Meaning Bank (GMB).png" />
  </details>

- [OntoNotes 5](https://bit.ly/3Q7bgsS) is a large corpus comprising various genres of text (news, conversational telephone speech, weblogs, usenet newsgroups, broadcast, talk shows) in three languages (English, Chinese, and Arabic) with structural information (syntax and predicate argument structure) and shallow semantics (word sense linked to an ontology and coreference).
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/OntoNotes 5.jpg" />
  </details>

#### Wikipedia

- [GUM-3.1.0](https://bit.ly/3xmegu0) is the Georgetown University Multilayer Corpus.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/GUM-3.1.0.png" />
  </details>

- [wikigold](https://bit.ly/3aulGSF) is a manually annotated collection of Wikipedia text.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/wikigold.png" />
  </details>

- [WikiNEuRal](https://bit.ly/3xafLdh) is a high-quality automatically-generated dataset for Multilingual Named Entity Recognition.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/WikiNEuRal.png" />
  </details>

### French

#### Medical

- <p><a href="https://bit.ly/3mgGzDG">QUAERO French Medical Corpus</a> has been initially developed as a resource for named entity recognition and normalization.</p>
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/QUAERO French Medical Corpus.jpeg" />
  </details>

#### News

- <p><a href="https://bit.ly/39fa5GS">Europeana Newspapers (Dutch, French, German)</a> is a Named Entity Recognition corpora for Dutch, French, German from Europeana Newspapers.</p>
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/Europeana Newspapers (Dutch, French, German).png" />
  </details>

#### Twitter

- <p><a href="https://bit.ly/3zebtV0">CAp 2017 - (Twitter data)</a> concerns the problem of Named Entity Recognition (NER) for tweets written in French.</p>
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/CAp 2017 - (Twitter data).png" />
  </details>

#### Wikipedia

- [DBpedia abstract corpus](https://bit.ly/3Q2OXo0) contains a conversion of Wikipedia abstracts in seven languages (dutch, english, french, german, italian, japanese and spanish) into the NLP Interchange Format (NIF).
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/DBpedia abstract corpus.png" />
  </details>

- [WikiNER](https://bit.ly/3PZq8t4) is a multilingual named entity recognition dataset from Wikipedia.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/WikiNER.png" />
  </details>

- [WikiNEuRal](https://bit.ly/3xafLdh) is a high-quality automatically-generated dataset for Multilingual Named Entity Recognition.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/WikiNEuRal - fr.png" />
  </details>

## Relation Extraction

Coming soon! 😘
