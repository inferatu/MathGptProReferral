# MathGptReferral: Automate Your Referrals

This repository contains the code for an application that automates the process of getting referrals for your account.

## Usage

There are two ways to use this application:

1. **Pre-built Executable**: Download the pre-built executable file from the releases. Choose the version that matches your language (RU for Russian, EN for English).
2. **Manual Build**: Build the application manually. Refer to the "Building Manually" section for instructions.

## Installation Guide

Follow these steps to install and run the application:

1. Clone this repository using the following command:
    ```bash
    git clone https://github.com/inferatu/MathGptReferral.git
    ```

2. Navigate to the cloned repository's directory.

3. Install the necessary dependencies. It's recommended to use a virtual environment for this:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the program with the following command:
    ```bash
    python run.py
    ```

## Building Manually

You can manually build the application using either PyInstaller or Nuitka:

1. **PyInstaller**:
    - Install PyInstaller:
        ```bash
        pip install pyinstaller
        ```
    - Navigate to the repository's directory and run this command:
        ```bash
        pyinstaller --onefile run.py
        ```
    - After running the command, a "dist" folder will be created where the `run.exe` file will be located.

2. **Nuitka**:
    - Install Nuitka:
        ```bash
        pip install nuitka
        ```
    - Run this command:
        ```bash
        python -m nuitka --follow-imports run.py
        ```
    - After some time, a "dist" folder will be created with the `run.exe` file.
