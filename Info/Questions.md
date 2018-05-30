Questions:

**1. Similarity Matrix, why I chose it?**

There was no explicit rating in the data, so needed to create an implicit rating matrix to calculate an USER:USER
distance metric. I decided to use Cosine Similarity after recognizing that not all users had data for assessment scores,
views and interests for each product/course type. This made my matrix very sparse. Cosine similarity works better than 
Traditional Euclidean Distance, for high dimensionality data such as data that is sparse. I chose then to get the average of the 3 different implicit rating matrixes.

*User Course Views Matrix:* Composite Key of Course Tags(Obtained through a join to Course Tags Table) and Level,  Rating matrix for each user is a mean of view_time_in_seconds for each course tag-level. 

*User Scores Matrix:* Rating Matrix for each user is mean of assessment score for each course tag.

*User Interest Matrix:* Rating Matrix for each user with count of interests by course tag.

*Rating Matrix:* 

Average of : *User Scores Matrix:* + *User Interest Matrix:* + *Rating Matrix:* not including when it is NAN/0

Opportunities for Improvement: 
    1. Normalizing/Standardizing the User Scores Matrix mean of scores and User Course Views.
    Due to Normal Distribution (in Exercise Description, this did not concern me initially)

    2. Use of Date to track users over time 

**2. To scale this application, what accommodations would I make?**

    1. Matrix is very sparse, I would consider using sparse matrix objects which require less memory.
    
    2. Furthermore, I consider using a distributed computing system to regenerate the rating matrix when needed. I suggest using Pyspark in a Hadoop ecosystem.

    3. Consider PCA to reduce dimensions, without loss of information

    4. Consider a Model based approach over a memory based approach for similar users.

**3. Other data I would need, given the context that this API would be use to help recommend courses or course tags to similar users?**

    1. Further Data: Explicit rating of courses by users

    2. New Courses in PluralSight with similar course tags, to build a product:user recommendation(Content filtering)

    3. User charactertics: Job title, experience, location etc.

 


