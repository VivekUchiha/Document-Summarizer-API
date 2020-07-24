import textract

SampleText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def getTextFromFile(filename):
    """
    This function will handle the core OCR processing of different file types.
    """
    text = textract.process(filename, method='tesseract').decode("utf8")  
    return text

if __name__ == '__main__':
	print(getTextFromFile('images/sample-form.jpg'))
