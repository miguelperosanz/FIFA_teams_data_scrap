# FIFA_teams_data_scrap
1) Script to scrap the database from the teams of every season of the videogame "FIFA". The data are scraped from the web sofifa.com, an excellent data base of 
football teams and football players. How does it work? let's imagine we want to download the data from the videogame FIFA 18. Then go ahead and type "df = scrap_fifa(18)". The database will be stored in df. I have used the "get" method for the database itself. The scrap of the Date of every new update of Fifa was a little bit more tricky and I had to use Beautifulsoup. The combination of both things was probably the trickiest part of this little project, which actually belongs to my bigger project about calculating odds for football games and who knows, maybe try to make some predictions about features such as number of goals in a game.


2) "scrap_last_update_fifa_teams" is the little brother of "FIFA_teams_data_scrap". It scraps the last update with the data of all the clubs from the webpage SOFIFA.com. This script is a simplified version of my repository "FIFA_teams_data_scrap". While "FIFA_teams_data_scrap" scrapped all the data from any season, this one scraps only the last update of a total of almost 700 club teams from all around the world. Execute the code, then just type type df = scrap_last_update()


Both files actually belong to the project & repository "football predictor". I thought it was nice to have them separated just in case somebody wants to use the scrapping of sofifa.com as an application itself.

Oh I forgot to mention, the code scraps data of only the 5 top leagues in Europe: english, german, french, spanish and italian.
