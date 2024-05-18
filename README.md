# Image Forgery and Rumour Detecion

** Overview **
This software is designed to detect image forgery and distinguish between true and false rumors. It combines advanced image processing techniques with natural language processing (NLP) to ensure the integrity of visual and textual content. The project includes two primary components: image forgery detection and rumor detection.

** Features **
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
