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

<h3>What is the distribution of restaurants of a given type of cuisine by zip? What is the distribution of restaurants with similar price range by zip? </h3>

Utilizing the below heatmap we see that almost 30% of all taco restaurants in an Austin zip code can be found within just 3 zip codes.  Downtown Austin (78702) has by far the highest density of taco restaurants, followed by a distant second and third of 78704 (Barton Hills/South Congress/South Lamar) and 78757 (North Shoal Creek/Crestview). Zip codes with a modest number of taco restaurants (14-16 total) include 78756 (Rosedale), 78745 (Westgate/Garrison Park), 78759 (West of the Domain), 78758 (North Central Austin), 78744 (Southeast Austin), 78705 (North and West of UT). Within this cohort of zip codes with a modest number of taco restaurants, 78759 (West of the Domain), has fewer taco restaurants that were rated highly (4-5) as compared to other zip codes in this cohort. We also note that 78744 and 78745, both in south Austin south of 290/71, have high concentrations of cheap taco restaurants ($), which would likely mean that competition in these neighborhoods would be higher. 

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

<h3>Which neighborhoods have populations of the target market based on income? </h3>

<h4>Taco Restaurant Density by Median Income*</h4>

*See below for instructions to view dynamic plots.

!["Median Income"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/Screen%20Shot%202018-03-14%20at%2011.07.41%20AM.png)

<h4>Presentation</h4>

[Link to Full Presentation](https://docs.google.com/presentation/d/1QLDXyW-qr9dcxX0ToU_s7tcpmEPBAlRHW_dnaCM8Bas/edit#slide=id.p)

<h4> Instructions to View Dynamic Plots </h4>

- Download output-mapbox_2 (mapbox visualizations) or output_yummy_client (geo-heatmap) directory from repo.

- In terminal enter: python -m http.server

- Open your browser and enter in the url bar: 127.0.0.1:8000

- Click on the html chart that you would like to load.
