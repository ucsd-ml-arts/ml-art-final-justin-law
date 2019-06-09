# Final Project

Justin Law, jklaw@ucsd.edu

(Your teammates' contact info, if appropriate)

## Abstract Proposal

FIRST STEP: Write up a description (in the form of an abstract) of what you will revisit for your final project. This should be one paragraph clearly describing your concept and approach. What are your desired creative goals? How are you expanding on something we covered in the class? How will you present your work next Wednesday in the final project presentations? 

** Answer **
Expanding on the previous project, I trained 5 different cycleGAN networks of subsets of the william blake images curated from before. The results from project 4 were interesting, but they can be improved upon by adjusting model hyperparamters and the number of hidden layers. The end goal is to take an input image and stylize it to william blake, but this will be achieved through various methods: run through multiple subsets, one subset. The 5 different cycleGANs will be trained on subsets of the paintings dataset (for example, boats) as well as one or more closely related (in style) William Blake paintings/water color/sketches. The final project results will be presented as a dozen or so select images generated from the 5 cycleGANs with input images as famous paintings or interesting images.

## Project Report

Upload your project report (4 pages) as a pdf with your repository, following this template: [google docs](https://docs.google.com/document/d/133H59WZBmH6MlAgFSskFLMQITeIC5d9b2iuzsOfa4E8/edit?usp=sharing).

## Model/Data

Briefly describe the files that are included with your repository:
- The trained models are in the .h5 files linked under technical results. But for a faster way to reproduce the results, see **Code**
second bullet point.
- training data:
    - dataset_paintings/paintings/boat is used for color1,color2,color3. dataset_paintings/paintings/chair is used for sketch.
    - dataset_paintings/paintings/* (every painting) is used for all.

## Code

Your code for generating your project:
- Jupyter notebooks: generate/all/generate.iypnb,generate/all/generate.iypnb,generate/all/generate.iypnb,generate/all/generate.iypnb
- In order to generate the results for the project, download this: https://drive.google.com/open?id=1O1pJXAZfTxH-lhxOKC3MaK5FBlcVnacD
and apply gunzip -> tar -xf on a linux machine. This will give the generate folder with the appropriate .h5 files. Extract to where
this github repo was cloned.
- Alternatively, download the models individually and copy the .h5 files into the respective generate/... folder where ... is [all,color1,color2,color3,sketch].

## Results

- in sample-results/ there are the .jpg I use in the final project report. See the ipynb notebooks in this repository and shift+right click on windows to save some of the results.

## Technical Notes

The trained models, along with their python notebook, are provided in the links below because of the large file size. The format is h5 for the weights and json for the network architecture. Each are about 500 MB each and are compressed into tar files.

- sketch/
	- link: https://drive.google.com/open?id=11b2jrL4G2XR5vf_ofU6QDhUuxptBTXgn
- color1/
	- link: https://drive.google.com/open?id=1YE3Uc8rodGqkXm_OdbbWJJxzfPC9bWIl
- color2/
	- link: https://drive.google.com/open?id=1SIA0ueT0fpuFcdLdEet-8ha4faWnPKll
- color3/
	- link: https://drive.google.com/open?id=1jRuSR5inMe2BaTR0iUQ0Hx0gj3Um3KBM
- all/
	- link: https://drive.google.com/open?id=1Hx_G6ovZDy-xAaPMfDXmDGUVu07lQDGF
## Reference

References to any papers, techniques, repositories you used:
- https://github.com/roberttwomey/ml-art-code/blob/master/week8/CycleGan/CycleGAN-keras.ipynb / https://github.com/tjwei/GANotebooks
- pix2pix paper: https://arxiv.org/abs/1611.07004v3
- cycleGAN paper: https://arxiv.org/abs/1703.10593v6