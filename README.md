
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

- [Document processing](#document-processing)
  - [Document Classification](#document-classification)
    - [English](#english)
  - [Key Information Extraction](#key-information-extraction)
    - [English](#english-1)
    - [Multilingual](#multilingual)
  - [Optical Character Recognition](#optical-character-recognition)
    - [English](#english-2)
  - [Document Layout Analysis](#document-layout-analysis)
    - [English](#english-3)
    - [Japanese](#japanese)
  - [Document Question Answering](#document-question-answering)
    - [English](#english-4)
- [Natural Language Processing](#natural-language-processing)
  - [Named-Entity Recognition](#named-entity-recognition)
    - [English](#english-5)
      - [Defense](#defense)
      - [Finance](#finance)
      - [Medical](#medical)
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

## Key Information Extraction

### English

- [CORD](https://bit.ly/3NmtdSc) The dataset consists of thousands of Indonesian receipts, which contains images and box/text annotations for OCR, and multi-level semantic labels for parsing. Labels are the bouding box position and the text of the key informations.
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://guillaumejaume.github.io/FUNSD/img/two_forms.png" />
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
    <img src="./images/GHEGA.jpeg" />
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

- <p><a href="https://bit.ly/395Qbyi">DocVQA</a> contains 50 K questions and 12K Images in the dataset. Images are collected from UCSF Industry Documents Library. Questions and answers are manually annotated.</p>
  <details>
    <summary><i>Preview</i></summary>
    <img src="https://bit.ly/3thmxNm" />
  </details>

# Natural Language Processing

## Named-Entity Recognition

Named-entity recognition (NER) (also known as (named) entity identification, entity chunking, and entity extraction) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.

State-of-the-art NER systems for English produce near-human performance. For example, the best system entering MUC-7 scored 93.39% of F-measure while human annotators scored 97.60% and 96.95%.

### English

#### Defense

- [re3d](https://bit.ly/3xcZLHq) focuses on entity and relationship extraction relevant to somebody operating in the role of a defence and security intelligence analyst.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/re3d.png" />
  </details>
  
  - [Airbus Aircraft Detection](https://www.kaggle.com/datasets/airbusgeo/airbus-aircrafts-sample-dataset/download) This tool can be used to detect automatically the number, size and type of aircrafts present on an airport. In turn, this can provide information about the activity of any airport.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/airbus detection.png" />
  </details>

- [Malware](https://bit.ly/3tdIwEM) consists of texts about malware. It was developed by researchers at the Singapore University of Technology and Design and DSO National Laboratories.
  <details>
    <summary><i>Preview</i></summary>
    <img src="./images/Malware.png" />
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
