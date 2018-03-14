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

Utilizing the below heatmap we see that almost 30% of all taco restaurants in an Austin zip code can be found within just 3 zip codes.  Downtown Austin (78702) has by far the highest density of taco restaurants, followed by a distant second and third of 78704 (Barton Hills/South Congress/South Lamar) and 78757 (North Shoal Creek/Crestview). 

<h4>Chart Heading*</h4>

!["heatmap"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/output_yummy_client/Heatmap%20of%20taco%20restaurants%20by%20zipcode%20in%20Austin%2C%20TX.png)

<h4>Chart Heading*</h4>


!["swarmmap"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/output_yummy_client/Swarmplot%20of%20taco%20restaurants%20by%20zipcode%20in%20Austin%2C%20TX.png)

<h4>Chart Heading*</h4>

*See below for instructions to view dynamic plots.
!["Cluster Map by Density"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/Screen%20Shot%202018-03-14%20at%2011.12.22%20AM.png)

<h4>Chart Heading*</h4>

*See below for instructions to view dynamic plots.

!["Geo heatmap"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/Screen%20Shot%202018-03-14%20at%2011.38.44%20AM.png)

<h4>Chart Heading*</h4>

*See below for instructions to view dynamic plots.

!["Location by Rating"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/Screen%20Shot%202018-03-14%20at%2011.09.00%20AM.png)

Note: Dots in red are restaurants restaurants that have not been rated.

<h3>Which neighborhoods have populations of target market based on income and support restaurants of a comparable price point? </h3>

<h4>Chart Heading*</h4>

*See below for instructions to view dynamic plots.

!["Median Income"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/Screen%20Shot%202018-03-14%20at%2011.07.41%20AM.png)

<h4>Chart Heading*</h4>

*See below for instructions to view dynamic plots.

!["all restaurants heatmap"](https://raw.githubusercontent.com/MadeleineC/TheYummyDataProject/master/output_yummy_client/Heatmap%20of%20restaurant%20restaurants%20by%20zipcode%20in%20Austin%2C%20TX.png)

<h4> Instructions to View Dynamic Mapbox Plots </h4>

- Download output-mapbox_2 directory from repo.

- In terminal enter: python -m http.server

- Open your browser and enter in the url bar: 127.0.0.1:8000

- Click on the html chart that you would like to load.
