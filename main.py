from classes.image import Image
from classes.ssim import SSIM

if __name__ == "__main__":
    #define input signals (i.e. the images to compare)
    ground_truth = Image("images/test.png")
    regenerated = Image("images/test.png")

    #define and calculate MSSIM
    ssim = SSIM()
    ssim.MSSIM(ground_truth, regenerated)

    #display results
    print(f"MSSIM: {ssim.mssim_val}")
    print(f"SSIM map: {ssim.ssim_map}")