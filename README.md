
Project Title: Image Encryption and Decryption using Java GUI

# Project Description:

This project focuses on developing a secure and user-friendly application for image encryption and decryption using Java. The main objective is to protect sensitive image data by transforming it into an unintelligible form using a secret key, and then restore it back to its original form only with the correct key.

The application features a Graphical User Interface (GUI) built using Java Swing, enabling users to easily interact with the system without requiring any command-line operations. Users can select an image file, input a secret key, and then either encrypt or decrypt the image using simple button clicks.

During encryption, the application applies a custom algorithm that scrambles the pixel values of the image based on the provided key, ensuring that the visual content is hidden and protected. The encrypted image appears distorted and meaningless to anyone who does not possess the correct key.

During decryption, the same key is used to reverse the encryption process, restoring the image to its original form. If an incorrect key is used, the output remains unintelligible, ensuring data confidentiality.

# This project demonstrates the concepts of:

* Symmetric key cryptography (same key used for both encryption and decryption),
* Secure image processing,
* Java-based GUI design,
* Practical implementation of encryption techniques in multimedia security.


# Technologies Used:

* Programming Language: Java
* GUI Framework: Java Swing
* Image Processing: BufferedImage, File I/O
* Encryption Logic: Custom pixel-level encryption algorithm based on key


