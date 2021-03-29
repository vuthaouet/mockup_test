from mockup_generator import Mockup3DGenerator
BACKROUND_DATA = {
    "Hoodie": "./sample_data/artworks/test.jpg",
}
ARTWORK_DATA = {
    "Front":"./sample_data/artworks/red.png",
    "Back":"./sample_data/artworks/red.png",
    "Sleeve":"./sample_data/artworks/red.png",
    "Hood":"./sample_data/artworks/red.png",
    "Mug":"./sample_data/artworks/red.png",
}

MOCKUP_DATA = [
        {
        "side_name": "Mug",
        "parts": [
            {
                "name": "",
                "cut_image_path": "./sample_data/mask_part/Mug/background_default.png",
            },
                {
                "name": "",
                "cut_image_path": "./sample_data/mask_part/Mug/default1.png",
            },
            {
                "name": "",
                "model_path": "./sample_data//models/mug1.model.npy",
                "cut_image_path": "./sample_data/mask_part/Mug/mug.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Mug"
            },
            {
                "name": "",
                "cut_image_path": "./sample_data/mask_part/Mug/fx.png",
            }
     ]},
    {
        "side_name": "BackTshirt1",
        "parts": [
            {
                "name": "",
                "cut_image_path": "./sample_data/mask_part/Tshirt/background_default.png",
            },
            {
                "name": "back.Back",
                "model_path": "./sample_data//models/Tshirt/tshirt.back.model.npy",
                "cut_image_path": "./sample_data/mask_part/Tshirt/back.Back.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Back"
            },

            {
                "name": "back.left_sleeve",
                "model_path": "./sample_data//models/Tshirt/tshirt.back.left_sleeve.model.npy",
                "cut_image_path": "./sample_data/mask_part/Tshirt/back.LeftSleeve.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Sleeve"
            },
            {
                "name": "back.right_sleeve",
                "model_path": "./sample_data//models/Tshirt/tshirt.back.right_sleeve.model.npy",
                "cut_image_path": "./sample_data/mask_part/Tshirt/back.RightSleeve.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Sleeve"
            },
            {
                "name": "back.neck",
                "model_path": "./sample_data//models/Tshirt/tshirt.back.back_neck.model.npy",
                "cut_image_path": "./sample_data/mask_part/Tshirt/back.Neck.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Front"
            },
            {
                "name": "",
                "cut_image_path": "./sample_data/mask_part/Tshirt/back.Back.png",
            },
]}
]



if __name__ == "__main__":
    mockup = Mockup3DGenerator(mockup_data=MOCKUP_DATA, artwork_data=ARTWORK_DATA, background_data = BACKROUND_DATA)
    print("----- STARTING -----")
    mockup.do_generate()
    print("----- DONE -----")
