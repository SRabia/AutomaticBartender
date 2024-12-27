# Automatic Bartender

The **Automatic Bartender** is a Python-based project designed to automate various bar tasks with a focus on user interaction and extensibility. The system can serve drinks, interact with users, and integrate additional features such as displaying or announcing the price of Bitcoin.

## Features

- Serve drinks based on user input.
- Modular and extensible design to add new features.
- Integration with external APIs (e.g., fetching Bitcoin prices).
- Support for text-to-speech (TTS) announcements.

## Setup

### Prerequisites

- Python 3.8 or higher
- Required Python libraries:
  - `requests`
  - `pyttsx3`

Install the dependencies:

```bash
./install.sh
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Cyrriuswhite/AutomaticBartender.git
   cd AutomaticBartender
   ```

2. Ensure all dependencies are installed by running:

   ```bash
    ./install.sh
   ```

3. Run the main script:

   ```bash
   python main.py
   ```

## Adding the Bitcoin Price Feature

The project includes a feature to fetch and display the current Bitcoin price using the CoinGecko API.

1. The `crypto.py` module provides the `get_bitcoin_price` function to fetch the current Bitcoin price.
2. This can be integrated into `main.py` to display or announce the price.

Example usage:

```python
from crypto import get_bitcoin_price

price = get_bitcoin_price()
if price:
    print(f"Current Bitcoin Price: ${price}")
```

## Contributing

We welcome contributions! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes with clear messages:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request with a detailed description of your changes.

### Guidelines

- Write clear, concise code with comments where necessary.
- Follow Python best practices (e.g., PEP 8).
- Test your changes before submitting a pull request.

## General Improvements

### Current Ideas for Improvement

1. **Enhanced API Integration**: Add support for additional cryptocurrencies or other APIs.
2. **GUI Development**: Create a graphical user interface for easier interaction.
3. **Voice Commands**: Integrate voice recognition to allow voice commands for drink orders.
4. **Error Handling**: Improve error handling for network-related issues or unexpected inputs.
5. **Unit Tests**: Implement unit tests for critical modules to ensure reliability.

### How to Suggest Improvements

If you have ideas for improvements or new features, feel free to open an issue on the repository. Provide a clear description and, if possible, a proposed solution.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Thank you for contributing to the **Automatic Bartender** project! Your help makes this project better for everyone.


