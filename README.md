# AirBnB MongoDB Analysis
### Data set
This data set is about the information of AirBnB in Oakland, California, United States. It comes from [Inside Airbnb website](https://insideairbnb.com/get-the-data/). 
The original data format is: [listings.csv.gz](https://data.insideairbnb.com/united-states/ca/oakland/2023-12-20/data/listings.csv.gz).
Here are the first 20 rows of the row data.
|   id      |   listing_url                          |   scrape_id  |   last_scraped  |   source           |   name                                                                      |   description  |   neighborhood_overview                                                                                                                                                                                     |   picture_url                                                                                              |   host_id  |   host_url                                   |   host_name        |   host_since  |   host_location  |   host_about                                                                                                                                                |   host_response_time  |   host_response_rate  |   host_acceptance_rate  |   host_is_superhost  |   host_thumbnail_url                                                                                                                |   host_picture_url                                                                                                                     |   host_neighbourhood              |   host_listings_count  |   host_total_listings_count  |   host_verifications                |   host_has_profile_pic  |   host_identity_verified  |   neighbourhood                       |   neighbourhood_cleansed  |   neighbourhood_group_cleansed  |   latitude           |   longitude  |   property_type                |   room_type        |   accommodates  |   bathrooms  |   bathrooms_text  |   bedrooms  |   beds  |   amenities  |   price     |   minimum_nights  |   maximum_nights  |   minimum_minimum_nights  |   maximum_minimum_nights  |   minimum_maximum_nights  |   maximum_maximum_nights  |   minimum_nights_avg_ntm  |   maximum_nights_avg_ntm  |   calendar_updated  |   has_availability  |   availability_30  |   availability_60  |   availability_90  |   availability_365  |   calendar_last_scraped  |   number_of_reviews  |   number_of_reviews_ltm  |   number_of_reviews_l30d  |   first_review  |   last_review  |   review_scores_rating  |   review_scores_accuracy  |   review_scores_cleanliness  |   review_scores_checkin  |   review_scores_communication  |   review_scores_location  |   review_scores_value  |   license  |   instant_bookable  |   calculated_host_listings_count  |   calculated_host_listings_count_entire_homes  |   calculated_host_listings_count_private_rooms  |   calculated_host_listings_count_shared_rooms  |   reviews_per_month  |
|-----------|----------------------------------------|--------------|-----------------|--------------------|-----------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------|----------------------------------------------|--------------------|---------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-----------------------|-------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|------------------------|------------------------------|-------------------------------------|-------------------------|---------------------------|---------------------------------------|---------------------------|---------------------------------|----------------------|--------------|--------------------------------|--------------------|-----------------|--------------|-------------------|-------------|---------|--------------|-------------|-------------------|-------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------|---------------------|--------------------|--------------------|--------------------|---------------------|--------------------------|----------------------|--------------------------|---------------------------|-----------------|----------------|-------------------------|---------------------------|------------------------------|--------------------------|--------------------------------|---------------------------|------------------------|------------|---------------------|-----------------------------------|------------------------------------------------|-------------------------------------------------|------------------------------------------------|----------------------|
|   3083    |   https://www.airbnb.com/rooms/3083    |   2.023E+13  |   #######       |   city scrape      |   Home in Oakland 路 鈽4.73 路 1 bedroom 路 1 bed 路 1 shared bath          |                |   The neighborhood is in a historic district with beautiful Victorian homes that are over 100 years old. It's close to the BART train and most major freeways. The weather is generally warm and pleasant.  |   https://a0.muscache.com/pictures/miso/Hosting-3083/original/368d71ef-491d-493e-b79e-c008460a8bd0.jpeg    |   3518     |   https://www.airbnb.com/users/show/3518     |   Traci            |   2008/10/8   |   Oakland, CA    | Hello! I am Traci, an artist and activist who has been at the forefront of Oakland's cultural renaissance for many years.                                   |   within an hour      |   100%                |   100%                  |   t                  |   https://a0.muscache.com/im/pictures/user/407462e1-52dd-4eab-80c2-0c8e2b94a496.jpg?aki_policy=profile_small                        |   https://a0.muscache.com/im/pictures/user/407462e1-52dd-4eab-80c2-0c8e2b94a496.jpg?aki_policy=profile_x_medium                        |   Prescott                        |   7                    |   7                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Prescott                |                                 |   37.81013           |   -122.2927  |   Private room in home         |   Private room     |   2             |              |   1 shared bath   |             |   1     |   []         |   $44.00    |   2               |   30              |   2                       |   2                       |   30                      |   30                      |   2                       |   30                      |                     |   t                 |   30               |   60               |   90               |   365               |   #######                |   59                 |   3                      |   1                       |   2014/8/2      |   #######      |   4.73                  |   4.76                    |   4.64                       |   4.86                   |   4.88                         |   4.58                    |   4.68                 |            |   t                 |   7                               |   0                                            |   7                                             |   0                                            |   0.52               |
|   3264    |   https://www.airbnb.com/rooms/3264    |   2.023E+13  |   #######       |   city scrape      |   Home in Oakland 路 鈽4.52 路 1 bedroom 路 1 bed 路 1 shared bath          |                | This neighborhood has become very very popular recently. New restaurants and fun shops opening all the time. Free outdoor cinema in summer. Lots of street festivals.                                       |   https://a0.muscache.com/pictures/322655/94b9c23b_original.jpg                                            |   3241     |   https://www.airbnb.com/users/show/3241     |   Rebecca          |   2008/9/27   |   Oakland, CA    |   Artist, teacher, gardner, recycler/reuser.                                                                                                                |   within a few hours  |   100%                |   44%                   |   t                  |   https://a0.muscache.com/im/users/3241/profile_pic/1356474407/original.jpg?aki_policy=profile_small                                |   https://a0.muscache.com/im/users/3241/profile_pic/1356474407/original.jpg?aki_policy=profile_x_medium                                |   Temescal                        |   4                    |   10                         |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Temescal                |                                 |   37.83522           |   -122.261   |   Private room in home         |   Private room     |   1             |              |   1 shared bath   |             |   1     |   []         |   $57.00    |   12              |   60              |   12                      |   12                      |   60                      |   60                      |   12                      |   60                      |                     |   t                 |   18               |   48               |   78               |   78                |   #######                |   37                 |   0                      |   0                       |   2009/7/13     |   2022/9/8     |   4.52                  |   4.29                    |   4                          |   4.81                   |   4.95                         |   4.67                    |   4.38                 |            |   f                 |   4                               |   0                                            |   4                                             |   0                                            |   0.21               |
|   5739    |   https://www.airbnb.com/rooms/5739    |   2.023E+13  |   #######       |   city scrape      |   Guest suite in Oakland 路 鈽4.97 路 Studio 路 1 bed 路 1 bath             |                |   We love the proximity to great restaurants, Whole Foods market, entertainment and transit options, while still feeling residential.                                                                       |   https://a0.muscache.com/pictures/116966/376a1fe0_original.jpg                                            |   9276     |   https://www.airbnb.com/users/show/9276     |   Leah And Gyorgy  |   2009/3/6    |   Oakland, CA    | We are a conscientious couple and will take good care of your place, and trust you will do the same with ours!                                              |   within an hour      |   100%                |   96%                   |   t                  |   https://a0.muscache.com/im/users/9276/profile_pic/1259100072/original.jpg?aki_policy=profile_small                                |   https://a0.muscache.com/im/users/9276/profile_pic/1259100072/original.jpg?aki_policy=profile_x_medium                                |   Harrison Street/Oakland Avenue  |   1                    |   2                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Adams Point             |                                 |   37.81266314006893  |   -122.258   |   Entire guest suite           |   Entire home/apt  |   2             |              |   1 bath          |             |   1     |   []         |   $100.00   |   4               |   29              |   4                       |   4                       |   1125                    |   1125                    |   4                       |   1125                    |                     |   t                 |   23               |   53               |   83               |   83                |   #######                |   320                |   18                     |   0                       |   2009/7/14     |   2023/11/9    |   4.97                  |   4.97                    |   4.97                       |   4.97                   |   4.98                         |   4.92                    |   4.92                 |            |   f                 |   1                               |   1                                            |   0                                             |   0                                            |   1.82               |
|   23637   |   https://www.airbnb.com/rooms/23637   |   2.023E+13  |   #######       |   city scrape      |   Home in Oakland 路 鈽4.87 路 1 bedroom 路 1 bed 路 1 private bath         |                |   Quiet residential neighborhood surrounded by oak and redwood trees.                                                                                                                                       |   https://a0.muscache.com/pictures/354b693c-06df-4ce6-97ff-8d40339cb880.jpg                                |   93339    |   https://www.airbnb.com/users/show/93339    |   Mika             |   2010/3/14   |   Oakland, CA    | College instructor.                                                                                                                                         |   N/A                 |   N/A                 |   0%                    |   f                  |   https://a0.muscache.com/im/users/93339/profile_pic/1268623349/original.jpg?aki_policy=profile_small                               |   https://a0.muscache.com/im/users/93339/profile_pic/1268623349/original.jpg?aki_policy=profile_x_medium                               |                                   |   1                    |   1                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Montclair               |                                 |   37.82994           |   -122.2098  |   Private room in home         |   Private room     |   1             |              |   1 private bath  |             |   1     |   []         |   $75.00    |   7               |   100             |   7                       |   7                       |   100                     |   100                     |   7                       |   100                     |                     |   t                 |   28               |   58               |   88               |   363               |   #######                |   49                 |   0                      |   0                       |   2010/3/17     |   2022/8/27    |   4.87                  |   4.82                    |   4.97                       |   4.97                   |   4.89                         |   4.95                    |   4.89                 |            |   f                 |   1                               |   0                                            |   1                                             |   0                                            |   0.29               |
|   24916   |   https://www.airbnb.com/rooms/24916   |   2.023E+13  |   #######       |   city scrape      |   Guest suite in Oakland 路 鈽4.52 路 Studio 路 2 beds 路 1 bath            |                |   great neighborhood, for walking , beautiful gardens,grocery shopping very close by, restaurants, movie theater, bus ,BART nearby                                                                          |   https://a0.muscache.com/pictures/2417484/1098d9e5_original.jpg                                           |   98716    |   https://www.airbnb.com/users/show/98716    |   Judy             |   2010/3/25   |   Oakland, CA    |   I have lived in this area my whole life and really enjoy sharing with guests all the wonderful restaurants,shops, and attractions we have to offer here!  |   within an hour      |   100%                |   100%                  |   f                  |   https://a0.muscache.com/im/pictures/user/565b924d-0c40-444f-aad4-6fd39ef0f659.jpg?aki_policy=profile_small                        |   https://a0.muscache.com/im/pictures/user/565b924d-0c40-444f-aad4-6fd39ef0f659.jpg?aki_policy=profile_x_medium                        |   Piedmont Avenue                 |   2                    |   5                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Piedmont Avenue         |                                 |   37.83169           |   -122.2518  |   Entire guest suite           |   Entire home/apt  |   2             |              |   1 bath          |             |   2     |   []         |   $109.00   |   21              |   180             |   2                       |   21                      |   1125                    |   1125                    |   20.2                    |   1125                    |                     |   t                 |   0                |   0                |   0                |   0                 |   #######                |   135                |   6                      |   1                       |   2010/6/29     |   #######      |   4.52                  |   4.56                    |   4.48                       |   4.79                   |   4.7                          |   4.83                    |   4.54                 |            |   f                 |   2                               |   2                                            |   0                                             |   0                                            |   0.82               |
|   29521   |   https://www.airbnb.com/rooms/29521   |   2.023E+13  |   #######       |   previous scrape  |   Home in Oakland 路 鈽4.64 路 2 bedrooms 路 2 beds 路 1 bath               |                |   Centrally located, walking distance to markets, boutiques, restaurants, parks and outdoor activities. Great neighborhood!                                                                                 |   https://a0.muscache.com/pictures/09205cda-384c-4410-aaa7-378783a40900.jpg                                |   124220   |   https://www.airbnb.com/users/show/124220   |   Kymi             |   2010/5/13   |   Chicago, IL    | I am a bi-coastal singer-songwriter who also works in high tech consulting.                                                                                 |   within an hour      |   100%                |   93%                   |   f                  |   https://a0.muscache.com/im/pictures/user/User-124220/original/91df060b-7db3-4870-81f8-1d76b542b264.jpeg?aki_policy=profile_small  |   https://a0.muscache.com/im/pictures/user/User-124220/original/91df060b-7db3-4870-81f8-1d76b542b264.jpeg?aki_policy=profile_x_medium  |   Shafter                         |   3                    |   4                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Shafter                 |                                 |   37.83618           |   -122.2558  |   Entire home                  |   Entire home/apt  |   4             |              |   1 bath          |             |   2     |   []         |             |   5               |   30              |   5                       |   5                       |   30                      |   30                      |   5                       |   30                      |                     |                     |   0                |   0                |   0                |   0                 |   #######                |   37                 |   1                      |   1                       |   2011/7/23     |   #######      |   4.64                  |   4.76                    |   4.57                       |   4.7                    |   4.84                         |   4.95                    |   4.73                 |            |   f                 |   2                               |   2                                            |   0                                             |   0                                            |   0.24               |
|   31573   |   https://www.airbnb.com/rooms/31573   |   2.023E+13  |   #######       |   city scrape      |   Home in Oakland 路 鈽4.48 路 3 bedrooms 路 3 beds 路 1.5 baths            |                |   Great neighborhood for walking, beautiful gardens                                                                                                                                                         |   https://a0.muscache.com/pictures/555319/10480de1_original.jpg                                            |   98716    |   https://www.airbnb.com/users/show/98716    |   Judy             |   2010/3/25   |   Oakland, CA    |   I have lived in this area my whole life and really enjoy sharing with guests all the wonderful restaurants,shops, and attractions we have to offer here!  |   within an hour      |   100%                |   100%                  |   f                  |   https://a0.muscache.com/im/pictures/user/565b924d-0c40-444f-aad4-6fd39ef0f659.jpg?aki_policy=profile_small                        |   https://a0.muscache.com/im/pictures/user/565b924d-0c40-444f-aad4-6fd39ef0f659.jpg?aki_policy=profile_x_medium                        |   Piedmont Avenue                 |   2                    |   5                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Piedmont Avenue         |                                 |   37.83234           |   -122.251   |   Entire home                  |   Entire home/apt  |   4             |              |   1.5 baths       |             |   3     |   []         |   $221.00   |   28              |   365             |   28                      |   28                      |   365                     |   365                     |   28                      |   365                     |                     |   t                 |   0                |   8                |   18               |   79                |   #######                |   163                |   5                      |   0                       |   #######       |   2023/1/24    |   4.48                  |   4.65                    |   4.49                       |   4.74                   |   4.62                         |   4.76                    |   4.53                 |            |   f                 |   2                               |   2                                            |   0                                             |   0                                            |   1.02               |
|   36702   |   https://www.airbnb.com/rooms/36702   |   2.023E+13  |   #######       |   city scrape      |   Home in Oakland 路 鈽4.90 路 2 bedrooms 路 3 beds 路 1 bath               |                |   Our neighborhood is walking distance to shopping and restaurants in Temescal and Rockridge.  There are lots of families in the neighborhood.                                                              |   https://a0.muscache.com/pictures/miso/Hosting-36702/original/deaf1ce7-9fe1-4c26-9dc3-40082cbb0550.jpeg   |   119361   |   https://www.airbnb.com/users/show/119361   |   Vito             |   2010/5/6    |   Oakland, CA    |   We are both chefs.                                                                                                                                        |   within a few hours  |   100%                |   88%                   |   t                  |   https://a0.muscache.com/im/pictures/user/912ef789-0dea-4945-b78a-80615d46f5ed.jpg?aki_policy=profile_small                        |   https://a0.muscache.com/im/pictures/user/912ef789-0dea-4945-b78a-80615d46f5ed.jpg?aki_policy=profile_x_medium                        |                                   |   1                    |   1                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Bushrod                 |                                 |   37.84219           |   -122.2678  |   Entire home                  |   Entire home/apt  |   4             |              |   1 bath          |             |   3     |   []         |   $125.00   |   7               |   29              |   7                       |   7                       |   29                      |   29                      |   7                       |   29                      |                     |   t                 |   0                |   0                |   17               |   220               |   #######                |   39                 |   5                      |   0                       |   2010/8/25     |   #######      |   4.9                   |   4.95                    |   4.95                       |   5                      |   4.97                         |   4.79                    |   4.84                 |            |   f                 |   1                               |   1                                            |   0                                             |   0                                            |   0.24               |
|   43343   |   https://www.airbnb.com/rooms/43343   |   2.023E+13  |   #######       |   previous scrape  |   Rental unit in Oakland 路 鈽5.0 路 1 bedroom 路 1 bed 路 1 bath           |                |   20 min walk to UC Berkeley. This area is excellent for bike lovers as well.                                                                                                                               |   https://a0.muscache.com/pictures/50705329/8c5ac544_original.jpg                                          |   147060   |   https://www.airbnb.com/users/show/147060   |   Jonathan         |   2010/6/17   |   Oakland, CA    |   Always searching for something delicious to eat. I love dessert and think it should be eaten first!                                                       |   within an hour      |   100%                |   100%                  |   t                  |   https://a0.muscache.com/im/users/147060/profile_pic/1408635439/original.jpg?aki_policy=profile_small                              |   https://a0.muscache.com/im/users/147060/profile_pic/1408635439/original.jpg?aki_policy=profile_x_medium                              |   Bushrod                         |   2                    |   6                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Bushrod                 |                                 |   37.84298           |   -122.2622  |   Entire rental unit           |   Entire home/apt  |   2             |              |   1 bath          |             |   1     |   []         |             |   14              |   29              |   14                      |   14                      |   29                      |   29                      |   14                      |   29                      |                     |                     |   0                |   0                |   0                |   0                 |   #######                |   22                 |   0                      |   0                       |   #######       |   2019/6/24    |   5                     |   5                       |   4.95                       |   4.77                   |   4.95                         |   4.68                    |   4.91                 |            |   f                 |   2                               |   2                                            |   0                                             |   0                                            |   0.2                |
|   46787   |   https://www.airbnb.com/rooms/46787   |   2.023E+13  |   #######       |   city scrape      |   Home in Oakland 路 鈽4.86 路 1 bedroom 路 1 bed 路 1 shared bath          |                |   Home is smack dab right in the heart of Temescal, Oakland's cool super hip neighborhood.                                                                                                                  |   https://a0.muscache.com/pictures/15632694/74be1d49_original.jpg                                          |   3241     |   https://www.airbnb.com/users/show/3241     |   Rebecca          |   2008/9/27   |   Oakland, CA    |   Artist, teacher, gardner, recycler/reuser.                                                                                                                |   within a few hours  |   100%                |   44%                   |   t                  |   https://a0.muscache.com/im/users/3241/profile_pic/1356474407/original.jpg?aki_policy=profile_small                                |   https://a0.muscache.com/im/users/3241/profile_pic/1356474407/original.jpg?aki_policy=profile_x_medium                                |   Temescal                        |   4                    |   10                         |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Temescal                |                                 |   37.83571           |   -122.2589  |   Private room in home         |   Private room     |   1             |              |   1 shared bath   |             |   1     |   []         |   $74.00    |   14              |   60              |   14                      |   14                      |   60                      |   60                      |   14                      |   60                      |                     |   t                 |   19               |   49               |   79               |   169               |   #######                |   18                 |   2                      |   0                       |   #######       |   2023/9/4     |   4.86                  |   4.56                    |   4.25                       |   5                      |   4.88                         |   4.75                    |   4.47                 |            |   f                 |   4                               |   0                                            |   4                                             |   0                                            |   0.11               |
|   46908   |   https://www.airbnb.com/rooms/46908   |   2.023E+13  |   #######       |   city scrape      |   Home in Oakland 路 鈽4.95 路 2 bedrooms 路 4 beds 路 1 bath               |                | Quiet residential street, within walking distance of shops in the "Dimond District" of Oakland and Dimond Park.                                                                                             |   https://a0.muscache.com/pictures/miso/Hosting-46908/original/45ad4201-1785-4040-a1c5-eb1ae684d9a3.jpeg   |   210654   |   https://www.airbnb.com/users/show/210654   |   Mercedes         |   2010/8/23   |   Oakland, CA    | I am an architect  who loves to travel and to host visitors alike...                                                                                        |   within a day        |   100%                |   92%                   |   t                  |   https://a0.muscache.com/im/users/210654/profile_pic/1282603011/original.jpg?aki_policy=profile_small                              |   https://a0.muscache.com/im/users/210654/profile_pic/1282603011/original.jpg?aki_policy=profile_x_medium                              |   Meadow Brook                    |   2                    |   3                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Upper Dimond            |                                 |   37.80252           |   -122.2083  |   Entire home                  |   Entire home/apt  |   4             |              |   1 bath          |             |   4     |   []         |   $176.00   |   30              |   180             |   1                       |   30                      |   180                     |   180                     |   29.9                    |   180                     |                     |   t                 |   0                |   0                |   16               |   291               |   #######                |   20                 |   5                      |   0                       |   #######       |   2023/9/2     |   4.95                  |   5                       |   5                          |   4.9                    |   5                            |   4.8                     |   4.95                 |            |   f                 |   2                               |   2                                            |   0                                             |   0                                            |   0.32               |
|   56645   |   https://www.airbnb.com/rooms/56645   |   2.023E+13  |   #######       |   city scrape      |   Home in Oakland 路 鈽4.65 路 1 bedroom 路 1 bed 路 1 shared bath          |                | Millsmont is almost a secret part of Oakland known mostly to locals.                                                                                                                                        |   https://a0.muscache.com/pictures/273c387a-0189-40bc-9efc-ee32f741cd84.jpg                                |   268781   |   https://www.airbnb.com/users/show/268781   |   Pam              |   #######     |   Oakland, CA    | I am a writer, content strategist and former documentary filmmaker.                                                                                         |   within an hour      |   100%                |   100%                  |   f                  |   https://a0.muscache.com/im/pictures/user/1c11ab37-ded1-4825-9d55-dd6e45c2d2b0.jpg?aki_policy=profile_small                        |   https://a0.muscache.com/im/pictures/user/1c11ab37-ded1-4825-9d55-dd6e45c2d2b0.jpg?aki_policy=profile_x_medium                        |   Central East Oakland            |   4                    |   7                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Millsmont               |                                 |   37.7769            |   -122.1804  |   Private room in home         |   Private room     |   1             |              |   1 shared bath   |             |   1     |   []         |   $38.00    |   28              |   300             |   5                       |   28                      |   1125                    |   1125                    |   27.5                    |   1125                    |                     |   t                 |   8                |   26               |   56               |   236               |   #######                |   43                 |   7                      |   0                       |   2017/5/22     |   2023/9/29    |   4.65                  |   4.74                    |   4.4                        |   4.81                   |   4.91                         |   4.49                    |   4.7                  |            |   f                 |   4                               |   0                                            |   4                                             |   0                                            |   0.54               |
|   85974   |   https://www.airbnb.com/rooms/85974   |   2.023E+13  |   #######       |   city scrape      |   Guesthouse in Oakland 路 鈽4.87 路 1 bedroom 路 1 bed 路 1 bath           |                |   Rockridge is a vibrant walking neighborhood filled with beautiful streets and gardens but close to amazing restaurants, cafes & amazing public transportation that takes you to SF in 20 mins!            |   https://a0.muscache.com/pictures/d94973fc-0308-49c3-bc4f-454fc39f697d.jpg                                |   471600   |   https://www.airbnb.com/users/show/471600   |   Ericka           |   2011/3/29   |   Oakland, CA    | I'm a commercial  photographer, an entrepreneur and a mama.                                                                                                 |   within an hour      |   100%                |   100%                  |   t                  |   https://a0.muscache.com/im/pictures/user/f063070d-7f9b-4cc5-bfdc-2b7b65330d31.jpg?aki_policy=profile_small                        |   https://a0.muscache.com/im/pictures/user/f063070d-7f9b-4cc5-bfdc-2b7b65330d31.jpg?aki_policy=profile_x_medium                        |   Shafter                         |   1                    |   2                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Shafter                 |                                 |   37.84211           |   -122.252   |   Entire guesthouse            |   Entire home/apt  |   2             |              |   1 bath          |             |   1     |   []         |   $188.00   |   3               |   60              |   3                       |   3                       |   60                      |   60                      |   3                       |   60                      |                     |   t                 |   23               |   53               |   80               |   355               |   #######                |   243                |   15                     |   1                       |   2011/5/17     |   #######      |   4.87                  |   4.93                    |   4.9                        |   4.96                   |   4.94                         |   4.95                    |   4.79                 |            |   f                 |   1                               |   1                                            |   0                                             |   0                                            |   1.58               |
|   136250  |   https://www.airbnb.com/rooms/136250  |   2.023E+13  |   #######       |   city scrape      |   Guesthouse in Oakland 路 鈽5.0 路 2 bedrooms 路 1 bed 路 1 bath           |                |   Quiet, safe, serene, wooded                                                                                                                                                                               |   https://a0.muscache.com/pictures/miso/Hosting-136250/original/de8a40eb-dc42-4707-888c-f00165f99c2f.jpeg  |   667229   |   https://www.airbnb.com/users/show/667229   |   Mark             |   2011/6/5    |   Danville, CA   |                                                                                                                                                             |   within a few hours  |   100%                |   100%                  |   t                  |   https://a0.muscache.com/im/users/667229/profile_pic/1307307080/original.jpg?aki_policy=profile_small                              |   https://a0.muscache.com/im/users/667229/profile_pic/1307307080/original.jpg?aki_policy=profile_x_medium                              |   Merriwood                       |   2                    |   4                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Merriwood               |                                 |   37.83699           |   -122.2145  |   Entire guesthouse            |   Entire home/apt  |   2             |              |   1 bath          |             |   1     |   []         |   $80.00    |   30              |   150             |   30                      |   30                      |   150                     |   150                     |   30                      |   150                     |                     |   t                 |   0                |   0                |   0                |   201               |   #######                |   13                 |   2                      |   0                       |   2017/1/15     |   2023/4/11    |   5                     |   4.92                    |   4.85                       |   5                      |   5                            |   4.85                    |   4.85                 |            |   f                 |   2                               |   1                                            |   1                                             |   0                                            |   0.15               |
|   151422  |   https://www.airbnb.com/rooms/151422  |   2.023E+13  |   #######       |   city scrape      |   Rental unit in Oakland 路 鈽5.0 路 1 bedroom 路 1 bed 路 1 bath           |                | In all of Oakland, I LOVE the Grand-Lake area.                                                                                                                                                              |   https://a0.muscache.com/pictures/39942894/d00e6520_original.jpg                                          |   729004   |   https://www.airbnb.com/users/show/729004   |   Amy              |   2011/6/21   |   Oakland, CA    | I enjoy community singing, music, dancing, hiking, reading, learning, lectures, and travel.                                                                 |   N/A                 |   N/A                 |   0%                    |   f                  |   https://a0.muscache.com/im/pictures/user/dbebcfa2-90f9-40aa-994a-3ed2e353c5df.jpg?aki_policy=profile_small                        |   https://a0.muscache.com/im/pictures/user/dbebcfa2-90f9-40aa-994a-3ed2e353c5df.jpg?aki_policy=profile_x_medium                        |                                   |   1                    |   1                          |   ['email', 'phone']                |   t                     |   f                       |   Oakland, California, United States  |   Adams Point             |                                 |   37.81089           |   -122.254   |   Entire rental unit           |   Entire home/apt  |   2             |              |   1 bath          |             |   1     |   []         |   $160.00   |   1               |   14              |   1                       |   1                       |   14                      |   14                      |   1                       |   14                      |                     |   t                 |   23               |   53               |   83               |   263               |   #######                |   9                  |   0                      |   0                       |   #######       |   2022/7/9     |   5                     |   4.89                    |   5                          |   5                      |   5                            |   5                       |   5                    |            |   f                 |   1                               |   1                                            |   0                                             |   0                                            |   0.08               |
|   155368  |   https://www.airbnb.com/rooms/155368  |   2.023E+13  |   #######       |   city scrape      |   Home in Oakland 路 鈽4.92 路 2 bedrooms 路 2 beds 路 1.5 baths            |                | We have lived here for over 30 years and love our neighborhood.                                                                                                                                             |   https://a0.muscache.com/pictures/miso/Hosting-155368/original/ff96ebb0-c974-4657-b8ff-fab6c23597f1.jpeg  |   728977   |   https://www.airbnb.com/users/show/728977   |   Susan            |   2011/6/21   |   Oakland, CA    | My husband Christopher and I love living and working in the Oakland Hills which is central to the whole SF Bay Area.                                        |   N/A                 |   N/A                 |   86%                   |   f                  |   https://a0.muscache.com/im/users/728977/profile_pic/1441146089/original.jpg?aki_policy=profile_small                              |   https://a0.muscache.com/im/users/728977/profile_pic/1441146089/original.jpg?aki_policy=profile_x_medium                              |   Upper Rockridge                 |   1                    |   1                          |   ['email', 'phone', 'work_email']  |   t                     |   t                       |   Oakland, California, United States  |   Upper Rockridge         |                                 |   37.84419           |   -122.2341  |   Entire home                  |   Entire home/apt  |   4             |              |   1.5 baths       |             |   2     |   []         |   $250.00   |   3               |   10              |   3                       |   3                       |   10                      |   10                      |   3                       |   10                      |                     |   t                 |   27               |   57               |   87               |   177               |   #######                |   305                |   4                      |   1                       |   2011/7/13     |   #######      |   4.92                  |   4.88                    |   4.94                       |   4.98                   |   4.96                         |   4.89                    |   4.87                 |            |   f                 |   1                               |   1                                            |   0                                             |   0                                            |   2.01               |
|   169599  |   https://www.airbnb.com/rooms/169599  |   2.023E+13  |   #######       |   city scrape      |   Guest suite in Oakland 路 鈽4.65 路 1 bedroom 路 1 bed 路 1 bath          |                | This neighborhood is mostly quiet and just a few minutes from gorgeous walks through the woods on Mountain Blvd.                                                                                            |   https://a0.muscache.com/pictures/1181141/bccb5919_original.jpg                                           |   808353   |   https://www.airbnb.com/users/show/808353   |   Marlene          |   2011/7/12   |   Oakland, CA    | I am a Bay Area Garden Designer for a design/build firm and I love what I do.                                                                               |   N/A                 |   N/A                 |   N/A                   |   f                  |   https://a0.muscache.com/im/users/808353/profile_pic/1310450670/original.jpg?aki_policy=profile_small                              |   https://a0.muscache.com/im/users/808353/profile_pic/1310450670/original.jpg?aki_policy=profile_x_medium                              |   Central East Oakland            |   1                    |   1                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Millsmont               |                                 |   37.77847           |   -122.1762  |   Entire guest suite           |   Entire home/apt  |   2             |              |   1 bath          |             |   1     |   []         |   $115.00   |   2               |   365             |   2                       |   2                       |   365                     |   365                     |   2                       |   365                     |                     |   t                 |   0                |   0                |   2                |   277               |   #######                |   191                |   0                      |   0                       |   2011/8/16     |   #######      |   4.65                  |   4.77                    |   4.66                       |   4.86                   |   4.8                          |   4.34                    |   4.64                 |            |   f                 |   1                               |   1                                            |   0                                             |   0                                            |   1.27               |
|   208186  |   https://www.airbnb.com/rooms/208186  |   2.023E+13  |   #######       |   city scrape      |   Home in Oakland 路 鈽4.74 路 1 bedroom 路 1 bed 路 1 private bath         |                |   walking distance to Trader Joe's, Lake Merritt, and a thriving shopping and restaurant part of town, but a small neighborhood feeling at home with plenty of street parking.                              |   https://a0.muscache.com/pictures/abb1daaf-f312-4c85-88de-b1c34795a141.jpg                                |   1024552  |   https://www.airbnb.com/users/show/1024552  |   LaurieAnn        |   2011/8/26   |   Oakland, CA    | I'm a dance teacher specializing in working with dance phobic people who can't learn from anyone else.                                                      |   within an hour      |   100%                |   100%                  |   t                  |   https://a0.muscache.com/im/users/1024552/profile_pic/1425785962/original.jpg?aki_policy=profile_small                             |   https://a0.muscache.com/im/users/1024552/profile_pic/1425785962/original.jpg?aki_policy=profile_x_medium                             |   Cleveland Heights               |   2                    |   2                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Cleveland Heights       |                                 |   37.80732           |   -122.2429  |   Private room in home         |   Private room     |   2             |              |   1 private bath  |             |   1     |   []         |   $69.00    |   3               |   120             |   3                       |   3                       |   1125                    |   1125                    |   3                       |   1125                    |                     |   t                 |   25               |   25               |   25               |   245               |   #######                |   306                |   6                      |   1                       |   #######       |   2023/12/2    |   4.74                  |   4.81                    |   4.65                       |   4.91                   |   4.91                         |   4.81                    |   4.74                 |            |   t                 |   2                               |   1                                            |   1                                             |   0                                            |   2.06               |
|   242472  |   https://www.airbnb.com/rooms/242472  |   2.023E+13  |   #######       |   city scrape      |   Guest suite in Oakland 路 鈽4.51 路 1 bedroom 路 1 bed 路 1 private bath  |                |   Rockridge is the best! You will have everything you need at your fingertips!                                                                                                                              |   https://a0.muscache.com/pictures/fbb09b86-4b8a-430a-81cb-384e92932c19.jpg                                |   1272555  |   https://www.airbnb.com/users/show/1272555  |   Amy              |   #######     |   Oakland, CA    | Single mom with grown children out of the house and extra space to share!                                                                                   |   within an hour      |   100%                |   100%                  |   f                  |   https://a0.muscache.com/im/users/1272555/profile_pic/1392416064/original.jpg?aki_policy=profile_small                             |   https://a0.muscache.com/im/users/1272555/profile_pic/1392416064/original.jpg?aki_policy=profile_x_medium                             |   Shafter                         |   2                    |   3                          |   ['email', 'phone']                |   t                     |   t                       |   Oakland, California, United States  |   Rockridge               |                                 |   37.84453           |   -122.2513  |   Private room in guest suite  |   Private room     |   2             |              |   1 private bath  |             |   1     |   []         |   $139.00   |   2               |   60              |   2                       |   2                       |   60                      |   60                      |   2                       |   60                      |                     |   t                 |   18               |   48               |   78               |   168               |   #######                |   208                |   0                      |   0                       |   #######       |   2022/10/3    |   4.51                  |   4.54                    |   4.36                       |   4.75                   |   4.7                          |   4.89                    |   4.54                 |            |   f                 |   2                               |   1                                            |   1                                             |   0                                            |   1.4                |
### Data srubbing
1. I found that all entries in the description column of `listings.csv` are empty, so I removed this column. 
2. I removed the Column `picture_url` to simplify the dataset, which is not useful for the data analysis.
3. I found that many characters run the risk of importing incorrectly, so I replaced all the ★ with * .
Here is my code:
```
import csv

def scrub_data(input_file_path, output_file_path):
    columns_to_remove = ['picture_url']
    columns_to_remove.append('description')
    
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = None
        
        for row in reader:
            # Initialize writer with adjusted headers on the first row
            if writer is None:
                headers = [key.replace('★', '*') for key in row.keys() if key not in columns_to_remove]
                writer = csv.DictWriter(outfile, fieldnames=headers)
                writer.writeheader()
            
            # Replace ★ with * in all fields
            adjusted_row = {key.replace('★', '*'): value.replace('★', '*') for key, value in row.items() if key not in columns_to_remove}
            
            writer.writerow(adjusted_row)

# File paths
input_file_path = 'data/listings.csv'
output_file_path = 'data/listings_clean.csv'

scrub_data(input_file_path, output_file_path)

output_file_path

```
## Data analysis in MongoDB
1. Show exactly two documents from the listings collection in any order. 
Here is the code:
```
db.listings.find().limit(2)
```
```
  {
    _id: ObjectId('660f2bb9c34b7fbd6a5a27a7'),
    id: 3083,
    listing_url: 'https://www.airbnb.com/rooms/3083',
    scrape_id: Long('20231220185646'),
    last_scraped: '2023-12-20',
    source: 'city scrape',
    name: 'Home in Oakland · *4.73 · 1 bedroom · 1 bed · 1 shared bath',
    neighborhood_overview: "The neighborhood is in a historic district with beautiful Victorian homes that are over 100 years old. It's close to the BART train and most major freeways. The weather is generally warm and pleasant.",
    host_id: 3518,
    host_url: 'https://www.airbnb.com/users/show/3518',
    host_name: 'Traci',
    host_since: '2008-10-08',
    host_location: 'Oakland, CA',
    host_about: `Hello! I am Traci, an artist and activist who has been at the forefront of Oakland's cultural renaissance for many years. As a native of "The Town" I offer experiential living thats rooted in care, my creativity as a performance and visual artist, and my heritage of black farmers. \n` +
      '\n' +
      'My rooms are cozy, the art gallery inspiring, fun tours and a lush garden can make you feel grounded and rejuvenated. Come stay with me, book an experience, or both!',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/407462e1-52dd-4eab-80c2-0c8e2b94a496.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/407462e1-52dd-4eab-80c2-0c8e2b94a496.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Prescott',
    host_listings_count: 7,
    host_total_listings_count: 7,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Oakland, California, United States',
    neighbourhood_cleansed: 'Prescott',
    neighbourhood_group_cleansed: '',
    latitude: 37.81013,
    longitude: -122.29266,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: '1 shared bath',
    bedrooms: '',
    beds: 1,
    amenities: '[]',
    price: '$44.00',
    minimum_nights: 2,
    maximum_nights: 30,
    minimum_minimum_nights: 2,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 30,
    maximum_maximum_nights: 30,
    minimum_nights_avg_ntm: 2,
    maximum_nights_avg_ntm: 30,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 30,
    availability_60: 60,
    availability_90: 90,
    availability_365: 365,
    calendar_last_scraped: '2023-12-20',
    number_of_reviews: 59,
    number_of_reviews_ltm: 3,
    number_of_reviews_l30d: 1,
    first_review: '2014-08-02',
    last_review: '2023-11-30',
    review_scores_rating: 4.73,
    review_scores_accuracy: 4.76,
    review_scores_cleanliness: 4.64,
    review_scores_checkin: 4.86,
    review_scores_communication: 4.88,
    review_scores_location: 4.58,
    review_scores_value: 4.68,
    license: '',
    instant_bookable: 't',
    calculated_host_listings_count: 7,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 7,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.52
  },
  {
    _id: ObjectId('660f2bb9c34b7fbd6a5a27a8'),
    id: 3264,
    listing_url: 'https://www.airbnb.com/rooms/3264',
    scrape_id: Long('20231220185646'),
    last_scraped: '2023-12-20',
    source: 'city scrape',
    name: 'Home in Oakland · *4.52 · 1 bedroom · 1 bed · 1 shared bath',
    neighborhood_overview: "This neighborhood has become very very popular recently. New restaurants and fun shops opening all the time. Free outdoor cinema in summer. Lots of street festivals. Farmer's market at DMV on Sundays. It is a very lively neighborhood.",
    host_id: 3241,
    host_url: 'https://www.airbnb.com/users/show/3241',
    host_name: 'Rebecca',
    host_since: '2008-09-27',
    host_location: 'Oakland, CA',
    host_about: 'Artist, teacher, gardner, recycler/reuser. \n\n',
    host_response_time: 'within a few hours',
    host_response_rate: '100%',
    host_acceptance_rate: '44%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/3241/profile_pic/1356474407/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/3241/profile_pic/1356474407/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Temescal',
    host_listings_count: 4,
    host_total_listings_count: 10,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Oakland, California, United States',
    neighbourhood_cleansed: 'Temescal',
    neighbourhood_group_cleansed: '',
    latitude: 37.83522,
    longitude: -122.26099,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1 shared bath',
    bedrooms: '',
    beds: 1,
    amenities: '[]',
    price: '$57.00',
    minimum_nights: 12,
    maximum_nights: 60,
    minimum_minimum_nights: 12,
    maximum_minimum_nights: 12,
    minimum_maximum_nights: 60,
    maximum_maximum_nights: 60,
    minimum_nights_avg_ntm: 12,
    maximum_nights_avg_ntm: 60,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 18,
    availability_60: 48,
    availability_90: 78,
    availability_365: 78,
    calendar_last_scraped: '2023-12-20',
    number_of_reviews: 37,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '2009-07-13',
    last_review: '2022-09-08',
    review_scores_rating: 4.52,
    review_scores_accuracy: 4.29,
    review_scores_cleanliness: 4,
    review_scores_checkin: 4.81,
    review_scores_communication: 4.95,
    review_scores_location: 4.67,
    review_scores_value: 4.38,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 4,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 4,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.21
  }
```

2. show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the pretty() function.
Here is the code:
```
db.listings.find().limit(10).pretty()
```
First 3 results:
```
{
    _id: ObjectId('660f2bb9c34b7fbd6a5a27a7'),
    id: 3083,
    listing_url: 'https://www.airbnb.com/rooms/3083',
    scrape_id: Long('20231220185646'),
    last_scraped: '2023-12-20',
    source: 'city scrape',
    name: 'Home in Oakland · *4.73 · 1 bedroom · 1 bed · 1 shared bath',
    neighborhood_overview: "The neighborhood is in a historic district with beautiful Victorian homes that are over 100 years old. It's close to the BART train and most major freeways. The weather is generally warm and pleasant.",
    host_id: 3518,
    host_url: 'https://www.airbnb.com/users/show/3518',
    host_name: 'Traci',
    host_since: '2008-10-08',
    host_location: 'Oakland, CA',
    host_about: `Hello! I am Traci, an artist and activist who has been at the forefront of Oakland's cultural renaissance for many years. As a native of "The Town" I offer experiential living thats rooted in care, my creativity as a performance and visual artist, and my heritage of black farmers. \n` +
      '\n' +
      'My rooms are cozy, the art gallery inspiring, fun tours and a lush garden can make you feel grounded and rejuvenated. Come stay with me, book an experience, or both!',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/407462e1-52dd-4eab-80c2-0c8e2b94a496.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/407462e1-52dd-4eab-80c2-0c8e2b94a496.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Prescott',
    host_listings_count: 7,
    host_total_listings_count: 7,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Oakland, California, United States',
    neighbourhood_cleansed: 'Prescott',
    neighbourhood_group_cleansed: '',
    latitude: 37.81013,
    longitude: -122.29266,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: '1 shared bath',
    bedrooms: '',
    beds: 1,
    amenities: '[]',
    price: '$44.00',
    minimum_nights: 2,
    maximum_nights: 30,
    minimum_minimum_nights: 2,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 30,
    maximum_maximum_nights: 30,
    minimum_nights_avg_ntm: 2,
    maximum_nights_avg_ntm: 30,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 30,
    availability_60: 60,
    availability_90: 90,
    availability_365: 365,
    calendar_last_scraped: '2023-12-20',
    number_of_reviews: 59,
    number_of_reviews_ltm: 3,
    number_of_reviews_l30d: 1,
    first_review: '2014-08-02',
    last_review: '2023-11-30',
    review_scores_rating: 4.73,
    review_scores_accuracy: 4.76,
    review_scores_cleanliness: 4.64,
    review_scores_checkin: 4.86,
    review_scores_communication: 4.88,
    review_scores_location: 4.58,
    review_scores_value: 4.68,
    license: '',
    instant_bookable: 't',
    calculated_host_listings_count: 7,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 7,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.52
  },
  {
    _id: ObjectId('660f2bb9c34b7fbd6a5a27a8'),
    id: 3264,
    listing_url: 'https://www.airbnb.com/rooms/3264',
    scrape_id: Long('20231220185646'),
    last_scraped: '2023-12-20',
    source: 'city scrape',
    name: 'Home in Oakland · *4.52 · 1 bedroom · 1 bed · 1 shared bath',
    neighborhood_overview: "This neighborhood has become very very popular recently. New restaurants and fun shops opening all the time. Free outdoor cinema in summer. Lots of street festivals. Farmer's market at DMV on Sundays. It is a very lively neighborhood.",
    host_id: 3241,
    host_url: 'https://www.airbnb.com/users/show/3241',
    host_name: 'Rebecca',
    host_since: '2008-09-27',
    host_location: 'Oakland, CA',
    host_about: 'Artist, teacher, gardner, recycler/reuser. \n\n',
    host_response_time: 'within a few hours',
    host_response_rate: '100%',
    host_acceptance_rate: '44%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/3241/profile_pic/1356474407/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/3241/profile_pic/1356474407/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Temescal',
    host_listings_count: 4,
    host_total_listings_count: 10,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Oakland, California, United States',
    neighbourhood_cleansed: 'Temescal',
    neighbourhood_group_cleansed: '',
    latitude: 37.83522,
    longitude: -122.26099,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1 shared bath',
    bedrooms: '',
    beds: 1,
    amenities: '[]',
    price: '$57.00',
    minimum_nights: 12,
    maximum_nights: 60,
    minimum_minimum_nights: 12,
    maximum_minimum_nights: 12,
    minimum_maximum_nights: 60,
    maximum_maximum_nights: 60,
    minimum_nights_avg_ntm: 12,
    maximum_nights_avg_ntm: 60,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 18,
    availability_60: 48,
    availability_90: 78,
    availability_365: 78,
    calendar_last_scraped: '2023-12-20',
    number_of_reviews: 37,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '2009-07-13',
    last_review: '2022-09-08',
    review_scores_rating: 4.52,
    review_scores_accuracy: 4.29,
    review_scores_cleanliness: 4,
    review_scores_checkin: 4.81,
    review_scores_communication: 4.95,
    review_scores_location: 4.67,
    review_scores_value: 4.38,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 4,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 4,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.21
  },
  {
    _id: ObjectId('660f2bb9c34b7fbd6a5a27a9'),
    id: 5739,
    listing_url: 'https://www.airbnb.com/rooms/5739',
    scrape_id: Long('20231220185646'),
    last_scraped: '2023-12-20',
    source: 'city scrape',
    name: 'Guest suite in Oakland · *4.97 · Studio · 1 bed · 1 bath',
    neighborhood_overview: 'We love the proximity to great restaurants, Whole Foods market, entertainment and transit options, while still feeling residential.',
    host_id: 9276,
    host_url: 'https://www.airbnb.com/users/show/9276',
    host_name: 'Leah And Gyorgy',
    host_since: '2009-03-06',
    host_location: 'Oakland, CA',
    host_about: 'We are a conscientious couple and will take good care of your place, and trust you will do the same with ours!  We are involved in the arts (music, dance, even food!) and love to share our love of the Bay Area with others. We look forward to meeting you...or your home!',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '96%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/9276/profile_pic/1259100072/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/9276/profile_pic/1259100072/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Harrison Street/Oakland Avenue',
    host_listings_count: 1,
    host_total_listings_count: 2,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Oakland, California, United States',
    neighbourhood_cleansed: 'Adams Point',
    neighbourhood_group_cleansed: '',
    latitude: 37.81266314006893,
    longitude: -122.25804724258587,
    property_type: 'Entire guest suite',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: '',
    beds: 1,
    amenities: '[]',
    price: '$100.00',
    minimum_nights: 4,
    maximum_nights: 29,
    minimum_minimum_nights: 4,
    maximum_minimum_nights: 4,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 4,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 23,
    availability_60: 53,
    availability_90: 83,
    availability_365: 83,
    calendar_last_scraped: '2023-12-20',
    number_of_reviews: 320,
    number_of_reviews_ltm: 18,
    number_of_reviews_l30d: 0,
    first_review: '2009-07-14',
    last_review: '2023-11-09',
    review_scores_rating: 4.97,
    review_scores_accuracy: 4.97,
    review_scores_cleanliness: 4.97,
    review_scores_checkin: 4.97,
    review_scores_communication: 4.98,
    review_scores_location: 4.92,
    review_scores_value: 4.92,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 1.82
  }
  ```

3.  Choose two hosts (by reffering to their host_id values) who are superhosts (available in the host_is_superhost field), and show all of the listings offered by both of the two hosts.
 ```
db.listings.find(
    {$or: [
        {'host_id':3241},
        {'host_id':210654}
    ] },
    { 
        'name': 1,
        'price': 1,
        'neighborhood': 1,
        'host_name': 1,
        'host_is_superhost': 1
    }
)
```
First three results:
```
   {
    _id: ObjectId('660f2bb9c34b7fbd6a5a27a8'),
    name: 'Home in Oakland · *4.52 · 1 bedroom · 1 bed · 1 shared bath',
    host_name: 'Rebecca',
    host_is_superhost: 't',
    price: '$57.00'
  },
  {
    _id: ObjectId('660f2bb9c34b7fbd6a5a27b0'),
    name: 'Home in Oakland · *4.95 · 2 bedrooms · 4 beds · 1 bath',
    host_name: 'Mercedes',
    host_is_superhost: 't',
    price: '$176.00'
  },
  {
    _id: ObjectId('660f2bb9c34b7fbd6a5a27b2'),
    name: 'Home in Oakland · *4.86 · 1 bedroom · 1 bed · 1 shared bath',
    host_name: 'Rebecca',
    host_is_superhost: 't',
    price: '$74.00'
  }
```
4. find all the unique host_name values. Here is the code:
```
db.listings.distinct("host_name")
```
First three results:
```
['A', 'Aaron', 'Abdulla']
```
5. find all of the places that have more than 2 beds in a neighborhood of your choice (referred to as either the neighborhood or neighbourhood_group_cleansed fields in the data file), ordered by review_scores_rating descending. only show the name, beds, review_scores_rating, and price.
```
db.listings.find(
    {$and: [
        {'beds': {
            $gt: 2
        }},
        {'neighbourhood_cleansed': 'Shafter'}
    ] },
    { 
        'name': 1,
        'beds': 1,
        'review_scores_rating': 1,
        'price': 1
    }
    ).sort(
        {'review_scores_rating': -1}
    )
```
First three results:
```
  {
    _id: ObjectId('660f2bb9c34b7fbd6a5a2957'),
    name: 'Home in Oakland · 3 bedrooms · 3 beds · 2.5 baths',
    beds: 3,
    price: '',
    review_scores_rating: ''
  },
  {
    _id: ObjectId('660f2bb9c34b7fbd6a5a2894'),
    name: 'Home in Oakland · *5.0 · 4 bedrooms · 4 beds · 3 baths',
    beds: 4,
    price: '',
    review_scores_rating: 5
  },
  {
    _id: ObjectId('660f2bb9c34b7fbd6a5a2895'),
    name: 'Home in Oakland · *5.0 · 3 bedrooms · 3 beds · 2 baths',
    beds: 3,
    price: '',
    review_scores_rating: 5
  }
```
6. show the number of listings per host
```
db.listings.aggregate(
    {$group: {
         _id: '$host_id', 
         listingCount: {$sum: 1}
        }
    }
)
```
First three results:
```
[
  { _id: 9671447, listingCount: 1 },
  { _id: 92187151, listingCount: 1 },
  { _id: 498429374, listingCount: 1 }
  ]
```
7. find the average review_scores_rating per neighborhood, and only show those that are 4 or above, sorted in descending order of rating
```
db.listings.aggregate([
  { $match: { review_scores_rating: { $gte: 4 } } },
  { $group: { _id: "$neighbourhood", avg_rating: { $avg: "$review_scores_rating" } } },
  { $sort: { avg_rating: -1 } }
])
```
First three results:
```
  {
    _id: 'Piedmont, California, United States',
    avg_rating: 4.931111111111111
  },
  {
    _id: 'Emeryville, California, United States',
    avg_rating: 4.8758333333333335
  },
  {
    _id: 'Berkeley, California, United States',
    avg_rating: 4.837073170731707
  }
```