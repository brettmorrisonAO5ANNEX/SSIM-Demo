# SSIM-Demo
This is a 'simple' implementation of SSIM using Python. It has many limitations: hard-coded 4 window split, assumes input images are the same size, designed for RGB color space... It works for the demo though! When run, the main function will output both an MSSIM value and an SSIM map in the form of a 2x2 matrix (read below for more info on these).

## Demo Diagram
![overview](https://github.com/brettmorrisonAO5ANNEX/SSIM-Demo/assets/49254129/018cdc35-17fc-4eee-adbf-365c9316a2ff)
## Paper 
https://ece.uwaterloo.ca/~z70wang/publications/ssim.pdf

NOTE: I got all the conceptual knowledge from the paper, but all code is my own. I'm sure there's a more efficient and generalizable approach out there, but this was made as a demo for a larger project on super-resolution!

## Overview
Structural Similarity Index (SSIM) is an objective image quality metric that is used for measuring the quality of an image that has undergone some reconstruction process. SSIM is known as a ‘full-reference’ metric because it is designed around the assumption that a high-resolution version of the image is available and can be used for comparison. A quality measurement is produced by comparing luminance, contrast, and structural components of different regions of the input images. Measuring quality in small regions of the inputs can provide insight into which regions are more ‘perceptually convincing’ than others. For this demo, I’ll call this an SSIM map. A more whole measure of quality can be found by averaging the SSIM values for all regions analyzed; this is called mean SSIM (MSSIM) and is typically used for applications like super-resolution, where an ML model must learn by minimizing a single loss function.

Compared with other objective quality metrics, like mean squared error (MSE) and peak signal-to-noise ratio (PSNR), which mainly focus on pixel-wise intensity differences, SSIM can be a more well-rounded metric. This is because it takes structural information about the images into account, which is very important for how we perceive scenes in real life. 

## Math
I created the following diagram using the equations discussed in the paper, hopefully, it helps with visualization a bit. Basically, SSIM is calculated by comparing measures of luminance, contrast, and structure (based on local image statistics)
from the ground truth and regenerated image...

![Course Layout](https://github.com/brettmorrisonAO5ANNEX/SSIM-Demo/assets/49254129/4d906492-9015-488a-a8b8-eb544f0a4cf0)

## Example

When run on the following images: ground truth (left) and 'regenerated' (right)

<img src="https://github.com/brettmorrisonAO5ANNEX/SSIM-Demo/assets/49254129/8a03936d-7172-4262-bec8-1fca9348bb38" alt="willy_gt" width="25%" height="25%">
<img src="https://github.com/brettmorrisonAO5ANNEX/SSIM-Demo/assets/49254129/4b7e5c06-646c-42b8-93ea-b6a0da34bee8" alt="willy_r" width="25%" height="25%">

we get the following output:

![Screenshot 2023-12-19 at 10 10 58 PM](https://github.com/brettmorrisonAO5ANNEX/SSIM-Demo/assets/49254129/26f3c7ef-7939-46d5-b513-46c14f8bf003)
