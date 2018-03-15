# TheYummyDataProject


<h2>Team Members</h2> 

- Yizhi
- Marko
- Madeleine
- Sarah

<h2>Project Description:</h2> 
We are a local data analysis group specialized in the food industry.
Clients provide us with three basic details about their desired restaurant:

- type of cuisine
- anticipated average order value (price)
- target markets they are considering (city & states).

We then provide data to clients to help them decide where they should expand or open a new restaurant.

<h2>Research Questions:</h2>

To answer the following research questions, we are utilizing the scenario that our client wants to open a cheap ($ on Google) taco restaurant and that she is considering neighborhoods in Austin, Texas.


<h3>What is the distribution of restaurants of a given type of cuisine by zip code? </h3>
By identifying the distribution of restaurants by cuisine across a city/state (by zip code), we can begin to suggest a zip code/area with a “need” for a restaurant of specific cuisine. In this case, our client is a “Taco Restaurant”, with a low average order value, looking to find an area to grow in Austin, Texas. We can assume that if an area is saturated with restaurants of similar cuisine type, the area may be too competitive to move into. To combat this, it is our suggestion that we concentrate on areas with moderate to low count of restaurant with similar cuisine type. We assume these zip codes are not overcome with competition and suggest a historical success for this type of cuisine.
Utilizing the “Heatmaps of Taco Restaurant Count by Price & Rating”, we see that almost 30% of all taco restaurants in an Austin zip code can be found within just 3 zip codes. 78702 (Parts of Downtown and East Austin) has the highest density of taco restaurants, followed by 78704 (Barton Hills/South Congress/South Lamar) and 78757 (North Shoal Creek/Crestview). 
Zip codes with a moderate number of taco restaurants (3% - 4% of total taco restaurants) include 78756 (Rosedale), 78745 (Westgate/Garrison Park), 78759 (West of the Domain), 78758 (North Central Austin), 78744 (Southeast Austin), 78705 (North and West of UT). Based on restaurant count alone,  78748, 78752 & 78751 also stand out as possible zip codes to look into with ranging from 10-12 restaurants in each  (2%-3% of total restaurants by cuisine). 


<h3>What is the distribution of restaurants by cuisine, by rating/review, by zip code?  </h3>
Ratings (Google Reviews) suggest a positive to negative response to a particular restaurant. We can assume that areas with high average ratings/reviews will be saturated with competition & high customer loyalty to the existing restaurants by cuisine type. For our purposes, by identifying the average rating of a particular restaurant type by zip code, we can continuing narrowing down to zip codes that have moderate to low ratings/sentiments in regards to a particular cuisine. This will allow us to identify areas with less competition, little current customer loyalty and a higher likelihood of success for a new, incoming restaurant. 
Utilizing the “Heatmaps of Taco Restaurant Count by Rating”, we can see that as the restaurant count by zip code increases, the percentage of 4+ star ratings steadily increases, while the percentage of 3-4 star ratings steadily decreases. We can assume that the more restaurants by cuisine a specific area has, the more likely potential customers can find a large number of highly reviewed restaurants - further strengthening the theory that these highly saturated areas are too competitive for a new restaurant/our client. 



<h3>What is the distribution of restaurants by cuisine with similar price range by zip? Which neighborhoods have populations of our target market based on income?</h3>
We assume that discretionary income plays a large part in where a consumer chooses to spend their money. By identifying median income by zip code, we can suggest an area that will likely hold potential customers within our client’s menu price range. 
Utilizing “Taco Restaurant Density by Median Income” Map, we can see that median incomes increase as you move west through each zip code. That being said, median income is lowest in 78712 and 78705 zip codes. In relation to these zip codes’ close proximity to the university, we can assume this lower income bracket is due to a larger student population. Our client's restaurant is expected to have an average order value on the lower end of the price scale ($). For this reason, we will likely target zip codes in low to mid income brackets, assuming the population is in search of new locations/restaurants within their price range & budget. 

<h2>Visualizations:</h2> 

<h4>Heatmaps of Taco Restaurant Count by Price and Rating</h4>

!["heatmap"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/output_yummy_client/Heatmap%20of%20taco%20restaurants%20by%20zipcode%20in%20Austin%2C%20TX.png)

<h4>Swarmplots of Restaurant Count by Price and Rating</h4>


!["swarmplot"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/output_yummy_client/Swarmplot%20of%20taco%20restaurants%20by%20zipcode%20in%20Austin%2C%20TX.png)

<h4>Taco Restaurant Density by Zip*</h4>

*See below for instructions to view dynamic plots.
!["Cluster Map by Density"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/Screen%20Shot%202018-03-14%20at%2011.12.22%20AM.png)

<h4>Heatmap Density of Taco Restaurants by Zip*</h4>

*See below for instructions to view dynamic plots.

!["Geo heatmap"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/Screen%20Shot%202018-03-14%20at%2011.38.44%20AM.png)

<h4>Map of Locations with Ratings*</h4>

*See below for instructions to view dynamic plots.

!["Taco Restaurant Location by Rating"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/Screen%20Shot%202018-03-14%20at%2011.09.00%20AM.png)

Note: Dots in red are restaurants that have not been rated.


<h4>Taco Restaurant Density by Median Income*</h4>

*See below for instructions to view dynamic plots.

!["Median Income"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/Screen%20Shot%202018-03-14%20at%2011.07.41%20AM.png)

<h4>Presentation</h4>

[Link to Full Presentation](https://docs.google.com/presentation/d/1QLDXyW-qr9dcxX0ToU_s7tcpmEPBAlRHW_dnaCM8Bas/edit#slide=id.p)
[Jupyter Notebook](https://github.com/MadeleineC/TheYummyDataProject/blob/master/YummyProject.ipynb)

<h4> Instructions to View Dynamic Plots </h4>

- Download output-mapbox_2 (mapbox visualizations) or output_yummy_client (geo-heatmap) directory from repo.

- In terminal enter: python -m http.server

- Open your browser and enter in the url bar: 127.0.0.1:8000

- Click on the html chart that you would like to load.
