# from_Taipy-walletWISE

# The readme is not yet complete

# <p align="center"><img src="https://github.com/Ujj1225/from_Taipy-walletWISE/blob/main/assets/wallet_wise_logo.jpg" width=300 /></p>

<p align="center">
    <p align="center">
        <a href="https://github.com/Ujj1225/from_Taipy-walletWISE" target="blank">
            <img src="https://img.shields.io/github/watchers/Rajendrakhanal/MyPeace?style=for-the-badge&logo=appveyor" alt="Watchers"/>
        </a>
        <a href="https://github.com/Ujj1225/from_Taipy-walletWISE/fork" target="blank">
            <img src="https://img.shields.io/github/forks/Rajendrakhanal/MyPeace?style=for-the-badge&logo=appveyor" alt="Forks"/>
        </a>
        <a href="https://github.com/Ujj1225/from_Taipy-walletWISE/stargazers" target="blank">
            <img src="https://img.shields.io/github/stars/Rajendrakhanal/MyPeace?style=for-the-badge&logo=appveyor" alt="Star"/>
        </a>
    </p>
    <p align="center">
        <a href="https://github.com/Ujj1225/from_Taipy-walletWISE/issues" target="blank">
            <img src="https://img.shields.io/github/issues/Rajendrakhanal/MyPeace?style=for-the-badge&logo=appveyor" alt="Issue"/>
        </a>
        <a href="https://github.com/Ujj1225/from_Taipy-walletWISE/pulls" target="blank">
            <img src="https://img.shields.io/github/issues-pr/Rajendrakhanal/MyPeace?style=for-the-badge&logo=appveyor" alt="Open Pull Request"/>
        </a>
    </p>
    <p align="center">
        <a href="https://github.com/Ujj1225/from_Taipy-walletWISE/blob/master/LICENSE" target="blank">
            <img src="https://img.shields.io/github/license/Rajendrakhanal/MyPeace?style=for-the-badge&logo=appveyor" alt="License" />
        </a>
    </p>
</p>

<p align="center">
</p>

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [License](#license)

## Features

- Income and Expense Tracker

  User can enter their Income, Expense along with the sector as headings. This allows them to comprehend and explore how much they are earning from which sector and how much they are spending on which sector.
  <details>
    <summary> UI of Tracker </summary>
    <img src="https://github.com/Rajendrakhanal/MyPeace/assets/95162952/08bdfcb1-861a-451c-b69e-60c24b4fc0a4" width=750/>
  </details>

- Insight Box

  Here, User's income and expense are analyzed, mathematically shown and 7 tips for making better, wiser financial decisions are displayed. 
  <details>
    <summary> Insight box before getting insights!</summary>
    <img src="https://github.com/Rajendrakhanal/MyPeace/assets/95162952/ea58c3a8-bcb4-4037-8bf0-4680e673e6e7" width=750/>

    <summary> Insight box after getting insights!</summary>
    <img src="https://github.com/Rajendrakhanal/MyPeace/assets/95162952/ea58c3a8-bcb4-4037-8bf0-4680e673e6e7" width=750/>
  </details>

- Realtime Visualization

  Implemented a visualizer where you can see the different headings from which you earnt money and the different headings on which you spent it.
  <details>
    <summary> Visualization </summary>
    <img src="https://github.com/Ujj1225/from_Taipy-walletWISE/blob/main/assets/getinsights.png" width=750/>
  </details>

## Demo

[walletWISE Project Demo Video]()

## Installation

### Prerequisites

Before running walletWISE, you will need an OpenAI API key from Gemini Services. You can obtain an API key by registering on the Gemini platform.

### Setup

#### Follow the given steps to set up walletWISE

1. Clone the repository:

   ```bash
   git clone git@github.com:Ujj1225/from_Taipy-walletWISE.git
   ```

2. Installation of required packages

   ```bash
    pip install -r requirements.txt
   ```

3. Setting up .env file for saving gemini api key

- Create a .env file

  ```bash
  # inside .env file
  API_KEY=******************************* # Your key
  ```

4. Running the project:

- Simply try to run the **main.py** file as it is the entry point of application
- You may do so by:

```bash
python3 main.py
```

## Dependencies

### Frontend

### Backend

- Taipy for full stack
- Other dependencies or requirements are mentioned in [requirements.txt](/requirements.txt)

## License

This project is licensed under the [MIT License](/LICENSE).
