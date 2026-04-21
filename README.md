# AI Photo Studio

A lightweight AI-powered web application that removes the background from uploaded images and replaces it with a solid color of your choice.

The application uses a deep learning segmentation model to automatically isolate the foreground subject and generate a clean background replacement.

This project demonstrates practical usage of AI models inside a production-style API service.

---

## Features

* Upload an image via web interface
* Automatic background removal using AI
* Replace background with a custom RGB color
* FastAPI-based REST API
* Simple web UI
* Local processing (no external API calls)
* Runs fully offline after the model is downloaded

---

## Tech Stack

* Python 3.12
* FastAPI
* Uvicorn
* rembg (background removal)
* Pillow (image processing)
* Jinja2 templates

AI segmentation model used:

U²-Net (downloaded automatically by rembg on first run)

---

## Project Structure

```
AI-Photo-Studio/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   └── config.py
│
├── services/
│   └── bg_remove.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── uploads/
│   └── outputs/
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/ananduashok/AI-Photo-Studio.git
cd AI-Photo-Studio
```

Create a virtual environment:

```
python3 -m venv venv
```

Activate the environment:

Linux / WSL

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

Start the server:

```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Open your browser:

```
http://localhost:8000
```

API documentation is available at:

```
http://localhost:8000/docs
```

---

## Usage

1. Upload an image
2. Choose the RGB background color
3. Submit the form
4. The AI removes the original background
5. A new solid color background is applied
6. The processed image is saved in:

```
static/outputs/
```

---

## Example Workflow

```
Upload Image
      ↓
AI Segmentation (U²-Net)
      ↓
Foreground Extraction
      ↓
Solid Background Replacement
      ↓
Processed Image Saved
```

---

## First Run

On the first run, the application automatically downloads the U²-Net model used for background removal.

The model is stored in:

```
~/.u2net/
```

Model size: ~176MB

This happens only once.

---

## Use Cases

* Product photography background cleanup
* Passport / ID photo preparation
* E-commerce image processing
* Profile photo editing
* Simple AI image processing demos

---

## Future Improvements

Potential upgrades:

* Drag and drop image upload
* Image preview before processing
* Download button for processed image
* Batch image processing
* AI-generated background scenes

---

## License

This project is open-source and available for educational and research purposes.

---

## Author

Created by Anandu

AI / Data Science portfolio project demonstrating computer vision model integration with a modern API backend.
