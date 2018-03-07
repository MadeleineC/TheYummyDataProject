# TheYummyDataProject
Project Title: TBD

Team Members
  Yizhi
  Marko
  Madeleine
  Sarah

Project Description/Outline: As a local data analysis group specialized in the food industry, we provide data to clients to help them decide where they should expand or open a new restaurant based on a type of cuisine and price. 

Research Questions to Answer: The client tells us their restaurant type e.g. pizza place with a certain price range. We will provide the following data analysis and visualization that can provide insights into the following questions:
- What is the distribution of restaurants with the type of cuisine among various neighborhoods in Austin? 
     Output:  A heat map of  restaurants  with interest  in Austin 
          A general type heatmap
          A heatmap considering the price range our customer is targeting
- What is the distribution of restaurants (not limited to any type of restaurants) with similar price range by zips in Austin?
  Output: A heatmap of restaurants with similar price range by zips in Austin
 Comparing 1 and 2, one can try to see whether our client’s type of restaurant is underrepresented in any neighborhood as compared to filled in restaurants in the same price range.

- Which neighborhoods have populations with discretionary income for the price category of our restaurant?
  Output: A heatmap of median income of neighborhoods in Austin (this is constant and do not have to change from a client to another)
  Output: A heatmap of rental rate of neighborhoods in Austin 
I would assume the heatmap for 3  should have a good overlap with 2, but if not this can identify suitable neighborhoods which can be filled in.     
Among these neighborhoods with my potential customers, how many restaurants of the similar kind are there and are they well received?
Output: Pick a couple or three neighborhoods within the discretionary income and run the following analysis:
Pie chart showing different kinds of restaurants
A histogram showing the distribution of prices among local restaurants 
A bar graph showing the popularity of local restaurants
A bar graph showing customers’ ratings of local restaurants
    
 5. Data sources or Data Sets to be Used
Median Income of neighborhoods
Restaurant density by Zip
Restaurant type
Restaurant popularity 
Restaurant rating

APIs to be consumed (if any)
Zillow API
Texas Neighborhood Boundary Shape Files - how to plot in Python using shape files
Zestimate
Rental price estimates
Home valuation estimates
GetUpadedProperty Details
All the details about the homes themselves (could be used to calculate price per square foot)
Yelp API

Rough Breakdown of Tasks
Create a Github Repository for Team
Got to APIs and find out we can retrieve
Make API calls from Zillow
Make API calls from yelp
Merge by Zip Code
