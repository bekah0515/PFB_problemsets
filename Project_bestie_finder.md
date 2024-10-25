{\rtf1\ansi\ansicpg1252\cocoartf2818
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fswiss\fcharset0 ArialMT;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww26400\viewh18000\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs36 \cf0 Project Bestie Finder :){\field{\*\fldinst{HYPERLINK "https://emojis.wiki/best-friend/"}}{\fldrslt 
\f1\fs44 \cb2 \expnd0\expndtw0\kerning0
\ul \outl0\strokewidth0 \strokec3 \uc0\u55357 \u56431 \u8205 \u9792 \u65039 }}\
Proposed by: Bekah and Lola\
\
Problem:  According to a study by Aalto University in Finland and the University of Oxford in England, your social circle shrinks by 30% soon after your mid-20s. It\'92s hard to make good friends when you\'92re chasing after your dream career and stuck in a routine. This will be a great way to find a potential compatible, long-lasting friendship, aka a bestie!\
Disclaimer: this is purely for fun, no undue meaning should be attached to its results. \
\
1. Input platform - design an interface where users answer series of personality-defining questions as well as qualities they look for in their bestie. The answers will be multiple choice. Depending on the answers, we will match user with another user with compatible/desired attributes! \
	- Questions will include: personality questions about the user and questions about characteristics they want in a bestie. \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 	- Questions will probe the following attributes: \
		- extroverted vs introverted\
		- love language (5 different)\
		- activities (e.g. arts or sports)\
		- leader vs follower \
		- early bird vs night owl \
		- zodiac signs (refer to zodiac compatibility)\
Programming concepts: input function, loops, redirecting output\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \
2. Store input \
	- The inputted answers will be weighted as a percentage and matched to a personality trait. \
		- e.g. if 7 out of 10 answers point to extrovert, we would add 0.70 extrovert as a label for this person\
	- Assign a code for each person with their attributes so that matching will be easier.  \
		- e.g. 0.7E\
	- Store the answers on characteristics they want in a bestie \'97 and assign another code\
		- e.g. if this person prefer an introvert, assign an \'91I\'92\
Programming concepts: dictionaries, lists \
\
3. Match with their bestie\
	- Using their bestie preference, match user with a bestie with the most similar/complementary answer\
Programming concepts: regular expressions, for loops, if loops, all the loops\
\
4. Output to screen:\
	- \'93birds of a feather\'94 : Report match that fits the best with their desired characteristics\
	- \'93opposites attract\'94 : Report the match that are most dissimilar with their desired characteristics\
	- Report % compatibility (how many of the character codes of their bestie match with what they want)\
Programming concepts: print, math, graphics \
\
Potential challenges: not large enough of a dataset to make a match for everyone; calculating % compatibility will need to be sorted out \
\
\
}