# Weekend EDAs
 
 My hands-on experience until now with data science is from assignments from my university, MOOCs
 and my thesis in [Molecular Dynamics](https://en.wikipedia.org/wiki/Molecular_dynamics).
 Although my thesis is interesting I was getting way too specialized tasks and knowledge and felt like
 doing something more general. So I am spending some time some days (not necessarily weekends, but it makes for
  a good title) on random topics that I consider that I could extract nice insights, visualizations and in general 
 have fun.  
  
  
  ## PageRank from Scratch  
 [Nb Viewer](https://nbviewer.jupyter.org/github/MikeXydas/Weekend-EDAs/blob/master/PageRank_from_Scratch.ipynb)  
 *Tags: PageRank, graph node importance*

PageRank is a well-known algorithm proposed by the founders of Google and had a major role at its success when it first
started as a search engine. In general, PageRank aims at finding the most important nodes on a huge graph of webpages.
In order to understand its inner workings I implemented it from scratch using `numpy` only. I start by assuming a perfect
graph (no spider traps, no dead-ends) and gradually lift these assumptions. Finally, I examine the memory complexity 
and present the final algorithm which could work on any graph regardless of its shape and size.


 ## Gaussian Processes and DnD  
 [Nb Viewer](https://nbviewer.jupyter.org/github/MikeXydas/Weekend-EDAs/blob/master/Gaussian_Processes_and_DnD.ipynb)  
 *Tags: Gaussian processes, regression, pymc3*

Recently, I started learning about Gaussian processes (GPs). Gaussian processes is a flexible tool
that can model many problems that we deal with in the field of Data Science. In this notebook, I showcase a small part
of that flexibility dealing with a simple regression problem, predicting challenge rating of dnd monsters given their
health points. I start by fitting a polynomial model using MCMC which I compare with the least squares fit. Then, I use 
a gaussian process to solve this regression problem and present its advantages over the two methods above.



  ## Covid-19 - Importance of testing
  [Nb Viewer](https://nbviewer.jupyter.org/github/MikeXydas/Weekend-EDAs/blob/master/Covid19_Testing_Importance.ipynb)    
  *Tags: data gathering, visualization*  
    
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

## Covid -19 - Time Series Forecasting
[Nb Viewer](https://nbviewer.jupyter.org/github/MikeXydas/Weekend-EDAs/blob/master/Covid19_Timeseries_Forecasting.ipynb)  
*Tags: timeseries analysis, polynomial regression, ARIMA*

My thesis professor is giving a Machine Learning class on his MSc students in the field of bioinformatics. 
Their first assignment is to gather data and forecast the future number of deaths and cases using [polynomial regression](https://en.wikipedia.org/wiki/Polynomial_regression). 
The main focus is to find the least complex model that fits our data using [Occam's razor](https://en.wikipedia.org/wiki/Occam%27s_razor) or as Einstein said
>“Everything should be **made** as **simple** as possible, but no simpler.”

I achieve this using the [BIC](https://en.wikipedia.org/wiki/Bayesian_information_criterion)
metric which penalties higher complexity models (higher degree polynomials).  

I then proceed to evaluate other models such as [ARIMA](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average).
  
A simple time series forecasting model will not be the perfect model since it won't be able to 
capture events like lockdowns but the simplicity allows us of more interpretable results
 which I am aiming to explore.
   
 **Disclaimer**: In any way should any of the models I have written be actually used for forecasting
 of future number of cases. I have done this for educational reasons. There is the field
 of [epidemiology](https://en.wikipedia.org/wiki/Epidemiology) which one should consult for
 accurate forecasting which takes into account more factors than the shape of the current curve.

  ## PCA on Fire Images
  [Nb Viewer](https://nbviewer.jupyter.org/github/MikeXydas/Weekend-EDAs/blob/master/PCA_On_Fire_Images.ipynb)    
   *Tags: PCA, noise reduction, image processing*  
  
  A friend of mine is having his thesis on fire recognition on images. Also, I have used
  PCA on many tasks of dimensionality reduction or, in general, study about the meaning of
  eigenvectors of the covariance matrix of a dataset.
      
  So combining the above I thought of using **PCA as a technique of noise reduction** on these fire images.
    
  You can download and play with the notebook. The dataset that I used is not available but **any image dataset
  can be used**.  
  **Tip:** For a greater understanding of the notebook I suggest printing the `.shape` of the arrays
  

