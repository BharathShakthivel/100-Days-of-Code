# 🔐 Caesar Cipher Encoder/Decoder

A simple command-line Python application that performs **Caesar Cipher** encryption and decryption. Built as a beginner-friendly project to demonstrate string manipulation, loops, functions, and basic user interaction.

---

## 📜 Description

This program allows users to:

* Encrypt (encode) messages using a Caesar Cipher.
* Decrypt (decode) previously encrypted messages.
* Continue encrypting/decrypting until they choose to exit.

The Caesar Cipher is a basic encryption technique where each letter in the message is shifted by a certain number of places in the alphabet.

---

## 🚀 Features

* Encode and decode messages.
* Preserves spaces and punctuation.
* Automatically wraps around the alphabet.
* Continues in a loop until the user chooses to exit.
* Uses ASCII art logo via the `art` package for a fun interface.

---

## 🛠️ How It Works

1. User is prompted to enter:

   * Whether to `encode` or `decode`
   * The message
   * The shift number
2. The program processes the message using the Caesar Cipher logic.
3. Output is displayed.
4. User is asked whether they want to run the program again.

---

## 📦 Requirements

* Python 3.x
* [`art`](https://pypi.org/project/art/) module for ASCII art logo

Install the `art` module using pip:

```bash
pip install art
```

---

## 🧪 Example

```bash
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello world!
Type the shift number:
> 5
Here is the encoded result: mjqqt btwqi!
```

---


