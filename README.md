# shamir-secret-sharing

# Code Architecture for Shamir's Secret Sharing Educational Tool

**Author:** Ghadir Alfadhl  
**Date:** November 26, 2024

## Overview

This Python-based educational tool, implemented using the Tkinter library, introduces the Shamir's Secret Sharing algorithm. It combines an interactive graphical user interface (GUI) with cryptographic functionality, providing students with a hands-on learning experience.

## Key Components

### 1. User Interface (UI)

Developed using Tkinter, the interface is organized using a grid layout and includes labels, buttons, text fields, and entry boxes for user interaction.

#### Features
- Input fields for the secret, number of shares, and threshold values.
- Buttons to generate shares, reconstruct the secret, and clear inputs.
- A math puzzle feature that introduces educational gamification.
- A visually engaging layout with customized colors and formatting.

### 2. Core Functionalities

#### Secret Sharing Logic
- Implements Shamir's Secret Sharing to divide a secret into **n** shares.
- Requires a threshold value **t** shares to reconstruct the original secret.
- Uses a randomly generated polynomial with cryptographically secure coefficients generated through PyCryptodome.

#### Secret Reconstruction
- Uses Lagrange interpolation to reconstruct the secret from the provided shares.
- Includes input validation and robust error handling to ensure reliability.

### 3. Supporting Features

#### Educational Elements
- Provides a brief explanation of Shamir's Secret Sharing through a popup window.
- Includes simple math puzzles to make the learning process more interactive and engaging.

#### Error Handling
- Validates user input before processing.
- Displays meaningful error messages when invalid data is entered.

#### Dynamic Updates
- Displays generated shares dynamically within the GUI.
- Shows reconstructed secrets immediately after successful reconstruction.

## Security Considerations

The application uses PyCryptodome to generate cryptographically secure random coefficients, helping ensure the integrity of the secret-sharing process. Input validation mechanisms further protect against incorrect or malformed input.

## Scalability and Educational Value

This application combines educational content with interactive cryptographic demonstrations. The design provides a foundation for future enhancements, including:

- Additional cryptographic algorithms.
- Multi-language support.
- Enhanced visualization of polynomial generation and interpolation.
- Advanced educational exercises and challenges.

## Technologies Used

- Python
- Tkinter
- PyCryptodome
- Shamir's Secret Sharing Algorithm
- Lagrange Interpolation
