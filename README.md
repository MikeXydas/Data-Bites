# Weekend EDAs

Having spent some time learning about the general field of Data Science (including but not limited to ML,
 hypothesis testing, data cleaning and extraction) I have decided to get my hands dirty 
 with some subjectively fun projects.
 
 My hands-on experience until now with data science is from assignments from my university, MOOCs
 and my current thesis in [Molecular Dynamics](https://en.wikipedia.org/wiki/Molecular_dynamics).
 Although my thesis is interesting I was getting way too specialized tasks and knowledge and felt like
 doing something more general. So I am spending some time some days (not necessarily weekends but it makes for
  a good title) on random topics that I consider that I could extract nice insights, visualizations, etc.  
  
  
  ## PCA on Fire Images :fire:
  [Jupyter Notebook](https://github.com/MikeXydas/Weekend-EDAs/blob/master/PCA_On_Fire_Images.ipynb)  
    
  A friend of mine is having his thesis on fire recognition on images. Also, I have used
  PCA on many tasks of dimensionality reduction or, in general, study about the meaning of
  eigenvectors of the covariance matrix of a dataset.
      
  So combining the above I thought of using **PCA as a technique of noise reduction** on these fire images.
    
  You can download and play with the notebook. The dataset that I used is not available but **any image dataset
  can be used**.  
  **Tip:** For a greater understanding of the notebook I suggest printing the `.shape` of the arrays
  
  
  ## Covid-19 - Importance of testing
  [Jupyter Notebook](https://github.com/MikeXydas/Weekend-EDAs/blob/master/Covid19_Testing_Importance.ipynb)  
    
  In the field of software development, one thing that makes everyone happy is finding security vulnerabilities.
  You cannot expect to have the perfect code that is fully robust and secure forever. New vulnerabilities are created 
  and the testing must be constant. As this [GitHub post](https://github.blog/2019-11-14-announcing-github-security-lab-securing-the-worlds-code-together/) says 
  >Today the process for addressing a new vulnerability is often ad hoc. 
  >Forty percent of new vulnerabilities in open source don’t have a CVE 
  >identifier when they’re announced, meaning they’re not included in any 
  >public database. Seventy percent of critical vulnerabilities remain unpatched 
  >30 days after developers have been notified.

Covid-19 is something much more than a security vulnerability. However, I will attempt to show
that some principles apply in this case too. We will attempt to show if the number of tests correlates
with how well the country manages to deal with the virus. 

## Covid -19 - Polynomial Fitting

My thesis professor is giving a Machine Learning class on his MSc students in the field of bioinformatics. Their first assignment is to gather data and forecast the future number of deaths and cases using [polynomial regression](https://en.wikipedia.org/wiki/Polynomial_regression). The main focus is to find the least complex model that fits our data using [Occam's razor](https://en.wikipedia.org/wiki/Occam%27s_razor) or as Einstein said
>“Everything should be **made** as **simple** as possible, but no simpler.”

A simple polynomial regression will not be the perfect model since it won't be able to capture events like lockdowns but the simplicity allows us of more interpretable results which I am aiming to explore.
   
