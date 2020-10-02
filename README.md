# FIFA_teams_data_scrap
Script to scrap the database from the teams of every season of the videogame "FIFA". The data are scraped from the web sofifa.com, an excellent data base of 
football teams and football players. The script consists of two functions: scrap_fifa() and add_fifa_time().

How does it work? let's imagine we want to download the data from the videogame FIFA 18. Then go ahead and type "scrap_fifa(18)". Name the data frame (for example 
df) and implement the dates of the rates just typing add_fifa_time(df). In the next days I will automatize both steps in just one step, which means, we will only
need to type scrap_fifa(18).

I have used the "get" method for the database itself. The scrap of the Date of every new update of Fifa (around 55 x year) was a little bit more tricky and 
I had to use Beautifulsoup. The combination of both things was probably the trickiest part of this little project, which actually belongs to my bigger project 
about calculating odds for football games and who knows, maybe try to make some predictions about features such as number of goals in a game.

I forgot to mention, the code scraps only the german, french, spanish and italian leagues.


