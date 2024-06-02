# SecurePass

**StealthPixels: Advanced Image Encryption Tool**

This advanced version of the Image Encryption program, named **StealthPixels**, includes the following features:

### Key Management
- **Set Encryption Key:** Allows users to set an encryption key within the range of 0 to 255.

### Image Encryption/Decryption
- **Encrypt Image:** Supports encryption of images using a specified key.
- **Decrypt Image:** Supports decryption of images using the same key used for encryption.

### Exception Handling
- **Error Handling:** Includes error handling for file operations and user inputs to enhance robustness.

### CLI Interaction
- **User-Friendly Interface:** Offers a command-line interface for users to perform image encryption, decryption, and key management.

### File Integrity Verification
- **Image Loading Validation:** Ensures the selected image file exists and is valid.

### Documentation
- **Descriptive Comments and Docstrings:** Improves code readability and maintainability.

This advanced version enhances the functionality and usability of the image encryption tool, making it suitable for real-world tasks, including secure image storage and transmission.

### How to Get and Use StealthPixels

#### Step 1: Clone the Repository
- **Open Terminal:** Open your terminal (Command Prompt, PowerShell, or any terminal you use).
- **Clone the Repository:** Use the `git clone` command followed by the URL of your GitHub repository.

```bash
git clone https://github.com/HEETLAW/StealthPixels.git
```

#### Step 2: Navigate to the Repository Directory
```bash
cd StealthPixels
```

#### Step 3: Ensure Required Dependencies are Installed
Ensure you have Python and the `Pillow` library installed. If not, you can install `Pillow` using pip:

```bash
pip install pillow
```

#### Step 4: Run the Script
You can now run your image encryption tool. Assuming your main script is named `StealthPixels.py`, you would run:

```bash
python StealthPixels.py
```

### Step 5: Using the Tool
Follow the prompts provided by the script to use the various functionalities:

#### Load Image
1. **Select (1)** to load an image.
2. **Enter the path** of the image to load.

#### Set Encryption Key
1. **Select (2)** to set the encryption key.
2. **Enter the key value** (between 0 and 255).

#### Encrypt Image
1. **Select (3)** to encrypt the loaded image.
2. **Enter the output path** for the encrypted image.

#### Decrypt Image
1. **Select (4)** to decrypt an encrypted image.
2. **Enter the path** of the encrypted image.
3. **Enter the output path** for the decrypted image.

#### Quit
1. **Select (5)** to quit the application.

### Example Commands

#### To encrypt an image:
1. **Load Image:** 
    - Enter the path of the image to load: `path/to/image.jpg`
2. **Set Encryption Key:** 
    - Enter the encryption key (0-255): `123`
3. **Encrypt Image:** 
    - Enter the output path for encrypted image: `path/to/encrypted_image.jpg`

#### To decrypt an image:
1. **Load Image:** 
    - Enter the path of the image to load: `path/to/image.jpg`
2. **Set Encryption Key:** 
    - Enter the encryption key (0-255): `123`
3. **Decrypt Image:** 
    - Enter the output path for decrypted image: `path/to/decrypted_image.jpg`
