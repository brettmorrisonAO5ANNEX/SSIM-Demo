from classes.image import Image
from classes.ssim import SSIM

if __name__ == "__main__":
    #define input signals (i.e. the images to compare)
    ground_truth = Image("images/willy_ground_truth.png")
    regenerated = Image("images/willy_pixelated.png")

    #save windows (not necessary but helps with visualizing regions being compared)
    ground_truth.save_windows("ground_truth")
    regenerated.save_windows("regenerated")

    #define and calculate MSSIM
    ssim = SSIM()
    ssim.MSSIM(ground_truth, regenerated)

    #display results
    print("")
    print(f"MSSIM: {ssim.mssim_val}")
    print("")
    print("SSIM map:")
    print(" ----------------------------------------")
    print(f"|{ssim.ssim_map[0,0]} | {ssim.ssim_map[0,1]}|")
    print(" ----------------------------------------")
    print(f"|{ssim.ssim_map[1,0]} | {ssim.ssim_map[1,1]}|")
    print("-----------------------------------------")