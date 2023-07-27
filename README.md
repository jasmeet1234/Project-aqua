# Project Aqua - Desktop Assistant


Project Aqua is a Python-based desktop assistant that can perform a variety of tasks using voice commands. It is designed to make your life easier by assisting you with different activities and providing helpful information. This README will guide you through setting up and using Project Aqua.

## Features

- **Voice Interaction**: Interact with Aqua using your voice commands.
- **Wikipedia Search**: Aqua can search for information on Wikipedia.
- **Web Browsing**: Ask Aqua to open specific websites like Google, YouTube, Stack Overflow, Facebook, and Twitter.
- **Time and Date**: Aqua can tell you the current time and date.
- **Jokes**: Need a laugh? Ask Aqua to tell you a joke.
- **Music Player**: Play music from a specified directory.
- **Location Search**: Aqua can find locations for you using Google Maps.
- **Send Emails**: Send emails using your voice commands.

## Prerequisites

To run Project Aqua, you'll need the following:

- Python 3.x installed on your system.
- Make sure to install the required Python packages using `pip install pyttsx3 speech_recognition wikipedia pyjokes`.

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the `aqua.py` file using the following command:

   ```
   python aqua.py
   ```

4. Once Aqua is up and running, it will greet you based on the time of day.

5. You can now start interacting with Aqua. Say "Hello" to trigger the greeting message, and then you can ask Aqua to perform various tasks.

### Example Voice Commands

- **"Wikipedia `<query>`"**: Aqua will search Wikipedia for the query and provide a summary of the results.

- **"Open YouTube"**: Aqua will open the YouTube website in your default web browser.

- **"Play music"**: Aqua will play music from the specified music directory.

- **"What's the time?"**: Aqua will tell you the current time.

- **"Send email"**: Aqua will ask you for the email content and recipient, and then send the email on your behalf.

- **"Tell me a joke"**: Aqua will share a funny joke with you.

### Exiting Aqua

To exit Project Aqua, simply say "Thank you," and Aqua will bid you farewell and close.

## Customization

You can customize Project Aqua to suit your preferences:

- **Change Voice**: If you want a different voice for Aqua, modify the `voices` list in the code. You can experiment with different indices (0 or 1) to change the voice.

- **Add Music**: You can add your music files to the music directory (specified in the code) and ask Aqua to play them.

## Contributions

Contributions to Project Aqua are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

## Disclaimer

Project Aqua is a personal project developed for educational purposes. It is not meant for production use, and the developer is not responsible for any misuse or damage caused by the software.

## Credits

Project Aqua is brought to you by https://github.com/jasmeet1234 It was inspired by various online tutorials and examples on desktop assistants. Special thanks to the developers of pyttsx3, speech_recognition, wikipedia, and pyjokes libraries, which made this project possible.

---

Have fun interacting with Aqua! If you have any questions or need assistance, feel free to reach out to me at havneetghotra123@gmail.com Happy coding!
