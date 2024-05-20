# IMAGE FORGERY AND RUMOUR DETECTION

**OVERVIEW**
This software is designed to detect image forgery and distinguish between true and false rumors. It combines advanced image processing techniques with natural language processing (NLP) to ensure the integrity of visual and textual content. The project includes two primary components: image forgery detection and rumor detection.

**FEATURES**
 * Image Forgery Detection
1. JPEG Compression Detection: Identifies inconsistencies in JPEG compression artifacts to detect tampering.
2. CFA Artifact Detection: Uses Color Filter Array (CFA) artifacts to reveal forgeries.
3. Noise Variance Inconsistency Detection: Detects variations in noise patterns across the image to find manipulated areas.
4. Copy-Move Detection: Identifies duplicated regions within an image to detect copy-move forgeries.
5. Double Compression Detection: Analyzes inconsistencies in compression artifacts to detect images compressed multiple times.
6. Single Compression Detection: Detects anomalies in single compressed images to reveal potential manipulations.
7. Metadata Analysis: Extracts and analyzes metadata from images to uncover hidden information and discrepancies.
8. Hex Viewer: Provides a hex viewer for examining the raw binary data of an image for detailed forensic analysis.

 * Rumor Detection
1. Classification and Regression: Utilizes machine learning models for classifying rumors and predicting their spread.
2. Decision Trees: Implements decision tree algorithms to enhance the accuracy of rumor detection.
3. TF-IDF Vectors: Employs Term Frequency-Inverse Document Frequency (TF-IDF) vectors for textual feature extraction.

 **Technical Details**
 * Technologies Used:
1. Python: Main programming language for both image and text processing.
2. OpenCV: For image processing tasks.
3. scikit-learn: For implementing machine learning algorithms.
4. TensorFlow: For deep learning models in rumor detection.
5. Natural Language Toolkit (NLTK): For NLP tasks in rumor detection.
6. Flask: For creating a web interface for the software.


**USUAGE**
1. First download all the files uploaded and put them in a folder
2. Make a folder named 'Image Forgery' and put the mentioned below files in that folder for the image forgery part
   - `FrogeryDection.py`
   - `GUI.py`
   - `Metadata_analysis.txt`
   - `Rumour_detection.py`
   - `hex.py`
   - `hex_viewer.txt`
   - `image_processing.py`
   - `main.py`
   - `noise_variance.py`
   - `output.png`
   - `temp.jpg`
   - `tempCodeRunnerFile.py`
   - `copy_move_cfa.py`
   - `double_jpeg_compression.py`
   - `encode_image.py`
4. Make a folder name 'venv' and put the downloaded folders in that folder:
   - `Lib.zip`
   - `Script.zip` and pyvenw.cfg
5. Make a folder name 'input' and put the below mentioned downloaded folders in that folder:
  - `CFA-Aritifiact Dection_input.zip`
  - `Compression-Detection_input.zip`
  - `Copy-Move_input.zip`
  - `Error-Level Analysis_input.zip`
  - `Image Extraction_input.zip`
  - `Metadata Analysis_input.zip`
  - `Noise inconsistensy_input.zip`
  - `String Exctraction_input.zip`
6. Put the Folders 'venv' and 'input' in the 'Image Forgery folder along with `_pycache_.zip` and `images_IF`
It should look like this
![image](https://github.com/Moitreyee-Das/Fake-Image-and-Rumour-detection/assets/166435448/a50d4c3e-d9bc-41e9-a915-561ea053800d)

7. Open the terminal and run the `GUI.py` file


8. Now for the front end part of the project, name a folder 'client' and put the following folders in that folder:
    - `Images.zip`
    - `package.json`
    - `package-lock.json`
    - `public.zip`
    - `scr.zip`
    - `gitignore`
9. Make a folder name `node_modules` and put all the node_modules folders in that folder
It should look like this
![image](https://github.com/Moitreyee-Das/Fake-Image-and-Rumour-detection/assets/166435448/0d35b629-a33e-4420-8f11-68a3477d8e19)

10. The folder `scr.zip` contains all the files so open that to access and use the react files.

11. 

