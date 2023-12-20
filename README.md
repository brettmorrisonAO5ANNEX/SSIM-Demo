# SSIM-Demo
![overview](https://github.com/brettmorrisonAO5ANNEX/SSIM-Demo/assets/49254129/018cdc35-17fc-4eee-adbf-365c9316a2ff)
## Source
https://ece.uwaterloo.ca/~z70wang/publications/ssim.pdf
## Overview
Structural Similarity Index (SSIM) is an objective image quality metric that is used for measuring the quality of an image that has undergone some reconstruction process. SSIM is known as a ‘full-reference’ metric because it is designed around the assumption that a high-resolution version of the image is available and can be used for comparison. A quality measurement is produced by comparing luminance, contrast, and structural components of different regions of the input images. Measuring quality in small regions of the inputs can provide insight into which regions are more ‘perceptually convincing’ than others. For the purposes of this demo, I’ll call this an SSIM map. A more whole measure of quality can be found by averaging the SSIM values for all regions analyzed; this is called mean SSIM (MSSIM) and is typically used for applications like super-resolution, where an ML model must learn by minimizing a single loss function.

Compared with other objective quality metrics, like mean squared error (MSE) and peak signal-to-noise ratio (PSNR), which mainly focus on pixel-wise intensity differences, SSIM can be a more well-rounded metric. This is because it takes structural information about the images into account, which is very important for how we perceive scenes in real life. 

## Math

