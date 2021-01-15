# ACM Research Coding Challenge (Spring 2021)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge-S21`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uqAJNXUe).

## Question One

Genome analysis is the identification of genomic features such as gene expression or DNA sequences in an individual's genetic makeup. A genbank file (.gb) format contains information about an individual's DNA sequence. The following dataset in `Genome.gb` contains a complete genome sequence of Tomato Curly Stunt Virus. 

**With this file, create a circular genome map and output it as a JPG/PNG/JPEG format.** We're not looking for any complex maps, just be sure to highlight the features and their labels.

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

##Important
Map.py is the main file, parse.py holds helper functions to parse the Genbank file

Also, green clockwise arrows represent genes on the main strand, read normally, while
read counter-clockwise arrows represent genes on the complementary strand, read in
'reverse'

##Libraries used
Biopython
matplotlib

##References
https://gist.github.com/peterk87/5422267

Used for reference on how to parse genbank file using biopython

https://stackoverflow.com/questions/62706502/circular-visualization-in-python-with-piled-ranges

Answer by Asmus used as reference for how to create the offset with stacked genes

##How I got my solution
When first looking at the problem, I had to deal with the initial obstacle of trying to figure out what a circular genome map was.
Surprisingly, this proved more difficult than the code itself as sifting through documentation on what _specifically_ a circular genome map must include was a lot harder than I initially anticipated.
Once I found adequate information on what a circular genome map generally included (and also cross-examined it with the information given in
the genbank file given to us) I started to get the picture forming in my head of what I wanted my end product to be.

Now came the coding itself. Immediately after figuring out what I wanted the circular genome map to look like
I sought out documentation on any libraries that might help me. In this search I also decided to stick with Python
for this project, especially since I didn't have too much experience with Python prior to this (aside from a primitive
discord bot), and I felt that this was a good chance to get knees-deep with the programming language.
It turned out to be a good choice as I found 2 libraries that would help me with this project;
Biopython to parse the genbank file and matplotlib to plot the genome itself. Afterwards, all that 
was left to be done was to look up documentation and references to figure out how to use the 2 libraries.
The primary difficulty in that particular section was getting the gene lines to automatically offset
if there was any overlap in location (for easier visibility).