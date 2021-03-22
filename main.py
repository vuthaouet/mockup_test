from mockup_generator import Mockup3DGenerator
BACKROUND_DATA = {
    "Hoodie": "./sample_data/artworks/test.jpg",
}
ARTWORK_DATA = {
    "Front":"./sample_data/artworks/red.png",
    "Back":"./sample_data/artworks/red.png",
    "Sleeve":"./sample_data/artworks/red.png",
    "Hood":"./sample_data/artworks/red.png",
    "Neck":"./sample_data/artworks/red.png",
    "Black":"./sample_data/artworks/JerseyBlack.png",
    "Red":"./sample_data/artworks/red.png",
    "Green" : "./sample_data/artworks/green.png",
    "Pink":"./sample_data/artworks/pink.png",
    "Yellow" : "./sample_data/artworks/yellow.png",
    "White" : "./sample_data/artworks/white.png",
    "Test":"./sample_data/artworks/testHoodie.png",
    "Mug":"./sample_data/artworks/mugtest3.png"
}

MOCKUP_DATA = [

#      {
#         "side_name": "Mug",
#         "parts": [
#             {
#                 "name": "",
#                 "cut_image_path": "./sample_data/cut_images/Mug/background_default.png",
#             },
# {
#                 "name": "",
#                 "cut_image_path": "./sample_data/cut_images/Mug/default.png",
#             },
#             {
#                 "name": "",
#                 "model_path": "./sample_data//models/mug1.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Mug/mug.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Mug"
#             },
#             {
#                 "name": "",
#                 "cut_image_path": "./sample_data/cut_images/Mug/fx.png",
#             }
#      ]},
{
        "side_name": "Mug1",
        "parts": [
            {
                "name": "",
                "cut_image_path": "./sample_data/cut_images/Mug/background_default.png",
            },
{
                "name": "",
                "cut_image_path": "./sample_data/cut_images/Mug/default1.png",
            },
            {
                "name": "",
                "model_path": "./sample_data//models/mug1.model.npy",
                "cut_image_path": "./sample_data/cut_images/Mug/mug.png",
                "shadow_image": "",  # can be None
                "artwork_side": "Mug"
            },
            {
                "name": "",
                "cut_image_path": "./sample_data/cut_images/Mug/fx.png",
            }
     ]}
#     {
#         "side_name": "FrontJersey",
#         "background_default":"./sample_data/background_default.png",
#         "shadow_image":"./sample_data/cut_images/Jersey.front.cut/fx.png",
#         "parts": [
#             {
#                 "name": "front.front",
#                 "model_path": "./sample_data//models/Jersey.front.model/front.Front.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Jersey.front.cut/front.Front.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
#             {
#                 "name": "front.left_sleeve",
#                 "model_path": "./sample_data//models/Jersey.front.model/front.RightSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Jersey.front.cut/front.RightSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "front.right_sleeve",
#                 "model_path": "./sample_data//models/Jersey.front.model/front.LeftSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Jersey.front.cut/front.LeftSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "front.back",
#                 "model_path": "./sample_data//models/Jersey.front.model/front.Back.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Jersey.front.cut/front.Back.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Back"
#             },
#  {
#                 "name": "front.LF",
#                 "model_path": "./sample_data//models/Jersey.front.model/front.LF.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Jersey.front.cut/front.LF.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Black"
#             },
# {
#                 "name": "front.RF",
#                 "model_path": "./sample_data//models/Jersey.front.model/front.RF.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Jersey.front.cut/front.RF.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Black"
#             },
#             {
#                 "name": "front.L",
#                 "model_path": "./sample_data//models/Jersey.front.model/front.Left.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Jersey.front.cut/front.Left.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Black"
#             },
#             {
#                 "name": "front.R",
#                 "model_path": "./sample_data//models/Jersey.front.model/front.Right.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Jersey.front.cut/front.Right.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Black"
#             },
#         ]
#     },
# {
#     "side_name": "BackJersey",
#     "background_default": "./sample_data/background_default.png",
#     "shadow_image": "./sample_data/cut_images/Jersey.back.cut/fx.png",
#
#     "parts": [
#             {
#                 "name": "back.back",
#                 "model_path": "./sample_data//models/Jersey.back.model/back.Back.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Jersey.back.cut/back.Back.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Back"
#             },
#             {
#                 "name": "back.left_sleeve",
#                 "model_path": "./sample_data//models/Jersey.back.model/back.LeftSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Jersey.back.cut/back.LeftSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "back.right_sleeve",
#                 "model_path": "./sample_data//models/Jersey.back.model/back.RightSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Jersey.back.cut/back.RightSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#
#         {
#             "name": "back.BackNeck",
#             "model_path": "./sample_data//models/Jersey.back.model/back.BackNeck.model.npy",
#             "cut_image_path": "./sample_data/cut_images/Jersey.back.cut/back.BackNeck.png",
#             "shadow_image": "",  # can be None
#             "artwork_side": "Black"
#         },
#         {
#             "name": "back.L",
#             "model_path": "./sample_data//models/Jersey.back.model/back.LB.model.npy",
#             "cut_image_path": "./sample_data/cut_images/Jersey.back.cut/back.LB.png",
#             "shadow_image": "",  # can be None
#             "artwork_side": "Black"
#         },
#         {
#             "name": "back.R",
#             "model_path": "./sample_data//models/Jersey.back.model/back.RB.model.npy",
#             "cut_image_path": "./sample_data/cut_images/Jersey.back.cut/back.RB.png",
#             "shadow_image": "",  # can be None
#             "artwork_side": "Black"
#         },
#         ]
#     },

#
#     {
#         "side_name": "FrontBomber",
#         "background_default":"./sample_data/cut_images/Bomber.front/background_default.png",
#         "shadow_image":"./sample_data/cut_images/Bomber.front/front.fx.png",
#         "parts": [
#             {
#                 "name": "front.Back",
#                 "model_path": "./sample_data//models/Bomber.front.model/front.Front.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Bomber.front/front.Front.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Red"
#             },
#
#             {
#                 "name": "front.left_sleeve",
#                 "model_path": "./sample_data//models/Bomber.front.model/front.RightSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Bomber.front/front.RightSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Red"
#             },
#             {
#                 "name": "front.right_sleeve",
#                 "model_path": "./sample_data//models/Bomber.front.model/front.LeftSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Bomber.front/front.LeftSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Red"
#             },
#             {
#                 "name": "front.right_pocket",
#                 "model_path": "./sample_data//models/Bomber.front.model/front.RightPocket.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Bomber.front/front.RightPocket.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Red"
#             },
#             {
#                 "name": "front.right_pocket",
#                 "model_path": "./sample_data//models/Bomber.front.model/front.LeftPocket.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Bomber.front/front.LeftPocket.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Red"
#             },
# ]},
#
# #
#     {
#         "side_name": "BackBomber",
#         "background_default":"./sample_data/cut_images/Bomber.back.cut/back.BackgroundDefault.png",
#         "shadow_image":"./sample_data/cut_images/Bomber.back.cut/back.fx.png",
#         "parts": [
#             {
#                 "name": "back.Back",
#                 "model_path": "./sample_data//models/Bomber.back.model/back.Back.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Bomber.back.cut/back.Back.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Test"
#             },
#
#             {
#                 "name": "back.left_sleeve",
#                 "model_path": "./sample_data//models/Bomber.back.model/back.RightSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Bomber.back.cut/back.RightSleeve1.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Test"
#             },
#             {
#                 "name": "back.right_sleeve",
#                 "model_path": "./sample_data//models/Bomber.back.model/back.LeftSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Bomber.back.cut/back.LeftSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Test"
#             },
# ]},
#
#     {
#         "side_name": "BackTshirt1",
#         "background_default":"./sample_data/cut_images/Tshirt/background_default.png",
#         "shadow_image":"./sample_data/cut_images/Tshirt/back.png",
#         "parts": [
#             {
#                 "name": "back.Back",
#                 "model_path": "./sample_data//models/Tshirt/tshirt.back.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Tshirt/back.Back.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Back"
#             },
#
#             {
#                 "name": "back.left_sleeve",
#                 "model_path": "./sample_data//models/Tshirt/tshirt.back.left_sleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Tshirt/back.LeftSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "back.right_sleeve",
#                 "model_path": "./sample_data//models/Tshirt/tshirt.back.right_sleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Tshirt/back.RightSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "back.neck",
#                 "model_path": "./sample_data//models/Tshirt/tshirt.back.back_neck.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Tshirt/back.Neck.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Neck"
#             },
# ]},
#     {
#         "side_name": "FrontTshirt",
#         "background_default":"./sample_data/cut_images/Tshirt/background_default.png",
#         "shadow_image":"./sample_data/cut_images/Tshirt/front.png",
#         "parts": [
#             {
#                 "name": "front.Front",
#                 "model_path": "./sample_data//models/Tshirt/tshirt.front.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Tshirt/front.Front.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
#
#             {
#                 "name": "back.left_sleeve",
#                 "model_path": "./sample_data//models/Tshirt/tshirt.front.left_sleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Tshirt/front.LeftSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "back.right_sleeve",
#                 "model_path": "./sample_data//models/Tshirt/tshirt.front.right_sleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Tshirt/front.RightSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "back.neck_back",
#                 "model_path": "./sample_data//models/Tshirt/tshirt.front.back_neck.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Tshirt/front.NeckBack.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Back"
#             },
#             {
#                 "name": "back.neck_front",
#                 "model_path": "./sample_data//models/Tshirt/tshirt.front_neck.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Tshirt/front.NeckFront.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
# ]},



# {
#         "side_name": "ToteBag",
#         "parts": [
#             {
#                 "name": "back.Back",
#                 "model_path": "./sample_data//models/test.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/test/2.mask.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Test"
#             },


# ]}
#     {
#         "side_name": "FrontHawaiian",
#         "parts": [
#             {
#                 "name": "front.Back",
#                 "model_path": "./sample_data//models/Hawaiian.front.model/Hawaiian.front.Back.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hawaiian.front.cut/front.Back2.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "HawaiianBack"
#             },
#
#             {
#                 "name": "front.left_sleeve",
#                 "model_path": "./sample_data//models/Hawaiian.front.model/Hawaiian.front.RightSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hawaiian.front.cut/front.LeftSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "LeftSleeve"
#             },
#             {
#                 "name": "front.right_sleeve",
#                 "model_path": "./sample_data//models/Hawaiian.front.model/Hawaiian.front.LeftSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hawaiian.front.cut/front.RightSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "RightSleeve"
#             },
#
#             {
#                 "name": "front.leftShirt",
#                 "model_path": "./sample_data//models/Hawaiian.front.model/Hawaiian.front.LeftShirt.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hawaiian.front.cut/front.LeftShirt1.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "FrontHawaiian"
#             },
#             {
#                 "name": "front.rightShirt",
#                 "model_path": "./sample_data//models/Hawaiian.front.model/Hawaiian.front.RightShirt.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hawaiian.front.cut/front.RightShirt2.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "FrontHawaiian"
#             },
#             {
#                 "name": "front.ve",
#                 "model_path": "./sample_data//models/Hawaiian.front.model/Hawaiian.front.Ve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hawaiian.front.cut/front.ve1.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Ve"
#             },
#
#             {
#                 "name": "front.centerNeck",
#                 "model_path": "./sample_data//models/Hawaiian.front.model/Hawaiian.front.CenterNeck.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hawaiian.front.cut/front.centeNeck.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "HawaiianNeck"
#             },
#             {
#                 "name": "front.leftNeck",
#                 "model_path": "./sample_data//models/Hawaiian.front.model/Hawaiian.front.LeftNeck.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hawaiian.front.cut/front.LeftNeck.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "LeftNeck"
#             },
#             {
#                 "name": "front.rightNeck",
#                 "model_path": "./sample_data//models/Hawaiian.front.model/Hawaiian.front.RightNeck.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hawaiian.front.cut/front.RightNeck1.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "RightNeck"
#             },
#
#
#
#
#         ]
#     },


    # {
    #     "side_name": "BackHawaiian",
    #     "parts": [
    #         {
    #             "name": "back.back",
    #             "model_path": "./sample_data//models/Hawaiian.back.model/HawaiianBackBack.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Hawaiian.back.cut/back.Back.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "HawaiianBack"
    #         },
    
    #         {
    #             "name": "back.Neck",
    #             "model_path": "./sample_data//models/Hawaiian.back.model/HawaiianBackNeck.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Hawaiian.back.cut/back.Neck2.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "FrontHawaiian"
    #         },
    #         {
    #             "name": "back.left_sleeve",
    #             "model_path": "./sample_data//models/Hawaiian.back.model/HawaiianBackSleeveLeft2.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Hawaiian.back.cut/back.LeftSleeve.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "LeftSleeve"
    #         },
    #         {
    #             "name": "back.right_sleeve",
    #             "model_path": "./sample_data//models/Hawaiian.back.model/HawaiianBackSleeveRight1.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Hawaiian.back.cut/back.RightSleeve.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "RightSleeve"
    #         },
    
    #     ]
    # },


#         {
#         "side_name": "FrontFleece",
#         "background_default": "./sample_data/cut_images/Fleece.front/background_default1.png",
#         "shadow_image": "./sample_data/cut_images/Fleece.front/front.png",
#         "parts": [
#             {
#                 "name": "front.leftShirt",
#                 "model_path": "./sample_data//models/Fleece.front/front.LeftFront.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.front/front.LeftFront.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
#             {
#                 "name": "front.rightShirt",
#                 "model_path": "./sample_data//models/Fleece.front/front.RightFront.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.front/front.RightFront.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
#             {
#                 "name": "front.LeftPocket",
#                 "model_path": "./sample_data//models/Fleece.front/front.LeftPocket.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.front/front.LeftPocket.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
#             {
#                 "name": "front.RightPocket",
#                 "model_path": "./sample_data//models/Fleece.front/front.RightPocket.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.front/front.RightPocket.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
#             {
#                 "name": "front.Hood",
#                 "model_path": "./sample_data//models/Fleece.front/front.Hood.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.front/front.Hood.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Hood"
#             },
#
#             {
#                 "name": "front.left_sleeve",
#                 "model_path": "./sample_data//models/Fleece.front/front.LeftSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.front/front.LeftSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "front.right_sleeve",
#                 "model_path": "./sample_data//models/Fleece.front/front.RightSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.front/front.RightSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#
#
#             {
#                 "name": "front.1",
#                 "model_path": "./sample_data//models/Fleece.front/front.1.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.front/front.1.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
#
#             {
#                 "name": "front.2",
#                 "model_path": "./sample_data//models/Fleece.front/front.2.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.front/front.2.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
#
#
#
#
#
#         ]
#     },
#
# {
#         "side_name": "BackFleece",
#         "background_default": "./sample_data/cut_images/Fleece.back/background_default.png",
#         "shadow_image": "./sample_data/cut_images/Fleece.back/back.png",
#         "parts": [
#             {
#                 "name": "back.back",
#                 "model_path": "./sample_data//models/Fleece.back/back.Back.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.back/back.Back.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Back"
#             },
#
#             {
#                 "name": "back.LeftHood",
#                 "model_path": "./sample_data//models/Fleece.back/back.LeftHood.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.back/back.LeftHood.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Hood"
#             },
#             {
#                 "name": "back.RightHood",
#                 "model_path": "./sample_data//models/Fleece.back/back.RightHood.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.back/back.RightHood.png",
#                 "shadow_image": "",  # can be None
#
#                 "artwork_side": "Hood"
#             },
#             {
#                 "name": "back.left_sleeve",
#                 "model_path": "./sample_data//models/Fleece.back/back.LeftSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.back/back.LeftSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "back.right_sleeve",
#                 "model_path": "./sample_data//models/Fleece.back/back.RightSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Fleece.back/back.RightSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#
#         ]
#     },

    # {
    #     "side_name": "Front",
    #     "artwork_path": "/home/vantrong291/Pictures/photos/3-front.jpg",
    #     "parts": [
    #         {
    #             "name": "front.left_sleeve",
    #             "model_path": "./sample_data//models/tshirt.front.left_sleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/front.left_sleeve-cut.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "front",
    #             "model_path": "./sample_data//models/tshirt.front.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/front.front-cut.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "front.right_sleeve",
    #             "model_path": "./sample_data//models/tshirt.front.right_sleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/front.right_sleeve-cut.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "front.bottom_hood",
    #             "model_path": "./sample_data//models/tshirt.front.bottom_hood.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/front.bottom_hood-cut.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Hood"
    #
    #         },
    #         {
    #             "name": "front.top_hood",
    #             "model_path": "./sample_data//models/tshirt.front.top_hood.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/front.top_hood-cut.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Hood"
    #         }
    # #     ]
 #    # },
 # {
 #     "side_name": "BackBandanatest1",
 #     "background_default": "./sample_data/cut_images/Bandana.front.cut/front.BackgroundDefault.png",
 #     "shadow_image": "./sample_data/cut_images/Bandana.back/back.png",
 #     "parts": [
 #            {
 #                "name": "back.back",
 #                "model_path": "./sample_data//models/bandana.back/Bandana.back.Back.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.back/back.Back.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Red"
 #            },
 #            {
 #                "name": "back.hood",
 #                "model_path": "./sample_data//models/bandana.back/Bandana.back.Hood.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.back/back.Hood.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Test"
 #            },
 #            {
 #                "name": "back.rightNeck",
 #                "model_path": "./sample_data//models/bandana.back/Bandana.back.NeckRight.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.back/back.RightNeck.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Test"
 #            },
 #            {
 #                "name": "back.NeckLeft",
 #                "model_path": "./sample_data//models/bandana.back/Bandana.back.NeckLeft.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.back/back.LeftNeck.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Test"
 #            },
 #            {
 #                "name": "back.right_sleeve",
 #                "model_path": "./sample_data//models/bandana.back/Bandana.back.RightSleeve.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.back/back.RightSleeve.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Red"
 #            },
 #
 #            {
 #                "name": "back.left_sleeve",
 #                "model_path": "./sample_data//models/bandana.back/Bandana.back.LeftSleeve.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.back/back.LeftSleeve.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Red"
 #            },
 #
 #
 #
 #
 #
 #        ]
 #    },
 # {
 #     "side_name": "FrontBandana",
 #     "background_default": "./sample_data/cut_images/Bandana.front.cut/background_default.png",
 #     "shadow_image": "./sample_data/cut_images/Bandana.front/front.png",
 #     "parts": [
 #            {
 #                "name": "front.Front",
 #                "model_path": "./sample_data//models/Bandana.front/Bandana.front.Front.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.front/front.Front.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Front"
 #            },
 #            {
 #                "name": "front.left_hood",
 #                "model_path": "./sample_data//models/Bandana.front/Bandana.front.LeftHood.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.front/front.LeftHood.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Hood"
 #            },
 #            {
 #                "name": "front.right_hood",
 #                "model_path": "./sample_data//models/Bandana.front/Bandana.front.RightHood.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.front/front.RightHood.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Hood"
 #            },
 #
 #
 #            {
 #                "name": "front.neck",
 #                "model_path": "./sample_data//models/Bandana.front/Bandana.front.Neck.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.front/front.Neck.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Neck"
 #            },
 #            {
 #                "name": "front.left_sleeve",
 #                "model_path": "./sample_data//models/Bandana.front/Bandana.front.LeftSleeve.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.front/front.LeftSleeve.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Sleeve"
 #            },
 #
 #            {
 #                "name": "front.right_sleeve",
 #                "model_path": "./sample_data//models/Bandana.front/Bandana.front.RightSleeve.model.npy",
 #                "cut_image_path": "./sample_data/cut_images/Bandana.front/front.RightSleeve.png",
 #                "shadow_image": "",  # can be None
 #                "artwork_side": "Sleeve"
 #            },
 #
 #
 #
 #        ]
 #    },




# {
#         "side_name": "Heart mug",
#         "parts": [
#             {
#                 "name": "left",
#                 "model_path": "./sample_data//models/HeartMug/heartMug.left.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/HeartMug/left1.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Mug"
#             },
#             {
#                 "name": "right",
#                 "model_path": "./sample_data//models/HeartMug/heartMug.right.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/HeartMug/right1.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Mug"
#             },

# ]
# }
# {
#         "side_name": "candle",
#         "parts": [
#             {
#                 "name": "left",
#                 "model_path": "./sample_data//models/candle.uch/candle.1.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/candle.uch/candle.1.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Candle"
#             },
#             {
#                 "name": "right",
#                 "model_path": "./sample_data//models/candle.uch/candle.2.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/candle.uch/candle.2.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Candle"
#             },

# ]
# }

# {
#         "side_name": "Hoodieback",
#         "background_default": "./sample_data/cut_images/Hoodie.back/background_default.png",
#         "shadow_image": "./sample_data/cut_images/Hoodie.back/back.png",
#         "parts": [
#             {
#                 "name": "back.Back",
#                 "model_path": "./sample_data//models/Hoodie.back/back.Back.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.back/back.Back.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Back"
#             },
#             {
#                 "name": "back.left_sleeve",
#                 "model_path": "./sample_data//models/Hoodie.back/back.LeftSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.back/back.LeftSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "back.right_sleeve",
#                 "model_path": "./sample_data//models/Hoodie.back/back.RightSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.back/back.RightSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#
#             {
#                 "name": "back.Hood",
#                 "model_path": "./sample_data//models/Hoodie.back/back.Hood.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.back/back.Hood.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Hood"
#             },
#             {
#                 "name": "back.1r",
#                 "model_path": "./sample_data//models/Hoodie.back/back.1.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.back/back.1.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "back.1l",
#                 "model_path": "./sample_data//models/Hoodie.back/back.2.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.back/back.2.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "back.2",
#                 "model_path": "./sample_data//models/Hoodie.back/back.31.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.back/back.3.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Back"
#             },
#         ]},
#
#         {
#         "side_name": "HoodieFront",
#         "mask":"./sample_data/mask/Hoodie1.png",
#         "background_default": "./sample_data/cut_images/Hoodie.front/background_default.png",
#         # "shadow_image": "./sample_data/cut_images/Tshirt/fx1.png",
#         "shadow_image": "./sample_data/cut_images/Hoodie.front/fx.png",
#         "parts": [
#
#             {
#                 "name": "front.Front",
#                 "model_path": "./sample_data//models/Hoodie.front/front.front.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.front/front.Front.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
#
#             {
#                 "name": "front.Pocket",
#                 "model_path": "./sample_data//models/Hoodie.front/front.pocket.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.front/front.Pocket.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
#
#             {
#                 "name": "front.left_sleeve",
#                 "model_path": "./sample_data//models/Hoodie.front/front.LeftSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.front/front.LeftSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "front.right_sleeve",
#                 "model_path": "./sample_data//models/Hoodie.front/front.RightSleeve.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.front/front.RightSleeve.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#
#
#
#             {
#                 "name": "front.LeftHood",
#                 "model_path": "./sample_data//models/Hoodie.front/front.LeftHood.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.front/front.LeftHood.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Hood"
#             },
#             {
#                 "name": "front.RightHood",
#                 "model_path": "./sample_data//models/Hoodie.front/front.RightHood.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.front/front.RightHood.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Hood"
#             },
#             {
#                 "name": "front.1r",
#                 "model_path": "./sample_data//models/Hoodie.front/front.1.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.front/front.1.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#
#             {
#                 "name": "front.2",
#                 "model_path": "./sample_data//models/Hoodie.front/front.2.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.front/front.2.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Sleeve"
#             },
#             {
#                 "name": "front.1l",
#                 "model_path": "./sample_data//models/Hoodie.front/front.3.model.npy",
#                 "cut_image_path": "./sample_data/cut_images/Hoodie.front/front.3.png",
#                 "shadow_image": "",  # can be None
#                 "artwork_side": "Front"
#             },
#
#         ]
#     },
    # {   "side_name": "Mask1",
    #     "parts": [
    #         {
    #             "name": "mask1",
    #             "model_path": "./sample_data//models/mask_3d_mockup.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/mask3dmockup1cut.2.png",
    #             "shadow_image": "mask_3d",  # can be None
    #             "artwork_side": "Mask1"
    #         },
    #
    #     ]
    # },
    # {
    #     "side_name": "Casual",
    #     "parts": [
    #         {
    #             "name": "Back",
    #             "model_path": "./sample_data//models/casual.model/casual.Back.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/casual.cut/Back.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #
    #         {
    #             "name": "right_sleeve",
    #             "model_path": "./sample_data//models/casual.model/casual.RightSleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/casual.cut/LeftSleeves.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "left_sleeve",
    #             "model_path": "./sample_data//models/casual.model/casual.LeftSleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/casual.cut/RightSleeves.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #
    #         {
    #             "name": "rightShirt",
    #             "model_path": "./sample_data//models/casual.model/casual.Right.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/casual.cut/Right2.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "leftShirt",
    #             "model_path": "./sample_data//models/casual.model/casual.Left.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/casual.cut/Left1.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #
    #         {
    #             "name": "centerNeck",
    #             "model_path": "./sample_data//models/casual.model/casual.CenterNeck.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/casual.cut/CenterNeck.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "rightNeck",
    #             "model_path": "./sample_data//models/casual.model/casual.RightNeck.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/casual.cut/RightNeck.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "leftNeck",
    #             "model_path": "./sample_data//models/casual.model/casual.LeftNeck.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/casual.cut/LeftNeck.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #
    #
    #
    #
    #     ]
    # },
    # {
    #     "side_name": "SweatshirtBack",
    #     "background_default":"./sample_data/cut_images/Bandana.front.cut/front.BackgroundDefault.png",
    #     "shadow_image":"./sample_data/cut_images/SweatShirt.back/fx.png",
    #     "parts": [
    #         {
    #             "name": "back.Back",
    #             "model_path": "./sample_data//models/SweatShirt.back/sweatshirt.back.Back.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.back/back.Back.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Back"
    #         },
    #         {
    #             "name": "back.left_sleeve",
    #             "model_path": "./sample_data//models/SweatShirt.back/sweatshirt.back.LeftSleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.back/back.LeftSleeve.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #         {
    #             "name": "back.right_sleeve",
    #             "model_path": "./sample_data//models/SweatShirt.back/sweatshirt.back.RightSleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.back/back.RightSleeve.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #         {
    #             "name": "back.Neck",
    #             "model_path": "./sample_data//models/SweatShirt.back/sweatshirt.back.Neck.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.back/back.Neck.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Back"
    #         },
    #         {
    #             "name": "back.1",
    #             "model_path": "./sample_data//models/SweatShirt.back/sweatshirt.back.1.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.back/back.1.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #
    #         {
    #             "name": "back.2",
    #             "model_path": "./sample_data//models/SweatShirt.back/sweatshirt.back.2.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.back/back.2.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Back"
    #         },
    #         {
    #             "name": "back.3",
    #             "model_path": "./sample_data//models/SweatShirt.back/sweatshirt.back.3.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.back/back.3.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #
    #
    #     ]
    # },
    # {
    #     "side_name": "SweatshirtFront3",
    #     "background_default":"./sample_data/cut_images/SweatShirt.front/background_default.png",
    #     "shadow_image":"./sample_data/cut_images/Sweatshirt.front/fx.png",
    #     "parts": [
    #         {
    #             "name": "front.Front",
    #             "model_path": "./sample_data//models/SweatShirt.front/sweatshirt.front.Front.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.front/front.Front.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "front.left_sleeve",
    #             "model_path": "./sample_data//models/SweatShirt.front/sweatshirt.front.RightSleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.front/front.RightSleeve.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #         {
    #             "name": "front.right_sleeve",
    #             "model_path": "./sample_data//models/SweatShirt.front/sweatshirt.front.LeftSleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.front/front.LeftSleeve.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #         {
    #             "name": "front.BackNeck",
    #             "model_path": "./sample_data//models/SweatShirt.front/sweatshirt.front.BackNeck.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.front/front.BackNeck.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Back"
    #         },
    #         {
    #             "name": "front.FrontNeck",
    #             "model_path": "./sample_data//models/SweatShirt.front/sweatshirt.front.FrontNeck.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.front/front.FrontNeck.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "front.1",
    #             "model_path": "./sample_data//models/SweatShirt.front/sweatshirt.front.1.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.front/front.1.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #
    #         {
    #             "name": "front.2",
    #             "model_path": "./sample_data//models/SweatShirt.front/sweatshirt.front.2.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.front/front.2.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "front.3",
    #             "model_path": "./sample_data//models/SweatShirt.front/sweatshirt.front.3.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Sweatshirt.front/front.3.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #
    #     ]},
    # {
    #     "side_name": "ZipBack",
    #     "background_default":"./sample_data/cut_images/Zip.front/background_default.png",
    #     "shadow_image":"./sample_data/cut_images/Zip.back/back.png",
    #     "parts": [
    #         {
    #             "name": "back.Back",
    #             "model_path": "./sample_data//models/Zip.back/back.Back.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.back/back.Back.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Back"
    #         },
    #         {
    #             "name": "back.left_sleeve",
    #             "model_path": "./sample_data//models/Zip.back/back.LeftSleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.back/back.LeftSleeve.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #         {
    #             "name": "back.right_sleeve",
    #             "model_path": "./sample_data//models/Zip.back/back.RightSleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.back/back.RightSleeve.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #         {
    #             "name": "back.Hood",
    #             "model_path": "./sample_data//models/Zip.back/back.Hood.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.back/back.Hood.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Hood"
    #         },
    #         {
    #             "name": "back.1l",
    #             "model_path": "./sample_data//models/Zip.back/back.1l.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.back/back.1l.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #
    #         {
    #             "name": "back.2",
    #             "model_path": "./sample_data//models/Zip.back/back.2.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.back/back.2.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Back"
    #         },
    #         {
    #             "name": "back.1r",
    #             "model_path": "./sample_data//models/Zip.back/back.1r.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.back/back.1r.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #
    #
    #     ]
    # },
    # {
    #     "side_name": "ZipFront3",
    #     "background_default":"./sample_data/cut_images/Zip.front/background_default.png",
    #     "shadow_image":"./sample_data/cut_images/Zip.front/front.png",
    #     "parts": [
    #         {
    #             "name": "front.Front",
    #             "model_path": "./sample_data//models/Zip.front/front.Front.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.front/front.Front.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "front.left_sleeve",
    #             "model_path": "./sample_data//models/Zip.front/front.right_sleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.front/front.RightSleeve.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #         {
    #             "name": "front.right_sleeve",
    #             "model_path": "./sample_data//models/Zip.front/front.left_sleeve.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.front/front.LeftSleeve.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #         {
    #             "name": "front.left_Hood",
    #             "model_path": "./sample_data//models/Zip.front/front.left_hood.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.front/front.LeftHood.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Hood"
    #         },
    #         {
    #             "name": "front.right_Hood",
    #             "model_path": "./sample_data//models/Zip.front/front.right_hood.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.front/front.RightHood.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Hood"
    #         },
    #         {
    #             "name": "front.Pocket",
    #             "model_path": "./sample_data//models/Zip.front/front.pocket.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.front/front.Pocket.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "front.1r",
    #             "model_path": "./sample_data//models/Zip.front/front.1r.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.front/front.1r.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #
    #         {
    #             "name": "front.2",
    #             "model_path": "./sample_data//models/Zip.front/front.2.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.front/front.2.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Front"
    #         },
    #         {
    #             "name": "front.1l",
    #             "model_path": "./sample_data//models/Zip.front/front.1l.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/Zip.front/front.1l.png",
    #             "shadow_image": "",  # can be None
    #             "artwork_side": "Sleeve"
    #         },
    #
    #     ]},
    # {"side_name": "Mask_kid",
    #  "parts": [
    #      {
    #          "name": "mask_kid",
    #          "model_path": "./sample_data//models/mask_kid.model.npy",
    #          "cut_image_path": "./sample_data/cut_images/mask_kid_cut.png",
    #          "shadow_image": "mask_kid",  # can be None
    #          "artwork_side": "Mask_kid"
    #      },
    #
    #  ]
    #  },
    # {"side_name": "Mask_with_BG",
    #  "parts": [
    #      {
    #          "name": "mask_with_BG",
    #          "model_path": "./sample_data//models/mask_BG.2.model.npy",
    #          "cut_image_path": "./sample_data/cut_images/mask_BG_cut.png",
    #          "shadow_image": "",  # can be None
    #          "artwork_side": "Mask_with_BG"
    #      },
    # #  ]
    #  }
    # {"side_name": "Mask_Man",
    #  "parts": [
    #      {
    #          "name": "mask_Man",
    #          "model_path": "./sample_data//models/Bandana.back/back.right_sleevet.model.npy",
    #          "cut_image_path": "./sample_data/cut_images/Bandana_back/back.right_sleevet-cut.png",
    #          "shadow_image": "",  # can be None
    #          "artwork_side": "Mask_new"
    #      },
    #  ]
    #  }
    # # {   "side_name": "Neck_gaiter",
    #     "parts": [
    #         {
    #             "name": "neck_gaiter",
    #             "model_path": "./sample_data//models/neck_gaiter.model.npy",
    #             "cut_image_path": "./sample_data/cut_images/neck_gaiter_cut.1.png",
    #             "shadow_image": "mask_3d",  # can be None
    #             "artwork_side": "Neck_gaiter"
    #         },
    #
    #     ]
    # },
    # {"side_name": "Wall_flag_ngang",
    #  "parts": [
    #      {
    #          "name": "wall_flag_ngang",
    #          "model_path": "./sample_data//models/wall_flag_ngang.model.npy",
    #          "cut_image_path": "./sample_data/cut_images/wall_flagC_ngang_cut.png",
    #          "shadow_image": "",  # can be None
    #          "artwork_side": "Wall_flag_ngang"
    #      },
    #
    #  ]
    #  },
    # {"side_name": "Flag_mockup3",
    #  "parts": [
    #      {
    #          "name": "flag_mockup3",
    #          "model_path": "./sample_data//models/flag_mockup3.5.model.npy",
    #          "cut_image_path": "./sample_data/cut_images/flag_mockup3_cut.png",
    #          "shadow_image": "",  # can be None
    #          "artwork_side": "Flag_mockup3"
    #      },
    #
    #  ]
    #  },
]



if __name__ == "__main__":
    mockup = Mockup3DGenerator(mockup_data=MOCKUP_DATA, artwork_data=ARTWORK_DATA, background_data = BACKROUND_DATA)
    print("----- STARTING -----")
    mockup.do_generate()
    print("----- DONE -----")
