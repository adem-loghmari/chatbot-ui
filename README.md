# Chatbot UI

This project is a modern chatbot interface with a strong focus on the underlying AI model. The main goal was to deliver a robust, intelligent conversational experience, leveraging advanced AI techniques to ensure high-quality, context-aware responses.

## AI Model Focus
- The core of this project is the AI model: `aymenelghali/mistralai-Mistral-7B-Instruct-v0.1`, carefully integrated for natural, engaging conversations.
- **SapBERT** was used for training the large language model (LLM), enhancing its understanding and semantic capabilities.
- **Mistral** serves as the backbone for the chatbot, providing fast and accurate conversational responses.
- Emphasis was placed on model performance, accuracy, and adaptability to various user queries.
- The backend is designed to be easily extendable for future improvements or integration with more advanced models.

## User Interface
- The interface is clean, intuitive, and visually appealing, providing a seamless chat experience.
- Built with modern web technologies (React, TypeScript, Tailwind CSS, Vite), the UI is fast, responsive, and accessible.
- Features include a dynamic chat window, markdown support, theme toggling, and a sidebar for easy navigation.
- The design ensures users can interact with the AI effortlessly, making the experience enjoyable and productive.

## Getting Started
1. Install dependencies:
   ```sh
   npm install
   ```
2. Start the development server:
   ```sh
   npm run dev
   ```
3. Open your browser at `http://localhost:5173` to use the chatbot UI.

## Project Structure
- `src/` - Main source code (components, context, interfaces, pages, etc.)
- `model/` - AI model backend (e.g., `app.py`)
- `testbackend/` - Backend testing scripts
- `demo/` - Demo assets

## License
This project is for educational and demonstration purposes.
