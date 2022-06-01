
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
  - [Document Layout Analysis](#document-layout-analysis)
    - [English](#english-2)
    - [Japanese](#japanese)
  - [Document Question Answering](#document-question-answering)


# Document processing

Documents are an essential part of many businesses in many fields such as law, finance and technology, among others. Automatic processing of documents such as invoices, contracts and resumes is lucrative and opens up many new business avenues. The fields of natural language processing and computer vision have seen considerable progress with the development of deep learning, so these methods have begun to be incorporated into contemporary document understanding systems.

Here is a curated list of datasets for intelligent document processing.

## Document Classification

### English

- [GHEGA](https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-3-030-57058-3_28/MediaObjects/493083_1_En_28_Fig1_HTML.png) contains two groups of documents: 110 data-sheets of electronic components and 136 patents. Each group is further divided in classes: data-sheets classes share the component type and producer; patents classes share the patent source.
  <details>
    <summary><i>Example</i></summary>
    <img src="./images/GHEGA.jpeg" />
  </details>

- [RVL-CDIP Dataset](https://www.cs.cmu.edu/~aharley/rvl-cdip/) The RVL-CDIP dataset consists of 400,000 grayscale images in 16 classes (letter, memo, email, file folder, form, handwritten, invoice, advertisement, budget, news article, presentation, scientific publication, questionnaire, resume, scientific report, specification), with 25,000 images per class.
  <details>
    <summary><i>Example</i></summary>
    <img src="https://production-media.paperswithcode.com/datasets/RVL-CDIP-0000000502-f579eaab_GQ7QoTc.jpg" />
  </details>

## Key Information Extraction

### English

- [CORD](https://github.com/clovaai/cord) The dataset consists of thousands of Indonesian receipts, which contains images and box/text annotations for OCR, and multi-level semantic labels for parsing. Labels are the bouding box position and the text of the key informations.
  <details>
    <summary><i>Example</i></summary>
    <img src="https://guillaumejaume.github.io/FUNSD/img/two_forms.png" />
  </details>


- [FUNSD](https://guillaumejaume.github.io/FUNSD/) A dataset for Text Detection, Optical Character Recognition, Spatial Layout Analysis and Form Understanding. Its consists of 199 fully annotated forms, 31485 words, 9707 semantic entities, 5304 relations.
  <details>
    <summary><i>Example</i></summary>
    <img src="https://github.com/clovaai/cord/raw/master/figure/sample.png" />
  </details>

- [NIST](https://www.nist.gov/srd/nist-special-database-2) The NIST Structured Forms Database consists of 5,590 pages of binary, black-and-white images of synthesized documents: 900 simulated tax submissions, 5,590 images of completed structured form faces, 5,590 text files containing entry field answers.
  <details>
    <summary><i>Example</i></summary>
    <img src="https://www.nist.gov/sites/default/files/styles/2800_x_2800_limit/public/images/2019/04/27/sd2.jpg" />
  </details>

- [SROIE](https://drive.google.com/open?id=1ShItNWXyiY1tFDM5W02bceHuJjyeeJl2) Consists of a dataset with 1000 whole scanned receipt images and annotations for the competition on scanned receipts OCR and key information extraction (SROIE). Labels are the bouding box position and the text of the key informations.
  <details>
    <summary><i>Example</i></summary>
    <img src="https://production-media.paperswithcode.com/datasets/Screenshot_2021-08-09_at_14.29.44.png" />
  </details>

### Multilingual

- [GHEGA](https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-3-030-57058-3_28/MediaObjects/493083_1_En_28_Fig1_HTML.png) contains two groups of documents: 110 data-sheets of electronic components and 136 patents. Each group is further divided in classes: data-sheets classes share the component type and producer; patents classes share the patent source.
  <details>
    <summary><i>Example</i></summary>
    <img src="./images/GHEGA.jpeg" />
  </details>

- [XFUND](https://github.com/doc-analysis/XFUND) is a multilingual form understanding benchmark dataset that includes human-labeled forms with key-value pairs in 7 languages (Chinese, Japanese, Spanish, French, Italian, German, Portuguese).




## Optical Character Recognition



## Document Layout Analysis

### English

- [DocBank](https://doc-analysis.github.io/docbank-page/index.html) includes 500K document pages, with 12 types of semantic units: abstract, author, caption, date, equation, figure, footer, list, paragraph, reference, section, table, title.
  <details>
    <summary><i>Example</i></summary>
    <img src="./images/DocBank.png" />
  </details>

- [Layout Analysis Dataset](http://www.primaresearch.org/datasets/Layout_Analysis) contains realistic documents with a wide variety of layouts, reflecting the various challenges in layout analysis. Particular emphasis is placed on magazines and technical/scientific publications which are likely to be the focus of digitisation efforts.
  <details>
    <summary><i>Example</i></summary>
    <img src="http://www.primaresearch.org/www/media/datasets/Layout_Analysis.png" />
  </details>

- [PubLayNet](https://github.com/ibm-aur-nlp/PubLayNet) is a large dataset of document images, of which the layout is annotated with both bounding boxes and polygonal segmentations.
  <details>
    <summary><i>Example</i></summary>
    <img src="https://d3i71xaburhd42.cloudfront.net/b5799d10df17de3232540e990da69553800d6376/6-Figure5-1.png" />
  </details>

- [TableBank](https://doc-analysis.github.io/tablebank-page/index.html) is a new image-based table detection and recognition dataset built with novel weak supervision from Word and Latex documents on the internet, contains 417K high-quality labeled tables.
  <details>
    <summary><i>Example</i></summary>
    <img src="./images/TableBank.png" />
  </details>

### Japanese

- [HJDataset](https://github.com/dell-research-harvard/HJDataset) contains over 250,000 layout element annotations of seven types. In addition to bounding boxes and masks of the content regions, it also includes the hierarchical structures and reading orders for layout elements for advanced analysis.
  <details>
    <summary><i>Example</i></summary>
    <img src="https://dell-research-harvard.github.io/HJDataset/assets/teaser.png" />
  </details>

## Document Question Answering

