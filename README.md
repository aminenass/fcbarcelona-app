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

![desktopversionresults](https://github.com/user-attachments/assets/52e1d4be-3652-4333-9126-fea37e2424c7)
![desktopstanding](https://github.com/user-attachments/assets/f45455d1-6cd5-4b31-8c61-336cfa39d4e0)
![desktopversionsq](https://github.com/user-attachments/assets/b0826b5e-523f-423c-98b5-2b5f25d2d63b)

![mobileversionresults](https://github.com/user-attachments/assets/bcf9b502-133b-4666-a6f6-0c81d525c847)
![mobilestanding](https://github.com/user-attachments/assets/5de661ca-ce74-41c3-b691-757ec43e11ab)
![mobileversionfullsq](https://github.com/user-attachments/assets/e40fa5be-1e0b-4d56-b216-aac801343375)



<h2>Acknowledgments</h2>

<li><a href = https://www.football-data.org/ >Football-Data </a> API for providing match and standings data. </li>
<li><a href = https://www.fcbarcelona.com/ >FC Barcelona </a> Official Website for player and coaching staff data.</li>
<li><a href = https://www.selenium.dev /> Selenium</a> for web scraping.</li>
<li><a href = https://www.mongodb.com />MongoDB</a> for database storage.</li>

<h3>Enjoy exploring FC Barcelona's match results, standings, and team details! ⚽ </h3>
