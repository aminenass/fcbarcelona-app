<h1>FC Barcelona Web App ⚽</h1>
This is a <a href =https://flask.palletsprojects.com/en/stable/ />Flask</a> web application that provides information about FC Barcelona, including match results, standings in La Liga and the UEFA Champions League, and details about the players and coaching staff. The app retrieves data from the <a href="https://www.football-data.org/">Football-Data API</a> for match results and standings, and uses Selenium to scrape player and coaching staff data from the official FC Barcelona website. To improve performance and reliability, the player and coaching staff data is stored in a MongoDB database using MongoEngine.

<h2>Features</h2>
<h3>Match Results</h3>
View match results for FC Barcelona in La Liga and the UEFA Champions League.
Results are retrieved from the Football-Data API.
<h3>Standings</h3>
View current standings for FC Barcelona in La Liga and the UEFA Champions League.
Standings are retrieved from the Football-Data API.
<h3>Players and Coaching Staff</h3>
View a list of FC Barcelona players and coaching staff, including their names and pictures.
Data is scraped from the official FC Barcelona website using Selenium and stored in MongoDB for faster and more reliable access.
<h2>Technologies Used</h2>
<h3>Backend</h3>
Flask (Python web framework)
MongoEngine (MongoDB ODM for Python)
Selenium (Web scraping for player and coaching staff data)
Football-Data API (For match results and standings)
<h3>Frontend</h3>
HTML, CSS, Tailwind CSS (Styling)
Jinja2 (Templating engine for Flask)
<h3>Database</h3>
MongoDB (NoSQL database for storing player and coaching staff data)
<h2>Pages</h2>
<h3>Match Results</h3>
URL: /
Displays match results for FC Barcelona in La Liga and the UEFA Champions League.
Data is retrieved from the Football-Data API.
<h3>Standings</h3>
URL: /standing
Displays current standings for FC Barcelona in La Liga and the UEFA Champions League.
Data is retrieved from the Football-Data API.
<h3>Players and Coaching Staff</h3>
URL: /squad
Displays a list of FC Barcelona players and coaching staff, including their names and pictures.
Data is scraped from the official FC Barcelona website and stored in MongoDB.


<h2>Preview</h2>

![desktopstanding](https://github.com/user-attachments/assets/4b27a3ee-3cd1-4391-85db-eb019097e2bf)
![desktopversionresults](https://github.com/user-attachments/assets/c2f576fe-7f73-4006-88f6-c95612f6edc2)
![desktopversionsq](https://github.com/user-attachments/assets/773e44bf-5874-4636-9479-872328046cea)

![mobilestanding](https://github.com/user-attachments/assets/697fe7c3-95cc-4699-8fd8-cb4ee47babe4)
![mobileversionfullsq](https://github.com/user-attachments/assets/9e895578-5afa-4484-b1bf-9d603866d56f)
![mobileversionresults](https://github.com/user-attachments/assets/b1daabd6-98e9-4099-b462-236a64c6c689)




<h2>Acknowledgments</h2>

<li><a href = https://www.football-data.org/ >Football-Data </a> API for providing match and standings data. </li>
<li><a href = https://www.fcbarcelona.com/ >FC Barcelona </a> Official Website for player and coaching staff data.</li>
<li><a href = https://www.selenium.dev /> Selenium</a> for web scraping.</li>
<li><a href = https://www.mongodb.com />MongoDB</a> for database storage.</li>

<h3>Enjoy exploring FC Barcelona's match results, standings, and team details! ⚽ </h3>
