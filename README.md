# 🔍 Patent Copilot - Patent Search Agent

A powerful AI-driven patent search tool that helps inventors and researchers find similar patents for their inventions using advanced search strategies and intelligent analysis.

## 🚀 Features

- **AI-Powered Analysis**: Uses Google's Gemini AI to extract key concepts and generate intelligent search strategies
- **Multi-Strategy Search**: Performs broad conceptual, specific technical, and alternative approach searches
- **Patent Database Access**: Searches Google Patents via SerpAPI for comprehensive results
- **Intelligent Results Analysis**: Provides similarity assessment and novelty gap analysis
- **User-Friendly Interface**: Simple command-line interface with clear instructions

## 📋 Requirements

- Python 3.8 or higher
- Google Gemini API key
- SerpAPI key

## 🛠️ Installation

1. **Clone or download the files**:
   ```bash
   # Ensure you have these files:
   # - patent_copilot.py
   # - requirements.txt
   # - README.md
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the same directory with your API keys:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   SERPAPI_API_KEY=your_serpapi_api_key_here
   ```

   **Important**: The `.env` file should be in the same directory as `patent_copilot.py`

## 🔑 API Keys Setup

### Google Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your `.env` file

### SerpAPI Key
1. Go to [SerpAPI](https://serpapi.com/)
2. Sign up for a free account (100 searches/month free)
3. Go to your dashboard and copy your API key
4. Add it to your `.env` file

## 🎯 Usage

1. **Run the application**:
   ```bash
   python patent_copilot.py
   ```

2. **Describe your invention** when prompted:
   - Be specific about technical features
   - Include functionality and uniqueness
   - Press Enter twice when finished

3. **Wait for analysis**:
   - The AI will extract key concepts
   - Multiple search strategies will be executed
   - Results will be analyzed and presented

## 📊 Example Usage

```
🔍 PATENT COPILOT - Patent Search Agent 🔍

Welcome! I'll help you search for patents similar to your invention.

📝 Please describe your invention:
(Press Enter twice when finished)

A smart water bottle that uses IoT sensors to track daily water intake,
monitors hydration levels, and sends personalized reminders to a mobile app.
The bottle includes temperature sensors and connects via Bluetooth.


🔍 Analyzing invention and searching for similar patents...
```

## 🎛️ How It Works

1. **Concept Extraction**: AI analyzes your invention description to identify key technical concepts
2. **Search Strategy Generation**: Creates multiple search approaches:
   - Broad conceptual search
   - Specific technical terms
   - Alternative descriptions
3. **Patent Database Search**: Uses SerpAPI to search Google Patents database
4. **Results Analysis**: AI processes found patents and provides:
   - Relevance assessment
   - Novelty gap analysis
   - Patent strategy recommendations

## 📁 File Structure

```
patent_copilot/
├── patent_copilot.py    # Main application
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .env               # API keys (create this file)
```

## 🔧 Configuration

The application includes several configurable parameters in the code:

- **Search Results Limit**: Currently set to 10 patents per search
- **AI Model**: Uses Gemini 1.5 Flash
- **Search Strategies**: Configured for 2-3 different approaches
- **Temperature**: Set to 0.3 for consistent results

## 🚨 Troubleshooting

### Common Issues

1. **"API Key not found"**:
   - Ensure `.env` file exists in the same directory
   - Check that API keys are correctly formatted
   - No spaces around the `=` sign

2. **"Module not found"**:
   - Run `pip install -r requirements.txt`
   - Ensure you're using the correct Python environment

3. **"Connection error"**:
   - Check your internet connection
   - Verify API keys are valid and active
   - Check API usage limits

4. **"No results found"**:
   - Try describing your invention differently
   - Use more general terms
   - Check if the technology area has patents

## 📈 Future Enhancements

- **Patent Classification**: Add automatic patent class detection
- **Prior Art Analysis**: Enhanced prior art searching
- **Export Functionality**: Save results to PDF/Excel
- **Web Interface**: Browser-based UI
- **Multiple Databases**: Support for additional patent databases
- **Collaboration Features**: Team sharing and annotations

## ⚖️ Legal Disclaimer

This tool is for research and educational purposes only. Patent search results should be verified by professional patent attorneys or agents. The tool does not provide legal advice and should not be used as the sole basis for patent decisions.

## 🤝 Contributing

Feel free to submit issues, feature requests, or improvements to enhance the patent search agent.

## 📜 License

This project is provided as-is for educational and research purposes.

---

**Happy Patent Searching! 🔍✨** 