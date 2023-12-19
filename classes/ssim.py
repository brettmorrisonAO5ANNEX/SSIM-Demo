from classes.image import Image
import numpy as np

class SSIM:
    # constructor
    def __init__(self, alpha=1, beta=1, gamma=1, K1=0.01, K2=0.03):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

        # since demo is for RGB images, L = 255
        self.C1 = (K1 * 255) ** 2
        self.C2 = (K2 * 255) ** 2
        self.C3 = self.C2 / 2

        self.ssim_map = np.zeros((2,2))

    # designed for images split into 4 windows
    def MSSIM(self, gt_hr, regen_hr):
        ssim_sum = 0.0

        # compute SSIM for each window of the input signals
        for i in range(4):
            window_SSIM = self.SSIM(gt_hr.windows[i], regen_hr.windows[i])
            ssim_sum += window_SSIM

            #fetching indeces of the SSIM map 
            map_y = 1 if i > 1 else 0
            map_x = 1 if i % 2 != 0 else 0

            self.ssim_map[map_y, map_x] = window_SSIM

        self.mssim_val = (ssim_sum / 4)

    def SSIM(self, gt_window, regen_window):
        ssim_sum = 0.0

        # calculate per channel average SSIM
        for i in range(3):
            ssim_sum += self.per_channel_SSIM(gt_window[:, :, i], regen_window[:, :, i])

        return ssim_sum / 3

    def per_channel_SSIM(self, gt_window_channel, regen_window_channel):
        luminance_comp = self.l(gt_window_channel, regen_window_channel)
        contrast_comp = self.c(gt_window_channel, regen_window_channel)
        structural_comp = self.s(gt_window_channel, regen_window_channel)

        return (luminance_comp ** self.alpha) * (contrast_comp ** self.beta) * (structural_comp ** self.gamma)

    def c(self, gt_window_channel, regen_window_channel):
        mu_x = np.mean(gt_window_channel)
        mu_y = np.mean(regen_window_channel)

        return (2*mu_x*mu_y + self.C1)/(mu_x**2 + mu_y**2 + self.C1)

    def l(self, gt_window_channel, regen_window_channel):
        sigma_x = np.std(gt_window_channel)
        sigma_y = np.std(regen_window_channel)

        return (2*sigma_x*sigma_y + self.C2)/(sigma_x**2 + sigma_y**2 + self.C2)

    def s(self, gt_window_channel, regen_window_channel):
        sigma_x = np.std(gt_window_channel)
        sigma_y = np.std(regen_window_channel)
        sigma_xy = np.cov(gt_window_channel, regen_window_channel)

        return (sigma_xy + self.C3)/(sigma_x*sigma_y + self.C3)
