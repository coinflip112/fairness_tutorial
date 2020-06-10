# A brief introduction to ML Fairness

## Presentation Section 
- What is ML Fairness 

- Why should we care?
	- Ethics (going to touch with great care, had this conversation waaay to many times and often turns very personal and political, better suited for a after hours talk, preferably with drinks)
	- Business impact with real world examples of large company fuck-ups
		- Amazon Hiring
		- Google Photos Object Detection 
		- Apple Card Gender Discrimination 
		- Less self-evident potential issues 

- How do we measure fairness?
	- Basic Metrics, how they simplify to 3 basic criteria
		- Independence 
		- Separation
		- Sufficiency 
	- Show impossibility for optimizing multiple metrics at the same time 
	- Sufficency <=> calibration (mention Logistic Regression)
	- How to choose metrics

- How do we make a model fair? 
	- Describe approaches (advantages/disadvantages)
		- Preprocessing 
		- Inprocessing
		- Postprocessing

## Case Study Section 
	
- Discrimination Mitigation

	- Simple problem, where interpretation is intuitive (Binary Classification)
	- Choose a fairness metric and explain why it's a good choice 
	- Choose a discrimination mitigation method 
		- Likely inprocessing, because there's the most research/are most interesting. 
		- Might fallback to post processing, if there's a lack of time. It's simple and model & task agnostic

	- TODO: decide on dataset and model 
		- Option A (Datasentics dataset)
			- should be binary classification (much easier to explain) 
			- dataset should include socio-demo features, ideally something that can obviously be considered a sensitive attribute (sex,race,sexual orientation,age).
			- If those are not avaialble location data should be good enough but will be harder to demonstrate
		
		- Option B (Toy dataset from papers/kaggle)
			- I already have the code from my experiments
			- Guaranteed that the methods work on the particular dataset
			- Much easier
			- Less interesting


## Available Fairness Tools (With demos)

- Fairness Ops
	- [Google fairness indicators](https://blog.tensorflow.org/2019/12/fairness-indicators-fair-ML-systems.html)
	- [Google ML fairness gym](https://github.com/google/ml-fairness-gym)
	- Other methods
- Discrimination Mitigation Algos Implementation
	- [IBM AI Fariness 360](https://github.com/IBM/AIF360/)
	- [FairLearn](https://github.com/fairlearn/fairlearn)
	- [Themis-Ml](https://github.com/cosmicBboy/themis-ml)

## Learning Resources 

- [Best incomplete book out there](https://fairmlbook.org)
	- Going to be the Deep Learning Book by Bengio et al. of the ML fairness world 
- [ACM Conference on Fairness, Accountability, and Transparency](https://facctconference.org/index.html)
	- Replaced [Fairness, Accountability, and Transparency in Machine Learning](https://www.fatml.org/) which was held in (2014-2018) 
	- It's not NeurIPS, but it's getting bigger every year. Decent cooperation with industry. Microsoft especially has a good research team 
- Bunch of random papers i can recommend. I have a reading list. Includes critics of the field such as Zachary Lipton (who does fairness research too btw)

## Summary and Larger points 

- Considering fairness in machine learning is not a checkbox like thing. Change up algo and move on approach is dangerous
- Inherent tradeof with model performance