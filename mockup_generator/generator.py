import os
import time

import cv2
import numpy as np
from PIL import Image, ImageChops

from warp_image import thinplate as tps, contants


class Mockup3DGenerator:
    def __init__(self, mockup_data, artwork_data, background_data,colors="#333333"):
        self.mockup_data = mockup_data
        self.artwork_data = artwork_data
        self.background_data = background_data
        self.colors = colors

    def do_generate(self):
        for side in self.mockup_data:
            start = time.time()
            main_side_image = Image.new("RGBA", (1000, 1000), (255, 255, 255))
            for part in side['parts']:
                if "model_path" not in part:
                    print('{} doesn’t have model'.format(part.get("name")))
                    image = Image.open(part['cut_image_path']).convert("RGBA")
                    main_side_image = Image.alpha_composite(main_side_image, image).convert("RGBA")
                else:
                    print('{} has  model'.format(part.get("name")))
                    artwork_image = Image.open(self.artwork_data[part['artwork_side']]).convert("RGBA")
                    artwork_image = np.array(artwork_image)
                    open_cv_artwork_image = cv2.cvtColor(artwork_image, cv2.COLOR_RGB2BGR)

                    # warp_artwork_image_name = "{}{}{}".format(prefix_name, SPLIT_CHAR, part.get("name"))
                    # print("Doing warp...")
                    resized_img = cv2.resize(open_cv_artwork_image, contants.shape)

                    if os.path.isfile(part['model_path']):

                        grid = np.load(part['model_path'], allow_pickle=True)

                        mapx, mapy = tps.tps_grid_to_remap(grid, contants.shape)
                        img = cv2.remap(resized_img, mapx, mapy, cv2.INTER_CUBIC)
                        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
                        warped = Image.fromarray(img).convert("RGBA")
                        # warped = warped.resize(warped.size, Image.ANTIALIAS)
                        # warped.save("warp."+ part['name'] +".png")
                        cut_image = Image.open(part['cut_image_path']).convert("RGBA")
                        # cut_image = cut_image.resize(cut_image.size, Image.ANTIALIAS)
                        # if (part['name'] == "front.Back"):
                        #     warped.putalpha(128)
                        # out = Image.composite(cut_image, warped, cut_image)

                        # background_image = Image.new("RGBA", (1000, 1000), (255, 255, 255))
                        main_side_image = Image.composite(warped, main_side_image, cut_image)
                        # out = out.convert('RGB')


                        # main_side_image = ImageChops.darker(out, main_side_image)
                        # main_side_image = main_side_image.resize(main_side_image.size, Image.ANTIALIAS)


                    else:
                        print("Model for {} not found".format(side['side_name'] + " | " + part['name']))
            # img_shadow = Image.open(side['shadow_image']).convert("RGBA")
            # main_side_image = Image.alpha_composite(main_side_image.convert("RGBA"), img_shadow)
            main_side_image = main_side_image.resize((3000,3000), Image.ANTIALIAS)
            end = time.time()
            print('[{:.4f} s] Generate mockup for {} executed'.format((end - start), side['side_name']))
            # if side['background']:
            #     background_image = Image.open(self.background_data[side['background']]).resize(contants.shape).convert("RGBA")
            #     mask_image = Image.open(side['mask']).convert("RGBA")
            #     main_side_image = Image.composite(main_side_image,background_image, mask_image)
            # else:
            #     print("Background {} not found".format(side['side_name']))
            main_side_image.resize(contants.shape)
            main_side_image.save(side['side_name'] +".png")
            main_side_image.show()
    def do_generate2(self):
        for side in self.mockup_data:
            start = time.time()
            main_side_image = Image.new("RGBA", (1000, 1000), (255, 255, 255))
            for part in side['parts']:

                artwork_image = Image.open(self.artwork_data[part['artwork_side']]).convert("RGBA")
                artwork_image = np.array(artwork_image)
                open_cv_artwork_image = cv2.cvtColor(artwork_image, cv2.COLOR_RGB2BGR)

                # warp_artwork_image_name = "{}{}{}".format(prefix_name, SPLIT_CHAR, part.get("name"))
                # print("Doing warp...")
                resized_img = cv2.resize(open_cv_artwork_image, contants.shape)

                if os.path.isfile(part['model_path']):

                    grid = np.load(part['model_path'], allow_pickle=True)

                    mapx, mapy = tps.tps_grid_to_remap(grid, contants.shape)
                    img = cv2.remap(resized_img, mapx, mapy, cv2.INTER_CUBIC)
                    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
                    warped = Image.fromarray(img).convert("RGBA")
                    # warped = warped.resize(warped.size, Image.ANTIALIAS)
                    # warped.save("warp."+ part['name'] +".png")
                    cut_image = Image.open(part['cut_image_path']).convert("RGBA")
                    # cut_image = cut_image.resize(cut_image.size, Image.ANTIALIAS)
                    # if (part['name'] == "front.Back"):
                    #     warped.putalpha(128)
                    out = Image.composite(cut_image, warped, cut_image)

                    # background_image = Image.new("RGBA", (1000, 1000), (255, 255, 255))
                    # main_side_image = Image.composite(warped, main_side_image, cut_image)
                    # out = out.convert('RGB')


                    main_side_image = ImageChops.darker(out, main_side_image)
                    # main_side_image = main_side_image.resize(main_side_image.size, Image.ANTIALIAS)


                else:
                    print("Model for {} not found".format(side['side_name'] + " | " + part['name']))
            # img_shadow = Image.open(side['shadow_image']).convert("RGBA")
            # main_side_image = Image.alpha_composite(main_side_image.convert("RGBA"), img_shadow)
            # main_side_image = main_side_image.resize((3000,3000), Image.ANTIALIAS)
            end = time.time()
            print('[{:.4f} s] Generate mockup for {} executed'.format((end - start), side['side_name']))
            # if side['background']:
            #     background_image = Image.open(self.background_data[side['background']]).resize(contants.shape).convert("RGBA")
            #     mask_image = Image.open(side['mask']).convert("RGBA")
            #     main_side_image = Image.composite(main_side_image,background_image, mask_image)
            # else:
            #     print("Background {} not found".format(side['side_name']))
            main_side_image.resize(contants.shape)
            main_side_image.save(side['side_name'] +".png")
            main_side_image.show()
    def do_generate3(self):
        for side in self.mockup_data:
            start = time.time()
            main_side_image = Image.new("RGBA", (1000, 1000), (255, 255, 255))
            for part in side['parts']:
                if "model_path" not in part:
                    print('{} doesn’t have model'.format(part.get("name")))
                    image = Image.open(part['cut_image_path']).convert("RGBA")
                    main_side_image = Image.alpha_composite(main_side_image, image).convert("RGBA")
                else:
                    print('{} has  model'.format(part.get("name")))
                    artwork_image = Image.open(self.artwork_data[part['artwork_side']]).convert("RGBA")
                    background_image = Image.new("RGBA", (3000, 1887), (255, 255, 255))
                    background_image.save("mugtestvt1.png")
                    artwork_image.show()
                    background_image.paste(artwork_image, None, artwork_image)
                    artwork_image = background_image
                    artwork_image.save("mugtestvt.png")
                    artwork_image.show()
                    artwork_image = np.array(artwork_image)
                    open_cv_artwork_image = cv2.cvtColor(artwork_image, cv2.COLOR_RGB2BGR)

                    # warp_artwork_image_name = "{}{}{}".format(prefix_name, SPLIT_CHAR, part.get("name"))
                    # print("Doing warp...")
                    resized_img = cv2.resize(open_cv_artwork_image, contants.shape)

                    if os.path.isfile(part['model_path']):

                        grid = np.load(part['model_path'], allow_pickle=True)

                        mapx, mapy = tps.tps_grid_to_remap(grid, contants.shape)
                        img = cv2.remap(resized_img, mapx, mapy, cv2.INTER_CUBIC)
                        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
                        warped = Image.fromarray(img).convert("RGBA")
                        # warped = warped.resize(warped.size, Image.ANTIALIAS)
                        # warped.save("warp."+ part['name'] +".png")
                        cut_image = Image.open(part['cut_image_path']).convert("RGBA")
                        # cut_image = cut_image.resize(cut_image.size, Image.ANTIALIAS)
                        # if (part['name'] == "front.Back"):
                        #     warped.putalpha(128)
                        # out = Image.composite(cut_image, warped, cut_image)

                        # background_image = Image.new("RGBA", (1000, 1000), (255, 255, 255))
                        out = Image.composite(warped, cut_image, cut_image)
                        out.show()
                        out.save("mugtest.png")
                        main_side_image.show()
                        main_side_image.paste(out, None, out)
                        # out = out.convert('RGB')


                        # main_side_image = ImageChops.darker(out, main_side_image)
                        # main_side_image = main_side_image.resize(main_side_image.size, Image.ANTIALIAS)


                    else:
                        print("Model for {} not found".format(side['side_name'] + " | " + part['name']))
            # img_shadow = Image.open(side['shadow_image']).convert("RGBA")
            # main_side_image = Image.alpha_composite(main_side_image.convert("RGBA"), img_shadow)

            main_side_image = main_side_image.resize((3000,3000), Image.ANTIALIAS)
            end = time.time()
            print('[{:.4f} s] Generate mockup for {} executed'.format((end - start), side['side_name']))
            # if side['background']:
            #     background_image = Image.open(self.background_data[side['background']]).resize(contants.shape).convert("RGBA")
            #     mask_image = Image.open(side['mask']).convert("RGBA")
            #     main_side_image = Image.composite(main_side_image,background_image, mask_image)
            # else:
            #     print("Background {} not found".format(side['side_name']))
            main_side_image.resize(contants.shape)
            main_side_image.save(side['side_name'] +".png")
            main_side_image.show()