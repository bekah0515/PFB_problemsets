# 👯‍♀️ Project Bestie Finder 👯‍♀️
**Proposed by: Bekah and Lola**

**Problem:** According to a study by Aalto University in Finland and the University of Oxford in England, your social circle shrinks by 30% soon after your mid-20s. It’s hard to make good friends when you’re chasing after your dream career and stuck in a routine. This will be a great way to find a potential compatible, long-lasting friendship, aka a **_bestie_**!

_Disclaimer: this is purely for fun, no undue meaning should be attached to its results._

**1. Input platform** - design an interface where users answer series of personality-defining questions as well as qualities they look for in their bestie. The answers will be multiple choice. Depending on the answers, we will match user with another user with compatible/desired attributes! 
- Questions will include: personality questions about the user and questions about characteristics they want in a bestie. 
- Questions will probe the following attributes: 
    - extroverted vs introverted
    - love language (5 different)
    - activities (e.g. arts or sports)
    - leader vs follower 
    - early bird vs night owl 
    - zodiac signs (refer to zodiac compatibility)

    _Programming concepts: input function, loops, redirecting output_


**2. Store input**
- The inputted answers will be weighted as a percentage and matched to a personality trait. 
	- e.g. if 7 out of 10 answers point to extrovert, we would add 0.70 extrovert as a label for this person
	
- Assign a code for each person with their attributes so that matching will be easier.  
	- e.g. 0.7E
	
- Store the answers on characteristics they want in a bestie — and assign another code
	- e.g. if this person prefer an introvert, assign an ‘I’
	
  _Programming concepts: dictionaries, lists_

**3. Match with your bestie**

- Using their bestie preference, match user with a bestie with the most similar/complementary answer

    _Programming concepts: regular expressions, for loops, if loops, all the loops_



**4. Output to screen:**
- “birds of a feather” : Report match that fits the best with their desired characteristics
- “opposites attract” : Report the match that are most dissimilar with their desired characteristics
- Report % compatibility (how many of the character codes of their bestie match with what they want)
_Programming concepts: print, math, graphics_ 

**Potential challenges:** not large enough of a dataset to make a match for everyone; calculating % compatibility will need to be sorted out 