# 🎥 **YouTube Video Content Summarizer**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://botpdf.streamlit.app/)

🔗 Live Demo: [[https://yt-summariz.streamlit.app/](https://yt-summariz.streamlit.app/)]

🚀 **Streamline your video learning experience!**  
**YouTube Video Content Summarizer** is a powerful web app built with **Streamlit** that allows you to extract and summarize content from any **YouTube video** 🎥 in just a few seconds. It uses **Azure OpenAI (GPT-4o)** 💻 to generate concise, accurate, and easy-to-understand summaries in **bullet points** or **paragraph formats**.  

This app is perfect for students, content creators, researchers, or anyone who wants to grasp the content of a long video quickly. 💡

---

## Project Image :
![image](https://github.com/user-attachments/assets/a369c063-70e0-484e-b1aa-fec3c4fea035)
![image](https://github.com/user-attachments/assets/db93ba37-1b5b-4dbd-b4d9-8140c789ec5d)



## ✅ **Features**

### 🚀 **1. Extract YouTube Video Transcript**
- Provide any YouTube video link 🔗, and the app will automatically extract the video transcript 🎤 using **YouTube Transcript API**.  
- If the video has no transcript or closed captions, an error will be shown.  

### ✍️ **2. Generate AI-Powered Summary**
- Once the transcript is extracted, the app uses **Azure OpenAI (GPT-4o)** to generate a summary based on the video content.  
- The summary can be:  
  - 📛 **Short** (Few bullet points)  
  - 📖 **Medium** (Detailed but concise)  
  - 📚 **Long** (Detailed and descriptive)  

### 📂 **3. Download Options**
- You can download both:  
  - ✅ **Summary in a text file (.txt)**  
  - ✅ **Full Transcript in a text file (.txt)**  

### 🌟 **4. Customization via Sidebar**
The app comes with an attractive **Sidebar** where you can customize:  
- 🔹 **Summary Length:** Short, Medium, or Long  
- 🔹 **Answer Type:** Paragraph or Bullet Points  

### ⏳ **5. Session History**
- Every time you generate a summary, it is saved in the session history.  
- You can revisit previous summaries or download them anytime.  

### 💖 **6. Error Handling**
- If the video URL is incorrect or the video has no transcript, the app will notify you with a friendly error message.  
- It ensures a smooth and user-friendly experience.  

---

## 🎨 **Tech Stack Used**
| Technology | Purpose |
|------------|---------|
| 🔠 **Python** | Backend Processing  |
| 💻 **Streamlit** | Web Interface  |
| 🎤 **YouTube Transcript API** | Extract Transcripts  |
| 🤖 **Azure OpenAI (GPT-4o)** | Generate AI-Powered Summaries  |
| 🌐 **Requests** | Fetch Video Metadata  |
| 🔗 **Regex** | Extract YouTube Video ID  |
| 📃 **dotenv** | Environment Variable Management  |

---

## 💻 **How to Run the Project Locally**

### 📚 **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/YouTube-Video-Content-Summarizer.git
cd YouTube-Video-Content-Summarizer
```

### 💽 **Step 2: Install Dependencies**
Make sure you have Python and pip installed. Then, run:
```bash
pip install -r requirements.txt
```

This will install:
- Streamlit
- youtube-transcript-api
- langchain-openai
- python-dotenv
- requests

### 🔑 **Step 3: Setup Environment Variables**
1. Create a `.env` file in the root directory.  
2. Add your **Azure OpenAI API Key** and **Azure Endpoint** like this:  

#### `.env` File
```
AZURE_OPENAI_API_KEY=your-openai-api-key
AZURE_OPENAI_ENDPOINT=your-azure-endpoint
```

Get your **API Key** from [Azure OpenAI Portal](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/).  

### 🌟 **Step 4: Run the Streamlit App**
Finally, run the app using:
```bash
streamlit run app.py
```

This will open the app in your browser at:  
🔗 **http://localhost:8501**

---

## 🌟 **App Walkthrough (How it Works?)**
### 💻 Step 1: Enter YouTube URL
Paste any YouTube video URL in the input field like:  
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### 🎤 Step 2: Extract Transcript
The app will automatically extract the transcript from the video using the **YouTube Transcript API**.  

### 🤖 Step 3: Generate Summary
The app sends the transcript to **Azure OpenAI (GPT-4o)** to generate a concise and meaningful summary.  
You can choose:  
- ✅ Short, Medium, Long Summary  
- ✅ Bullet Points or Paragraph Format  

### 📂 Step 4: Download Summary & Transcript
You can download:  
- **Summary** in a text file.  
- **Full Transcript** in a text file.  

---

## 🎁 **Made with Love ❤️**
This project was built with 💻 **Streamlit** + 🤖 **Azure OpenAI** to simplify video content consumption.  
If you liked this project, give it a ⭐ **star** on GitHub.  

🔗 **Connect with me on:**  
- 🌟 [LinkedIn]([https://www.linkedin.com/in/prateek-gaur-3099a7228/])  
- 🔗 [GitHub]([https://github.com/your-username](https://github.com/DrDarkShadow))  

---

## 🤝 **Contribute**
If you'd like to contribute, fork the repository and submit a pull request. Contributions are always welcome!  

---

## 🌟 **Future Improvements 🚀**
- [ ] Support multi-lingual transcripts  
- [ ] Add support for audio/podcast summarization  
- [ ] Improve download formats (PDF, DOCX)  
- [ ] Add more models like Gemini, Claude, etc.  

---

## ✨ **License**
This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute it.  

---

## 🎉 **Thank You! ❤️**
Thanks for visiting the project.  
**Now go ahead and start summarizing YouTube videos like a pro!** 🎥 💻 🚀  

_If you face any issues, feel free to open an issue on GitHub._

