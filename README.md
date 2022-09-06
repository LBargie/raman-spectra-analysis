# Raman spectra analysis workflow
I found some .spc files of Raman spectra in a folder from when I used to postdoc and I thought I'd see what the data looked like when I used Python to do the analysis. I do not remember what the experiment was that the spectra were collected from so it would be interesting to see how the workflow looks with some relevant data. 

The workflow consists of importing, baseline correcting, scaling and performing principal component analysis (PCA) on the Raman spectra.

There are two functions that I included: 

  1. The read_spc() function takes a .spc file and converts the data to a Pandas dataframe.
  2. The baseline_als_optimized() function performs an asymmetric least squares baseline correction of the y axis data.
  
I make no claims to fully understand how the basline correction works. I found the code for the function here:

https://stackoverflow.com/questions/29156532/python-baseline-correction-library

and you can read more again the aymmetric least squares algorithm here:

https://pubs.rsc.org/en/content/articlehtml/2015/an/c4an01061b

Click on the example_read_raman.ipynb to see the code and the outputs from the analysis.
