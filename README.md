# Secured File Access

This project provides a secure way to access files, potentially using a graphical user interface as suggested by the image files. It appears to involve user interaction to determine correct or incorrect access attempts.

## How it Works

Based on the file names, the project likely:

1.  Presents a user interface (`mine.py` suggests a Python script, potentially using a GUI library).
2.  Handles user input related to file access (implied by `img/icons8-correct-20.png` and `img/icons8-wrong-20.png`).
3.  Secures file access (implied by `img/icons8-secured-file-24.png`).
4.  Configuration files (`.idx/dev.nix`, `.vscode/settings.json`) suggest a development environment setup and potential project settings.

Further details would require inspecting the content of the `mine.py` file.
## Modules Used

Based on the `mine.py` file, the following modules are used:

*   `tkinter`: For creating the graphical user interface.
*   `tkinter.filedialog`: For opening file dialogs to select files.
*   `tkinter.messagebox`: For displaying message boxes.
*   `cryptography.fernet`: For performing encryption and decryption.


## Technologies Used

*   Python (suggested by `mine.py`)
*   Nix (indicated by `.idx/dev.nix`)
*   VS Code (indicated by `.vscode/settings.json`)

## Workflow Flowchart
 ``` mermaid
 graph TD
    A[Start] --> B{Select File};
    B --> C{Choose Operation};
    C --> D[Encrypt];
    C --> E[Decrypt];
    D --> F[Generate Key];
    F --> G[Save Encrypted File & Key File];
    G --> H[End];
    E --> I{Is file .enc?};
    I -->|Yes| J[Select Key File];
    J --> K[Decrypt File];
    K --> L[Save Decrypted File];
    L --> H;
    I -->|No| B;
```


## Credits

 This project was developed by 
 S. Likhitha 
 Department of Computer Science and Engineering (CSE)
 at MVGR College of Engineering.