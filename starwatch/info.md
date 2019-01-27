# Implementation

## Approaches

To find the entity name of one entity, we only need to sear in the first three pages. The name will either be in the title of the document or in the description of the document.

The most important information lies in the auditor's part and the financial statements. Generally,there will be related word(s) indicating that one section may is related to auditing or financial report.

As convention, auditors will explicitly state which part is their opinion, and they will also indicate the audit period. Finally, one auditing partner will sign on his/her report, and here is where the auditor name can be founded.

As for the financial data, they can be explicitly found in the Income Statement (which may have different name in different companies' report)


### Recognizing the entity name

1. The file name contains the entity name.
2. If the file name is not available, then we can fallback to the second method. If there are some address in the last page, then the line above the address is likely to be a company name.
3. If there is not any address in the last page (which is VERY unlikely), we can fallback to a supervised machine learning algorithm. The algorithm is described as follows:

First, we calculate the frequency of all the words in the training set files, and generate a table; this is the training process. The first step can generate a representative word frequency table for typical annual reports. Then, we calculate the word frequency table of the file that need to be tested and compare it with the frequency table of the training set. It is likely that the words that have unexpected high frequency is a part of the company name. Finally, we can search these words in the first three pages of the report, and it is likely that we can find the company name.

There are totally 2,487,246 words in the training set

## Difficulties

The OCR results are not good. Thus, we use a Python library pdfMine plus some self-written code to transform the pdf files to xml files.

# API

We encapsulate out files into one package `starWatch`. There are 3 important functions provided. 

## PDF to XML converter

`starLook.pdf2xml(f)` converts a PDF to a machine readable XML file. This function is wrapper and enhancer of the ![pdfmine](https://github.com/pdfminer/pdfminer.six) library. It is founded useful when we processing this project.

The format of the returned object should

Parameters:
- `f`: file to open. It should be either a file, a filename string or a Path.
