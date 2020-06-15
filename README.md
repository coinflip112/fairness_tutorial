# A brief introduction to ML Fairness

## Presentation Section 
- What is ML Fairness 

- Why should we care?
	- Business impact
		- Amazon Hiring
		- Google Photos Object Detection 
		- Apple Card Gender Discrimination

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

## Available Fairness Tools

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