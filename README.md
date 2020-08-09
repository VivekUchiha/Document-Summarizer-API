
# Document Summarizer API


An API which provides methods to summarize  text present in an image using Latent Dirichlet Allocation algorithm.
  

## Prerequisites
- python3 & pip3
## Setup

- Install tesseract-oct
```
$ sudo apt-get install tesseract-ocr
``` 
  
- Install pipenv.
```
$ pip3 install pipenv
```
- Clone this repository and change working directory to project folder.
```
$ git clone https://github.com/VivekUchiha/Document-Summarizer-API.git && cd Document-Summarizer-API
```

- Activate virtual environment and start install dependencies.

```
$ pipenv shell
$ pipenv install
```

  

## Running

  

```
$ python3 app.py
```

## Example

### Input

![Image](/sample.jpg?raw=true "Title")

### Output

```
{
  "extracted_text": [
    "Incidentally it has to be noted in this regard that Acop asked Elvas to make the analysis and it was to him that",
    "Elvas submitted his report Like the result of the third examination of the alleged suicide note however the",
    "Elvas report was suppressed in Acop s office Do these acts not make Acop liable for suppressing evidence ",
    " Another expert on handwriting analysis Ron Rice studied the alleged suicide note Rice did an analysis ",
    " Annex of the alleged suicide note He found the so called suicide note a fabrication His written",
    "conclusions follow "
  ],
  "topics": [
    [
      "acop",
      "note",
      "elvas",
      "conclusions",
      "suicide",
      "report",
      "follow"
      "alleged",
      "analysis",
      "suppressed",
      "rice",
      "acts",
      "expert",
      "like",
      "evidence",
      "studied",
      "submitted",
      "suppressing",
      "ron",
      "result",
      "liable",
      "handwriting",
      "examination",
      "office",
      "written"
    ]
  ]
}
```