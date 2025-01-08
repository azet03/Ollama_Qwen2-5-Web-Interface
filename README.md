# Ollama Qwen2-5 Web Interface

A modern, user-friendly web interface for interacting with the Qwen2-5 language model through Ollama. This project bridges the gap between Ollama's powerful capabilities and end-users by providing an intuitive, web-based chat interface.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## 🌟 Features

- **Interactive Web Interface**: Clean and responsive design for seamless interaction
- **Real-time Chat**: Smooth conversation flow with Qwen2-5 model
- **Context Management**: Maintains conversation history for contextual responses
- **Modern UI/UX**: Built with modern web technologies for the best user experience
- **Easy Deployment**: Simple setup process with clear instructions

## 🚀 Prerequisites

Before you begin, ensure you have the following installed:
- [Ollama](https://ollama.ai/) with Qwen2-5 model
- Python 3.8 or higher
- Node.js (for frontend development)

## 💻 Installation

1. Clone the repository
   ```bash
   git clone https://github.com/azet03/Ollama_Qwen2-5-Web-Interface.git
   cd Ollama_Qwen2-5-Web-Interface
   ```

2. Install dependencies
   ```bash
   # Backend dependencies
   pip install -r requirements.txt
   
   # Frontend dependencies
   cd frontend
   npm install
   ```

3. Configure Ollama
   - Ensure Ollama is running
   - Verify Qwen2-5 model is installed:
     ```bash
     ollama pull qwen2-5
     ```

4. Start the application
   ```bash
   # Start backend
   python app.py
   
   # Start frontend (in a new terminal)
   cd frontend
   npm start
   ```

## 🔧 Configuration

The application can be configured through environment variables or a config file:

- `PORT`: Server port (default: 3000)
- `OLLAMA_HOST`: Ollama API host (default: http://localhost:11434)
- `MODEL_NAME`: Model name (default: qwen2-5)

## 🎯 Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Start chatting with the AI through the interface
3. Use the clear button to start a new conversation
4. Adjust model parameters in the settings panel

## 🤝 Contributing

Contributions are always welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your PRs are well-documented and maintain the existing code style.

## 🐛 Troubleshooting

Common issues and solutions:

- **Ollama Connection Error**: Ensure Ollama is running and accessible
- **Model Not Found**: Verify the model is properly installed with `ollama list`
- **Port Already in Use**: Change the port in configuration

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to [Ollama](https://ollama.ai/) for the amazing model serving platform
- The Qwen team for their excellent language model
- All contributors who help improve this project

