<!-- PROJECT LOGO -->
<br />
<div align="center">


<h3 align="center">Battlefield - Guess the Weapon (BF-GTW)</h3>

  <p align="center">
    Full stack CRUD web application based on the video game Battlefield franchise where users guess the name of the weapon. 
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contrigmailbuting">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Screenshot of BFV main game page][main_game_page-screenshot]](https://github.com/haminkim1/BF-GTW/blob/main/images/main_game_page.png)
### Video Demo
- Youtube URL (gameplay only)
- Youtube URL (high level overview for CS50)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Technologies Used

* [![Flask][Flask.py]][Flask-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![SQLite][SQLite.org]][SQLite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Install Python 3 at https://www.python.org/.
* Install the libraries used for the project from requirements.txt. For example on windows:
  ```sh
  pip install -r requirements.txt
  ```


### Launching

* Run app.py to start the server from an IDE of choice. VS Code is recommended. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Home Page
[![Home page][home-page-screenshot]](https://github.com/haminkim1/BF-GTW/blob/main/images/home.png)
- Users register and login to play games. User details are stored in the database. 
- Users can play without creating an account which will generate a random username. The username gets stored in another database to prevent generating the same username.  

### Register Page
[![Register page][register-screenshot]](https://github.com/haminkim1/BF-GTW/blob/main/images/register.png)
- Passwords are hashed and salted using the Werkzeug library. 

### Login Page
[![Login page][login-screenshot]](https://github.com/haminkim1/BF-GTW/blob/main/images/login.png)
- Username and hashed passwords are checked from the database to make sure the login details are accurate.

### Games Page
[![Games page][games_page-screenshot]](https://github.com/haminkim1/BF-GTW/blob/main/images/games_page.png)
- Images are randomly scraped from Wikipedia pages using the BeautifulSoup library. 
- Only BFV is functional. Other modes will be coming soon. 

### BFV Page
[![Screenshot of BFV main game page][main_game_page-screenshot]](https://github.com/haminkim1/BF-GTW/blob/main/images/main_game_page.png)
- Users can choose difficulty of the game. 
- [![Difficulty page][difficulty-screenshot]](https://github.com/haminkim1/BF-GTW/blob/main/images/difficulty.PNG)
- Weapons are randomly shuffled after starting the game. At each round, the weapon is removed from the randomly sorted list.<br><br>
- Users can press hint if they are unsure of the name of the weapon. The weapon type and first letter of the weapon will be displayed. 
- (image of hint)

### Game Win Page
[![Game Win page][game_win-screenshot]](https://github.com/haminkim1/BF-GTW/blob/main/images/game_win.png)
- This page will be displayed if the user completes guessing all the weapons without losing their life to 0. 

### Game Over Page
[![Game Over page][game_over-screenshot]](https://github.com/haminkim1/BF-GTW/blob/main/images/game_over.png)
- This page will be displayed if the user fails to complete guessing all the weapons and loses all their lives.

### Profile Page
[![Profile page][profile-screenshot]](https://github.com/haminkim1/BF-GTW/blob/main/images/profile.png)
- The page shows their user details, highest score of each game mode and difficulty and a table logging past games they have played. 
- Games log from the table will be selected and tabulated based on username. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>








<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ha-min Kim  - hakimnz1997@gmail.com

Project Link: [https://github.com/haminkim1/BF-GTW](https://github.com/haminkim1/BF-GTW)

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/haminkim1/BF-GTW.svg?style=for-the-badge
[contributors-url]: https://github.com/haminkim1/BF-GTW/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/haminkim1/BF-GTW.svg?style=for-the-badge
[forks-url]: https://github.com/haminkim1/BF-GTW/network/members
[stars-shield]: https://img.shields.io/github/stars/haminkim1/BF-GTW.svg?style=for-the-badge
[stars-url]: https://github.com/haminkim1/BF-GTW/stargazers
[issues-shield]: https://img.shields.io/github/issues/haminkim1/BF-GTW.svg?style=for-the-badge
[issues-url]: https://github.com/haminkim1/BF-GTW/issues
[license-shield]: https://img.shields.io/github/license/haminkim1/BF-GTW.svg?style=for-the-badge
[license-url]: https://github.com/haminkim1/BF-GTW/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ha-min-kim-ab0037126

[difficulty-screenshot]: images/difficulty.PNG
[game_over-screenshot]: images/game_over.png
[games_page-screenshot]: images/games_page.png
[game_win-screenshot]: images/game_win.png
[home-page-screenshot]: images/home.png
[login-screenshot]: images/login.png
[main_game_page-screenshot]: images/main_game_page.png
[profile-screenshot]: images/profile.png
[register-screenshot]: images/register.png

[Flask.py]: https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=flask
[Flask-url]: https://flask.palletsprojects.com/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[SQLite.org]: https://img.shields.io/badge/SQLite-003B57.svg?style=for-the-badge&logo=sqlite
[SQLite-url]: https://www.sqlite.org/index.html
